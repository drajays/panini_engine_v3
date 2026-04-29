"""
2.4.71  सुपो धातुप्रातिपदिकयोः  —  VIDHI

पदच्छेदः  सुपः / धातु-प्रातिपदिकयोः

अनुवृत्तिः  लुक् 2.4.58

अनुवृत्तिसहितं सूत्रम्  धातु-प्रातिपदिकयोः सुपः लुक्

Meaning (śāstra summary):
धातोः प्रातिपदिकस्य वा अवयवरूपेण विद्यमानस्य सुप्-प्रत्ययस्य लुक् भवति।

Engine (v3, glass-box):
**2.4.71** applies only when a recipe arms **luk** and confirms that the
*avayava* bearing internal *sup* are already *prātipadika*-tagged (śāstra link
to **1.2.46** *kṛttaddhitasamāsāś ca* — the *padāntara-sū* are *prātipadika*
before *sup* is elided from that community):

  • ``state.meta['2_4_71_luk_arm'] == True`` — request *luk*.
  • ``state.meta['pratipadika_avayava_ready'] == True`` — recipe asserts
    *prātipadika* readiness on members.

On success: **zero-width ghost** each internal ``sup`` ``Term`` (clear
``varnas``, add ``luk_lopa``; retain ``sup`` / ``pratyaya`` tags); set
``2_4_71_luk_arm`` to ``False`` and ``2_4_71_luk`` to ``True`` (completion).
See ``engine/lopa_ghost.py``.

Mechanical blindness:
  - ``cond()`` reads only tags + ``state.meta`` keys (never vibhakti/vacana).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import LUK_LOPA_GHOST_TAG, state_live_sup_indexes
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("2_4_71_luk_arm"):
        return False
    if not state.meta.get("pratipadika_avayava_ready"):
        return False
    return len(state_live_sup_indexes(state)) > 0


def act(state: State) -> State:
    idxs = state_live_sup_indexes(state)
    if not idxs:
        return state
    for i in idxs:
        t = state.terms[i]
        t.varnas.clear()
        t.tags.add(LUK_LOPA_GHOST_TAG)
    state.meta["2_4_71_luk_arm"] = False
    state.meta["2_4_71_luk"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.71",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "DhAtu-prAtipadikayoH supaH luk",
    text_dev       = "धातुप्रातिपदिकयोः सुपः लुक्",
    padaccheda_dev = "सुपः / धातु-प्रातिपदिकयोः",
    why_dev        = "धातु/प्रातिपदिक-अवयवे विद्यमानस्य सुपः लुक् (आर्म्ड-मेटा)।",
    anuvritti_from = ("2.4.58", "2.4.70"),
    cond           = cond,
    act            = act,
    # *sup* may be abstract; ``flat_slp1()`` unchanged on ghost transition — R1
    # would false-alarm without this flag.
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)

