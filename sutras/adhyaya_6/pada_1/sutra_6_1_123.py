"""
6.1.123  अवङ् स्फोटायनस्य  —  VIDHI

Padaccheda: अवङ् स्फोटायनस्य

अवङ् स्फोटायनस्य (6.1.123)
Pāṭha: ashtadhyayi.com data.txt row i=61123 (Art. 14).
Kāśikā 6.1.123: gavāgram, gavājinam, gavaudanam, gavoṣṭram; Laghukaumudī: gavāgram, go'gram.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

_AC = frozenset("aAiIuUfFxXeEoO")
META = "avang_6_1_123"


def _find(state: State):
    live = _live(state)
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if "pada" not in left.tags or left.meta.get(META):
            continue
        flat = "".join(v.slp1 for v in left.varnas)
        if flat.endswith("go") and right.varnas[0].slp1 in _AC:
            return i
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    left = state.terms[i]
    left.varnas[-1:] = [mk("a"), mk("v")]              # avaṅ replaces the eṅ (o); ṅ is it, so the whole sthānin goes
    left.meta[META] = True
    state.meta["__why_now_dev__"] = "पदान्त-एङन्तस्य गोः अचि परे अवङ् विभाषा (६.१.१२३)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.123",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'avaN sPowAyanasya',
    text_dev              = 'अवङ् स्फोटायनस्य',
    samagra_slp1          = "padAntAt goH aci avaN viBAzA sPowAyanasya",
    samagra_dev           = "पदान्तात् गोः अचि अवङ् विभाषा स्फोटायनस्य",
    padaccheda_dev        = "अवङ् स्फोटायनस्य",
    why_dev               = "काशिका ६.१.१२३ — पदान्तस्य एङन्तस्य गोः अचि परे स्फोटायनमतेन अवङादेशः विभाषा (गवाग्रम्, गवाजिनम्)।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default=False,
    vibhasha_scope=_new_cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
