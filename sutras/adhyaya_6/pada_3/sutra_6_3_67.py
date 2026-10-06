"""
6.3.67  अरुर्द्विषदजन्तस्य मुम्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=63067
- Kāśikā: "अरुंतम्, द्विषंतम्, परंतपः।"
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (परंतपः)

Before a *khit* affix, *ajanta* (and अरुस्/द्विषत्) upapada takes **मुम्**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_GATE_KEY: str = "6_3_67_arurdvizad_67"
_AC = frozenset("aAiIuUfFxXeEoO")


def _khit_present(state: State) -> bool:
    for t in state.terms:
        up = (t.meta.get("upadesha_slp1") or "").strip()
        marks = t.meta.get("it_markers") or set()
        if up == "Kac" or t.meta.get("khit") is True or "K" in marks:
            return True
    return False


def _upapada_idx(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.meta.get("6_3_67_mum_done"):
            continue
        if "dhatu" in t.tags or t.kind == "pratyaya":
            continue
        if not t.varnas:
            continue
        flat = "".join(v.slp1 for v in t.varnas)
        ajanta = t.varnas[-1].slp1 in _AC
        named = flat in {"arus", "aruz", "dvizat", "para"} or (t.meta.get("upadesha_slp1") or "") in {
            "para", "arus", "dvizat",
        }
        if ajanta or named:
            return i
    return None


def cond(state: State) -> bool:
    return _khit_present(state) and _upapada_idx(state) is not None


def act(state: State) -> State:
    i = _upapada_idx(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas.append(mk("m"))
    t.meta["6_3_67_mum_done"] = True
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.67",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "arurdvizadajantasya mum",
    text_dev              = "अरुर्द्विषदजन्तस्य मुम्",
    samagra_slp1          = "uttarapade arus-dvizas-ajantasya mum treH anavyayasya Kiti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे अरुस्-द्विषस्-अजन्तस्य मुम् त्रेः अनव्ययस्य खिति",
    padaccheda_dev        = "अरुः-द्विषत्-अच्-अन्तस्य मुम्",
    why_dev               = "खिद्-परे अजन्त-उपपदस्य मुम् (पर → परम् → परं)।",
    anuvritti_from        = ('6.3.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
