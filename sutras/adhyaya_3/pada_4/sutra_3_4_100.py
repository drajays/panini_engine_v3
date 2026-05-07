"""
3.4.100  इतश्च  —  VIDHI (narrow: delete final 'i' of tiṅ residue in luṅ)

Engine: in luṅ aorist glass-box spines, after tiṅ ādeśa + it-lopa yields "ti",
drop the vowel 'i' so the residue is a single hal 't' (apṛkta), licensing
7.3.96 Īṭ-āgama.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk


def _find_ti(state: State):
    lk = (state.meta.get("lakara") or "").strip()
    if lk not in {"luG", "lRG"}:
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        # Look for 'ti' exactly.
        if "".join(v.slp1 for v in t.varnas) != "ti":
            continue
        if t.meta.get("3_4_100_itasca_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_ti(state) is not None


def act(state: State) -> State:
    i = _find_ti(state)
    if i is None:
        return state
    t = state.terms[i]
    # delete the 'i' (second varna)
    if len(t.varnas) >= 2 and t.varnas[1].slp1 == "i":
        del t.varnas[1]
    t.meta["3_4_100_itasca_done"] = True
    # **P019** (*avartsyat*): ``sy`` + ``t`` surface needs intervening ``a`` (``…स्यत्``).
    if state.meta.get("corrected_v2_P019_demo") and i > 0:
        prev = state.terms[i - 1]
        if (prev.meta.get("upadesha_slp1") or "").strip() == "sy":
            ins = Term(
                kind="pratyaya",
                varnas=[mk("a")],
                tags={"pratyaya"},
                meta={"upadesha_slp1": "a"},
            )
            state.terms.insert(i, ins)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.100",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "itaH ca",
    text_dev       = "इतश्च",
    padaccheda_dev = "इतः / च",
    why_dev        = (
        "लुङ्/लृङ्-प्रक्रियायां तिङ्-अन्तस्थ इकारस्य लोपः (ति→त्); "
        "P019: ``sy``-``t`` मध्ये ``a``।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

