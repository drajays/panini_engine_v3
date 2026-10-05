"""
7.2.63  ऋतो भारद्वाजस्य  —  VIDHI

Padaccheda: ऋतः भारद्वाजस्य

ऋतो भारद्वाजस्य (7.2.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "7_2_63_no_thal_it"


def _hit(state: State) -> bool:
    """ऋतो भारद्वाजस्य (7.2.61 अचस्तास्वत् थल्यनिटो नित्यम् continues): an aniṭ
    ऋ-final root takes no iṭ before थल् — जहर्थ, सस्मर्थ, दधर्थ (7.2.66 keeps it for ऋ)."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "Tal" for t in state.terms):
        return False
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dh is None or not dh.meta.get("anit_dhatu") or not dh.varnas:
        return False
    up = (dh.meta.get("upadesha_slp1") or "").rstrip("~").rstrip("YN")      # the root as given: guṇa/rapara has turned f into ar
    return up.endswith("f") and len(up) > 1


def cond(state: State) -> bool:
    return not state.paribhasha_gates.get(_GATE_KEY) and _hit(state)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fto BAradvAjasya",
    text_dev              = "ऋतो भारद्वाजस्य",
    padaccheda_dev        = "ऋतः भारद्वाजस्य",
    why_dev               = "अनिटः ऋदन्तात् थलि इडभावः (जहर्थ, सस्मर्थ)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
