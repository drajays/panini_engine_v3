"""
7.4.25  अकृत्सार्वधातुकयोर्दीर्घः  —  VIDHI

Two operational paths:
  1. Arm ``corrected_v2_P016_7_4_25_arm``: narrow P016 path (lohitay stem).
  2. Arm ``ashir_7_4_25_recipe``: āśīr-liṅ — fires as a trace marker.
     BU (bhū) already has the long ū; dīrgha is vacuous here.  The rule
     formally applies before ārdhadhātuka (yāsuṭ is ārdhadhātuka context).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _site_p016(state: State) -> bool:
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "lohitay":
            continue
        if len(t.varnas) < 2:
            continue
        if t.varnas[-1].slp1 != "y" or t.varnas[-2].slp1 != "a":
            continue
        nxt = state.terms[i + 1]
        if nxt.kind != "pratyaya":
            continue
        up_n = (nxt.meta.get("upadesha_slp1") or "").strip()
        sap_surface = len(nxt.varnas) == 1 and nxt.varnas[0].slp1 == "a"
        if up_n not in {"a", "Sap"} and not sap_surface:
            continue
        if t.meta.get("7_4_25_dirgha_done"):
            continue
        return True
    return False


def _karmani_vacuous_dirgha(state: State) -> bool:
    """Karmaṇi/bhāve: *yaḳ* path — *dīrgha* vacuous when *aṅga* already has long *ī/ū*."""
    if state.meta.get("7_4_25_karmani_done"):
        return False
    if not any("dhatu" in t.tags and "bhava_karma_usage" in t.tags for t in state.terms):
        return False
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if any(v.slp1 in {"U", "I", "F", "X"} for v in t.varnas):
            return True
    return False


def cond(state: State) -> bool:
    if state.meta.get("ashir_7_4_25_recipe"):
        return not state.meta.get("7_4_25_ashir_done")
    if _karmani_vacuous_dirgha(state):
        return True
    return _site_p016(state)


def act(state: State) -> State:
    if _karmani_vacuous_dirgha(state) and not state.meta.get("ashir_7_4_25_recipe"):
        state.meta["7_4_25_karmani_done"] = True
        state.meta.pop("7_4_25_karmani_yak_arm", None)
        state.samjna_registry["7.4.25_karmani_vacuous"] = True
        return state
    if state.meta.get("ashir_7_4_25_recipe"):
        # Vacuous for BU (ū already long); fires as trace record only.
        state.meta["7_4_25_ashir_done"] = True
        state.meta.pop("ashir_7_4_25_recipe", None)
        state.samjna_registry["7.4.25_dirgha_ashir"] = True
        return state

    if not _site_p016(state):
        return state
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "lohitay":
            continue
        nxt = state.terms[i + 1]
        up_n = (nxt.meta.get("upadesha_slp1") or "").strip()
        sap_surface = len(nxt.varnas) == 1 and nxt.varnas[0].slp1 == "a"
        if up_n not in {"a", "Sap"} and not sap_surface:
            continue
        t.varnas[-2] = mk("A")
        t.meta["7_4_25_dirgha_done"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.25",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="akftsArvadhAtukayor dIrGaH",
    text_dev="अकृत्सार्वधातुकयोर्दीर्घः",
    padaccheda_dev="अकृतः / सार्वधातुकयोः / दीर्घः",
    why_dev=(
        "आर्धधातुके (आशीर्-लिङ्-यासुट्) परे अङ्गान्त-स्वरस्य दीर्घः "
        "(भू-धातौ तु ऊ-दीर्घः पूर्वमेव — शून्य-प्रयोगः)।"
    ),
    anuvritti_from=("7.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
