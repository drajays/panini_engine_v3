"""
SLP1 ↔ Devanāgarī — single *rendering* path for flat SLP1 strings.

Uses the engine phonology stack (``parse_slp1_upadesha_sequence`` +
``slp1_to_devanagari``), not ad-hoc per-character replacement.
"""
from __future__ import annotations

# Optional: IAST for labels / tools only (keeps a single extra scheme here).
try:
    from indic_transliteration import sanscript
except ImportError:  # pragma: no cover — extra scheme only
    sanscript = None  # type: ignore[assignment]

from phonology.joiner import slp1_to_devanagari
from phonology.tokenizer import devanagari_to_slp1_flat
from phonology.varna import parse_slp1_upadesha_sequence


def slp1_to_dev(text: str) -> str:
    """Render flat SLP1 (e.g. ``SAlIyaH``) to Devanāgarī (``शालीयः``)."""
    t = (text or "").strip()
    if not t:
        return ""
    varnas = parse_slp1_upadesha_sequence(t)
    return slp1_to_devanagari(varnas)


def dev_to_slp1(text: str) -> str:
    """Normalize Devanāgarī to flat SLP1 (inverse of :func:`slp1_to_dev` / UI path)."""
    return devanagari_to_slp1_flat((text or "").strip())


def slp1_to_iast(text: str) -> str:
    """SLP1 → IAST; requires ``indic-transliteration``."""
    if sanscript is None:
        raise RuntimeError(
            "slp1_to_iast needs package indic-transliteration "
            "(pip install indic-transliteration)"
        )
    return str(
        sanscript.transliterate(text, sanscript.SLP1, sanscript.IAST)
    )


# Known good pairs for smoke tests and docs (not an exhaustive test oracle).
_KNOWN_SLP1_DEV: dict[str, str] = {
    "SAlIyaH": "शालीयः",
    "SAlIya": "शालीय",
    "SAlA": "शाला",
    "mAlIyaH": "मालीयः",
    "mAlIya": "मालीय",
    "mAlA": "माला",
}


def validate_transliteration() -> None:
    """
    Assert engine phonology + joiner still match expected Devanagarī
    for a small allowlisted set.  Call from tests only.
    """
    errors: list[str] = []
    for slp, expected in _KNOWN_SLP1_DEV.items():
        got = slp1_to_dev(slp)
        if got != expected:
            errors.append(f"  slp1_to_dev({slp!r}) = {got!r} (expected {expected!r})")
    if errors:
        raise AssertionError("Transliteration validation failed:\n" + "\n".join(errors))


__all__ = [
    "dev_to_slp1",
    "slp1_to_dev",
    "slp1_to_iast",
    "validate_transliteration",
]
