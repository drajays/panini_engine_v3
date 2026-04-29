"""
1.2.6  इन्धिभवतिभ्यां च  —  VIDHI (narrow demo)

Demo slice (ईधे):
  For dhātu `inD` (इन्ध्) in liṭ, treat the following liṭ-ending `e` as *kit*
  (kṅit-locus for downstream 6.4.24), i.e. tag it with ``kngiti``.

Engine:
  - recipe arms via ``state.meta['1_2_6_indhi_bhavati_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State) -> int | None:
    if not state.meta.get("lakara_liT"):
        return None
    if not state.meta.get("1_2_6_indhi_bhavati_arm"):
        return None
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return None
    up = (state.terms[0].meta.get("upadesha_slp1") or "").strip()
    if up not in {"inD", "Bavati"}:
        return None
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() == "e":
            if "kngiti" in t.tags:
                return None
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("kngiti")
    state.meta["1_2_6_indhi_bhavati_arm"] = False
    state.samjna_registry["1.2.6_indhi_bhavati_kngiti"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.6",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="indhi-BavatibhyAm ca (narrow)",
    text_dev="इन्धिभवतिभ्यां च",
    padaccheda_dev="इन्धि-भवतिभ्याम् / च",
    why_dev="इन्ध्-भू-आदौ लिट्-प्रत्ययस्य कित्व-व्यवहारः (6.4.24-प्रसङ्गः)।",
    anuvritti_from=("1.2.5",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

