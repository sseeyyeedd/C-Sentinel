# cparser.py (Final Diagnostic Version)
import os
import subprocess
import pycparser


def parse_c_code(file_path):
    """
    This is a diagnostic version to find the exact reason the
    preprocessor is failing.
    """
    print("[*] Preparing to preprocess the C file...")
    try:
        # Step 1: Find the path to pycparser's fake headers
        pycparser_path = os.path.dirname(pycparser.__file__)
        fake_includes_path = os.path.join(pycparser_path, 'utils', 'fake_includes')

        print(f"[*] Found fake includes path at: {fake_includes_path}")

        # Step 2: Build the complete command
        command = [
            'gcc',
            '-E',
            '-nostdinc',
            '-I' + fake_includes_path,
            file_path
        ]

        # --- DIAGNOSTIC STEP ---
        print("\n--- Please run the following command manually in your terminal ---")
        # To make it easy to copy, we'll format it as a single string
        command_str = ' '.join(f'"{c}"' if ' ' in c else c for c in command)
        print(f"\n{command_str}\n")
        print("--- After running it, report if it succeeded or failed ---")
        import sys
        sys.exit()
        # --- END DIAGNOSTIC STEP ---

    except Exception as e:
        print(f"[!] An error occurred before preprocessing: {e}")
        return None