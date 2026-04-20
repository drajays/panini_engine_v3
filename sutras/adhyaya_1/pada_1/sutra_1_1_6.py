"""
1.1.6  दीधीवेवीटाम्  —  PRATISHEDHA  (representative)

"Of दीधी, वेवी, and इट् — there is NO (guṇa / vṛddhi) before an
 iko-starting pratyaya."

This is a classical PRATISHEDHA / niṣedha: it blocks the guṇa rule
(6.1.87) from firing when the aṅga is one of these three.

Representative behaviour: we add 6.1.87 to state.blocked_sutras when
a current Term carries the upadeśa identity of dīdhī / vevī / iṭ.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


_FORBIDDEN_ROOTS = frozenset({"dIDI", "vevI", "iw"})


def cond(state: State) -> bool:
    # Fire iff some Term is one of the three AND 6.1.87 is not already blocked.
    if "6.1.87" in state.blocked_sutras:
        return False
    return any(
        t.meta.get("upadesha_slp1") in _FORBIDDEN_ROOTS
        for t in state.terms
    )


def act(state: State) -> State:
    state.blocked_sutras.add("6.1.87")
    return state


SUTRA = SutraRecord(
    sutra_id         = "1.1.6",
    sutra_type       = SutraType.PRATISHEDHA,
    text_slp1        = "dIDIvevIwAm",
    text_dev         = "दीधीवेवीटाम्",
    padaccheda_dev   = "दीधी-वेवी-इटाम्",
    why_dev          = "दीधी-वेवी-इट् — एषाम् गुण-वृद्धि-निषेधः।",
    anuvritti_from   = (),
    cond             = cond,
    act              = act,
    blocks_sutra_ids = ("6.1.87",),
)

register_sutra(SUTRA)
