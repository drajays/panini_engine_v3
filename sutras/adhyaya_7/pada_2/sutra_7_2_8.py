"""
7.2.8  नेड् वशि कृति  —  VIDHI

Padaccheda: न इट् वशि कृति

नेड् वशि कृति (7.2.8)
Pāṭha: ashtadhyayi.com data.txt row i=72008 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology.pratyahara import build_pratyahara

_VAS = build_pratyahara("v", "S")      # vaś: v r l ñ m ṅ ṇ n jh bh gh ḍh dh j b g ḍ d
_BLOCKS = ("7.2.35",)                  # ārdhadhātukasyeḍ valādeḥ


def _site(state: State):
    """A kṛt pratyaya that begins with a vaś letter and stands after an aṅga."""
    if not adhikara_in_effect("7.2.8", state, "6.4.1"):
        return None
    for i, t in enumerate(state.terms):
        if i and "krt" in t.tags and "pratyaya" in t.tags and t.varnas and t.varnas[0].slp1 in _VAS \
                and any("anga" in u.tags or "dhatu" in u.tags for u in state.terms[:i]):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.8",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "neq vaSi kfti",
    text_dev              = "नेड् वशि कृति",
    samagra_slp1          = "aNgasya na iw vaSi kfti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न इट् वशि कृति",
    padaccheda_dev        = "न इट् वशि कृति",
    why_dev               = "नेड् वशि कृति — वशादौ कृति इडागमः न (सुशर्मा)।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
