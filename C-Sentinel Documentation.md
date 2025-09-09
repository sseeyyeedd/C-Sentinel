#  C-Sentinel: Static Analysis & DSL Guide For Compilers Like C

**C-Sentinel** is a static analysis tool for detecting **security vulnerabilities** in C code using a custom rule-based DSL (Domain-Specific Language).  
It combines **ANTLR-based DSL parsing** with **pycparser’s C AST parsing** to apply **security checks** automatically.

## Members

-- 1. **Seyed Ali Hosseini** . [Github_link](https://github.com/sseeyyeedd)

-- 2. **Mahdi Mazloomi** . [Github_link](https://github.com/mahdimm82)

-- 3. **Meysam Asali** . [Github_link](https://github.com/MeysamAsali)

-- 4. **Ramin Kalantari** . [Github_link](https://github.com/ramklan1234).

---

##  High-Level Architecture

- **DSL Rule Parsing**: ANTLR grammar defines the `.sen` DSL, parsed in Python.
    
-  **C Code Parsing**: C source → AST via pycparser.
    
-  **AST Normalization**: Simplifies AST for rule checking.
    
- **Security Analysis**: Rule-based checks (buffer overflows, taint, memory safety…).
    
-  **Reporting**: Violations reported in CLI.
    

Main components:

-  `main.py`: Entry point, CLI tool, orchestrates workflow.
    
-  `parser.py`: Parses DSL rules via ANTLR.
    
-  `cparser.py`: Wraps C parsing logic.
    
-  `engine.py`: Core analysis + AST visitors (overflow, taint, format, etc.).
    
-  `checker.py`: Runs the auditor.
    
-  `.antlr/`: ANTLR-generated files.
    

---

## Using C-Sentinel

### 1️⃣ Rule System (`.sen` Files)

Rules are defined in **C-Sentinel DSL**.  
Examples: block dangerous functions, enforce literal format strings, check null access, prevent double-free, etc.

Grammar defined in: `CSentinel.g4`.

---

### 2️⃣ Running the Tool

```bash
python main.py --rules <path-to-rules.sen> --source <path-to-source.c>
```

- `--rules`: Path to `.sen` rule file.
    
- `--source`: Path to `.c` file for analysis.
    

 **Example Output:**

```
[*] Loading rules from: rules.sen
[*] Successfully loaded 5 rule(s).
[*] Parsing C source from: test.c
[*] C code parsed successfully into an AST.
[*] Normalizing AST...
[*] AST normalized with 2 modification(s).

--- Running Security Analysis ---

[!] Found 1 security violation(s):

  - Function 'strcpy' is forbidden by ruleset.

[*] Analysis complete.
```

---

### 3️⃣ How It Works (Internals)

1.  **Load DSL Rules** (ANTLR → internal rule model).
    
2.  **Parse Source Code** (C → AST via pycparser).
    
3.  **Normalize AST** (simplify for matching).
    
4.  **Run Security Analysis**:
    
    - Stateless checks → forbidden functions, format string rules.
        
    - Stateful checks → integer overflow, taint flow, memory safety.
        
5. **Report Violations** (human-readable output).
    

---

##  CSentinel DSL Grammar Guide

This section explains how to write `.sen` files.

---

###  File Structure

A `.sen` file = multiple rules:

```sen
rule <RuleName> {
    ...contents...
}
```

---

###  Rule Types

#### 1. Block Rule

Block dangerous functions:

```sen
block <FunctionName> {
    error "Reason"
}
```

An Example:

```sen
block system {
    error "system() is forbidden due to command injection risks."
}
```

---

#### 2. 📞 On Call Rule

Checks when a function is **called**:

```sen
on call <FunctionName>(params...) {
    ...checks...
}
```

Allowed checks:

- `if <expr> overflows { ... }`
    
- `require_literal_format { ... }`
    
- `require_null_after { ... }`
    
- `require_no_double_free { ... }`
    
- `require_auto_free_unused { ... }`
    

✅ Example:

```sen
on call strcpy(dst, src) {
    require_literal_format {
        error "Only literal format strings are allowed."
    }
    if length(src) overflows {
        error "Buffer overflow risk detected."
    }
}
```

---

#### 3. 👁 On Access Rule

Checks when a variable is accessed:

```sen
on access <VariableName> {
    require_not_null {
        error "Variable must not be null."
    }
}
```

✅ Example:

```sen
on access buffer {
    require_not_null {
        error "Buffer cannot be null before use."
    }
}
```

---

#### 4. Untrusted Source Rule

Mark a function as an **untrusted data source**:

```sen
source <FunctionName> {
    error "Reason"
}
```

An Example:

```sen
source getenv {
    error "Environment variables are untrusted input."
}
```

---

#### 5. Dangerous Sink Rule

Mark a function as a **dangerous sink**:

```sen
sink <FunctionName> {
    error "Reason"
}
```

An Example:

```sen
sink printf {
    error "Direct printf() may lead to format string vulnerabilities."
}
```

---

#### 6. Sanitizer Rule

Define a **sanitizer** (safe function):

```sen
sanitizer <FunctionName> {
}
```

✅ Example:

```sen
sanitizer escape_html {
}
```

---

### Math Expressions

Rules can use simple math expressions:

```sen
if x + y overflows {
    error "Integer overflow detected."
}
```

Operators: `+`, `-`, `*`, `/`  
Operands: variables or numbers.

---

### 🎯 Actions

Each rule specifies an action, typically:

```sen
error "Message here."
```

An Example:

```sen
error "Freeing memory twice is forbidden."
```

---

## A Complete Example

```sen
rule MemorySafety {
    block free {
        error "Manual calls to free() are not allowed."
    }

    on call strcpy(dst, src) {
        if length(src) overflows {
            error "Possible buffer overflow in strcpy."
        }
    }

    on access buffer {
        require_not_null {
            error "Buffer must not be null."
        }
    }
}
```

---

## 📌 Quick Cheat Sheet

|Rule Type|Syntax Example|Purpose|
|---|---|---|
|🚫 Block|`block free { error "..." }`|Ban dangerous functions|
|📞 On Call|`on call strcpy(...) { ... }`|Add checks on function calls|
|👁 On Access|`on access var { require_not_null { ... } }`|Enforce null-safety on variables|
|🟢 Source|`source getenv { error "..." }`|Mark untrusted input sources|
|🔴 Sink|`sink printf { error "..." }`|Mark unsafe data sinks|
|🧼 Sanitizer|`sanitizer escape_html { }`|Define functions that sanitize inputs|

---

## References

-  [pycparser Documentation](https://github.com/eliben/pycparser)
    
-  [ANTLR Documentation](https://www.antlr.org/)
    
-  Project Source: [sseeyyeedd/C-Sentinel](https://github.com/sseeyyeedd/C-Sentinel)
    

---