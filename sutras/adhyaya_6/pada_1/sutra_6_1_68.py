"""
6.1.68  हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्  —  VIDHI (universal)

The apṛkta *hal* (single consonant *su* / *ti* / *si* residue) is dropped after:

  (a) a **hal**-final *aṅga* (consonant-final stem), or
  (b) a **dīrgha-Ī**-final *aṅga* (*ṅī*-anta, long *ī* strī pratyaya), or
  (c) a **dīrgha-Ā**-final *aṅga* (*Āp*-anta, long *ā* strī pratyaya / *ṭāp*).

Engine (universal): scans all adjacent *(aṅga, sup)* pairs.  The *sup* must be
exactly one *varna*, tagged **apṛkta** (by **1.2.41**), and that *varna* must be
``s``.  The *aṅga*'s final *varna* must be in HAL, or be long ``A`` or ``I``.

``cond`` / ``_find_eligible_boundary`` use only the phonological environment.

When a rule application succeeds, ``act`` may also set **demo-scoped** registry
keys if ``state.meta`` carries a known arm **and** the eligible *aṅga* bears
the matching witness tag (telemetry only; not read by ``cond``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import HAL

from sutras.adhyaya_1.pada_2.sutra_1_2_41 import TAG_APRKTA

# Finals that licence 6.1.68 on the ṅī / Āp (dīrgha) branch.
_DIRGHA_STRĪ_FINALS = frozenset({"A", "I"})

# (meta arm key, ``samjna_registry`` stamp, required subset of *aṅga* ``tags``)
_DEMO_6_1_68_SIGNATURES: tuple[tuple[str, str, frozenset[str]], ...] = (
    ("P041_6_1_68_arm", "6.1.68_hal_sup_lopa_P041", frozenset({"P041_agnicit_demo"})),
    (
        "prakriya_37_6_1_68_tApanta_arm",
        "6.1.68_tApanta_sup_lopa_prakriya_37",
        frozenset({"prakriya_37_pAcakavndArikA_Atap_demo"}),
    ),
    (
        "prakriya_36_ardhaBAj_sup_lopa_arm",
        "6.1.68_ardhaBAj_sup_lopa_prakriya_36",
        frozenset({"prakriya_36_ardhaBAj_demo"}),
    ),
    (
        "prakriya_35_vAc_sup_lopa_arm",
        "6.1.68_vAc_sup_lopa_prakriya_35",
        frozenset({"prakriya_35_vAc_sup_demo"}),
    ),
    ("P039_6_1_68_tApanta_arm", "6.1.68_tApanta_sup_lopa_P039", frozenset({"P039_viSAKA_demo"})),
)


def _stamp_demo_6_1_68_aliases(state: State, anga_i: int) -> None:
    if anga_i < 0 or anga_i >= len(state.terms):
        return
    tags = state.terms[anga_i].tags
    for meta_key, reg_key, need in _DEMO_6_1_68_SIGNATURES:
        if not state.meta.get(meta_key):
            continue
        if not need.issubset(tags):
            continue
        state.samjna_registry[reg_key] = True


def _find_eligible_boundary(state: State) -> int | None:
    """
    Return index *i* such that ``terms[i]`` is an *aṅga* eligible under 6.1.68
    and ``terms[i+1]`` is an apṛkta ``s`` (*sup*).
    """
    for i in range(len(state.terms) - 1):
        anga = state.terms[i]
        pr = state.terms[i + 1]
        if "anga" not in anga.tags:
            continue
        if not anga.varnas:
            continue
        final = anga.varnas[-1].slp1
        if final not in HAL and final not in _DIRGHA_STRĪ_FINALS:
            continue
        if "sup" not in pr.tags:
            continue
        if len(pr.varnas) != 1:
            continue
        if TAG_APRKTA not in pr.tags:
            continue
        if pr.varnas[0].slp1 != "s":
            continue
        # Long-ā / long-ī strī (ङी·आप्) before apṛkta ``s`` of *su* (प्रथमा
        # एकवचनम्): **6.1.68** applies.  सम्बुद्धि-एकवचनम् is handled by **7.3.106**
        # + **6.1.69** instead — do not delete ``s`` here or **7.3.106** never sees
        # the ``su`` residue (``cond`` is tag-based only; no ``vibhakti`` read).
        if final in _DIRGHA_STRĪ_FINALS and "sambuddhi" in pr.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_eligible_boundary(state) is not None


def act(state: State) -> State:
    i = _find_eligible_boundary(state)
    if i is None:
        return state
    pr = state.terms[i + 1]
    pr.varnas.clear()
    state.terms.pop(i + 1)
    state.samjna_registry["6.1.68_aprkta_sup_lopa"] = True
    _stamp_demo_6_1_68_aliases(state, i)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.68",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hal~yAbbhyo dIrghAt sutisyapfktaM hal",
    text_dev       = "हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्",
    padaccheda_dev = "हल्-ङि-आभ्यः / दीर्घात् / सु-तिसि-अपृक्तम् / हल्",
    why_dev        = "हल्-अन्तात् / ङी-आभ्-अन्तात् दीर्घात् अङ्गात् परस्य अपृक्त-सु-हल्-लोपः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
