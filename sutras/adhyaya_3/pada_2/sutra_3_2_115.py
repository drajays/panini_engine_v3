"""
3.2.115  परोक्षे लिट्  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  Introduce lakāra liṭ when the recipe marks parokṣa-bhūta context.

Engine:
  - recipe arms via ``state.meta['liT_lakara_recipe']``.
  - sets ``state.meta['lakara_liT'] = True`` and appends a placeholder pratyaya
    Term with ``upadesha_slp1 = 'liT'``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 32115 · परोक्षे लिट्
              padaccheda: परोक्षे लिट्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ् | 32084: भूते | 32111: अनद्यतने
  Source #2 — Kāśikā 3.2.115 udāharaṇa:
                तस्य विशेषणं परोक्षग्रहणम्
                ननु च धात्वर्थः सर्वः परोक्ष एव? सत्यमेतत्
                स यत्र नास्ति
  Cross-check — surface pinned by: tests/unit/test_IDe_lit_indh.py, tests/unit/test_jakzatuH_lit_ad_gas.py, tests/unit/test_kf_lit_kartari.py
  Reference record: sutra_ref_out/3_2_115.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    return bool(state.meta.get("liT_lakara_recipe")) and not state.meta.get("lakara_liT")


def act(state: State) -> State:
    if not cond(state):
        return state
    state.meta["lakara_liT"] = True
    state.meta["liT_lakara_recipe"] = False
    lit = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("liT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "liT"},
    )
    # drop it-marker T (as in laT placeholder handling)
    if lit.varnas and lit.varnas[-1].slp1 == "T":
        del lit.varnas[-1]
    state.terms.append(lit)
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.115",
    sutra_type=SutraType.VIDHI,
    text_slp1="parokze liT",
    text_dev="परोक्षे लिट्",
    padaccheda_dev="परोक्षे / लिट्",
    why_dev="परोक्ष-भूते लिट्-लकार-प्रत्ययः विधीयते (विभिदतुः)।",
    anuvritti_from=("3.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

