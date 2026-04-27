"""
6.1.68  हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्  —  VIDHI

Narrow v3: when ``state.meta["6_1_68_arm"]``, the *aṅga* ``Term`` ends in a
*hal*, the following *sup* is a single *s* tagged *apṛkta* (**1.2.41**), drop
that *s* ``Varna`` (and remove an emptied *sup* ``Term``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import HAL

from sutras.adhyaya_1.pada_2.sutra_1_2_41 import TAG_APRKTA


def _eligible(state: State) -> bool:
    if not state.meta.get("6_1_68_arm"):
        return False
    if len(state.terms) < 2:
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags or len(pr.varnas) != 1:
        return False
    if TAG_APRKTA not in pr.tags:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if not anga.varnas or anga.varnas[-1].slp1 not in HAL:
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    pr = state.terms[-1]
    pr.varnas.clear()
    state.terms.pop()
    state.samjna_registry["6.1.68_sut_aprkta_hal_lopa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.68",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hal~yAbbhyo dIrghAt sutisyapfktaM hal",
    text_dev       = "हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्",
    padaccheda_dev = "हल्-ङि-आभ्यः / दीर्घात् / सु-तिसि-अपृक्तम् / हल्",
    why_dev        = "हल्-अन्ताद् अङ्गात् परस्य अपृक्त-सु-हल्-लोपः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
