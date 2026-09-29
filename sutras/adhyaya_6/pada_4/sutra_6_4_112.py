"""
6.4.112  श्नाऽभ्यस्तयोरातः  —  VIDHI

Padaccheda: श्ना-अभ्यस्तयोः आतः

श्नाऽभ्यस्तयोरातः (6.4.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_112_SnAByasta_112"


def _find(state: State) -> int | None:
    """श्नाभ्यस्तयोरातः (क्ङिति, अचि — 6.4.98/6.4.77): the ā of śnā (and of an
    abhyasta) drops before a vowel-initial kṅit ending — क्रीणन्ति, क्रीणन्तु."""
    for i, t in enumerate(state.terms[:-1]):
        if "SnA_vikaraṇa" not in t.tags or not t.varnas or t.varnas[-1].slp1 != "A":
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        # jh counts as vowel-initial: 7.1.3 झोऽन्तः makes it अन्ति / अन्तु / अन्
        if nxt is None:
            continue
        jh = (nxt.meta.get("upadesha_slp1") or "").strip() in {"jhi", "Ji", "Ja", "jha"}
        if not jh and nxt.varnas[0].slp1 not in "aAiIuUfFxXeEoO":
            continue
        if "kngiti" in nxt.tags or nxt.meta.get("is_apit"):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].varnas = state.terms[i].varnas[:-1]
    # no longer an upadeśa: its new final न् must not be read as halantyam it
    state.terms[i].tags.discard("upadesha")
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.112",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'SnAByastayorAtaH',
    text_dev              = 'श्नाऽभ्यस्तयोरातः',
    padaccheda_dev        = "श्ना-अभ्यस्तयोः आतः",
    why_dev               = "(सूत्रम् 6.4.112) श्नाऽभ्यस्तयोरातः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
