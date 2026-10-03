"""
3.3.13  लृट् शेषे च  —  VIDHI

Padaccheda: लृट् शेषे च

Glass-box: under the **3.3.3** *bhaviṣyati* adhikāra, when the recipe arms
``lfT_recipe`` (future, not *anadyatana*-restricted — the *śeṣa* of 3.3.15),
attach the *lṛṭ* *lac* placeholder (``lf``, halantya ṭ pre-stripped) after the
*dhātu*. Idempotent: no second *lṛṭ* term is added.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 33013 · लृट् शेषे च
              padaccheda: लृट् शेषे च
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ् | 33003: भविष्यति | 33010: क्रियायाम्  क्रियार्थायाम्
  Source #2 — Kāśikā 3.3.13 udāharaṇa:
                शेषः क्रियार्थोपपदादन्यः
                करिष्यामीति व्रजति
                हरिष्यामीति व्रजति
  Cross-check — Vidyut surface ✓ भविष्यति / गमिष्यति; surface pinned by
                tests/unit/test_tinanta_abhavisyat_lrg.py, tests/unit/test_gam_lrt_7_2_58.py
  Reference record: sutra_ref_out/3_3_13.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.lakara_attach import attach_lakara, lakara_site
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _has_lfT(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == "lRT" for t in state.terms)


def cond(state: State) -> bool:
    if lakara_site(state, "lrt_derivation", "3.3.13", ("lfT_recipe",)):
        return True
    if not state.meta.get("lfT_recipe") or _has_lfT(state):
        return False
    return adhikara_in_effect("3.3.13", state, "3.3.3")


def act(state: State) -> State:
    if lakara_site(state, "lrt_derivation", "3.3.13", ("lfT_recipe",)):
        return attach_lakara(state, "lRT")
    vs = parse_slp1_upadesha_sequence("lRT")
    if vs and vs[-1].slp1 == "T":
        vs = vs[:-1]
    state.terms.append(Term(
        kind="pratyaya",
        varnas=vs,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "lRT"},
    ))
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.13",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "lfw Seze ca",
    text_dev       = "लृट् शेषे च",
    padaccheda_dev = "लृट् शेषे च",
    why_dev        = "भविष्यति काले (अनद्यतनात् शेषे च) धातोः लृट्-लकारः।",
    anuvritti_from = ("3.3.3", "3.3.10"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
