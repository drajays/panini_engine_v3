"""
8.4.56  वाऽवसाने  —  VIDHI

At avasāna (word boundary / pause), jaś consonants optionally become car
(voiceless stops).  In practice always applied for final-position forms.

Engine: when armed with ``8_4_56_arm``, find the final consonant 'd' of the
merged pada (placed there by 8.2.39 jhal→jaś) and convert back to 't' (car).

Jaś→car map (subset relevant to laṅ/luṅ):  d→t, g→k, j→c, b→p, etc.
For laṅ 3sg, 8.2.39 converts final 't'→'d', then 8.4.56 converts 'd'→'t'.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "8_4_56_vAvasAne_56"

# jaś → car: voiced obstruents → their voiceless equivalents at avasāna
_JAS_TO_CAR: dict[str, str] = {
    "d": "t",  "D": "T",  "g": "k",  "G": "K",
    "b": "p",  "B": "P",  "j": "c",  "J": "C",
    "q": "w",  "Q": "W",
}


def _find_jas_final(state: State) -> int | None:
    """Find the index of a jaś final consonant in the merged pada."""
    if not state.terms:
        return None
    t = state.terms[0] if len(state.terms) == 1 else None
    if t is None:
        return None
    if not t.varnas:
        return None
    last = t.varnas[-1]
    if last.slp1 in _JAS_TO_CAR:
        return len(t.varnas) - 1
    return None


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not state.meta.get("8_4_56_arm"):
        return False
    return _find_jas_final(state) is not None


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"] = "8.4.56"
    i = _find_jas_final(state)
    if i is not None:
        old_slp1 = state.terms[0].varnas[i].slp1
        car_slp1 = _JAS_TO_CAR[old_slp1]
        state.terms[0].varnas[i] = parse_slp1_upadesha_sequence(car_slp1)[0]
        state.samjna_registry["8.4.56_jas_to_car"] = f"{old_slp1}→{car_slp1}"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA'vasAne",
    text_dev              = "वाऽवसाने",
    padaccheda_dev        = "वा अवसाने",
    why_dev               = "(सूत्रम् 8.4.56) वाऽवसाने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
