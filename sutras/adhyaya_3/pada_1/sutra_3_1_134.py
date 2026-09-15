"""
3.1.134  नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः  —  VIDHI (narrow: *ac*)

**Pāṭha:** *nandi-grahi-pacādibhyo lyu-ṇini-ac-aḥ* — from *nandī*–*grahi*–*pacādi*
roots, *lyu*, *ṇini*, *ac*, …

Narrow v3 (``prakriya_20`` *devam* leg):
  • ``state.meta['prakriya_20_3_1_134_arm']`` and ``state.meta['prakriya_20_nandi_pacadi']``.
  • Exactly one ``Term``: *dhātu* ``divi~`` (``upadesha_slp1`` ``divi~``), no *kṛt*
    yet.
  • ``act`` — append **ac** *kṛt* ``Term`` (``a`` + ``c`` *it*); ``dit_pratyaya``
    meta for **7.3.86**; ``citi_krt_ac`` for **6.1.163**; clear the arm.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31134 · नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः
              padaccheda: नन्दि-ग्रहि-पच्-आदिभ्यः ल्यु-णिनिँ-अचः
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ्
  Source #2 — Kāśikā 3.1.134 udāharaṇa:
                त्रिभ्यो गणेभ्यस्त्रयः प्रत्यया यथासंख्यं भवन्ति
                नन्दनः
                वाशनः
  Cross-check — surface pinned by: tests/unit/test_devam_krt.py, tests/unit/test_sutra_3_1_134_nandi_pacadi_ac.py
  Reference record: sutra_ref_out/3_1_134.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk


def _eligible(state: State) -> bool:
    if not state.meta.get("prakriya_20_3_1_134_arm"):
        return False
    if not state.meta.get("prakriya_20_nandi_pacadi"):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != "divi~":
        return False
    if any("krt" in t.tags for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=[mk("a"), mk("c")],
        tags={"pratyaya", "krt", "upadesha"},
        meta={
            "upadesha_slp1": "ac",
            "dit_pratyaya" : True,
            "citi_krt_ac"  : True,
        },
    )
    state.terms.append(pr)
    state.meta.pop("prakriya_20_3_1_134_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.134",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "nandi-grahi-pacAdibhyo lyuRini-acaH",
    text_dev       = "नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः",
    padaccheda_dev = "नन्दि-ग्रहि-पचादिभ्यः / ल्यु-णिनि-अचः",
    why_dev        = "पचाद्यङ्गात् अच्-प्रत्ययः (दिव् → देव-, प्रक्रिया-२०)।",
    anuvritti_from = ("3.1.91",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
