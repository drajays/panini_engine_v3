"""
7.4.61  शर्पूर्वाः खयः  —  VIDHI

Padaccheda: शर्-पूर्वाः खयः

शर्पूर्वाः खयः (7.4.61)
Pāṭha: ashtadhyayi.com data.txt row i=74061 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_AC = frozenset("aAiIuUeEoOfFxX")
_SAR = frozenset("Szs")                    # śar
_KHAY = frozenset("kKcCwWtTpP")        # khay: the voiceless stops


def _find(state: State):
    """अभ्यास: an onset of śar + khay: the khay stays, all other hals of the abhyāsa are elided (paspaśa, tasthau; Kāśikā 7.4.61)."""
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags or t.meta.get("7_4_61_done") or t.meta.get("7_4_60_haladi_done"):
            continue
        vs = t.varnas
        vi = next((j for j, v in enumerate(vs) if v.slp1 in _AC), None)
        if vi is not None and vi >= 2 and vs[0].slp1 in _SAR and vs[1].slp1 in _KHAY:
            return ti
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    ti = _find(state)
    t = state.terms[ti]
    # Kāśikā 7.4.61: abhyāsasya śarpūrvāḥ khayaḥ śiṣyante, anye halo lupyante — the khay after the śar stays and every OTHER hal of the abhyāsa goes
    # (the apavāda of 7.4.60 ādiśeṣa, Nyāsa: anādiśeṣo 'yam ādiśeṣaṃ bādhate), so 7.4.60 finds nothing left to trim: ska → ku, spa → pa.
    keep = t.varnas[1]
    t.varnas = [keep] + [v for v in t.varnas[2:] if v.slp1 in _AC]
    t.meta["7_4_61_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.61",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "SarpUrvAH KayaH",
    text_dev              = "शर्पूर्वाः खयः",
    samagra_slp1          = "aByAsasya AdiH Sar-pUrvAH KayaH hal SezaH",
    samagra_dev           = "अभ्यासस्य आदिः शर्-पूर्वाः खयः हल् शेषः",
    padaccheda_dev        = "शर्-पूर्वाः खयः",
    why_dev               = "अभ्यासस्य शर्पूर्वाः खयः शिष्यन्ते (शर् पूर्व वाले खय् रहते हैं; शेष का लोप) — चुस्कुन्दे में स्कुन्द् → कुन्द्।",
    anuvritti_from        = ('7.4.58', '7.4.60'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
