from engine import SecurityAuditor

def run_checker(dsl_rules, c_ast, source_lines=None):
    if c_ast is None:
        return ["[!] AST is empty. Cannot run analysis."]

    try:
        auditor = SecurityAuditor(dsl_rules, source_lines)
        errors = auditor.run_analysis(c_ast)
        return errors if errors else []
    except Exception as e:
        return [f"[!] Error while running checker: {e}"]
