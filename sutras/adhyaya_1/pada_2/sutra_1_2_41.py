"""
1.2.41  अपृक्त एकाल् प्रत्ययः  —  SAMJNA (narrow: tag apṛkta on single-hal pratyaya)

Engine: if a pratyaya Term consists of a single consonant (one HAL varṇa),
tag it as 'apfkta_1_2_41' and record in registry (audit). Used by 7.3.96.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL


TAG_APRKTA = "apfkta_1_2_41"


def _eligible(state: State):
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if TAG_APRKTA in t.tags:
            continue
        if len(t.varnas) == 1 and t.varnas[0].slp1 in HAL:
            yield i


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    idxs = list(_eligible(state))
    if not idxs:
        return state
    prev = state.samjna_registry.get("1.2.41_apfkta_indices")
    if not isinstance(prev, frozenset):
        prev = frozenset()
    s = set(prev)
    for i in idxs:
        state.terms[i].tags.add(TAG_APRKTA)
        s.add(i)
    state.samjna_registry["1.2.41_apfkta_indices"] = frozenset(s)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.41",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "apfkta ekAl pratyayaH",
    text_dev       = "अपृक्त एकाल् प्रत्ययः",
    padaccheda_dev = "अपृक्तः / एकाल् / प्रत्ययः",
    why_dev        = "एक-हल्-प्रत्ययः अपृक्त-संज्ञकः (ईट्-आगम ७.३.९६ इत्यादि-प्रसङ्गे)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

