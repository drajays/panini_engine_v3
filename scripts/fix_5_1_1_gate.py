"""One-off: replace the out-of-scope 5.1.1 adhikara gate in 5.x sutra modules by the most specific
corpus-governing registered adhikara (ashtadhyayi.com adhikara/ data)."""
import glob, re
ROOT = "/Users/dr.ajayshukla/ashtadhyayi/adhikara"
T = lambda s: tuple(map(int, s.split(".")))
scope = {}
for f in glob.glob("sutras/adhyaya_[345]/*/*.py"):
    s = open(f).read(); m = re.search(r'adhikara_scope\s*=\s*\("([\d.]+)",\s*"([\d.]+)"\)', s)
    if "SutraType.ADHIKARA" in s and m: scope[m.group(1)] = m.group(2)
n = 0
for f in glob.glob("sutras/adhyaya_5/*/*.py"):
    s = open(f).read()
    if not re.search(r'adhikara_in_effect\([^)]*"5\.1\.1"\)', s): continue
    sid = re.search(r"sutra_(\d+_\d+_\d+)", f).group(1).replace("_", ".")
    if T(sid) <= (5, 1, 17): continue
    a, p, _ = sid.split(".")
    g = [x for x in re.findall(r"\[(\d+\.\d+\.\d+)\]", open(f"{ROOT}/pada-{a}.{p}/{sid}.txt").read()) if T(x) < T(sid)]
    h = max((x for x in g if x in scope and T(scope[x]) >= T(sid)), key=T)
    s2 = re.sub(r'(adhikara_in_effect\([^)]*)"5\.1\.1"\)', rf'\1"{h}")', s)
    s2 = s2.replace("anuvritti_from        = ('5.1.1',)", f"anuvritti_from        = ('{h}',)")
    open(f, "w").write(s2); n += 1
print(n)
