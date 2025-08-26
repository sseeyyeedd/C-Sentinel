from antlr4 import *
import argparse
from parser import parse_dsl_rules
from cparser import parse_c_code
from engine import SecurityAuditor

def main():
    # بخش ۱: دریافت ورودی‌ها از خط فرمان
    arg_parser = argparse.ArgumentParser(description='CSentinel - A C Static Analyzer based on a custom DSL.')
    arg_parser.add_argument('--rules', required=True, help='Path to the CSentinel rule file (.sen)')
    arg_parser.add_argument('--source', required=True, help='Path to the C source file to analyze')
    args = arg_parser.parse_args()

    # بخش ۲: فراخوانی پارسرها
    print(f"[*] Loading rules from: {args.rules}")
    dsl_rules = parse_dsl_rules(args.rules)
    print(f"[*] Successfully loaded {len(dsl_rules)} rule(s).")
    # print(dsl_rules) # می‌توانید برای دیباگ کردن، قوانین خوانده شده را چاپ کنید

    print(f"[*] Parsing C source from: {args.source}")
    c_ast = parse_c_code(args.source)
    if not c_ast:
        print("[!] Failed to parse C code. Please check the source file for errors. Exiting.")
        return
    print("[*] C code parsed successfully into an AST.")

    # بخش ۳: فراخوانی موتور تحلیل (در گام بعدی تکمیل می‌شود)
    print("\n--- Running Security Analysis ---")

    # auditor = SecurityAuditor(dsl_rules)
    # errors = auditor.run_analysis(c_ast)

    # فعلا به صورت موقت یک لیست خالی برای خطاها در نظر می‌گیریم
    auditor = SecurityAuditor(dsl_rules)
    errors = auditor.run_analysis(c_ast)

    # بخش ۴: گزارش نتایج
    if errors:
        print(f"\n[!] Found {len(errors)} security violation(s):")
        for error in errors:
            print(f"  - {error}")
    else:
        print("\n[*] Analysis complete. No violations found (engine not yet implemented).")


if __name__ == '__main__':
    main()