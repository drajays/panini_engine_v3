"""
1.1.43  सुडनपुंसकस्य  —  SAMJNA

Narrow v3:
  • ``state.meta["1_1_43_arm"]`` + final *sup* whose *upadeśa* begins with ``s``
    (e.g. *su*–*m* row) → ``sarvanamasthana`` tag (read by **7.1.70** / **7.1.72**).
  • ``prakriya_21`` — ``state.meta["prakriya_21_1_1_43_am_arm"]`` + *tṛc* stem
    (``krt_tfc``) + ``am`` *sup* → same tag so **7.3.110** / **6.4.11** can see
    *sarvanāmasthāna* without reading ``(vibhakti, vacana)``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

TAG = "sarvanamasthana"


def _eligible_s_sup(state: State) -> bool:
    if not state.meta.get("1_1_43_arm"):
        return False
    if not state.terms:
        return False
    pr = state.terms[-1]
    if pr.kind != "pratyaya" or "sup" not in pr.tags:
        return False
    if not pr.varnas:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if TAG in pr.tags:
        return False
    return True


def _eligible_prakriya_21_am(state: State) -> bool:
    if not state.meta.get("prakriya_21_1_1_43_am_arm"):
        return False
    if len(state.terms) < 2:
        return False
    ang = state.terms[-2]
    pr = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags:
        return False
    if pr.kind != "pratyaya" or "sup" not in pr.tags:
        return False
    if (pr.meta.get("upadesha_slp1") or "").strip() != "am":
        return False
    if TAG in pr.tags:
        return False
    return True


def _eligible_sup_sarvanamasthana(state: State) -> bool:
    """
    New path (v3.2): fires when a sup term has 'sup_sarvanamasthana_eligible' tag
    AND the stem is non-napumsaka.  Does NOT require the 1_1_43_arm meta flag.
    This encodes: सुड् अनपुंसकस्य — the su-p (sarvanamasthana-eligible cells)
    of non-neuter declension receive sarvanamasthana saṃjñā.
    """
    # Find a sup pratyaya that is eligible but not yet tagged
    sup_term = None
    for t in state.terms:
        if t.kind == "pratyaya" and "sup" in t.tags:
            if "sup_sarvanamasthana_eligible" in t.tags and TAG not in t.tags:
                sup_term = t
                break
    if sup_term is None:
        return False
    # Stem must be non-napumsaka: no napuṃsaka tag on any prakriti/prātipadika term
    for t in state.terms:
        if "prātipadika" in t.tags or t.kind == "prakriti":
            if "napuṃsaka" in t.tags:
                return False
    return True


def cond(state: State) -> bool:
    return (
        _eligible_s_sup(state)
        or _eligible_prakriya_21_am(state)
        or _eligible_sup_sarvanamasthana(state)
    )


def act(state: State) -> State:
    if _eligible_sup_sarvanamasthana(state):
        # Tag all eligible-but-untagged sup terms
        for t in state.terms:
            if (
                t.kind == "pratyaya"
                and "sup" in t.tags
                and "sup_sarvanamasthana_eligible" in t.tags
                and TAG not in t.tags
            ):
                t.tags.add(TAG)
        state.samjna_registry["1.1.43_su_sarvanamasthana"] = True
        return state
    if not (_eligible_s_sup(state) or _eligible_prakriya_21_am(state)):
        return state
    pr = state.terms[-1]
    pr.tags.add(TAG)
    state.samjna_registry["1.1.43_su_sarvanamasthana"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.43",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "suDanapuMsakasya",
    text_dev       = "सुडनपुंसकस्य",
    padaccheda_dev = "सुड्-अनपुंसकस्य",
    why_dev        = "सु-प्रत्ययः (नपुंसकाद् भिन्नः) सर्वनामस्थान-संज्ञकः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
