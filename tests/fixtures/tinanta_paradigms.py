"""
tests/fixtures/tinanta_paradigms.py — BHŪ tiṅanta paradigm wrappers.

These thin wrappers call ``pipelines.tinanta.derive`` for the complete
bhū paradigm across laṭ, lṛṭ, laṅ, liṅ, āśīr-liṅ, luṅ, and lṛṅ lakāras.

Use these in tests instead of importing wrapper functions from
``pipelines.tinanta`` directly — the tinanta module will shed these
in Phase 5 (pipeline thinning) and this file becomes the single source.
"""
from __future__ import annotations

from pipelines.tinanta import derive
from engine.state import State


# ── laṭ ──────────────────────────────────────────────────────────────────────
def derive_bhavati() -> State:
    return derive("BU", "laT", "kartari", 3, 1)

def derive_bhavataH() -> State:
    return derive("BU", "laT", "kartari", 3, 2)

def derive_bhavanti() -> State:
    return derive("BU", "laT", "kartari", 3, 3)

def derive_bhavasi() -> State:
    return derive("BU", "laT", "kartari", 2, 1)

def derive_bhavathah() -> State:
    return derive("BU", "laT", "kartari", 2, 2)

def derive_bhavatha() -> State:
    return derive("BU", "laT", "kartari", 2, 3)

def derive_bhavami() -> State:
    return derive("BU", "laT", "kartari", 1, 1)

def derive_bhavavah() -> State:
    return derive("BU", "laT", "kartari", 1, 2)

def derive_bhavamah() -> State:
    return derive("BU", "laT", "kartari", 1, 3)


# ── lṛṭ ──────────────────────────────────────────────────────────────────────
def derive_bhavisyati() -> State:
    return derive("BU", "lRT", "kartari", 3, 1)

def derive_bhavisyatah() -> State:
    return derive("BU", "lRT", "kartari", 3, 2)

def derive_bhavisyanti() -> State:
    return derive("BU", "lRT", "kartari", 3, 3)

def derive_bhavisyasi() -> State:
    return derive("BU", "lRT", "kartari", 2, 1)

def derive_bhavisyathah() -> State:
    return derive("BU", "lRT", "kartari", 2, 2)

def derive_bhavisyatha() -> State:
    return derive("BU", "lRT", "kartari", 2, 3)

def derive_bhavisyami() -> State:
    return derive("BU", "lRT", "kartari", 1, 1)

def derive_bhavisyavah() -> State:
    return derive("BU", "lRT", "kartari", 1, 2)

def derive_bhavisyamah() -> State:
    return derive("BU", "lRT", "kartari", 1, 3)


# ── laṅ ──────────────────────────────────────────────────────────────────────
def derive_abhavat() -> State:
    return derive("BU", "laG", "kartari", 3, 1)

def derive_abhavataM() -> State:
    return derive("BU", "laG", "kartari", 3, 2)

def derive_abhavan() -> State:
    return derive("BU", "laG", "kartari", 3, 3)

def derive_abhavaH() -> State:
    return derive("BU", "laG", "kartari", 2, 1)

def derive_abhavataM2() -> State:
    return derive("BU", "laG", "kartari", 2, 2)

def derive_abhavata() -> State:
    return derive("BU", "laG", "kartari", 2, 3)

def derive_abhavam() -> State:
    return derive("BU", "laG", "kartari", 1, 1)

def derive_abhavaV() -> State:
    return derive("BU", "laG", "kartari", 1, 2)

def derive_abhavaM() -> State:
    return derive("BU", "laG", "kartari", 1, 3)


# ── liṅ (vidhi) ───────────────────────────────────────────────────────────────
def derive_bhavet() -> State:
    return derive("BU", "liG", "kartari", 3, 1)

def derive_bhavetam() -> State:
    return derive("BU", "liG", "kartari", 3, 2)

def derive_bhaveyuH() -> State:
    return derive("BU", "liG", "kartari", 3, 3)

def derive_bhaveH() -> State:
    return derive("BU", "liG", "kartari", 2, 1)

def derive_bhavetam2() -> State:
    return derive("BU", "liG", "kartari", 2, 2)

def derive_bhaveta() -> State:
    return derive("BU", "liG", "kartari", 2, 3)

def derive_bhaveyam() -> State:
    return derive("BU", "liG", "kartari", 1, 1)

def derive_bhaveva() -> State:
    return derive("BU", "liG", "kartari", 1, 2)

