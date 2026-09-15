"""
3.1.44  च्लेः सिच्  —  VIDHI (narrow: cli → sic)

Engine: if a pratyaya Term has upadeśa "cli", replace its varṇas with upadeśa
"sic" (and tag as pratyaya upadeśa). Subsequent it-lopa (1.3.3/1.3.9) will
strip the final c-it, leaving "si" (or operationally "s").

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31044 · च्लेः सिच्
              padaccheda: च्लेः सिच्
              anuvṛtti:   31043: लुङि
  Source #2 — Kāśikā 3.1.44 udāharaṇa:
                इकार उच्चारणार्थः
                अकार्षीत्
                अहार्षीत्
  Cross-check — surface pinned by: tests/unit/test_acaEzIt_pipeline.py, tests/unit/test_tinanta_abhut_lung.py
  Reference record: sutra_ref_out/3_1_44.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _cli_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "cli":
            return i
    return None


def cond(state: State) -> bool:
    return _cli_index(state) is not None


def act(state: State) -> State:
    i = _cli_index(state)
    if i is None:
        return state
    t = state.terms[i]
    # In luṅ prakriyā, the phonetic 'i' in सिच् is uccāraṇārtha in our glass-box
    # recipes; the productive marker is 's' and the final 'c' is the it-letter.
    # Keep ``upadesha_slp1`` as "sic" for downstream identification (e.g. 7.2.1),
    # but place only ``s`` + ``c`` on the tape so the standard it-chain yields just ``s``.
    t.varnas = parse_slp1_upadesha_sequence("sc")
    t.meta["upadesha_slp1"] = "sic"
    t.tags.add("upadesha")
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.44",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "cleH sic",
    text_dev       = "च्लेः सिच्",
    padaccheda_dev = "च्लेः / सिच्",
    why_dev        = "च्लि-आगमस्य स्थाने सिच्-आदेशः (लुङ्-सिच्-प्रक्रिया)।",
    anuvritti_from = ("3.1.43",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

