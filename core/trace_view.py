"""
core/trace_view.py — presentation layer for engine traces.
─────────────────────────────────────────────────────────

Turns a raw ``State.trace`` (SLP1 strings + sūtra ids) into something a human
or an HTTP client can read: Devanāgarī forms, sūtra text, anuvṛtti links.

Pure view code — it never touches ``State`` internals and is never imported by
``engine`` or ``sutras``.  Shared by ``webui`` (HTML) and ``api`` (JSON).
"""
from __future__ import annotations

import sutras  # noqa: F401 — fills SUTRA_REGISTRY
from core.i18n_hi import hint_for_sutra
from engine import SUTRA_REGISTRY

# ─────────────────────────────────────────────────────────────────
# Presentation-layer transliteration helpers
# (pure view code — never touches State internals)
# ─────────────────────────────────────────────────────────────────

# Structural step IDs → clean Devanāgarī labels shown in the UI.
STRUCTURAL_DEV: dict[str, str] = {
    "__MERGE__"             : "पद-मेलनम्",
    "__FIXED_POINT__"       : "स्थिर-बिन्दुः",
    "__TRIPADI_ENTER__"     : "त्रिपाद्याः-प्रवेशः",
    "__ANGA_SWEEP__"        : "अङ्ग-परीक्षा",
    "__IT_LOPA_PASS__"      : "इत्-लोपः",
    "__SANDHI_PASS__"       : "सन्धिः",
    "__COMPOUND_MERGE__"    : "समास-मेलनम्",
}


def slp1_str_to_dev(slp1_str: str) -> str:
    """
    Convert a flat SLP1 form string (as stored in trace form_before/form_after)
    to Devanāgarī for display.

    Strategy: parse the SLP1 string through the engine's phoneme parser so that
    conjunct consonants, mātrās, and halanta virāmas are rendered correctly by
    the joiner — identical to how State.flat_dev() works on the live State tape.

    Structural IDs (e.g. '__MERGE__') are mapped to Devanāgarī labels.
    Empty strings stay empty.  Unparseable strings fall back to the original.
    """
    if not slp1_str:
        return ""
    # Structural marker
    if slp1_str in STRUCTURAL_DEV:
        return STRUCTURAL_DEV[slp1_str]
    try:
        from phonology.varna import parse_slp1_upadesha_sequence
        from phonology.joiner import slp1_to_devanagari
        varnas = parse_slp1_upadesha_sequence(slp1_str)
        return slp1_to_devanagari(varnas)
    except Exception:
        return slp1_str  # safe fallback — never break the UI


def enrich_trace(raw_trace: list[dict]) -> list[dict]:
    """
    Add presentation-layer fields to every trace step dict:

      form_before_dev   : Devanāgarī rendering of form_before (SLP1 → Dev)
      form_after_dev    : Devanāgarī rendering of form_after  (SLP1 → Dev)
      _sutra_text_dev   : sūtra text from SUTRA_REGISTRY (was already set inline)
      _padaccheda_dev   : padaccheda from SUTRA_REGISTRY
      _anuvritti_from   : list of IDs from SUTRA_REGISTRY
      _is_structural    : True for __MERGE__ etc.
      _structural_dev   : Devanāgarī label for structural steps

    The original SLP1 strings in form_before / form_after are left intact;
    only the _dev variants are added.  State objects are never imported here.
    """
    out = []
    for step in raw_trace:
        sid = step.get("sutra_id", "")
        rec = SUTRA_REGISTRY.get(sid) if sid and not sid.startswith("__") else None
        is_struct = bool(sid.startswith("__")) if sid else False

        fb = step.get("form_before", "") or ""
        fa = step.get("form_after",  "") or ""

        out.append({
            **step,
            # Devanāgarī transliterations (presentation only)
            "form_before_dev" : slp1_str_to_dev(fb),
            "form_after_dev"  : slp1_str_to_dev(fa),
            # Sūtra metadata from registry
            "_is_structural"  : is_struct,
            "_structural_dev" : STRUCTURAL_DEV.get(sid, "") if is_struct else "",
            "_sutra_text_dev" : getattr(rec, "text_dev",       None),
            "_padaccheda_dev" : getattr(rec, "padaccheda_dev", None),
            "_anuvritti_from" : list(getattr(rec, "anuvritti_from", ()) or ()),
            # Learner aid, not the sūtra's meaning — see core/i18n_hi (UNREVIEWED).
            "_hint_hi"        : hint_for_sutra(sid) if sid else "",
        })
    return out


def filter_surface_changed(trace: list[dict]) -> list[dict]:
    """Only the steps that actually changed the form.

    The reading a scholar usually wants: saṃjñā and adhikāra rows are real
    applications, but they leave the tape untouched, so a surface-only view
    shows the derivation's operations.
    """
    return [s for s in trace if s.get("form_before") != s.get("form_after")]
