"""
3.4.100  इतश्च  —  VIDHI (laṅ/luṅ/lṛṅ: drop final 'i' of tiṅ ādeśa)

Drops the final 'i' of a tiṅ ādeśa in laṅ / luṅ / lṛṅ contexts:
  tip→ti → t,  sip→si → s,  jhi → jh  (then 7.1.3 converts jh→ant for 3pl).

Note: mip→mi is handled by 3.4.101 (apavāda); 3.4.100 naturally skips 'mi'
when 3.4.101 has already converted it to 'am' (varnas end in 'm' not 'i').
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk


def _find_i_final_tin(state: State):
    """Find a tiṅ ādeśa term ending in 'i' in laṅ/luṅ/lṛṅ context."""
    lk = (state.meta.get("lakara") or "").strip()
    if lk not in {"luG", "lRG", "laG", "liG", "AsIrliG"}:
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_100_itasca_done"):
            continue
        vs = t.varnas
        if not vs or vs[-1].slp1 != "i":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_i_final_tin(state) is not None


def act(state: State) -> State:
    i = _find_i_final_tin(state)
    if i is None:
        return state
    t = state.terms[i]
    # Drop the final 'i' varna.
    if t.varnas and t.varnas[-1].slp1 == "i":
        del t.varnas[-1]
    t.meta["3_4_100_itasca_done"] = True
    # P019 (avartsyat): sy + t needs intervening a between vikaraṇa and t.
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
        "लङ्/लुङ्/लृङ्-प्रक्रियायां तिङ्-अन्तस्थ इकारस्य लोपः "
        "(ति→त्, सि→स्, झि→झ्); लङि: ७.१.३-पूर्वं झि→झ् → अन्त्।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

