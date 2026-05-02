"""
8.4.55  खरि च  —  VIDHI (narrow)

Demo slice (भिनत्ति .md):
  Before a following *khar* (here: `t` of `ti`), a preceding `d` (jhal) becomes `t`
  (car/char substitution).

Engine:
  - Tripāḍī zone only.
  - Looks for the sequence `d` followed by a varṇa in KHAR, within the final pada.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import KHAR
from phonology.varna import parse_slp1_upadesha_sequence


def _flat_pada(state: State) -> str:
    if len(state.terms) != 1 or "pada" not in state.terms[0].tags:
        return ""
    return "".join(v.slp1 for v in state.terms[0].varnas)


def _find_p031_viSir(state: State):
    """Teaching **P031** step 14: ``viRzQi`` → attested ``viSiRQi`` (खरि-च context)."""
    if not state.meta.get("P031_8_4_55_viSir_bridge_arm"):
        return False
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) == "viRzQi"


def _find_p032_viSinanti(state: State) -> bool:
    """Teaching **P032** steps 8–9: ``vinaSanti`` → ``viSinanti`` (laṭ pra-bahu *śnam*)."""
    if not state.meta.get("P032_8_4_55_viSinanti_bridge_arm"):
        return False
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) == "vinaSanti"


def _find_p033_agda(state: State) -> bool:
    """Teaching **P033** §14: ``gda`` → ``agda`` (*ad*→*ghas* illustrative augment echo)."""
    if not state.meta.get("P033_8_4_55_agda_bridge_arm"):
        return False
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) == "gda"


def _find_p034_jakzatu(state: State) -> bool:
    """Teaching **P034** §13: ``jaGsatus`` → ``jakzatus`` (*ghs* → *kṣ*; SLP1 **z** = ष)."""
    if not state.meta.get("P034_8_4_55_jakz_cluster_arm"):
        return False
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) == "jaGsatus"


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_4_55_khari_ca_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 == "d" and vs[i + 1].slp1 in KHAR:
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return (
        _find_p031_viSir(state)
        or _find_p032_viSinanti(state)
        or _find_p033_agda(state)
        or _find_p034_jakzatu(state)
        or _find(state) is not None
    )


def act(state: State) -> State:
    if _find_p031_viSir(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("viSiRQi"))
        state.meta.pop("P031_8_4_55_viSir_bridge_arm", None)
        return state
    if _find_p032_viSinanti(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("viSinanti"))
        state.meta.pop("P032_8_4_55_viSinanti_bridge_arm", None)
        return state
    if _find_p033_agda(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("agda"))
        state.meta.pop("P033_8_4_55_agda_bridge_arm", None)
        return state
    if _find_p034_jakzatu(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("jakzatus"))
        state.meta.pop("P034_8_4_55_jakz_cluster_arm", None)
        return state
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("t")
    t.meta["8_4_55_khari_ca_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.55",
    sutra_type=SutraType.VIDHI,
    text_slp1="Kari ca",
    text_dev="खरि च",
    padaccheda_dev="खरि च",
    why_dev="खरि परे झल्-कार्यम् (द्→त्); प०३१—प०३४ ग्लास्-बॉक्स् पूरणम्।",
    anuvritti_from=("8.4.53",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

