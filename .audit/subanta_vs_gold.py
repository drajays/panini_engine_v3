"""Scanner(+resolver) vs vendored gold: which (winner > loser) decisions precede a wrong form?"""
import json, glob, collections
import sutras
from pipelines.subanta import derive
bad=collections.Counter(); ex={}; tot=ok=0
for f in sorted(glob.glob('data/reference/shabda_gold/*.json')):
    d=json.load(open(f)); stem=d['stem_slp1']; linga=d['linga']
    for cell,forms in d['cells'].items():
        v,n=map(int,cell.split('-')); tot+=1
        try: s=derive(stem,v,n,linga=linga,autonomous_scanner=True)
        except Exception as e: bad[('ERR',type(e).__name__)]+=1; continue
        if s.flat_dev() in forms: ok+=1; continue
        pairs={(t['sutra_id'],t.get('block_reason','')[:60]) for t in s.trace if t.get('status')=='BLOCKED'}
        key=tuple(sorted(pairs))
        bad[key]+=1; ex.setdefault(key,(stem,cell,s.flat_dev(),forms))
print(tot,ok)
for k,c in bad.most_common(25): print(c,ex.get(k),'\n    ',k)
