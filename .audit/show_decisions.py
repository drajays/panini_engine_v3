import sys, sutras
import engine.resolver as R
import pipelines.subanta as S
orig=R.resolve_with_reason
def spy(c,st,*a,**k):
    d=orig(c,st,*a,**k)
    if len(c)>1: print(f"   {st.flat_slp1():<16} {sorted(c)} -> {d.winner} [{d.layer}]")
    return d
R.resolve_with_reason=spy
stem,v,n,linga=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
s=S.derive(stem,v,n,linga=linga,autonomous_scanner=True); print(s.flat_slp1())
