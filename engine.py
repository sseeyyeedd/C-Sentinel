# engine.py
from pycparser import c_ast
from cparser import header_defs_lines_count


class TaintAnalysisVisitor(c_ast.NodeVisitor):
    def __init__(self, dsl_rules):
        self.dsl_rules = dsl_rules
        self.tainted_vars = set()
        self.errors = []

        # Extract sources, sinks, and sanitizers from the rules
        self.sources = {s['func']: s['message'] for r in dsl_rules for s in r.sources}
        self.sinks = {s['func']: s['message'] for r in dsl_rules for s in r.sinks}
        self.sanitizers = {s for r in dsl_rules for s in r.sanitizers}

    def visit_Assignment(self, node):
        # Taint propagation: if the right side is tainted, the left side becomes tainted.
        # This is a simplification; a full engine would need to check expressions deeply.
        if isinstance(node.rvalue, c_ast.ID) and node.rvalue.name in self.tainted_vars:
            self.tainted_vars.add(node.lvalue.name)

        # Check for sanitization
        if isinstance(node.rvalue, c_ast.FuncCall) and node.rvalue.name.name in self.sanitizers:
            if node.lvalue.name in self.tainted_vars:
                self.tainted_vars.remove(node.lvalue.name) # It's now clean

        self.generic_visit(node)

    def visit_FuncCall(self, node):
        func_name = node.name.name

        # Is this function a source of taint?
        if func_name in self.sources:
            # Simplification: assume the first argument to a source function becomes tainted.
            # E.g., in scanf("%s", &name), 'name' becomes tainted.
            if node.args and node.args.exprs:
                # The argument to scanf is often &var, which is a UnaryOp.
                first_arg = node.args.exprs[0]
                if isinstance(first_arg, c_ast.UnaryOp) and first_arg.op == '&':
                    if isinstance(first_arg.expr, c_ast.ID):
                        self.tainted_vars.add(first_arg.expr.name)

        # Is this function a sink, and is it being called with tainted data?
        if func_name in self.sinks:
            if node.args and node.args.exprs:
                for arg in node.args.exprs:
                    if isinstance(arg, c_ast.ID) and arg.name in self.tainted_vars:
                        self.errors.append(
                            f"Line {node.name.coord.line - header_defs_lines_count}: Taint Violation! "
                            f"Tainted variable '{arg.name}' is used in sink function '{func_name}'. "
                            f"Message: {self.sinks[func_name]}"
                        )
                        break # Report once per sink call

        self.generic_visit(node)
# A new, small visitor just for finding a specific math operation
class FindBinaryOpVisitor(c_ast.NodeVisitor):
    def __init__(self, op_to_find):
        self.op_to_find = op_to_find
        self.found = False

    def visit_BinaryOp(self, node):
        if node.op == self.op_to_find:
            self.found = True

