"""
7.3.32  हनस्तोऽचिण्णलोः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=73032
- Kāśikā: "घातः, घातकः।" (चिण्-णल्-वर्जं णिति नकारस्य तकारः)
- Cross-validation: tests/unit/test_bhattikavya_1_2.py (समूलघातम्)

णित् परे (चिण्/णल् वर्जयित्वा) हन्-धातोः नकारस्य तकारः।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk

_GATE_KEY: str = "7_3_32_hanastoci_32"
_BLOCKED = frozenset({"ciR", "Ral", "Nal"})


def _nit_follows(state: State, di: int) -> bool:
    for j in range(di + 1, len(state.terms)):
        pr = state.terms[j]
        if pr.kind != "pratyaya":
            continue
        up = (pr.meta.get("upadesha_slp1") or "").strip()
        if up in _BLOCKED:
            return False
        itm = pr.meta.get("it_markers") or set()
        if "N" in itm or "R" in itm or "nit" in pr.tags:
            return True
        if up in {"Ramul", "Namul", "Rvul"}:
            return True
    return False


def _site(state: State):
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return None
    if not adhikara_in_effect("7.3.32", state, "6.4.1"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or not t.varnas:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in {"han", "han~"} and t.varnas[0].slp1 not in {"h", "G"}:
            continue
        # final n of हन् / घन् / घान्
        if t.varnas[-1].slp1 != "n":
            continue
        if not _nit_follows(state, i):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = mk("t")
    t.meta["7_3_32_n_to_t_done"] = True
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.32",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'hanastociRRaloH',
    text_dev              = 'हनस्तोऽचिण्णलोः',
    padaccheda_dev        = "हनः तः अ-चिण्-णलोः",
    why_dev               = "णिति परे हन्तेर्नकारस्य तकारः — चिण्-णल् वर्जयित्वा (घातम्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
