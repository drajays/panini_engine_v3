"""
3.1.48  णिश्रिद्रुस्रुभ्यः कर्त्रि चङ्  —  VIDHI (narrow: P037 *caṅ* before *luṅ*)

Teaching JSON **P037** (*āṭīṭat*, *aṭ* + *ṇic* + *luṅ* + *caṅ* + *tip*):
  insert a *caṅ* *vikaraṇa* placeholder immediately before the *lakāra* ``luG``
  ``Term`` on the tape.

Blindness: fires only when ``state.meta['P037_3_1_48_caN_arm']`` is set.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk

def _luG_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() == "luG":
            return i
    return None


def _matches(state: State) -> bool:
    if not state.meta.get("P037_3_1_48_caN_arm"):
        return False
    if state.samjna_registry.get("P037_3_1_48_caN_inserted"):
        return False
    li = _luG_index(state)
    if li is None or li == 0:
        return False
    if li > 0 and (state.terms[li - 1].meta.get("upadesha_slp1") or "").strip() == "caY":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    li = _luG_index(state)
    assert li is not None
    ca = Term(
        kind="pratyaya",
        varnas=[mk("a")],  # *caṅ* augment ``a`` (narrow P037 surface slice).
        tags={"pratyaya", "vikarana", "anit_ardhadhatuka", "ardhadhatuka"},
        meta={"upadesha_slp1": "caY", "P037_caN": True},
    )
    state.terms.insert(li, ca)
    state.samjna_registry["P037_3_1_48_caN_inserted"] = True
    state.meta.pop("P037_3_1_48_caN_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.48",
    sutra_type=SutraType.VIDHI,
    text_slp1="RiSridruguroByaH kartari zi caY",
    text_dev="णिश्रिद्रुस्रुभ्यः कर्तरि चङ्",
    padaccheda_dev="णि-श्रि-द्रु-स्रु-भ्यः कर्तरि चङ्",
    why_dev=(
        "ण्यन्त-आदिषु धातुषु कर्तरि लुङि चङावागमः (ग्लास-बॉक्स्: P३७ — "
        "``luG`` स्थाने पूर्वं ``caY`` टर्म्)।"
    ),
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
