"""
6.1.198  आमन्त्रितस्य च  —  ANUVADA (narrow *glass-box*)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61198):** *āmantriṭasya ca* — *ādyudātta*
on the *āmantrita* stem.

Narrow v3:
  • ``prakriya_26`` — *indra* *sambuddhi*: ``sAmantrita`` + ``prakriya_26_6_1_198_arm``.
  • ``prakriya_28`` — **मेघातिथे मन्महे**: after **2.1.2** *parāṅgavat*, stamp
    ``meta['prakriya_28_AdyudAtta_note']`` on ``terms[0]``.
  • ``prakriya_29`` — **गौरावस्कन्दिन्**: after **6.1.197** *ñaṇityādi* stamp, confirms
    ``meta['prakriya_29_AdyudAtta_note']`` on ``terms[0]``.
  • ``prakriya_32`` — tri-vocative **ऐडविड …**: ``meta['prakriya_32_EdaviDa_AdyudAtta_note']``
    on ``terms[0]`` (``EdaviDa``).

No *svara* columns on the flat tape (same policy as **6.1.158**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _prakriya_26_site(state: State) -> bool:
    if not state.meta.get("prakriya_26_6_1_198_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "sAmantrita" not in t0.tags:
        return False
    if t0.meta.get("prakriya_26_AdyudAtta_note"):
        return False
    return True


def _prakriya_32_site(state: State) -> bool:
    if not state.meta.get("prakriya_32_6_1_198_arm"):
        return False
    if len(state.terms) < 3:
        return False
    t0 = state.terms[0]
    if "sAmantrita" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "EdaviDa":
        return False
    if t0.meta.get("prakriya_32_EdaviDa_AdyudAtta_note"):
        return False
    return True


def _prakriya_28_site(state: State) -> bool:
    if not state.meta.get("prakriya_28_6_1_198_arm"):
        return False
    if len(state.terms) < 2:
        return False
    if not state.samjna_registry.get("2.1.2_subAmantrite_parA~ggavat_28"):
        return False
    t0 = state.terms[0]
    if t0.meta.get("upadesha_slp1") != "meGAtithe":
        return False
    if t0.meta.get("prakriya_28_AdyudAtta_note"):
        return False
    return True


def _prakriya_29_site(state: State) -> bool:
    if not state.meta.get("prakriya_29_6_1_198_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "sAmantrita" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "gaurAvaskandin":
        return False
    if not t0.meta.get("prakriya_29_YiRityAdi_first_udAtta_note"):
        return False
    if t0.meta.get("prakriya_29_AdyudAtta_note"):
        return False
    return True


def cond(state: State) -> bool:
    return (
        _prakriya_32_site(state)
        or _prakriya_28_site(state)
        or _prakriya_29_site(state)
        or _prakriya_26_site(state)
    )


def act(state: State) -> State:
    if _prakriya_32_site(state):
        state.terms[0].meta["prakriya_32_EdaviDa_AdyudAtta_note"] = True
        state.meta.pop("prakriya_32_6_1_198_arm", None)
        return state
    if _prakriya_28_site(state):
        state.terms[0].meta["prakriya_28_AdyudAtta_note"] = True
        state.meta.pop("prakriya_28_6_1_198_arm", None)
        return state
    if _prakriya_29_site(state):
        state.terms[0].meta["prakriya_29_AdyudAtta_note"] = True
        state.meta.pop("prakriya_29_6_1_198_arm", None)
        return state
    if _prakriya_26_site(state):
        state.terms[0].meta["prakriya_26_AdyudAtta_note"] = True
        state.meta.pop("prakriya_26_6_1_198_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.198",
    sutra_type=SutraType.ANUVADA,
    text_slp1="aamantritasya ca",
    text_dev="आमन्त्रितस्य च",
    padaccheda_dev="आमन्त्रितस्य च",
    why_dev="आमन्त्रिते आद्युदात्त-अनुवादः (*prakriya_26* / *28* / *29* / *32*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
