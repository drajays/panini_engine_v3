"""
3.2.135  तृन्  —  VIDHI (narrow ``split_prakriyas_11`` **P003**)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=32135):** *tṛn* — agent-noun **tṛn** (*kartari*
*kṛt*) after the dhātu (``anuvṛtti``: ``dhātoḥ``, ``kṛt``, ``pratyaya``, etc.).

**Engine:** appends **तृन्** as SLP1 ``tfn`` (``t`` + ``f`` + ``n`` — ``n`` *it* via **1.3.3**) so the
post-merge stem ends in ``f`` (same tape shape as **tṛc**) when ``meta['prakriya_P003_3_2_135_tRn_arm']``
and ``vac`` bears ``prakriya_P003_vaktA_demo``. (Commentary often writes ``tRn``; phonemic parse here is ``tfn``.)

Full *śāstra* scope (**3.2.123** *vartamāne*, **3.2.134** *ā kvib…*, etc.) is offline —
glass-box **P003** only.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("prakriya_P003_3_2_135_tRn_arm"):
        return False
    if state.meta.get("prakriya_P003_3_2_135_done"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_P003_vaktA_demo" in t.tags for t in state.terms):
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "tfn" for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("tfn")),
        tags={"pratyaya", "upadesha", "krt", "ardhadhatuka"},
        meta={
            "upadesha_slp1": "tfn",
            "upadesha_slp1_original": "tfn",
            "krit_pratyaya": "tfn",
        },
    )
    state.terms.append(pr)
    state.meta["prakriya_P003_3_2_135_done"] = True
    state.meta["prakriya_P003_3_2_135_tRn_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.135",
    sutra_type=SutraType.VIDHI,
    text_slp1="tfn",
    text_dev="तृन्",
    padaccheda_dev="तृन्",
    why_dev="कर्तरि तृन् (*P003* **वक्ता**, धातु **वच्**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
