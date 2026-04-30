"""
8.4.66  उदात्तादनुदात्तस्य स्वरितः  —  SAMJNA (narrow demo)

**Pāṭha:** *udāttād anudāttasya svaritaḥ*.

Engine:
  • **Phit** path (``prakriya_17``): registers ``samjna_registry['phit_phiSa_anta_udAtta_candidate']``
    when a **phiṣa**-class stem is **not** already blocked by **Phit 4.18**
    (``phit_418_sarvAnudAtta`` absent).  Fires only in **Tripāḍī**.
  • ``prakriya_26`` (*indra* *sambuddhi* accent chain): when ``prakriya_26_8_4_66_arm``,
    ``tripadi_zone``, and ``upadesha_slp1 == 'indra'``, registers
    ``samjna_registry['prakriya_26_svarita_locus']`` (no *svara* columns on tape).
  • ``prakriya_27`` (**आगच्छ** accent demo): when ``prakriya_27_8_4_66_arm``,
    ``tripadi_zone``, **Phiṭ**/**8.1.6** + **8.1.28** *śruti* prerequisites hold,
    registers ``samjna_registry['prakriya_27_svarita_locus']``.
  • ``prakriya_28`` (**मेघातिथे मन्महे**): **2.1.2** + **6.1.198** prerequisites,
    registers ``samjna_registry['prakriya_28_svarita_locus']``.
  • ``prakriya_29`` (**गौरावस्कन्दिन्** vocative): **6.1.197**/**6.1.198** *śruti*
    prerequisites, registers ``samjna_registry['prakriya_29_svarita_locus']``.
  • ``prakriya_31`` (RV **इमं मे …** spine): ``imam`` + ``me``, **8.1.22** + **6.1.197**
    *śruti* prerequisites, registers ``samjna_registry['prakriya_31_me_svarita_locus']``.
  • ``prakriya_32`` — ``EdaviDa`` first vocative (triplet tape): **6.1.198** prerequisite,
    registers ``samjna_registry['prakriya_32_EdaviDa_svarita_locus']``.

Full **8.4.66** *vidhi* on the varṇa tape is not modelled here.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _stem(state: State):
    if not state.terms:
        return None
    t0 = state.terms[0]
    if "phiSa_pratipadika" not in t0.tags:
        return None
    up = (t0.meta.get("upadesha_slp1") or "").strip()
    if not up:
        return None
    return up


def _EdaviDa_prakriya_32(state: State) -> bool:
    if not state.meta.get("prakriya_32_8_4_66_arm"):
        return False
    if not state.tripadi_zone:
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if t0.meta.get("upadesha_slp1") != "EdaviDa":
        return False
    if not t0.meta.get("prakriya_32_EdaviDa_AdyudAtta_note"):
        return False
    if state.samjna_registry.get("prakriya_32_EdaviDa_svarita_locus"):
        return False
    return True


def _indra_prakriya_26(state: State) -> bool:
    if not state.meta.get("prakriya_26_8_4_66_arm"):
        return False
    if not state.tripadi_zone:
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if t0.meta.get("upadesha_slp1") != "indra":
        return False
    if state.samjna_registry.get("prakriya_26_svarita_locus"):
        return False
    return True


def _imam_me_prakriya_31(state: State) -> bool:
    if not state.meta.get("prakriya_31_8_4_66_arm"):
        return False
    if not state.tripadi_zone:
        return False
    if len(state.terms) < 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if t0.meta.get("upadesha_slp1") != "imam":
        return False
    if t1.meta.get("upadesha_slp1") != "me":
        return False
    if not t0.meta.get("prakriya_31_imam_first_udAtta_note"):
        return False
    if not t1.meta.get("prakriya_31_me_anudAtta_from_8122"):
        return False
    if state.samjna_registry.get("prakriya_31_me_svarita_locus"):
        return False
    return True


def _gaurAvaskandin_prakriya_29(state: State) -> bool:
    if not state.meta.get("prakriya_29_8_4_66_arm"):
        return False
    if not state.tripadi_zone:
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if t0.meta.get("upadesha_slp1") != "gaurAvaskandin":
        return False
    if not t0.meta.get("prakriya_29_YiRityAdi_first_udAtta_note"):
        return False
    if not t0.meta.get("prakriya_29_AdyudAtta_note"):
        return False
    if state.samjna_registry.get("prakriya_29_svarita_locus"):
        return False
    return True


def _meghAtithe_prakriya_28(state: State) -> bool:
    if not state.meta.get("prakriya_28_8_4_66_arm"):
        return False
    if not state.tripadi_zone:
        return False
    if len(state.terms) < 2:
        return False
    t0 = state.terms[0]
    if t0.meta.get("upadesha_slp1") != "meGAtithe":
        return False
    if not state.samjna_registry.get("2.1.2_subAmantrite_parA~ggavat_28"):
        return False
    if not t0.meta.get("prakriya_28_AdyudAtta_note"):
        return False
    if state.samjna_registry.get("prakriya_28_svarita_locus"):
        return False
    return True


def _agaccha_prakriya_27(state: State) -> bool:
    if not state.meta.get("prakriya_27_8_4_66_arm"):
        return False
    if not state.tripadi_zone:
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "tinanta_accent_demo" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "AgacCa":
        return False
    if not state.samjna_registry.get("prakriya_27_phit481_upasarga_A_udAtta"):
        return False
    if not t0.meta.get("prakriya_27_gaccha_base_anudAtta_note"):
        return False
    if state.samjna_registry.get("prakriya_27_svarita_locus"):
        return False
    return True


def cond(state: State) -> bool:
    if _EdaviDa_prakriya_32(state):
        return True
    if _imam_me_prakriya_31(state):
        return True
    if _gaurAvaskandin_prakriya_29(state):
        return True
    if _meghAtithe_prakriya_28(state):
        return True
    if _agaccha_prakriya_27(state):
        return True
    if _indra_prakriya_26(state):
        return True
    if not state.tripadi_zone:
        return False
    if not state.meta.get("phit_1_1_arm"):
        return False
    if state.samjna_registry.get("phit_418_sarvAnudAtta"):
        return False
    if "phit_phiSa_anta_udAtta_candidate" in state.samjna_registry:
        return False
    return _stem(state) is not None


def act(state: State) -> State:
    if _EdaviDa_prakriya_32(state):
        state.samjna_registry["prakriya_32_EdaviDa_svarita_locus"] = True
        state.meta.pop("prakriya_32_8_4_66_arm", None)
        return state
    if _imam_me_prakriya_31(state):
        state.samjna_registry["prakriya_31_me_svarita_locus"] = True
        state.meta.pop("prakriya_31_8_4_66_arm", None)
        return state
    if _gaurAvaskandin_prakriya_29(state):
        state.samjna_registry["prakriya_29_svarita_locus"] = True
        state.meta.pop("prakriya_29_8_4_66_arm", None)
        return state
    if _meghAtithe_prakriya_28(state):
        state.samjna_registry["prakriya_28_svarita_locus"] = True
        state.meta.pop("prakriya_28_8_4_66_arm", None)
        return state
    if _agaccha_prakriya_27(state):
        state.samjna_registry["prakriya_27_svarita_locus"] = True
        state.meta.pop("prakriya_27_8_4_66_arm", None)
        return state
    if _indra_prakriya_26(state):
        state.samjna_registry["prakriya_26_svarita_locus"] = True
        state.meta.pop("prakriya_26_8_4_66_arm", None)
        return state
    up = _stem(state)
    if up is None:
        return state
    state.samjna_registry["phit_phiSa_anta_udAtta_candidate"] = frozenset({up})
    state.meta.pop("phit_1_1_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.66",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "udAttAd anudAttasya svaritaH",
    text_dev       = "उदात्तादनुदात्तस्य स्वरितः",
    padaccheda_dev = "उदात्तात् अनुदात्तस्य स्वरितः",
    why_dev        = "फिट् १.१ (*फिषोऽन्त उदात्तः*) इत उत्सर्ग-अङ्कनम् — पूर्णं ८.४.६६-विधिं नास्ति।",
    anuvritti_from = ("8.4.65",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
