import subprocess, sys, glob
files=sys.argv[1:] or sorted(glob.glob('tests/**/test_*.py',recursive=True))
bad=[]
for f in files:
    try:
        r=subprocess.run([sys.executable,'-m','pytest',f,'-q','-p','no:cacheprovider','-q'],capture_output=True,text=True,timeout=400)
        last=r.stdout.strip().splitlines()[-1] if r.stdout.strip() else 'no output'
    except subprocess.TimeoutExpired: last='TIMEOUT'
    if 'passed' not in last or 'failed' in last or last=='TIMEOUT':
        bad.append((f,last)); print('BAD',f,last,flush=True)
print('done',len(files),'bad',len(bad))
