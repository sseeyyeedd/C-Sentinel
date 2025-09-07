# engine.py (Corrected version with all __init__ methods)
from pycparser import c_ast
from cparser import header_defs_lines_count
import sys
def get_code_line(source_lines, line_num):
    corrected_line_index = line_num - header_defs_lines_count - 1
    if 0 <= corrected_line_index < len(source_lines):
        return source_lines[corrected_line_index].strip()
    return "[Code line not available]"

# ===================================================================
# 1. Specialized Visitors
# ===================================================================

class BlockRuleVisitor(c_ast.NodeVisitor):
    def __init__(self, dsl_rules, source_lines):
        self.dsl_rules = dsl_rules
        self.source_lines = source_lines
        self.errors = []
    def visit_FuncCall(self, node):
        function_name = node.name.name
        for rule in self.dsl_rules:
            for blocked_func, message in rule.blocks:
                if function_name == blocked_func:
                    line_num = node.name.coord.line
                    code_line = get_code_line(self.source_lines, line_num)
                    error_msg = (
                        f"Line {line_num - header_defs_lines_count}: Violation of rule '{rule.name}'.\n"
                        f"\t> {code_line}\n"
                        f"\tMessage: Forbidden function call to '{blocked_func}'. {message}"
                    )
                    self.errors.append(error_msg)

class FormatStringVisitor(c_ast.NodeVisitor):
    def __init__(self, dsl_rules, source_lines):
        self.dsl_rules = dsl_rules
        self.source_lines = source_lines
        self.errors = []
    def visit_FuncCall(self, node):
        function_name = node.name.name
        for rule in self.dsl_rules:
            for req in rule.literal_requires:
                if function_name == req['func']:
                    if node.args and node.args.exprs:
                        first_arg = node.args.exprs[0]
                        is_string_literal = (isinstance(first_arg, c_ast.Constant) and first_arg.type == 'string')
                        if not is_string_literal:
                            line_num = node.name.coord.line
                            code_line = get_code_line(self.source_lines, line_num)
                            error_msg = (
                                f"Line {line_num - header_defs_lines_count}: Violation of rule '{rule.name}'.\n"
                                f"\t> {code_line}\n"
                                f"\tMessage: Call to '{function_name}' requires a string literal. {req['message']}"
                            )
                            self.errors.append(error_msg)
class ConstantPropagationVisitor(c_ast.NodeVisitor):
    """این Visitor مقادیر ثابت متغیرها را در یک تابع ردیابی می‌کند."""
    def __init__(self):
        self.constants = {}

    def visit_Decl(self, node):
        if (node.init and
                isinstance(node.init, c_ast.Constant) and
                node.init.type == 'int'):
            self.constants[node.name] = int(node.init.value)
        self.generic_visit(node)

    def visit_Assignment(self, node):
        if (isinstance(node.lvalue, c_ast.ID) and
                isinstance(node.rvalue, c_ast.Constant) and
                node.rvalue.type == 'int'):
            self.constants[node.lvalue.name] = int(node.rvalue.value)
            # اگر متغیری با یک مقدار غیرثابت مقداردهی شود، آن را از لیست حذف می‌کنیم
        elif isinstance(node.lvalue, c_ast.ID) and node.lvalue.name in self.constants:
            del self.constants[node.lvalue.name]
        self.generic_visit(node)
class IntegerOverflowVisitor(c_ast.NodeVisitor):
    def __init__(self, dsl_rules, source_lines,constants):
        self.dsl_rules = dsl_rules
        self.source_lines = source_lines
        self.constants = constants
        self.errors = []
    def visit_FuncCall(self, node):
        function_name = node.name.name
        for rule in self.dsl_rules:
            for call_rule in rule.calls:
                if function_name == call_rule['func']:
                    if not node.args: continue
                    # به جای جستجوی ساده، عبارت را تحلیل می‌کنیم
                    for arg_node in node.args.exprs:
                        eval_visitor = ExpressionEvaluator(self.constants)
                        is_overflow, is_potential = eval_visitor.evaluate(arg_node)

                        if is_overflow:
                            line_num = node.name.coord.line
                            self.errors.append(
                                f"Line {line_num - header_defs_lines_count}: Violation of rule '{rule.name}'.\n"
                                f"\t> {get_code_line(self.source_lines, line_num)}\n"
                                f"\tMessage: DEFINITE integer overflow detected in an argument to '{function_name}'. {call_rule['message']}"
                            )
                        elif is_potential:
                            line_num = node.name.coord.line
                            self.errors.append(
                                f"Line {line_num - header_defs_lines_count}: Warning for rule '{rule.name}'.\n"
                                f"\t> {get_code_line(self.source_lines, line_num)}\n"
                                f"\tMessage: POTENTIAL integer overflow detected (non-constant values). {call_rule['message']}"
                            )


