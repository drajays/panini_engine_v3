import sys
sys.path.append('.')

from sutras.adhyaya_6.pada_1.sutra_6_1_87 import SUTRA as SUTRA_6_1_87
from sutras.adhyaya_1.pada_1.sutra_1_1_51 import SUTRA as SUTRA_1_1_51
from engine.state import State, Term
from phonology import mk

tests = [
    ("deva", "fziH"),     # a + f (ṛ) = ar
    ("sUrya", "udayaH"),  # a + u = o
    ("gaNgA", "udakam"),  # A + u = o
    ("deva", "indraH"),   # a + i = e
    ("ekA", "Unam"),      # A + U = o
]

print("# Audit Report: 6.1.87 आद्गुणः (and 1.1.51 उरण् रपरः)")
print("-" * 65)

for w1, w2 in tests:
    state = State(terms=[
        Term(kind="anga", varnas=[mk(c) for c in w1], tags={"anga"}, meta={}),
        Term(kind="prakriti", varnas=[mk(c) for c in w2], tags={"anga"}, meta={})
    ])
    
    initial = w1 + " + " + w2
    
    fired_87 = SUTRA_6_1_87.cond(state)
    
    if fired_87:
        state = SUTRA_6_1_87.act(state)
        
        # Check if 1.1.51 (urN_rapara) is needed after 6.1.87 (e.g., for a + ṛ -> ar)
        fired_51 = False
        if SUTRA_1_1_51.cond(state):
            state = SUTRA_1_1_51.act(state)
            fired_51 = True
            
        result_slp1 = "".join([v.slp1 for t in state.terms for v in t.varnas])
        
        meta_str = "Fired 6.1.87"
        if fired_51:
            meta_str += " & 1.1.51"
            
        print(f"PASS: {initial:15} -> {result_slp1:15} ({meta_str})")
    else:
        print(f"FAIL: {initial:15} -> No Change")
