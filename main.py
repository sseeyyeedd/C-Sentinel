from antlr4 import *
import argparse
from parser import parse_dsl_rules
from cparser import parse_c_code
from checker import run_checker
from transformer import normalize_ast

def main():
    arg_parser = argparse.ArgumentParser(description='CSentinel - A C Static Analyzer based on a custom DSL.')
    arg_parser.add_argument('--rules', required=True, help='Path to the CSentinel rule file (.sen)')
    arg_parser.add_argument('--source', required=True, help='Path to the C source file to analyze')
    args = arg_parser.parse_args()

    print(f"[*] Loading rules from: {args.rules}")
    dsl_rules = parse_dsl_rules(args.rules)
    print(f"[*] Successfully loaded {len(dsl_rules)} rule(s).")

    print(f"[*] Parsing C source from: {args.source}")
    try:
        with open(args.source,'r',encoding='utf-8') as f:
            source_code_lines = f.readlines()
    except Exception as e:
        print(f"[!] Error reading source file: {e}")
        return

    c_ast = parse_c_code(args.source)
    if not c_ast:
        print("[!] Failed to parse C code. Please check the source file for errors. Exiting.")
        return
    print("[*] C code parsed successfully into an AST.")

    print("[*] Normalizing AST...")
    c_ast, mods = normalize_ast(c_ast)
    if mods:
        print(f"[*] AST normalized with {len(mods)} modification(s).")

    print("\n--- Running Security Analysis ---")
    errors = run_checker(dsl_rules, c_ast, source_code_lines)

    if errors:
        print(f"\n[!] {len(errors)} تخلف امنیتی پیدا شد:")
        for v in errors:
            print("\n----------------------------------------")
            print(f"- خط {v.line}: {v.message}")
            print(f"\t> {v.code_line}")
            if v.suggestion:
                print(f"\t💡 پیشنهاد: {v.suggestion}")
        print("----------------------------------------")
    else:
        print("\n[*] تحلیل کامل شد. هیچ تخلفی پیدا نشد.")

if __name__ == '__main__':
    main()
