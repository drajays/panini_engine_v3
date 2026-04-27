"""
7.3.96  अस्तिसिचोऽपृक्ते  —  VIDHI (narrow: Īṭ augment after sic before apṛkta t)

Engine: when a sic-derived 's' pratyaya is followed by an apṛkta single-hal
tiṅ residue 't', insert 'I' between them (at start of the tiṅ term).
This supports glass-box aorist forms like अचैषीत्.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk, HAL


def _find(state: State):
    if len(state.terms) < 3:
        return None
    # Expect [... dhātu, sic_term, tin_term]
    for i in range(len(state.terms) - 2):
        dh, sic, tin = state.terms[i], state.terms[i + 1], state.terms[i + 2]
        if "dhatu" not in dh.tags:
            continue
        if sic.kind != "pratyaya" or tin.kind != "pratyaya":
            continue
        if sic.meta.get("7_3_96_Iw_done"):
            return None
        # Identify sic by a marker meta set by 3.1.44 or pipeline.
        if (sic.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        if not tin.varnas:
            continue
        # apṛkta: single hal 't' (after 3.4.100)
        if len(tin.varnas) != 1 or tin.varnas[0].slp1 not in HAL:
            continue
        return i + 2
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    j = _find(state)
    if j is None:
        return state
    tin = state.terms[j]
    tin.varnas.insert(0, mk("I"))
    # Record on sic term for idempotency.
    state.terms[j - 1].meta["7_3_96_Iw_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.96",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "asti-sico apfkTe (Iw)",
    text_dev       = "अस्तिसिचोऽपृक्ते",
    padaccheda_dev = "अस्ति-सिचोः / अपृक्ते",
    why_dev        = "सिच्-परस्य अपृक्त-तिङ्-प्रत्ययस्य पूर्वं ईट्-आगमः (अचैषीत्-प्रक्रिया)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

