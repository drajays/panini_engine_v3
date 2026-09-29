"""
3.1.48  णिश्रिद्रुस्रुभ्यः कर्तरि चङ्  —  VIDHI (narrow: P037 *caṅ* before *luṅ*)

Teaching JSON **P037** (*āṭīṭat*, *aṭ* + *ṇic* + *luṅ* + *caṅ* + *tip*):
  insert a *caṅ* *vikaraṇa* placeholder immediately before the *lakāra* ``luG``
  ``Term`` on the tape.

Blindness: fires only when ``state.meta['P037_3_1_48_caN_arm']`` is set.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31048 · णिश्रिद्रुस्रुभ्यः कर्तरि चङ्
              padaccheda: णि-श्रि-द्रु-स्रुभ्यः कर्तरि चङ्
              anuvṛtti:   31022: धातोः | 31043: लुङि | 31044: च्लेः
  Source #2 — Kāśikā 3.1.48 udāharaṇa:
                अचीकरत्
                अजीहरत्
                अशिश्रियत्
  Cross-check — surface pinned by: tests/unit/test_AwIwat_luN_aT_Nic_caN_tip.py
  Reference record: sutra_ref_out/3_1_48.json
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


_CAN_STEMS = frozenset({"Sri", "dru", "sru"})


def _general(state: State):
    """णिश्रिद्रुस्रुभ्यः कर्तरि चङ्: cli after a ṇijanta (or श्रि, द्रु, स्रु) in kartari
    becomes caṅ (ṅit, aniṭ): अचूचुरत्, अशिश्रियत्."""
    cli = next((t for t in state.terms if (t.meta.get("upadesha_slp1") or "").strip() == "cli"), None)
    dh = next((t for t in state.terms if "dhatu" in t.tags), None)
    if cli is None or dh is None or "kartari" not in dh.tags:
        return None
    if dh.meta.get("nijanta") or "".join(v.slp1 for v in dh.varnas) in _CAN_STEMS:
        return cli
    return None

def cond(state: State) -> bool:
    if _general(state) is not None:
        return True
    return _matches(state)


def act(state: State) -> State:
    g = _general(state)
    if g is not None:
        g.varnas = [mk("a")]
        g.meta["upadesha_slp1"] = "caG"
        g.meta["it_markers"] = {"c", "G"}
        g.kind = "pratyaya"
        g.tags |= {"pratyaya", "vikarana", "kngiti", "ardhadhatuka", "anit_ardhadhatuka"}
        return state
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
    text_slp1='RiSridrusruByaH kartari caN',
    text_dev='णिश्रिद्रुस्रुभ्यः कर्तरि चङ्',
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
