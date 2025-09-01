# cparser.py (Final, Pure Python Version)
import re
import pycparser

# A minimal set of C type definitions that pycparser needs to parse
# standard C code. This string contains no preprocessor directives.
MINIMAL_C_DEFS = """
    typedef int size_t;
    typedef int __builtin_va_list;
    typedef int __gnuc_va_list;
    typedef int va_list;
    typedef int __int64_t;
    typedef int __uint64_t;
    typedef int FILE;
    typedef int ptrdiff_t;
"""

header_defs_lines_count = len(MINIMAL_C_DEFS.splitlines()) if MINIMAL_C_DEFS else 0


def parse_c_code(file_path):
    """
    Parses a C file using a pure Python approach. It combines a minimal
    set of C definitions with the source code after stripping all
    preprocessor directives (#include, #define, etc.).
    """
    try:
        # Step 1: Read the user's source code
        with open(file_path, 'r', encoding='utf-8') as f:
            user_code = f.read()

        # Step 1: Create a regex to find and remove all C-style comments.
        # This handles both // single-line and /* multi-line */ comments.
        comment_re = re.compile(
            r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )

        def remove_comments(text):
            def replacer(match):
                s = match.group(0)
                if s.startswith('/'):
                    return " "
                else:
                    return s

            return re.sub(comment_re, replacer, text)

        code_no_comments = remove_comments(user_code)
        # Step 3 Remove ALL preprocessor directives from the user's code.
        # This regex finds any line starting with '#' and removes it.
        cleaned_code = re.sub(r'^#.*$', '', user_code, flags=re.MULTILINE)

        # Step 3: Combine our minimal definitions with the cleaned user code.
        full_code_to_parse = MINIMAL_C_DEFS + cleaned_code

        # Step 4: Parse the final, pure C code string.
        parser = pycparser.CParser()
        ast = parser.parse(full_code_to_parse, filename=file_path)
        return ast

    except Exception as e:
        print(f"[!] Error parsing C code: {e}")
        return None