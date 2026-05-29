"""
7.1.93  अनङ् सौ  —  VIDHI

Padaccheda: अनङ् सौ

In the 1sg (sau = su pratyaya context), the stem sakhi takes the ādeśa
"anang" (= aN = [a,n] after ṅ-IT lopa). ṅit→antya-ādeśa: replaces the
final 'i' of sakhi with [a,n].

Result: sakh+[i] → sakh+[a,n] = sakhan
Then 6.4.8 dīrgha: sakhān
Then 6.1.68 apṛkta s-lopa, then 8.2.7 n-lopa: sakhā

Engine: arm ``anaN_recipe`` + finds sakhi-type stem (prātipadika ending in 'i'
tagged sakhi_ikarant) and replaces final 'i' with [a,n] (anang after ṅ-lopa).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology     import mk

_GATE_KEY: str = "7_1_93_anaN_93"


def _find_sakhi_stem(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "sakhi_ikarant" not in t.tags:
            continue
        if t.meta.get("7_1_93_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 not in {"i", "I"}:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not state.meta.get("anaN_recipe"):
        return False
    return _find_sakhi_stem(state) is not None


def act(state: State) -> State:
    idx = _find_sakhi_stem(state)
    if idx is None:
        return state
    t = state.terms[idx]
    # Replace final 'i' with [a, n] (anang = aN after ṅ-IT lopa)
    t.varnas[-1] = mk("a")
    t.varnas.append(mk("n"))
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["7_1_93_done"] = True
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta.pop("anaN_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anaN sO",
    text_dev              = "अनङ् सौ",
    padaccheda_dev        = "अनङ् सौ",
    why_dev               = (
        "सखि-शब्दस्य सौ-प्रत्यये परे 'अनङ्'-आदेशः — "
        "अन्त्य-इकारस्य स्थाने [अ,न्] (ṅकार-लोपानन्तरम्): "
        "सखि → सखन् → सखान् → सखा।"
    ),
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
