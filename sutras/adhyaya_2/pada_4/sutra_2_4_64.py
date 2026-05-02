"""
2.4.64  यञञोश्च  —  VIDHI (narrow: **P042** *yañ* *luk* before *jas*)

JSON ``split_prakriyas_11/P042.json`` cites **2.4.64** for *luk* of **yañ** in the
*bahu-vacana* *gotra* frame (*gārgyāḥ*).

Engine: recipe-only **luk** marker — no separate **yañ** ``Term`` remains once
``gArgya`` is already fused (**P042** structural merge before *sup*); this slice
registers audit keys for **1.1.60**/**1.1.61** follow-up in the recipe.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("P042_2_4_64_arm"):
        return False
    if len(state.terms) < 2:
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "P042_gArgya_stem" not in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if (pr.meta.get("upadesha_slp1") or "").strip() != "jas":
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    state.samjna_registry["2.4.64_P042_yanna_luk_audit"] = True
    state.meta.pop("P042_2_4_64_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.64",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "yaYayoSca (narrow P042)",
    text_dev       = "यञञोश्च — P042 संक्षेपः",
    padaccheda_dev = "यञञोः / च",
    why_dev        = "यञ्-लुक्-प्रसङ्गः (गार्ग्याः, P042) — संक्षेप-छेदः।",
    anuvritti_from = ("2.4.58",),
    cond           = cond,
    act            = act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
