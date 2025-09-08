from pycparser import c_ast, c_generator

def normalize_ast(ast):
    modifications = []

    class ASTNormalizer(c_ast.NodeVisitor):
        def visit_Assignment(self, node):
            if node.op != '=':
                node.op = '='
                modifications.append(f"Changed assignment operator at line {node.coord.line} to '='")
            self.generic_visit(node)

        def visit_BinaryOp(self, node):
            if node.op not in ['+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=']:
                modifications.append(f"Binary op '{node.op}' at line {node.coord.line} replaced with '+'")
                node.op = '+'
            self.generic_visit(node)

    normalizer = ASTNormalizer()
    normalizer.visit(ast)

    return ast, modifications
