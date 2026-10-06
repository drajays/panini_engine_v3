"""
6.4.78  अभ्यासस्यासवर्णे  —  VIDHI

Padaccheda: अभ्यासस्य असवर्णे

अभ्यासस्यासवर्णे (6.4.78)
Pāṭha: ashtadhyayi.com data.txt row i=64078 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _abhyasa_dhatu(state: State):
    """(abhyāsa, dhātu) adjacent on the tape, or None."""
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" in t.tags and "dhatu" in state.terms[i + 1].tags:
            return t, state.terms[i + 1]
    return None

_IYUV = {"i": "iy", "I": "iy", "u": "uv", "U": "uv"}
_SAVARNA = {"i": "iI", "I": "iI", "u": "uU", "U": "uU"}


def _find(state: State):
    """अभ्यासस्यासवर्णे: an इ/उ abhyāsa before a non-savarṇa vowel takes इयङ्/उवङ्
    (इ+एख → इयेख, उ+ओख → उवोख)."""
    hit = _abhyasa_dhatu(state)
    if hit is None:
        return None
    ab, dh = hit
    if ab.meta.get("6_4_78_done") or len(ab.varnas) != 1 or ab.varnas[0].slp1 not in _IYUV:
        return None
    if not dh.varnas or dh.varnas[0].slp1 not in _AC or dh.varnas[0].slp1 in _SAVARNA[ab.varnas[0].slp1]:
        return None
    return ab


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    ab = _find(state)
    a, b = _IYUV[ab.varnas[0].slp1]
    ab.varnas = [mk(a), mk(b)]
    ab.meta["6_4_78_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "6.4.78",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "aByAsasyAsavarRe",
    text_dev              = "अभ्यासस्यासवर्णे",
    samagra_slp1          = "aByAsasya yvoH asavarRe aci iyaN-uvaNO",
    samagra_dev           = "अभ्यासस्य य्वोः असवर्णे अचि इयङ्-उवङौ",
    padaccheda_dev        = "अभ्यासस्य असवर्णे",
    why_dev               = "अभ्यासस्य इवर्णोवर्णयोः असवर्णे अचि परे इयङुवङौ (इयेख, उवोख)।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ("6.1.77",),    # abhyāsa i/u before a non-savarṇa vowel: iy/uv, not y/v (iyarti)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
