"""
6.1.109  एङः पदान्तादति  —  VIDHI  (apavāda of 6.1.78)

पदान्त ए/ओ followed by short अ: the अ is elided (pūrvarūpa; avagraha in
writing) — ``te`` + ``atra`` → ``te 'tra``, ``vanO`` ... not ``tayatra``.
Padānta = left Term carries the ``pada`` tag (1.4.14 / 1.4.17).
Pāṭha: ashtadhyayi.com data.txt row i=61109 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def padanta_eng_before_short_a(left, right) -> bool:
    """Shared with 6.1.78 so the apavāda is decided in one place."""
    return bool(
        "pada" in left.tags and left.varnas and right.varnas
        and left.varnas[-1].slp1 in ("e", "o") and right.varnas[0].slp1 == "a"
    )


def _find(state: State):
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if PRAGHYA_TERM_TAG in left.tags or right.meta.get("avagraha"):
            continue
        if padanta_eng_before_short_a(left, right):
            return j
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    j = _find(state)
    if j is None:
        return state
    del state.terms[j].varnas[0]
    state.terms[j].meta["avagraha"] = True
    state.meta["__why_now_dev__"] = (
        "पदान्त-एङः (ए/ओ) परे ह्रस्व-अकारस्य पूर्वरूपम् (अवग्रहः); यथा ते+अत्र → तेऽत्र। (६.१.१०९)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.109",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "eNaH padAntAdati",
    text_dev       = "एङः पदान्तादति",
    samagra_slp1   = "padAntAt eNaH ati pUrvaH",
    samagra_dev    = "पदान्तात् एङः अति पूर्वः",
    padaccheda_dev = "एङः पदान्तात् अति",
    why_dev        = "पदान्तात् एङः परस्य ह्रस्वाकारस्य पूर्वरूपम्।",
    apavada_of     = ("6.1.78",),
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