class ExpressionEvaluator(c_ast.NodeVisitor):
    """یک Visitor کوچک برای ارزیابی یک عبارت و بررسی سرریز."""

    def __init__(self, constants):
        self.constants = constants
        self.value = None
        self.is_constant = True

    def evaluate(self, node):
        self.visit(node)
        # اگر عبارت کاملاً ثابت بود و سرریز داشت
        if self.is_constant and self.value is not None and self.value > sys.maxsize:
            return (True, False)  # سرریز قطعی
        # اگر عبارت شامل متغیرهای غیرثابت بود
        if not self.is_constant:
            return (False, True)  # سرریز بالقوه
        # در غیر این صورت، مشکلی نیست
        return (False, False)

    def visit_Constant(self, node):
        self.value = int(node.value)

    def visit_ID(self, node):
        if node.name in self.constants:
            self.value = self.constants[node.name]
        else:
            self.is_constant = False  # متغیر ثابت نیست
            self.value = None

    def visit_BinaryOp(self, node):
        if node.op in ['+', '-', '*', '/']:
            left_eval = ExpressionEvaluator(self.constants)
            left_eval.visit(node.left)

            right_eval = ExpressionEvaluator(self.constants)
            right_eval.visit(node.right)

            if left_eval.is_constant and right_eval.is_constant:
                if node.op == '+':
                    self.value = left_eval.value + right_eval.value
                elif node.op == '-':
                    self.value = left_eval.value - right_eval.value
                elif node.op == '*':
                    self.value = left_eval.value * right_eval.value
                # ... (می‌توان تقسیم را نیز اضافه کرد) ...
            else:
                self.is_constant = False
                self.value = None


