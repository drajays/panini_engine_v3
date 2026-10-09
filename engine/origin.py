"""
engine/origin.py — what a derived stem remembers of its making (AMENDMENT 22).

A stem built from a Lexicon entry carries, as Term tags, a *record* of its vyutpatti:

    origin_pratyaya:<upadeśa>   the pratyaya that ends the stem (matu~p, tfc, kvip …)
    origin_it:<letter>          an it-letter that the real it-prakaraṇa (1.3.2–1.3.9) took from that pratyaya
    origin_dhatu:<upadeśa>      a dhātu the stem was made from

These are facts about the tape's history, never saṃjñā. The saṃjñās are *derived* here, each by the definition its sūtra gives:

* **ugit** (7.1.70 उगिदचां …): "uk" is the pratyāhāra u-ṛ-ḷ; an aṅga is ugit when a pratyaya that is its avayava has one of
  them as it-letter. Nyāsa/Padamañjarī on 7.1.70: *"avayavāvayavenāpi samudāyasya sambandho bhavatyeva … pratyayasyāvayavo ya uk
  itsaṃjñakas tenāṅgasyāpi sambandho'styeva; aṅgam apy ugid eva"* — the aṅga is ugit because its pratyaya is. Patañjali (adhātoḥ):
  the stem keeps this even when it has been a dhātu before (*gomatyati* … *gomān*), so the record is of the stem's own last pratyaya.
* **tṛc / tṛn-anta** (6.4.11, 6.1.66, 7.3.110, 1.1.43 …): the aṅga ends in the pratyaya tṛc or tṛn (tadanta, 1.1.72).
* **dhātu in the stem** (6.4.8, 6.4.12, 6.4.13 "han"): a component of the vyutpatti is that dhātu.
"""
from __future__ import annotations

from typing import Iterable

PRATYAYA = "origin_pratyaya:"
IT = "origin_it:"
DHATU = "origin_dhatu:"
ORIGIN_PREFIXES = (PRATYAYA, IT, DHATU)

_UK = frozenset("uUfFxX")          # u, ṛ, ḷ (the uk pratyāhāra, short and long)
_TRC = frozenset({"tfc", "tfn"})


def _tags(term) -> Iterable[str]:
    return term.tags if hasattr(term, "tags") else term


def origin_tags_of(pratyaya_upadesha: str | None, it_letters: Iterable[str], dhatus: Iterable[str]) -> set[str]:
    out: set[str] = set()
    if pratyaya_upadesha:
        out.add(PRATYAYA + pratyaya_upadesha)
    out |= {IT + str(c) for c in it_letters}
    out |= {DHATU + d for d in dhatus}
    return out


def last_pratyaya(term) -> str | None:
    return next((t[len(PRATYAYA):] for t in _tags(term) if t.startswith(PRATYAYA)), None)


def is_ugit(term) -> bool:
    """7.1.70: the aṅga's own final pratyaya has u / ṛ / ḷ as its it-letter."""
    return any(t.startswith(IT) and t[len(IT):] in _UK for t in _tags(term))


def is_trc_anta(term) -> bool:
    """6.4.11 etc.: the aṅga ends in tṛc / tṛn."""
    return last_pratyaya(term) in _TRC


def has_dhatu(term, upadesha_prefix: str) -> bool:
    """The stem was made from the dhātu whose upadeśa starts with ``upadesha_prefix`` (han → 'han')."""
    return any(t.startswith(DHATU) and t[len(DHATU):].startswith(upadesha_prefix) for t in _tags(term))


def record_from_terms(terms) -> set[str]:
    """The vyutpatti record of a stem that is about to be merged from these live Terms.

    Read from the Terms themselves after the real it-prakaraṇa: the *last* pratyaya Term (even if its varṇas are gone —
    kvip after 6.1.67 — it is still what ended the stem, 1.1.62) gives ``origin_pratyaya`` and its ``it_markers`` ; every dhātu
    Term gives ``origin_dhatu``. Nothing here is stamped from outside."""
    terms = list(terms)
    last = terms[-1] if terms and terms[-1].kind == "pratyaya" else None
    dhatus = [(t.meta.get("upadesha_slp1") or "") for t in terms if "dhatu" in t.tags and "abhyasa" not in t.tags]
    return origin_tags_of(last.meta.get("upadesha_slp1") if last is not None else None,
                          sorted(last.meta.get("it_markers", ())) if last is not None else [], dhatus)
