"""
6.4.92  मितां ह्रस्वः  —  VIDHI (narrow demo)

Glass-box slice (हिडनीय.md):
  For a *mit* dhātu followed by ṇic, shorten the **upadhā** vowel before ṇic.
  Here: ``heq`` (हेड्) → ``hiq`` (हिड्), i.e. penultimate *एच्* → *इक्* — delegated to
  ``phonology.ec_ig_hrasva`` (same resolver bundle as **1.1.48**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.ec_ig_hrasva import ec_ig_replacement_slp1


def _find(state: State):
    if len(state.terms) < 2:
        return None
    dh = state.terms[0]
    nic = state.terms[1]
    if "dhatu" not in dh.tags or "anga" not in dh.tags:
        return None
    if "mit" not in dh.tags:
        return None
    if "nic" not in nic.tags:
        return None
    if dh.meta.get("6_4_92_mit_hrasva_done"):
        return None
    vs = dh.varnas
    if len(vs) < 2:
        return None
    # Upadhā = penultimate phoneme row (see note: ए → इ).
    pen = vs[-2].slp1
    if ec_ig_replacement_slp1(pen) is None:
        return None
    return 0


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    ti = _find(state)
    if ti is None:
        return state
    dh = state.terms[ti]
    pen = dh.varnas[-2].slp1
    rep = ec_ig_replacement_slp1(pen)
    if rep is None:
        return state
    dh.varnas[-2] = mk(rep)
    dh.meta["6_4_92_mit_hrasva_done"] = True
    dh.meta["6_4_92_via_ec_ig_bundle"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.92",
    sutra_type=SutraType.VIDHI,
    text_slp1="mitAm hrasvaH",
    text_dev="मितां ह्रस्वः",
    padaccheda_dev="मिताम् / ह्रस्वः",
    why_dev="मित्-धातोः उपधायाः ह्रस्वः णिचि परे (हेड्→हिड्)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