class MemorySafetyVisitor(c_ast.NodeVisitor):
    def __init__(self, dsl_rules, source_lines):
        self.dsl_rules = dsl_rules
        self.source_lines = source_lines
        self.errors = []
    def visit_FuncDef(self, node):
        if node.body and node.body.block_items :
            self._check_null_after_free(node.body.block_items)
            self._check_double_free(node.body.block_items)
            self._check_unused_memory(node.body.block_items)
        self.generic_visit(node)

    def _check_null_after_free(self,block_items):
        monitored_funcs = {req['func']: req for rule in self.dsl_rules for req in rule.null_after_requires}
        for i in range(len(block_items) - 1):
            current_stmt, next_stmt = block_items[i], block_items[i + 1]
            if isinstance(current_stmt, c_ast.FuncCall) and current_stmt.name.name in monitored_funcs:
                if not current_stmt.args or not current_stmt.args.exprs or not isinstance(current_stmt.args.exprs[0],
                                                                                          c_ast.ID): continue
                pointer_freed = current_stmt.args.exprs[0].name
                is_nullified = False
                if isinstance(next_stmt, c_ast.Assignment) and next_stmt.op == '=' and isinstance(next_stmt.lvalue,
                                                                                                  c_ast.ID) and next_stmt.lvalue.name == pointer_freed:
                    if isinstance(next_stmt.rvalue, c_ast.Constant) and next_stmt.rvalue.value == '0':
                        is_nullified = True
                if not is_nullified:
                    rule_info = monitored_funcs[current_stmt.name.name]
                    line_num = current_stmt.coord.line
                    self.errors.append(
                        f"Line {line_num - header_defs_lines_count}: Violation of rule 'EnforceNullAfterFree'.\n"
                        f"\t> {get_code_line(self.source_lines, line_num)}\n"
                        f"\tMessage: Pointer '{pointer_freed}' is not set to NULL after '{current_stmt.name.name}'. {rule_info['message']}"
                    )
    def check_function_body(self, body_node):
        if not body_node or not body_node.block_items:
            return

            # --- اصلاح کلیدی: فراخوانی هر سه تابع بررسی ---
        self._check_null_after_free(body_node.block_items)
        self._check_double_free(body_node.block_items)
        self._check_unused_memory(body_node.block_items)

    def _check_double_free(self, block_items):
        # *** منطق اصلاح‌شده ***
        double_free_funcs = {check['func'] for rule in self.dsl_rules for check in rule.double_free_checks}
        freed_vars = set()
        for stmt in block_items:
            if isinstance(stmt, c_ast.FuncCall) and stmt.name.name in double_free_funcs:
                if stmt.args and stmt.args.exprs and isinstance(stmt.args.exprs[0], c_ast.ID):
                    pointer_name = stmt.args.exprs[0].name
                    if pointer_name in freed_vars:  # اگر قبلاً آزاد شده باشد
                        rule_info = next((r for r in self.dsl_rules if r.name == 'BanDoubleFree'), None)
                        if rule_info:
                            line_num = stmt.coord.line
                            code_line = get_code_line(self.source_lines, line_num)
                            self.errors.append(
                                f"Line {line_num - header_defs_lines_count}: Violation of rule '{rule_info.name}'.\n"
                                f"\t> {code_line}\n"
                                f"\tMessage: Pointer '{pointer_name}' is freed more than once. {rule_info.double_free_checks[0]['message']}"
                            )
                    else:
                        # فقط اشاره‌گرهای غیر NULL را به عنوان آزاد شده علامت بزن
                        # چون free(NULL) امن است و نباید جلوی free بعدی را بگیرد
                        if pointer_name != 'NULL':
                            freed_vars.add(pointer_name)

    def _check_unused_memory(self, block_items):
        unused_mem_funcs = {check['func'] for rule in self.dsl_rules for check in rule.free_unused_checks}
        allocated_vars = {stmt.name: {'used': False, 'node': stmt} for stmt in block_items if
                          isinstance(stmt, c_ast.Decl) and stmt.init and isinstance(stmt.init,
                                                                                    c_ast.FuncCall) and stmt.init.name.name in unused_mem_funcs}
        for i, stmt in enumerate(block_items):
            for var_name in allocated_vars:
                if stmt != allocated_vars[var_name]['node']:
                    usage_visitor = FindVarUsageVisitor(var_name)
                    usage_visitor.visit(stmt)
                    if usage_visitor.found:
                        allocated_vars[var_name]['used'] = True
        for var_name, data in allocated_vars.items():
            if not data['used']:
                rule_info = next((r for r in self.dsl_rules if r.name == 'FreeUnusedMemory'), None)
                if rule_info:
                    node = data['node']
                    line_num = node.coord.line
                    self.errors.append(
                        f"Line {line_num - header_defs_lines_count}: Violation of rule '{rule_info.name}'.\n"
                        f"\t> {get_code_line(self.source_lines, line_num)}\n"
                        f"\tMessage: Allocated memory for '{var_name}' is not used or freed. {rule_info.free_unused_checks[0]['message']}"
                    )
# --- CORRECTED TaintAnalysisVisitor ---
class TaintAnalysisVisitor(c_ast.NodeVisitor):
    def __init__(self, dsl_rules, source_lines):
        self.dsl_rules = dsl_rules
        self.source_lines = source_lines
        self.tainted_vars = set()
        self.errors = []
        self.sources = {s['func']: s['message'] for r in dsl_rules for s in r.sources}
        self.sinks = {s['func']: s['message'] for r in dsl_rules for s in r.sinks}
        self.sanitizers = {s for r in dsl_rules for s in r.sanitizers}
    def visit_Assignment(self, node):
        if isinstance(node.rvalue, c_ast.ID) and node.rvalue.name in self.tainted_vars:
            if isinstance(node.lvalue, c_ast.ID): self.tainted_vars.add(node.lvalue.name)
        if isinstance(node.rvalue, c_ast.FuncCall) and node.rvalue.name.name in self.sanitizers:
            if isinstance(node.lvalue, c_ast.ID) and node.lvalue.name in self.tainted_vars:
                self.tainted_vars.remove(node.lvalue.name)
        self.generic_visit(node)
    def visit_FuncCall(self, node):
        func_name = node.name.name
        if func_name in self.sources:
            if node.args and node.args.exprs:
                first_arg = node.args.exprs[0]
                if isinstance(first_arg, c_ast.UnaryOp) and first_arg.op == '&':
                    if isinstance(first_arg.expr, c_ast.ID):
                        self.tainted_vars.add(first_arg.expr.name)
        if func_name in self.sinks:
            if node.args and node.args.exprs:
                for arg in node.args.exprs:
                    if isinstance(arg, c_ast.ID) and arg.name in self.tainted_vars:
                        line_num = node.name.coord.line
                        code_line = get_code_line(self.source_lines, line_num)
                        self.errors.append(
                            f"Line {line_num - header_defs_lines_count}: Taint Violation! "
                            f"Tainted variable '{arg.name}' used in sink function '{func_name}'. Message: {self.sinks[func_name]}"
                        )
                        break
        self.generic_visit(node)

