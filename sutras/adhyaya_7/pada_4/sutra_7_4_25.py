"""
7.4.25  अकृत्सार्वधातुकयोर्दीर्घः  —  VIDHI

Two operational paths:
  1. Arm ``corrected_v2_P016_7_4_25_arm``: narrow P016 path (lohitay stem).
  2. Arm ``ashir_7_4_25_recipe``: āśīr-liṅ — fires as a trace marker.
     BU (bhū) already has the long ū; dīrgha is vacuous here.  The rule
     formally applies before ārdhadhātuka (yāsuṭ is ārdhadhātuka context).
Pāṭha: ashtadhyayi.com data.txt row i=74025 (Art. 14).
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


_SHORT_IU = {"i": "I", "u": "U"}


def _vidhi_ling_yasut(state: State, j: int) -> bool:
    """yāsuṭ of *vidhi*-liṅ is sārvadhātuka (part of its tiṅ): yuyAt, not *yUyAt. Only āśīr-liṅ's is ārdhadhātuka."""
    t = state.terms[j]
    if "yasut_agama" not in t.tags and "ling_sIyuw" not in t.tags:
        return False
    tin = next((u for u in state.terms[j + 1:] if "tin_adesha_3_4_78" in u.tags), None)
    return tin is not None and "ashir_liG" not in tin.tags and "ardhadhatuka" not in tin.tags and "ardhadhatuka" not in t.tags


def _ajanta_before_kngit_y(state: State) -> int | None:
    """अकृत्सार्वधातुकयोर्दीर्घः (with 7.4.22 यि क्ङिति): a final i/u of the aṅga
    lengthens before a y-ādi kṅit that is neither kṛt nor sārvadhātuka — yak
    (क्षूयते), āśīrliṅ yāsuṭ (चीयात्). ṛ is left to riṅ/guṇa (7.4.28/29): riṅ is
    taught short, so क्रियते keeps its i."""
    for i, t in enumerate(state.terms[:-1]):
        nxt = state.terms[i + 1]
        if ("dhatu" in t.tags and t.varnas and t.varnas[-1].slp1 in _SHORT_IU
                and not t.meta.get("7_4_28_riN_done")      # riṅ is taught short
                and "kngiti" in nxt.tags and nxt.varnas and nxt.varnas[0].slp1 == "y"
                and "krt" not in nxt.tags and "sarvadhatuka" not in nxt.tags
                and "sarvadhatuka_3_4_113" not in nxt.tags
                and not _vidhi_ling_yasut(state, i + 1)):
            return i
    return None


def cond(state: State) -> bool:
    if _ajanta_before_kngit_y(state) is not None:
        return True
    if state.meta.get("ashir_7_4_25_recipe"):
        return not state.meta.get("7_4_25_ashir_done")
    if _karmani_vacuous_dirgha(state):
        return True
    return _site_p016(state)


def act(state: State) -> State:
    i = _ajanta_before_kngit_y(state)
    if i is not None:
        t = state.terms[i]
        t.varnas[-1] = mk(_SHORT_IU[t.varnas[-1].slp1])
        return state
    if _karmani_vacuous_dirgha(state) and not state.meta.get("ashir_7_4_25_recipe"):
        state.meta["7_4_25_karmani_done"] = True
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
    text_slp1='akftsArvaDAtukayordIrGaH',
    text_dev='अकृत्सार्वधातुकयोर्दीर्घः',
    samagra_slp1="aNgasya akftsArvaDAtukayoH dIrGaH kNiti yi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="अङ्गस्य अकृत्सार्वधातुकयोः दीर्घः क्ङिति यि",
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
