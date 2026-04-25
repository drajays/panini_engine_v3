import re
from pathlib import Path

def main():
    canon = Path("core/canonical_pipelines.py")
    krdanta = Path("pipelines/krdanta.py")
    test_file = Path("tests/constitutional/test_no_new_duplicates.py")

    # 1. Fix the variable name in the test file for the ratchet script
    if test_file.exists():
        t_text = test_file.read_text()
        t_text_fixed = re.sub(
            r"(MAX_ALLOWED_DUPLICATES|MAX_DUPLICATES|ALLOWED_DUPLICATES)\s*=", 
            "MAX_DUPLICATE_GROUPS =", 
            t_text
        )
        if "MAX_DUPLICATE_GROUPS" not in t_text_fixed:
            t_text_fixed += "\nMAX_DUPLICATE_GROUPS = 10\n"
        test_file.write_text(t_text_fixed)

    # 2. Add helper to canonical_pipelines.py
    canon_text = canon.read_text()
    fn_name = "P01_samjna_1_1_3_to_1_1_100"

    # Auto-detect dispatch function name
    dispatch_fn = "apply_rule"
    if "apply_sutra(" in canon_text: dispatch_fn = "apply_sutra"
    elif "run_sutra(" in canon_text: dispatch_fn = "run_sutra"

    new_fn = f"""
def {fn_name}(state):
    for sid in ["1.1.3", "1.1.7", "1.1.8", "1.1.9", "1.1.10", "1.1.11", "1.1.12", "1.1.13", "1.1.14", "1.1.100"]:
        state = {dispatch_fn}(state, sid)
    return state
"""
    if fn_name not in canon_text:
        canon.write_text(canon_text + "\n" + new_fn)
        print(f"✓ Added {fn_name} to canonical_pipelines.py")

    # 3. Replace duplicate blocks in krdanta.py
    krdanta_text = krdanta.read_text()
    # Matches the exact sequence of rule applications, preserving indentation
    pattern = r"(?sm)^([ \t]*)(state\s*=\s*\w+\(state,\s*['\"]1\.1\.3['\"]\).*?state\s*=\s*\w+\(state,\s*['\"]1\.1\.100['\"]\))"

    def replacer(match):
        indent = match.group(1)
        return f"{indent}# Collapsed structural block 1685e23755e3\n{indent}state = {fn_name}(state)"

    new_krdanta, count = re.subn(pattern, replacer, krdanta_text)

    if count > 0:
        if fn_name not in new_krdanta:
            lines = new_krdanta.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("import ") or line.startswith("from "):
                    lines.insert(i+1, f"from core.canonical_pipelines import {fn_name}")
                    break
            new_krdanta = "\n".join(lines) + "\n"
        krdanta.write_text(new_krdanta)
        print(f"✓ Successfully collapsed {count} blocks in krdanta.py")
    else:
        print("⚠ No matching sutra blocks found in krdanta.py. Check if already collapsed.")

if __name__ == "__main__":
    main()
