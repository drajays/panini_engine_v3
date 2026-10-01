"""
3.1.66  चिण् भावकर्मणोः  —  VIDHI

Padaccheda: चिण् भाव-कर्मणोः

Sources consulted:
- ashtadhyayi.com data.txt row i=31066 — anuvṛtti लुङि (3.1.43), च्लेः
  (3.1.44), ते (3.1.60 चिण् ते पदः)
- Kāśikā: "भावे तावत् — अशायि भवता। कर्मणि खल्वपि — अकारि कटो देवदत्तेन,
  अहारि भारो यज्ञदत्तेन।"
- Cross-validation: Vidyut / ashtadhyayi.com karmaṇi luṅ 3sg अभावि, अपाचि;
  regression tests tests/unit/test_tinanta_bhu_karmani_all_lakaras.py,
  tests/unit/test_upadesha_inputs.py

In luṅ (3.1.43 च्लि), when the following tiṅ is त (the anuvṛtti ते) and the
dhātu is used in bhāva or karman (the prayoga tag ``bhava_karma_usage``), च्लि
is replaced by चिण्. The ādeśa is written in upadeśa — च्, इ, ण् — so 1.3.7
(चुटू) and 1.3.3 (हलन्त्यम्) remove its it-letters and 1.3.9 leaves इ; the
ṇit-ness is recorded for 7.2.115/7.2.116. चिण् is ārdhadhātuka by 3.4.114.
6.4.104 चिणो लुक् then deletes the त.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not any("bhava_karma_usage" in t.tags for t in state.terms):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if t.kind != "pratyaya" or (t.meta.get("upadesha_slp1") or "").strip() != "cli":
            continue
        nxt = state.terms[i + 1]
        if "tin_adesha_3_4_78" not in nxt.tags:
            return None
        if "".join(v.slp1 for v in nxt.varnas) != "ta":
            return None
        return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas = parse_slp1_upadesha_sequence("ciR")
    t.meta["upadesha_slp1"] = "ciR"
    t.meta["it_markers"] = {"c", "R"}
    t.tags.update({"upadesha", "ardhadhatuka", "vikarana"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.66",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ciR BAvakarmaRoH",
    text_dev       = "चिण् भावकर्मणोः",
    padaccheda_dev = "चिण् भाव-कर्मणोः",
    why_dev        = "भावे कर्मणि च लुङि तशब्दे परे च्लेः चिण्-आदेशः (अकारि, अभावि)।",
    anuvritti_from = ("3.1.43", "3.1.44", "3.1.60"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