class SecurityAuditor(c_ast.NodeVisitor):
    """
    Walks the C Abstract Syntax Tree (AST) and checks for violations
    against a set of rules defined in the CSentinel DSL.
    """
    def __init__(self, dsl_rules):
        self.dsl_rules = dsl_rules
        self.errors = []

    def run_analysis(self, c_ast):
        """Public method to start the analysis."""
        taint_visitor = TaintAnalysisVisitor(self.dsl_rules)
        self.visit(c_ast)
        taint_visitor.visit(c_ast)
        # return taint_visitor.errors


        for error in taint_visitor.errors:
            self.errors.append(error)
        return self.errors

    def visit_FuncCall(self, node):
        """
        This method is automatically called for every function call
        found in the C code's AST.
        """
        function_name = node.name.name

        # --- IMPLEMENTING THE 'block' RULE ---
        # Iterate through all the loaded DSL rules
        for rule in self.dsl_rules:
            # Check each 'block' definition within the rule
            for blocked_func, message in rule.blocks:
                if function_name == blocked_func:
                    # If the function call in the C code matches a blocked function...
                    error_msg = (
                        f"Line {node.name.coord.line - header_defs_lines_count}: Violation of rule '{rule.name}'. "
                        f"Forbidden function call to '{blocked_func}'. "
                        f"Message: {message}"
                    )
                    self.errors.append(error_msg)

        for rule in self.dsl_rules:
            for call_rule in rule.calls:
                if function_name == call_rule['func']:
                    # We found a call to a function monitored by a rule.
                    # Now, let's check for the dangerous operation in its arguments.

                    # For now, we'll just look for the first operator in the condition string.
                    # A more advanced parser could handle complex expressions.
                    op_to_find = None
                    if '+' in call_rule['condition']:
                        op_to_find = '+'
                    elif '*' in call_rule['condition']:
                        op_to_find = '*'
                    elif '-' in call_rule['condition']:
                        op_to_find = '-'
                    elif '/' in call_rule['condition']:
                        op_to_find = '/'

                    if op_to_find:
                        # For each argument passed to the function...
                        for arg_node in node.args.exprs:
                            # ...search for the dangerous binary operation.
                            op_visitor = FindBinaryOpVisitor(op_to_find)
                            op_visitor.visit(arg_node)
                            if op_visitor.found:
                                error_msg = (
                                    f"Line {node.name.coord.line - header_defs_lines_count}: Violation of rule '{rule.name}'. "
                                    f"Potential overflow with '{op_to_find}' in an argument to '{function_name}'. "
                                    f"Message: {call_rule['message']}"
                                )
                                self.errors.append(error_msg)
                                break  # Stop checking other args for this call

        for rule in self.dsl_rules:
            for require_rule in rule.literal_requires:
                if function_name == require_rule['func']:
                    # We found a call to a function monitored by this rule.
                    # Check if the first argument exists and is a string literal.
                    if node.args and node.args.exprs:
                        first_arg = node.args.exprs[0]
                        # In pycparser AST, string literals are of type 'Constant'
                        # and their type is 'string'.
                        is_string_literal = (
                                isinstance(first_arg, c_ast.Constant) and
                                first_arg.type == 'string'
                        )

                        if not is_string_literal:
                            error_msg = (
                                f"Line {node.name.coord.line - header_defs_lines_count}: Violation of rule '{rule.name}'. "
                                f"Call to '{function_name}' requires a string literal as the first argument. "
                                f"Message: {require_rule['message']}"
                            )
                            self.errors.append(error_msg)

    def visit_Compound(self, node):
        """
        This method is called for every compound block (i.e., code inside {}).
        This is where we can check for rules involving sequences of statements.
        """
        # --- NEW: implementation for FreeUnusedMemory detection ---
        free_unused_funcs = set()
        for rule in self.dsl_rules:
            for func in getattr(rule, 'free_unused_checks', []):
                if isinstance(func, dict) and 'func' in func:
                    free_unused_funcs.add(func['func'])
                else:
                    free_unused_funcs.add(func)

        # Track malloc'd pointers and their usage
        malloc_calls = []  # List of (pointer_name, stmt)
        used_vars = set()

        # Helper: recursively find all used variable names in an AST node
        def find_used_vars(ast_node):
            if isinstance(ast_node, c_ast.ID):
                used_vars.add(ast_node.name)
            elif isinstance(ast_node, c_ast.StructRef):
                # e.g., ptr->field or ptr.field
                find_used_vars(ast_node.name)
            elif isinstance(ast_node, c_ast.ArrayRef):
                # e.g., ptr[index]
                find_used_vars(ast_node.name)
                find_used_vars(ast_node.subscript)
            elif isinstance(ast_node, c_ast.UnaryOp):
                find_used_vars(ast_node.expr)
            elif isinstance(ast_node, c_ast.BinaryOp):
                find_used_vars(ast_node.left)
                find_used_vars(ast_node.right)
            elif isinstance(ast_node, c_ast.FuncCall):
                find_used_vars(ast_node.name)
                if ast_node.args:
                    for arg in getattr(ast_node.args, 'exprs', []):
                        find_used_vars(arg)
            elif isinstance(ast_node, c_ast.Assignment):
                find_used_vars(ast_node.lvalue)
                find_used_vars(ast_node.rvalue)
            # Recursively check children for other node types
            for child in getattr(ast_node, 'children', lambda: [])():
                find_used_vars(child)

        if node.block_items:
            for stmt in node.block_items:
                # Detect malloc calls
                # Detect malloc calls in assignments and declarations with initialization
                if isinstance(stmt, c_ast.Assignment):
                    rvalue = stmt.rvalue
                    if isinstance(rvalue, c_ast.Cast) and isinstance(rvalue.expr, c_ast.FuncCall):
                        func_call = rvalue.expr
                        if func_call.name.name in free_unused_funcs:
                            if func_call.args and func_call.args.exprs:
                                if isinstance(stmt.lvalue, c_ast.ID):
                                    malloc_calls.append((stmt.lvalue.name, stmt))
                    elif isinstance(rvalue, c_ast.FuncCall) and rvalue.name.name in free_unused_funcs:
                        if rvalue.args and rvalue.args.exprs:
                            if isinstance(stmt.lvalue, c_ast.ID):
                                malloc_calls.append((stmt.lvalue.name, stmt))

                # Handle Decl with initialization: e.g., char* abcd = (char*)malloc(10);
                if isinstance(stmt, c_ast.Decl) and stmt.init is not None:
                    init = stmt.init
                    if isinstance(init, c_ast.Cast) and isinstance(init.expr, c_ast.FuncCall):
                        func_call = init.expr
                        if func_call.name.name in free_unused_funcs:
                            if func_call.args and func_call.args.exprs:
                                malloc_calls.append((stmt.name, stmt))
                    elif isinstance(init, c_ast.FuncCall) and init.name.name in free_unused_funcs:
                        if init.args and init.args.exprs:
                            malloc_calls.append((stmt.name, stmt))
                # Recursively find all used variable names in the statement
                find_used_vars(stmt)

            # After scanning all statements, check for malloc'd pointers that are neither used nor freed
            for pointer_name, malloc_stmt in malloc_calls:
                was_freed = False
                for stmt in node.block_items:
                    if isinstance(stmt, c_ast.FuncCall) and stmt.name.name == 'free':
                        if stmt.args and stmt.args.exprs:
                            arg = stmt.args.exprs[0]
                            if isinstance(arg, c_ast.ID) and arg.name == pointer_name:
                                was_freed = True
                                break
                # Only report if pointer is neither used nor freed
                if pointer_name not in used_vars and not was_freed:
                    for rule in self.dsl_rules:
                        for check in getattr(rule, 'free_unused_checks', []):
                            func_name = check['func'] if isinstance(check, dict) and 'func' in check else check
                            # malloc_stmt may be Decl or Assignment; get function name accordingly
                            malloc_func_name = None
                            if hasattr(malloc_stmt, 'init') and malloc_stmt.init is not None:
                                # Decl with init
                                if isinstance(malloc_stmt.init, c_ast.Cast) and isinstance(malloc_stmt.init.expr, c_ast.FuncCall):
                                    malloc_func_name = malloc_stmt.init.expr.name.name
                                elif isinstance(malloc_stmt.init, c_ast.FuncCall):
                                    malloc_func_name = malloc_stmt.init.name.name
                            elif hasattr(malloc_stmt, 'rvalue') and malloc_stmt.rvalue is not None:
                                # Assignment
                                if isinstance(malloc_stmt.rvalue, c_ast.Cast) and isinstance(malloc_stmt.rvalue.expr, c_ast.FuncCall):
                                    malloc_func_name = malloc_stmt.rvalue.expr.name.name
                                elif isinstance(malloc_stmt.rvalue, c_ast.FuncCall):
                                    malloc_func_name = malloc_stmt.rvalue.name.name
                            # Fallback: if malloc_stmt.name is a string
                            if malloc_func_name is None and hasattr(malloc_stmt, 'name') and isinstance(malloc_stmt.name, str):
                                malloc_func_name = malloc_stmt.name
                            if func_name == malloc_func_name:
                                error_msg = (
                                    f"Line {malloc_stmt.coord.line - header_defs_lines_count}: Violation of rule '{rule.name}'. "
                                    f"Allocated memory for pointer '{pointer_name}' is not used or freed before end of block. "
                                    f"Message: {check['message'] if isinstance(check, dict) and 'message' in check else ''}"
                                )
                                self.errors.append(error_msg)
        
        # --- NEW: Rule implementation for 'require_null_after' ---
        # Get a list of all functions that require a null check after them
        monitored_funcs = {}
        for rule in self.dsl_rules:
            for req in rule.null_after_requires:
                monitored_funcs[req['func']] = {'rule': rule.name, 'message': req['message']}

        # Iterate through the statements in the block, looking ahead by one
        if node.block_items:
            n = len(node.block_items)
            for i in range(n):
                current_stmt = node.block_items[i]
                next_stmt = node.block_items[i + 1] if i + 1 < n else None

                # Check if the current statement is a call to a monitored function (e.g., free)
                if isinstance(current_stmt, c_ast.FuncCall) and current_stmt.name.name in monitored_funcs:
                    func_name = current_stmt.name.name
                    # Check that the function call has an argument
                    if not current_stmt.args or not current_stmt.args.exprs:
                        continue

                    pointer_freed = current_stmt.args.exprs[0].name

                    nullified = False
                    if next_stmt is not None:
                        is_assignment = isinstance(next_stmt, c_ast.Assignment) and next_stmt.op == '='
                        if is_assignment:
                            assigned_to = next_stmt.lvalue.name
                            is_null_assignment = (
                                (isinstance(next_stmt.rvalue, c_ast.Constant) and next_stmt.rvalue.value == '0') or
                                (isinstance(next_stmt.rvalue, c_ast.ID) and next_stmt.rvalue.name == 'NULL')
                            )
                            if assigned_to == pointer_freed and is_null_assignment:
                                nullified = True
                    # If not nullified, or if it's the last statement, report error
                    if not nullified:
                        rule_info = monitored_funcs[func_name]
                        error_msg = (
                            f"Line {current_stmt.coord.line - header_defs_lines_count}: Violation of rule '{rule_info['rule']}'. "
                            f"Pointer '{pointer_freed}' is not set to NULL immediately after call to '{func_name}'. "
                            f"Message: {rule_info['message']}"
                        )
                        self.errors.append(error_msg)

        # --- NEW: Rule implementation for double-free detection ---
        double_free_funcs = set()
        for rule in self.dsl_rules:
            for func in getattr(rule, 'double_free_checks', []):
                # If func is a dict, extract the function name
                if isinstance(func, dict) and 'func' in func:
                    double_free_funcs.add(func['func'])
                else:
                    double_free_funcs.add(func)

        freed_vars = set()
        if node.block_items:
            for stmt in node.block_items:
                if isinstance(stmt, c_ast.FuncCall) and stmt.name.name in double_free_funcs:
                    if stmt.args and stmt.args.exprs:
                        arg = stmt.args.exprs[0]
                        pointer_name = None
                        if isinstance(arg, c_ast.ID):
                            pointer_name = arg.name
                        # You may want to handle more complex pointer expressions here
                        if pointer_name:
                            if pointer_name in freed_vars:
                                error_msg = (
                                    f"Line {stmt.coord.line - header_defs_lines_count}: Double-free violation. "
                                    f"Pointer '{pointer_name}' is freed more than once."
                                )
                                self.errors.append(error_msg)
                            else:
                                freed_vars.add(pointer_name)


        self.generic_visit(node)