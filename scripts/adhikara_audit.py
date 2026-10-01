"""1b: compare adhikāra ids each sutra module consults (adhikara_in_effect / stack id checks) with the ashtadhyayi.com adhikara corpus -> docs/ADHIKARA_AUDIT.md"""
import glob, re, collections
ROOT = "/Users/dr.ajayshukla/ashtadhyayi/adhikara"
def corpus(sid):
    a, p, _ = sid.split(".")
    try: return set(re.findall(r"\[(\d+\.\d+\.\d+)\]", open(f"{ROOT}/pada-{a}.{p}/{sid}.txt").read()))
    except FileNotFoundError: return None
rows, tot = [], collections.Counter()
for f in sorted(glob.glob("sutras/adhyaya_*/pada_*/sutra_*.py")):
    m = re.search(r"sutra_(\d+)_(\d+)_(\d+)\.py", f); sid = ".".join(m.groups())
    src = open(f).read()
    used = set(re.findall(r'adhikara_in_effect\([^,]+,[^,]+,\s*["\'](\d+\.\d+\.\d+)["\']', src))
    used |= set(re.findall(r'e\.get\("id"\)\s*==\s*["\'](\d+\.\d+\.\d+)["\']', src))
    used.discard(sid)
    gov = corpus(sid)
    if gov is None: tot["no corpus file"] += 1; continue
    if not used and not gov: tot["both empty"] += 1; continue
    if not used: tot["corpus governs, code silent"] += 1; rows.append((sid, "code silent", "", sorted(gov))); continue
    if used <= gov: tot["code consults a governing adhikara"] += 1; continue
    tot["code consults adhikara corpus does not list"] += 1; rows.append((sid, "MISMATCH", sorted(used - gov), sorted(gov)))
out = ["# Adhikāra audit (sutras/ code vs ashtadhyayi.com corpus)", "", *[f"- {k}: {v}" for k, v in tot.items()], "",
       "'code silent' = corpus says an adhikāra governs the sūtra but the module never checks one (it may be implicit via phase frames).", "",
       "## Mismatches (code checks an adhikāra the corpus doesn't list)", ""]
out += [f"- {s}: code {u}, corpus {g}" for s, k, u, g in rows if k == "MISMATCH"]
out += ["", "## Silent (first 150)", ""] + [f"- {s}: {g}" for s, k, u, g in rows if k != "MISMATCH"][:150]
open("docs/ADHIKARA_AUDIT.md", "w").write("\n".join(out) + "\n"); print(dict(tot))