# --- CORRECTED NullPointerVisitor ---
class NullPointerVisitor(c_ast.NodeVisitor):
    def __init__(self, dsl_rules, source_lines):
        self.dsl_rules = dsl_rules
        self.source_lines = source_lines
        self.pointer_states = {}
        self.errors = []
        self.monitored_vars = {req['var']: {'rule': rule.name, 'message': req['message']} for rule in self.dsl_rules for req in rule.access_requires}

    def visit_Decl(self, node):
        # *** این متد جدید و کلیدی است ***
        # بررسی مقداردهی اولیه در زمان اعلان متغیر
        if isinstance(node.type, c_ast.PtrDecl) and node.name in self.monitored_vars:
            if node.init:
                is_null_const = (isinstance(node.init, c_ast.Constant) and node.init.value == '0')
                is_null_cast = (isinstance(node.init, c_ast.Cast) and
                                isinstance(node.init.expr, c_ast.Constant) and
                                node.init.expr.value == '0')
                if is_null_const or is_null_cast:
                    self.pointer_states[node.name] = 'NULL'
                elif isinstance(node.init, c_ast.FuncCall) and node.init.name.name == 'malloc':
                    self.pointer_states[node.name] = 'NOT_NULL'
        self.generic_visit(node)

    def visit_Assignment(self, node):
        if isinstance(node.lvalue, c_ast.ID) and node.lvalue.name in self.monitored_vars:
            is_null_const = (isinstance(node.rvalue, c_ast.Constant) and node.rvalue.value == '0')
            is_null_cast = (isinstance(node.rvalue, c_ast.Cast) and
                            isinstance(node.rvalue.expr, c_ast.Constant) and
                            node.rvalue.expr.value == '0')
            if is_null_const or is_null_cast:
                self.pointer_states[node.lvalue.name] = 'NULL'
            elif isinstance(node.rvalue, c_ast.FuncCall) and node.rvalue.name.name == 'malloc':
                self.pointer_states[node.lvalue.name] = 'NOT_NULL'
            else:
                self.pointer_states[node.lvalue.name] = 'UNKNOWN'
        self.generic_visit(node)

    def _check_dereference(self, node, ptr_node):
        if isinstance(ptr_node, c_ast.ID) and ptr_node.name in self.monitored_vars:
            var_name = ptr_node.name
            if self.pointer_states.get(var_name) == 'NULL':
                rule_info = self.monitored_vars[var_name]
                line_num = node.coord.line
                code_line = get_code_line(self.source_lines, line_num)
                error_msg = (
                    f"Line {line_num - header_defs_lines_count}: Violation of rule '{rule_info['rule']}'.\n"
                    f"\t> {code_line}\n"
                    f"\tMessage: Pointer '{var_name}' is dereferenced while it is NULL. {rule_info['message']}"
                )
                self.errors.append(error_msg)

    def visit_UnaryOp(self, node):
        if node.op == '*':
            self._check_dereference(node, node.expr)
        self.generic_visit(node)

    def visit_StructRef(self, node):
        if node.type == '->':
            self._check_dereference(node, node.name)
        self.generic_visit(node)

    def visit_If(self, node):
        condition = node.cond
        ptr_name, condition_is_null = None, None

        if isinstance(condition, c_ast.BinaryOp) and isinstance(condition.right,
                                                                c_ast.Constant) and condition.right.value == '0':
            if isinstance(condition.left, c_ast.ID) and condition.left.name in self.monitored_vars:
                ptr_name = condition.left.name
                if condition.op == '==':
                    condition_is_null = True
                elif condition.op == '!=':
                    condition_is_null = False

        if ptr_name is not None:
            original_state = self.pointer_states.copy()

            # Analyze 'then' block
            self.pointer_states[ptr_name] = 'NULL' if condition_is_null else 'NOT_NULL'
            self.visit(node.iftrue)

            # Restore state and analyze 'else' block
            self.pointer_states = original_state
            if node.iffalse:
                self.pointer_states[ptr_name] = 'NOT_NULL' if condition_is_null else 'NULL'
                self.visit(node.iffalse)

            self.pointer_states = original_state
        else:
            self.generic_visit(node)
