"""
3.1.134  नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः  —  VIDHI (narrow: *ac*)

**Pāṭha:** *nandi-grahi-pacādibhyo lyu-ṇini-ac-aḥ* — from *nandī*–*grahi*–*pacādi*
roots, *lyu*, *ṇini*, *ac*, …

Narrow v3 (``prakriya_20`` *devam* leg):
  • ``state.meta['prakriya_20_3_1_134_arm']`` and ``state.meta['prakriya_20_nandi_pacadi']``.
  • Exactly one ``Term``: *dhātu* ``divu~`` (``upadesha_slp1`` ``divu~``), no *kṛt*
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
from engine.krt_eligibility import krt_insertion_eligible, requested_krt_upadesha
from phonology import mk

_PACADI = frozenset({"vid", "vida", "vida~", "pac", "div", "divu", "divu~"})
_GATE_KEY = "3_1_134_nandi_pacadi_ac"


def _dhatu(state: State):
    return next((t for t in state.terms if "dhatu" in t.tags), None)


def _eligible_prakriya_20(state: State) -> bool:
    if not state.meta.get("prakriya_20_nandi_pacadi"):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != "divu~":
        return False
    if any("krt" in t.tags for t in state.terms):
        return False
    return True


def _eligible_pacadi_ac(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.134", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    if requested_krt_upadesha(state) != "ac":
        return False
    if any("krt" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    dh = _dhatu(state)
    if dh is None:
        return False
    up = (dh.meta.get("upadesha_slp1") or "").strip()
    flat = "".join(v.slp1 for v in dh.varnas)
    return up in _PACADI or flat in _PACADI or up.rstrip("~") in _PACADI


def _eligible(state: State) -> bool:
    return _eligible_prakriya_20(state) or _eligible_pacadi_ac(state)


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=[mk("a"), mk("c")],
        tags={"pratyaya", "krt", "upadesha", "ardhadhatuka"},
        meta={
            "upadesha_slp1": "ac",
            "dit_pratyaya": True,
            "citi_krt_ac": True,
        },
    )
    state.terms.append(pr)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["krt_kind"] = "3.1.134"
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.134",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'nandigrahipacAdiByo lyuRinyacaH',
    text_dev       = 'नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः',
    samagra_slp1   = "pratyayaH paraSca AdyudAttaSca DAtoH nandi-grahi-pacAdiByaH lyu-Rini-acaH kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "प्रत्ययः परश्च आद्युदात्तश्च धातोः नन्दि-ग्रहि-पचादिभ्यः ल्यु-णिनि-अचः कृत्",
    padaccheda_dev = "नन्दि-ग्रहि-पचादिभ्यः / ल्यु-णिनि-अचः",
    why_dev        = "पचाद्यङ्गात् अच्-प्रत्ययः (दिव् → देव-, प्रक्रिया-२०)।",
    anuvritti_from = ("3.1.91",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
