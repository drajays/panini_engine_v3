"""
1.3.1  भूवादयो धातवः  —  SAMJNA

Upadeśa items listed in the Dhātupāṭha (starting with ``bhū``) receive the
technical name *dhātu* — prerequisite for ``धातोः``-scoped rules (3.1.91 ff.).

Engine: registers that the dhātu-upadeśa term has been recognized under this
sūtra (glass-box trace); does not alter ``varṇa``s.

  • ``prakriya_35`` — ``spfS`` dhātu anchor for **३.१.६२** neighbourhood (``prakriya_35_1_3_1_arm`` +
    ``prakriya_35_spfSa_kvin_demo``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site_prakriya_35_spfSa(state: State) -> bool:
    if not state.meta.get("prakriya_35_1_3_1_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "prakriya_35_spfSa_kvin_demo" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "spfS":
        return False
    if "dhatu" not in t0.tags or "upadesha" not in t0.tags:
        return False
    return state.samjna_registry.get("1.3.1_prakriya_35_spfSa") is None


def _site_bhuvadi_generic(state: State) -> bool:
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags or "upadesha" not in t0.tags:
        return False
    return state.samjna_registry.get("1.3.1_bhuvadi_dhatu") is None


def cond(state: State) -> bool:
    return _site_prakriya_35_spfSa(state) or _site_bhuvadi_generic(state)


def act(state: State) -> State:
    if _site_prakriya_35_spfSa(state):
        state.samjna_registry["1.3.1_prakriya_35_spfSa"] = True
        state.samjna_registry["1.3.1_bhuvadi_dhatu"] = True
        state.samjna_registry["dhatu"] = frozenset({"1.3.1"})
        state.meta.pop("prakriya_35_1_3_1_arm", None)
        return state
    if _site_bhuvadi_generic(state):
        state.samjna_registry["1.3.1_bhuvadi_dhatu"] = True
        state.samjna_registry["dhatu"] = frozenset({"1.3.1"})
        return state
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.1",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "bhUvAdayo dhAtavaH",
    text_dev       = "भूवादयो धातवः",
    padaccheda_dev = "भू-आदयः धातवः",
    why_dev        = "भू आदि गणे पठितानां धातूनां धातु-संज्ञा (उपदेश एव अधिकृतः)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
