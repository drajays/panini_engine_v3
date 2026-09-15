"""
3.1.7  धातोः कर्मणः समानकर्तृकादिच्छायां वा  —  VIDHI

In the sense of desire (icchā), add the sanādi pratyaya ``san`` (surface ``is``)
after the dhātu.

Structural trigger (CONSTITUTION Art. 13): ``state.meta["san_recipe"] == "san"``
coordination key (like ``krtya_recipe``).  No arm flag needed.
Backward-compat: ``3_1_7_san_arm`` still accepted so existing pipelines continue.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31007 · धातोः कर्मणः समानकर्तृकादिच्छायां वा
              padaccheda: धातोः कर्मणः समान-कर्तृकात् इच्छायाम् वा
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31005: सन्
  Source #2 — Kāśikā 3.1.7 udāharaṇa:
                कर्मत्वं समानकर्तृकत्वं च धातोरर्थद्वारकम्
                कर्तुमिच्छति
                जिहीर्षति
  Cross-check — surface pinned by: tests/constitutional/test_no_new_duplicates.py, tests/unit/test_akurvAtAm_laG_tanadi_kf.py, tests/unit/test_cicIzati_ci_san_desiderative.py
  Reference record: sutra_ref_out/3_1_7.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _wants_san(state: State) -> bool:
    if state.meta.get("san_recipe") == "san":
        return True
    return bool(state.meta.get("3_1_7_san_arm"))


def cond(state: State) -> bool:
    if not _wants_san(state):
        return False
    # avoid duplicates
    return not any((t.meta.get("upadesha_slp1") or "").strip() in {"san", "is"} and "sanadi" in t.tags for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    san = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("is"),
        # Not marked as `upadesha` so 1.3.3 (halantyam) doesn't delete final `s`.
        tags={"pratyaya", "sanadi", "ardhadhatuka"},
        meta={"upadesha_slp1": "is"},
    )
    state.terms.append(san)
    state.meta.pop("san_recipe", None)
    state.meta["3_1_7_san_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.7",
    sutra_type=SutraType.VIDHI,
    text_slp1="DAtoH karmaNaH samAnakartfka-icchAyAm vA (narrow)",
    text_dev="धातोः कर्मणः समानकर्तृकादिच्छायां वा",
    padaccheda_dev="धातोः / कर्मणः / समानकर्तृकात् / इच्छायाम् / वा",
    why_dev="इच्छार्थे धातोः सन्-प्रत्ययः (रुरुदिषति)।",
    anuvritti_from=("3.1.1", "3.1.2"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