def derive_bhavema() -> State:
    return derive("BU", "liG", "kartari", 1, 3)


# ── āśīr-liṅ ─────────────────────────────────────────────────────────────────
def derive_bhuyat() -> State:
    return derive("BU", "AsIrliG", "kartari", 3, 1)

def derive_bhuyastam() -> State:
    return derive("BU", "AsIrliG", "kartari", 3, 2)

def derive_bhuyasuh() -> State:
    return derive("BU", "AsIrliG", "kartari", 3, 3)

def derive_bhuyah() -> State:
    return derive("BU", "AsIrliG", "kartari", 2, 1)

def derive_bhuyastam2() -> State:
    return derive("BU", "AsIrliG", "kartari", 2, 2)

def derive_bhuyasta() -> State:
    return derive("BU", "AsIrliG", "kartari", 2, 3)

def derive_bhuyasam() -> State:
    return derive("BU", "AsIrliG", "kartari", 1, 1)

def derive_bhuyasva() -> State:
    return derive("BU", "AsIrliG", "kartari", 1, 2)

def derive_bhuyasma() -> State:
    return derive("BU", "AsIrliG", "kartari", 1, 3)


# ── luṅ ──────────────────────────────────────────────────────────────────────
def derive_abhut() -> State:
    return derive("BU", "luG", "kartari", 3, 1)

def derive_abhutam() -> State:
    return derive("BU", "luG", "kartari", 3, 2)

def derive_abhuvan() -> State:
    return derive("BU", "luG", "kartari", 3, 3)

def derive_abhuh() -> State:
    return derive("BU", "luG", "kartari", 2, 1)

def derive_abhutam2() -> State:
    return derive("BU", "luG", "kartari", 2, 2)

def derive_abhuta() -> State:
    return derive("BU", "luG", "kartari", 2, 3)

def derive_abhuvam() -> State:
    return derive("BU", "luG", "kartari", 1, 1)

def derive_abhuva() -> State:
    return derive("BU", "luG", "kartari", 1, 2)

def derive_abhuma() -> State:
    return derive("BU", "luG", "kartari", 1, 3)


# ── lṛṅ ──────────────────────────────────────────────────────────────────────
def derive_abhavisyat() -> State:
    return derive("BU", "lRG", "kartari", 3, 1)

def derive_abhavisyatam() -> State:
    return derive("BU", "lRG", "kartari", 3, 2)

def derive_abhavisyan() -> State:
    return derive("BU", "lRG", "kartari", 3, 3)

def derive_abhavisyah() -> State:
    return derive("BU", "lRG", "kartari", 2, 1)

def derive_abhavisyatam2() -> State:
    return derive("BU", "lRG", "kartari", 2, 2)

def derive_abhavisyata() -> State:
    return derive("BU", "lRG", "kartari", 2, 3)

def derive_abhavisyam() -> State:
    return derive("BU", "lRG", "kartari", 1, 1)

def derive_abhavisyav() -> State:
    return derive("BU", "lRG", "kartari", 1, 2)

def derive_abhavisyam2() -> State:
    return derive("BU", "lRG", "kartari", 1, 3)


# ── Complete paradigm maps (gold for testing) ─────────────────────────────────
BHU_LAT_KARTARI: dict[tuple[int, int], str] = {
    (3, 1): "भवति",  (3, 2): "भवतः",  (3, 3): "भवन्ति",
    (2, 1): "भवसि",  (2, 2): "भवथः",  (2, 3): "भवथ",
    (1, 1): "भवामि", (1, 2): "भवावः", (1, 3): "भवामः",
}

BHU_LRT_KARTARI: dict[tuple[int, int], str] = {
    (3, 1): "भविष्यति",  (3, 2): "भविष्यतः",  (3, 3): "भविष्यन्ति",
    (2, 1): "भविष्यसि",  (2, 2): "भविष्यथः",  (2, 3): "भविष्यथ",
    (1, 1): "भविष्यामि", (1, 2): "भविष्यावः", (1, 3): "भविष्यामः",
}

BHU_LAG_KARTARI: dict[tuple[int, int], str] = {
    (3, 1): "अभवत्",  (3, 2): "अभवताम्", (3, 3): "अभवन्",
    (2, 1): "अभवः",   (2, 2): "अभवतम्",  (2, 3): "अभवत",
    (1, 1): "अभवम्",  (1, 2): "अभवाव",   (1, 3): "अभवाम",
}
