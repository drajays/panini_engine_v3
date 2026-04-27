# Scheduling block audit (``apply_rule`` chains)

Read-only AST scan of **ordered** ``apply_rule("x.y.z", …)`` calls.  Strings that are not the first argument to ``apply_rule`` are ignored.

- **scanned_py_files**: `20`
- **duplicate_cross_file_groups**: `0`

## Result

**CLEAN**: no duplicate contiguous ``apply_rule`` blocks (length ≥ 3) found across multiple files.
