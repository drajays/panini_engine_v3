"""
pipelines/patha_pipeline.py — पाठ-विश्लेषण-प्रणाली
────────────────────────────────────────────────────

Takes Devanāgarī Sanskrit text, tokenizes it into words, and identifies
each word-form by looking it up in a pre-computed form index built from
the engine's subanta derivations.

Architecture (CONSTITUTION Art. 1):
  - Index built by running derive() for every (stem, vibhakti, vacana, linga)
    in PATHA_LEXICON — no gold shortcuts, no bypass rules.
  - Analysis is O(1) dictionary lookup per word-token.
  - Full prakriyā trace: re-run derive() for any matched (stem,v,vac,linga).

v1 scope:
  • Closed-world: recognizes only stems listed in PATHA_LEXICON.
  • No sandhi-viccheda: caller must provide vicchinna (pre-split) forms.
  • No tinanta (verbal) analysis.
  • Ambiguity: multiple stems may share a surface form → all returned.

Lexicon classes supported:
  अकारान्त पुंलिङ्ग    — rāma, deva, yoga, dharma, loka, mārga, arjuna, śiva,
                          nara, kāma, mokṣa, śiṣya, vana (as puṃ)
  अकारान्त नपुंसक     — jñāna, sukha, satya, phala, vana
  इकारान्त पुंलिङ्ग(घि)  — hari, kavi, muni
  उकारान्त पुंलिङ्ग(घि)  — śambhu, guru, bhānu, vāyu
  सर्वनाम             — sarva
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import re
from typing import NamedTuple

import sutras  # noqa: F401 — fills SUTRA_REGISTRY
from pipelines.subanta import derive
from phonology.joiner import slp1_to_devanagari


# ── Vibhakti / vacana / linga display labels ─────────────────────

_VIB_SHORT = {
    1: "प्र", 2: "द्वि", 3: "तृ", 4: "च",
    5: "पं",  6: "ष",    7: "स",  8: "सं",
}
_VIB_LONG = {
    1: "प्रथमा",  2: "द्वितीया", 3: "तृतीया",  4: "चतुर्थी",
    5: "पञ्चमी", 6: "षष्ठी",    7: "सप्तमी",  8: "सम्बोधन",
}
_VAC_SHORT = {1: "एक", 2: "द्वि", 3: "बहु"}
_VAC_LONG  = {1: "एकवचन", 2: "द्विवचन", 3: "बहुवचन"}
_LINGA_SHORT = {"pulliṅga": "पुं", "strīliṅga": "स्त्री", "napuṃsaka": "न"}
_LINGA_LONG  = {"pulliṅga": "पुंलिङ्ग", "strīliṅga": "स्त्रीलिङ्ग", "napuṃsaka": "नपुंसकलिङ्ग"}


def cell_label_short(vibhakti: int, vacana: int, linga: str) -> str:
    return f"{_VIB_SHORT[vibhakti]}.{_VAC_SHORT[vacana]}.{_LINGA_SHORT.get(linga, '?')}"


def cell_label_long(vibhakti: int, vacana: int, linga: str) -> str:
    return (f"{_VIB_LONG[vibhakti]} {_VAC_LONG[vacana]} "
            f"({_LINGA_LONG.get(linga, linga)})")


# ── Lexicon ───────────────────────────────────────────────────────
# Each entry: (stem_slp1, linga, stem_dev, gloss_en, class_short)

class LexEntry(NamedTuple):
    stem_slp1  : str
    linga      : str
    stem_dev   : str   # prātipadika in Devanāgarī (no vibhakti)
    gloss_en   : str
    class_short: str   # e.g. "अकारान्त", "इकारान्त · घि"


PATHA_LEXICON: tuple[LexEntry, ...] = (
    # ── अकारान्त पुंलिङ्ग ──────────────────────────────────────
    LexEntry("rAma",    "pulliṅga",  "राम",   "Rāma",            "अकारान्त"),
    LexEntry("deva",    "pulliṅga",  "देव",   "god, deity",       "अकारान्त"),
    LexEntry("nara",    "pulliṅga",  "नर",    "man, person",      "अकारान्त"),
    LexEntry("yoga",    "pulliṅga",  "योग",   "yoga, union",      "अकारान्त"),
    LexEntry("Darma",   "pulliṅga",  "धर्म",  "dharma, duty",     "अकारान्त"),
    LexEntry("loka",    "pulliṅga",  "लोक",   "world, realm",     "अकारान्त"),
    LexEntry("mArga",   "pulliṅga",  "मार्ग", "path, way",        "अकारान्त"),
    LexEntry("arjuna",  "pulliṅga",  "अर्जुन","Arjuna",           "अकारान्त"),
    LexEntry("Siva",    "pulliṅga",  "शिव",   "Śiva",             "अकारान्त"),
    LexEntry("kAma",    "pulliṅga",  "काम",   "desire, love",     "अकारान्त"),
    LexEntry("mokza",   "pulliṅga",  "मोक्ष", "liberation",       "अकारान्त"),
    LexEntry("Sizya",   "pulliṅga",  "शिष्य", "disciple, student","अकारान्त"),
    LexEntry("kRzRa",   "pulliṅga",  "कृष्ण", "Kṛṣṇa",           "अकारान्त"),
    LexEntry("prakASa", "pulliṅga",  "प्रकाश","light, radiance",  "अकारान्त"),
    # ── अकारान्त नपुंसक ─────────────────────────────────────────
    LexEntry("jYAna",   "napuṃsaka", "ज्ञान", "knowledge",        "अकारान्त न"),
    LexEntry("suKa",    "napuṃsaka", "सुख",   "happiness, joy",   "अकारान्त न"),
    LexEntry("satya",   "napuṃsaka", "सत्य",  "truth",            "अकारान्त न"),
    LexEntry("Pala",    "napuṃsaka", "फल",    "fruit, result",    "अकारान्त न"),
    LexEntry("vana",    "napuṃsaka", "वन",    "forest, grove",    "अकारान्त न"),
    LexEntry("karma",   "napuṃsaka", "कर्म",  "action, karma",    "अकारान्त न"),
    # ── इकारान्त पुंलिङ्ग (घिसंज्ञक) ──────────────────────────
    LexEntry("hari",    "pulliṅga",  "हरि",   "Viṣṇu, Hari",      "इकारान्त · घि"),
    LexEntry("kavi",    "pulliṅga",  "कवि",   "poet",             "इकारान्त · घि"),
    LexEntry("muni",    "pulliṅga",  "मुनि",  "sage, ascetic",    "इकारान्त · घि"),
    # ── उकारान्त पुंलिङ्ग (घिसंज्ञक) ──────────────────────────
    LexEntry("SamBu",   "pulliṅga",  "शम्भु", "Śambhu, Śiva",     "उकारान्त · घि"),
    LexEntry("guru",    "pulliṅga",  "गुरु",  "teacher, guru",    "उकारान्त · घि"),
    LexEntry("BAnu",    "pulliṅga",  "भानु",  "sun, Bhānu",       "उकारान्त · घि"),
    LexEntry("vAyu",    "pulliṅga",  "वायु",  "wind, Vāyu",       "उकारान्त · घि"),
    # ── अकारान्त सर्वनाम ────────────────────────────────────────
    LexEntry("sarva",   "pulliṅga",  "सर्व",  "all, every",       "सर्वनाम"),
)


# ── Form index ────────────────────────────────────────────────────

_FORM_INDEX: dict[str, list[dict]] | None = None


def build_form_index() -> dict[str, list[dict]]:
    """
    Build form_dev → [analysis, …] index by running derive() for every
    (stem, vibhakti, vacana, linga) in PATHA_LEXICON.
    Idempotent; result cached in module-level _FORM_INDEX.
    """
    global _FORM_INDEX
    if _FORM_INDEX is not None:
        return _FORM_INDEX

    index: dict[str, list[dict]] = {}
    for entry in PATHA_LEXICON:
        for v in range(1, 9):
            for vac in range(1, 4):
                try:
                    state = derive(entry.stem_slp1, v, vac, linga=entry.linga)
                    if not state.terms:
                        continue
                    form_dev = slp1_to_devanagari(state.terms[0].varnas)
                    if not form_dev:
                        continue
                    analysis = {
                        "stem_slp1"   : entry.stem_slp1,
                        "stem_dev"    : entry.stem_dev,
                        "linga"       : entry.linga,
                        "vibhakti"    : v,
                        "vacana"      : vac,
                        "gloss_en"    : entry.gloss_en,
                        "class_short" : entry.class_short,
                        "form_slp1"   : state.flat_slp1(),
                        "label_short" : cell_label_short(v, vac, entry.linga),
                        "label_long"  : cell_label_long(v, vac, entry.linga),
                    }
                    index.setdefault(form_dev, []).append(analysis)
                except Exception:
                    pass

    _FORM_INDEX = index
    return index


def get_form_index() -> dict[str, list[dict]]:
    """Return (building on first call) the form index."""
    return build_form_index()


# ── Tokenizer ─────────────────────────────────────────────────────

_PUNCT = re.compile(r"[।॥|!?.,;:\(\)\[\]{}'\"''\n\r\t]+")


def tokenize(text: str) -> list[str]:
    """
    Split Devanāgarī Sanskrit text into word-tokens.
    Replaces punctuation (daṇḍa, double-daṇḍa, etc.) with spaces,
    then splits on whitespace. Preserves anusvāra (ं) and visarga (ः)
    as part of their respective words.
    """
    cleaned = _PUNCT.sub(" ", text)
    return [t for t in cleaned.split() if t]


# ── Analysis ──────────────────────────────────────────────────────

def analyze_word(form_dev: str) -> dict:
    """Look up a single surface form in the index and return its analysis."""
    index     = get_form_index()
    analyses  = index.get(form_dev, [])
    return {
        "form_dev"   : form_dev,
        "analyses"   : analyses,
        "recognized" : len(analyses) > 0,
        "ambiguous"  : len(analyses) > 1,
        "count"      : len(analyses),
    }


def analyze_patha(text: str) -> dict:
    """
    Tokenize Sanskrit text and analyze each token.
    Returns a structured result suitable for JSON serialization.
    """
    tokens    = tokenize(text)
    words     = [analyze_word(t) for t in tokens]
    recognized = sum(1 for w in words if w["recognized"])
    ambiguous  = sum(1 for w in words if w["ambiguous"])
    return {
        "text"         : text,
        "words"        : words,
        "total"        : len(words),
        "recognized"   : recognized,
        "unrecognized" : len(words) - recognized,
        "ambiguous"    : ambiguous,
        "lexicon_size" : len(PATHA_LEXICON),
        "index_forms"  : len(get_form_index()),
    }


# ── Lexicon info ──────────────────────────────────────────────────

def lexicon_info() -> list[dict]:
    """Return lexicon entries as dicts for the web UI."""
    return [
        {
            "stem_slp1"  : e.stem_slp1,
            "stem_dev"   : e.stem_dev,
            "linga"      : e.linga,
            "gloss_en"   : e.gloss_en,
            "class_short": e.class_short,
        }
        for e in PATHA_LEXICON
    ]


__all__ = [
    "PATHA_LEXICON",
    "LexEntry",
    "analyze_patha",
    "analyze_word",
    "build_form_index",
    "cell_label_long",
    "cell_label_short",
    "get_form_index",
    "lexicon_info",
    "tokenize",
]
