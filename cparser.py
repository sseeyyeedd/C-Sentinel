from pycparser import c_parser, c_ast

class CParser:
    def __init__(self):
        self.parser = c_parser.CParser()

    def parse(self, source_code):
        try:
            ast = self.parser.parse(source_code)
            return ast
        except Exception as e:
            print("Error parsing C code:", e)
            return None


def parse_c_code(file_path):
    with open(file_path, 'r') as f:
        source = f.read()
    cp = CParser()
    return cp.parse(source)