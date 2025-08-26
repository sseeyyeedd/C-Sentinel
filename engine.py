# engine.py
from pycparser import c_ast

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
        self.errors = []
        self.visit(c_ast)
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
                        f"Line {node.name.coord.line}: Violation of rule '{rule.name}'. "
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
                                    f"Line {node.name.coord.line}: Violation of rule '{rule.name}'. "
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
                                f"Line {node.name.coord.line}: Violation of rule '{rule.name}'. "
                                f"Call to '{function_name}' requires a string literal as the first argument. "
                                f"Message: {require_rule['message']}"
                            )
                            self.errors.append(error_msg)