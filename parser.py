from antlr4 import FileStream, CommonTokenStream
from gen.CSentinelLexer import CSentinelLexer
from gen.CSentinelParser import CSentinelParser
from gen.CSentinelVisitor import CSentinelVisitor

class DSLRule:
    def __init__(self, name):
        self.name = name
        self.blocks = []
        self.calls = []
        self.literal_requires = []
        self.null_after_requires = []
        self.sources = []
        self.sinks = []
        self.sanitizers = []

    def __repr__(self):
        return f"DSLRule(name={self.name}, blocks={self.blocks}, calls={self.calls})"

class RuleVisitor(CSentinelVisitor):
    def __init__(self):
        self.rules = []

    def visitSenFile(self, ctx):
        for rule_ctx in ctx.rule_():
            self.visit(rule_ctx)
        return self.rules

    def visitRule(self, ctx):
        name = ctx.ID().getText()
        rule = DSLRule(name)
        for child in ctx.children:
            if isinstance(child, CSentinelParser.BlockRuleContext):
                op = child.ID().getText()
                message = child.action().STRING().getText().strip('"')
                rule.blocks.append((op, message))
            elif isinstance(child, CSentinelParser.OnRuleContext):
                func = child.ID(0).getText()
                args = [arg.getText() for arg in child.ID()[1:]] if child.ID() else []
                ifStmt = child.ifStmt(0) if child.ifStmt() else None
                if ifStmt:
                    condition = ifStmt.expr().getText()
                    message = ifStmt.action().STRING().getText().strip('"')
                    rule.calls.append({"func": func, "args": args, "condition": condition, "message": message})
                elif child.requireLiteralStmt():
                    requireStmt = child.requireLiteralStmt(0)
                    message = requireStmt.action().STRING().getText().strip('"')
                    rule.literal_requires.append({"func": func, "message": message})
                elif child.requireNullStmt():
                    requireStmt = child.requireNullStmt(0)
                    message = requireStmt.action().STRING().getText().strip('"')
                    rule.null_after_requires.append({"func": func, "message": message})
            elif isinstance(child, CSentinelParser.SourceRuleContext):
                func_name = child.ID().getText()
                message = child.action().STRING().getText().strip('"')
                rule.sources.append({'func': func_name, 'message': message})
            elif isinstance(child, CSentinelParser.SinkRuleContext):
                func_name = child.ID().getText()
                message = child.action().STRING().getText().strip('"')
                rule.sinks.append({'func': func_name, 'message': message})
            elif isinstance(child, CSentinelParser.SanitizerRuleContext):
                func_name = child.ID().getText()
                rule.sanitizers.append(func_name)
        self.rules.append(rule)


def parse_dsl_rules(file_path):
    stream = FileStream(file_path)
    lexer = CSentinelLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = CSentinelParser(tokens)
    tree = parser.senFile()

    visitor = RuleVisitor()
    rules = visitor.visit(tree)
    return rules