# --- CORRECTED FindBinaryOpVisitor ---
class FindBinaryOpVisitor(c_ast.NodeVisitor):
    # This helper visitor is simple and doesn't need dsl_rules or source_lines
    def __init__(self, op_to_find):
        self.op_to_find = op_to_find
        self.found = False
    def visit_BinaryOp(self, node):
        if node.op == self.op_to_find:
            self.found = True
        self.generic_visit(node)
class FindVarUsageVisitor(c_ast.NodeVisitor):
    def __init__(self, var_to_find):
        self.var_to_find, self.found = var_to_find, False
    def visit_ID(self, node):
        if node.name == self.var_to_find: self.found = True
# ===================================================================
# 2. Main Coordinator
# ===================================================================
class FuncDefVisitor(c_ast.NodeVisitor):
    """یک Visitor کمکی فقط برای پیدا کردن تمام تعاریف توابع در AST."""
    def __init__(self):
        self.func_defs = []
    def visit_FuncDef(self, node):
        self.func_defs.append(node)
        # از پیمایش بازگشتی جلوگیری می‌کنیم تا توابع تودرتو جداگانه پیدا شوند
        # self.generic_visit(node)
class SecurityAuditor:
    def __init__(self, dsl_rules, source_lines):
        self.dsl_rules = dsl_rules
        self.source_lines = source_lines
        self.c_ast = None
    def run_analysis(self, c_ast):
        self.c_ast = c_ast
        all_errors = []

        # مرحله ۱: اجرای Visitorهای سراسری (Stateless)
        # اینها به محدوده تابع وابسته نیستند و یک بار روی کل فایل اجرا می‌شوند.
        stateless_visitors = [
            BlockRuleVisitor,
            FormatStringVisitor
        ]
        for visitor_class in stateless_visitors:
            visitor_instance = visitor_class(self.dsl_rules, self.source_lines)
            visitor_instance.visit(self.c_ast)
            all_errors.extend(visitor_instance.errors)

        # مرحله ۲: اجرای Visitorهای محدود به تابع (Stateful)
        # ابتدا تمام توابع را پیدا می‌کنیم.
        func_finder = FuncDefVisitor()
        func_finder.visit(self.c_ast)

        # سپس به ازای هر تابع، تحلیل‌های حالت‌مند را اجرا می‌کنیم.
        for func_node in func_finder.func_defs:

            # گام ۲.۱: مقادیر ثابت را فقط در محدوده این تابع پیدا می‌کنیم.
            const_visitor = ConstantPropagationVisitor()
            const_visitor.visit(func_node.body)
            constants_in_func = const_visitor.constants

            # گام ۲.۲: IntegerOverflowVisitor را با دیکشنری ثابت‌ها ایجاد می‌کنیم.
            overflow_visitor = IntegerOverflowVisitor(self.dsl_rules, self.source_lines, constants_in_func)
            overflow_visitor.visit(func_node.body)
            all_errors.extend(overflow_visitor.errors)

            # گام ۲.۳: سایر Visitorهای حالت‌مند را اجرا می‌کنیم.
            other_stateful_visitors = [
                MemorySafetyVisitor,
                TaintAnalysisVisitor,
                NullPointerVisitor
            ]
            for visitor_class in other_stateful_visitors:
                visitor_instance = visitor_class(self.dsl_rules, self.source_lines)
                visitor_instance.visit(func_node.body)
                all_errors.extend(visitor_instance.errors)

        return all_errors