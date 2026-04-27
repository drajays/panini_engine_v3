"""
6.1.125  प्लुतप्रगृह्याच्च नित्यम् अचि  —  SAMJNA (operational core)

*Pluta* or *pragṛhya* before an *ac*-initial following *pada* / *term*:
*prakṛti-bhāva* is *nitya* at that boundary (no *savarna-dīrgha* / *yaṇ* across it).

v3 implements the *pragṛhya* ‖ *ac* half: **1.1.11** tags the left *term*;
**6.1.101** / **6.1.77** skip cross-*term* operations from that *term*.
This sūtra registers the *prayoga* in ``samjna_registry`` (R2) and stamps the
right *term* ``meta`` once per boundary so repeated scheduling does not loop.

*Pluta* is not yet modeled on ``Term``s; when it is, extend ``_boundary_index``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.pratyahara import AC

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

_REGISTRY_KEY = "6.1.125_prakRti_aci"
_META_ACK = "6_1_125_prakRti_aci_ack"


def _boundary_index(state: State) -> int | None:
    for i in range(len(state.terms) - 1):
        left, right = state.terms[i], state.terms[i + 1]
        if PRAGHYA_TERM_TAG not in left.tags:
            continue
        if right.meta.get(_META_ACK):
            continue
        if not right.varnas:
            continue
        if right.varnas[0].slp1 not in AC:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _boundary_index(state) is not None


def act(state: State) -> State:
    i = _boundary_index(state)
    if i is None:
        return state
    right = state.terms[i + 1]
    right.meta[_META_ACK] = True
    state.samjna_registry[_REGISTRY_KEY] = state.samjna_registry.get(_REGISTRY_KEY, 0) + 1
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.125",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "plutapragfhyAc ca nityam aci",
    text_dev       = "प्लुतप्रगृह्याच्च नित्यम् अचि",
    padaccheda_dev = "प्लुत-प्रगृह्यात् च नित्यम् अचि",
    why_dev        = (
        "प्रगृह्यान्तात् परस्य अच्-आदौ प्रकृतिभावो नित्यः; "
        "अत्र संज्ञा-प्रयोगः (सन्धि-विधयः ६.१.१०१/७७ इतरत्र निरुद्धाः)।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
