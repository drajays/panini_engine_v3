"""
1.2.41  अपृक्त एकाल् प्रत्ययः  —  SAMJNA (narrow: tag apṛkta on single-hal pratyaya)

Engine: if a pratyaya Term consists of a single consonant (one HAL varṇa),
tag it as 'apfkta_1_2_41' and record in registry (audit). Used by 7.3.96.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


TAG_APRKTA = "apfkta_1_2_41"


def _eligible(state: State):
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if TAG_APRKTA in t.tags:
            continue
        # ekāl = any single AL (phoneme), not just consonants
        if len(t.varnas) == 1:
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
    state.meta["__why_now_dev__"] = (
        "एक-अल् (एक-वर्ण) प्रत्ययः 'अपृक्त'-संज्ञां प्राप्नोति; अनया संज्ञया "
        "ईट्-आगम-आदि-विधयः (यथा ७.३.९६) प्रवर्तन्ते। (१.२.४१)"
    )
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

