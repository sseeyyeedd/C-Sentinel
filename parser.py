from antlr4 import FileStream, CommonTokenStream
from gen.CSentinelLexer import CSentinelLexer
from gen.CSentinelParser import CSentinelParser
from gen.CSentinelVisitor import CSentinelVisitor

class DSLRule:
    def __init__(self, name):
        self.name = name
        self.blocks = []
        self.calls = [] 

    def __repr__(self):
        return f"DSLRule(name={self.name}, blocks={self.blocks}, calls={self.calls})"

class RuleVisitor(CSentinelVisitor):
    def __init__(self):
        self.rules = []

    def visitDslFile(self, ctx):
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
                args = [arg.getText() for arg in child.ID()[1:]]
                ifStmt = child.ifStmt()
                if ifStmt:
                    left = ifStmt.expr().ID(0).getText()
                    right = ifStmt.expr().ID(1).getText()
                    condition = f"{left} + {right}"
                    message = ifStmt.action().STRING().getText().strip('"')
                    rule.calls.append({"func": func, "args": args, "condition": condition, "message": message})
        self.rules.append(rule)


def parse_dsl_rules(file_path):
    stream = FileStream(file_path)
    lexer = CSentinelLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = CSentinelParser(tokens)
    tree = parser.dslFile()

    visitor = RuleVisitor()
    rules = visitor.visit(tree)
    return rules
