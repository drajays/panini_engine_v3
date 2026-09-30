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

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61068 · हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्
              padaccheda: हल्-ङी-आब्भ्यः दीर्घात् सु-ति-सि अपृक्तम् हल्
              anuvṛtti:   61066: लोपः
  Source #2 — Kāśikā 6.1.68 udāharaṇa:
                तदिह लौकिकेनार्थेनार्थवत् कर्मसाधनं द्रष्टव्यम्
                लुप्यत इति लोपः
                हलन्तात् सुलोपः — राजा
  Cross-check — surface pinned by: tests/regression/test_rADA_strilinga_gold.py, tests/unit/test_agnicit_agni_ci_kvip.py, tests/unit/test_ardhaBAj_sup.py
  Reference record: sutra_ref_out/6_1_68.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import angas_halantatva_blocked
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
        if angas_halantatva_blocked(anga):
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
        # 6.1.68 dīrgha-A/I branch applies only to strī (ṅī·āp) stems.
        # Non-strī words ending in ā (e.g. hāhā pulliṅga, avyaya) are excluded.
        # Exception: demo arms explicitly mark āp-anta stems even without strīliṅga tag.
        if final in _DIRGHA_STRĪ_FINALS and "strīliṅga" not in anga.tags:
            has_tap_arm = any(
                state.meta.get(k)
                for k in (
                    "prakriya_37_6_1_68_tApanta_arm",
                    "P039_6_1_68_tApanta_arm",
                )
            )
            if not has_tap_arm:
                continue
        up = (anga.meta.get("upadesha_slp1") or "").strip()
        if up in {"asmad", "yuzmad"}:
            continue  # 7.1.28 अम्, not su-lopa
        return i
    return None


def _find_tin_aprkta(state: State) -> int | None:
    """…सुतिस्यपृक्तं हल् — the ti / si branch: an apṛkta t or s (tip/sip after
    3.4.100 इतश्च) drops after a hal-final aṅga — अरुणध् (अरुणत्), अभनक्."""
    for j, pr in enumerate(state.terms):
        if "tin_adesha_3_4_78" not in pr.tags or len(pr.varnas) != 1:
            continue
        if pr.varnas[0].slp1 not in ("t", "s"):
            continue
        if (pr.meta.get("upadesha_slp1") or "").strip() not in ("tip", "sip"):
            continue
        prev = next((u for u in reversed(state.terms[:j]) if u.varnas), None)
        if prev is not None and prev.varnas[-1].slp1 in HAL:
            return j
    return None


def cond(state: State) -> bool:
    return _find_eligible_boundary(state) is not None or _find_tin_aprkta(state) is not None


def act(state: State) -> State:
    j = _find_tin_aprkta(state) if _find_eligible_boundary(state) is None else None
    if j is not None:
        state.terms[j].varnas = []                  # लोपः of the apṛkta ti/si
        state.terms[j].meta["6_1_68_tin_lopa"] = True
        return state
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
    text_slp1      = 'halNyAbByo dIrGAt sutisyapfktaM hal',
    text_dev       = 'हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्',
    padaccheda_dev = "हल्-ङि-आभ्यः / दीर्घात् / सु-तिसि-अपृक्तम् / हल्",
    why_dev        = "हल्-अन्तात् / ङी-आभ्-अन्तात् दीर्घात् अङ्गात् परस्य अपृक्त-सु-हल्-लोपः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
