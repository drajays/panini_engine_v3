import sys
sys.path.append('.')

from sutras.adhyaya_6.pada_1.sutra_6_1_101 import SUTRA
from engine.state import State, Term
from phonology import mk

tests = [
    ("muni", "ISaH"),
    ("SrI", "ISaH"),
    ("BAnu", "udayaH"),
    ("daitya", "ariH"),
    ("gaNgA", "ariH"),
    ("nadI", "indraH"),
]

print("# Audit Report: 6.1.101 अकः सवर्णे दीर्घः")
print("-" * 50)

for w1, w2 in tests:
    # Build a simple state with two terms
    state = State(terms=[
        Term(kind="prakriti", varnas=[mk(c) for c in w1], tags=set(), meta={}),
        Term(kind="prakriti", varnas=[mk(c) for c in w2], tags=set(), meta={})
    ])
    
    initial = w1 + " + " + w2
    
    # Check if cond() fires
    fires = SUTRA.cond(state)
    
    if fires:
        # Act and see the output
        new_state = SUTRA.act(state)
        result_slp1 = "".join([v.slp1 for t in new_state.terms for v in t.varnas])
        print(f"PASS: {initial:15} -> {result_slp1:15} (Fired: Yes)")
    else:
        print(f"FAIL: {initial:15} -> No Change      (Fired: No)")
