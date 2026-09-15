"""
3.3.173  आशिषि लिङ्लोटौ  —  VIDHI

In the sense of benediction (*āśīḥ*), introduce **liṅ** as the lakāra
placeholder.  Fires whenever the āśīr-liṅ coordination key is active and no
liṅ placeholder has yet been appended (idempotency guard).

cond: ``state.meta["ashir_liG"]`` is set (recipe coordination key, not an arm)
  AND no liG lakāra placeholder is already on the tape.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 33173 · आशिषि लिङ्लोटौ
              padaccheda: आशिषि लिङ्-लोटौ
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ्
  Source #2 — Kāśikā 3.3.173 udāharaṇa:
                प्रकृत्यर्थविशेषणं चैतत्
                चिरं जीव्याद् भवान्
                चिरं जीवतु भवान्
  Cross-check — surface pinned by: tests/unit/test_BitzIzwa_ashir_ling.py, tests/unit/test_saGgasIzwa_sam_gam_ashir_ling.py, tests/unit/test_tinanta_bhuyat_ashirling.py
  Reference record: sutra_ref_out/3_3_173.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("ashir_liG"):
        return False
    return not any((t.meta.get("upadesha_slp1") or "").strip() == "liG" for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    liG = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("liG"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "liG"},
    )
    state.terms.append(liG)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.173",
    sutra_type=SutraType.VIDHI,
    text_slp1="ASizi liG-loTow",
    text_dev="आशिषि लिङ्लोटौ",
    padaccheda_dev="आशिषि / लिङ्-लोटौ",
    why_dev="आशीः-अर्थे लिङ्-लकारः।",
    anuvritti_from=("3.3.157",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
