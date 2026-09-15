"""
engine/sthanivat.py — **1.1.56** *sthānivadādeśo 'nalvidhau* (engine policy).

Eight *anal-āśrita* *guṇa-dharma* types extend from the *sthānin* to its *ādeśa*
when ``state.paribhasha_gates['sthanivadbhava']`` is True (set by **1.1.56**).

**Al-āśrita** properties (``halantatva``, ``vantatva``, ``visargantatva``,
``yanaditva``) do **not** extend at an *al-vidhi* ādeśa locus, nor when the
pedagogical blockers below apply (same-site / after / before / nimitta-elsewhere).

**It-saṃjñā** (*kit*, *ñit*, *ṇit*, *pit*, *apit*) **always** extends to the
ādeśa (even when *al*-blockers apply). **3.4.87** *serhyapicc* teaches *apit*
(not *pit*) on *hi* from *sip*.

Downstream ``cond()`` reads inherited *tags* / ``meta`` on the *ādeśa* *Term* — not
the pre-substitution surface (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, FrozenSet, Iterable

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1
from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import is_tin_adesha

# ── Eight guṇa-dharma keys (pedagogy + meta trace) ───────────────────────
DHATUTVA = "dhatutva"
ANGATVA = "angatva"
KRT_PRATYAYATVA = "krt_pratyayatva"
TADDHITA_PRATYAYATVA = "taddhita_pratyayatva"
AVYAYATVA = "avyayatva"
SUP_PRATYAYATVA = "sup_pratyayatva"
TING_PRATYAYATVA = "ting_pratyayatva"
PADATVA = "padatva"

ALL_ANAL_ASHRITA_GUNADHARMAS: frozenset[str] = frozenset({
    DHATUTVA,
    ANGATVA,
    KRT_PRATYAYATVA,
    TADDHITA_PRATYAYATVA,
    AVYAYATVA,
    SUP_PRATYAYATVA,
    TING_PRATYAYATVA,
    PADATVA,
})

_KTVATOSUN_KASUN = frozenset({"ktvA", "tosun", "kasun", "tumun", "lyap"})
_META_STHANIN_UPADESHA = "sthanin_upadesha_slp1"
_META_STHANIVAT_FROM = "sthanivat_from"
_META_GUNADHARMAS = "sthanivat_gunadharmas"
_META_STHANIVAT_BLOCK = "sthanivat_block"

# Pedagogical block reasons (al-āśrita scope — no स्थानिवद्भाव on ādeśa).
BLOCK_AL_SAME_SITE = "al_same_site"
BLOCK_AL_AFTER_STHANIN = "al_after_sthanin"
BLOCK_AL_BEFORE_STHANIN = "al_before_sthanin"
BLOCK_NIMITTA_ELSEWHERE = "nimitta_elsewhere"

# Al-āśrita *guṇa-dharma* keys (phonemic / locus — not the eight anal types).
HALANTATVA = "halantatva"
VANTATVA = "vantatva"
VISARGANTATVA = "visargantatva"
YANADITVA = "yanaditva"

ALL_AL_ASHRITA_GUNADHARMAS: frozenset[str] = frozenset({
    HALANTATVA,
    VANTATVA,
    VISARGANTATVA,
    YANADITVA,
})

# It-saṃjñā keys (always extend to ādeśa per स्थानिवद्भाव).
KIT_SAMJNA = "kit_samjna"
NIT_SAMJNA = "nit_samjna"
ANIT_SAMJNA = "anit_samjna"
PIT_SAMJNA = "pit_samjna"
APIT_SAMJNA = "apit_samjna"

ALL_IT_SAMJNAS: frozenset[str] = frozenset({
    KIT_SAMJNA,
    NIT_SAMJNA,
    ANIT_SAMJNA,
    PIT_SAMJNA,
    APIT_SAMJNA,
})

_MARKER_TO_IT_SAMJNA: dict[str, str] = {
    "k": KIT_SAMJNA,
    "K": KIT_SAMJNA,
    "Y": NIT_SAMJNA,
    "N": NIT_SAMJNA,
    "R": NIT_SAMJNA,
    "p": PIT_SAMJNA,
    "P": PIT_SAMJNA,
}


def sthanivat_enabled(state: State) -> bool:
    return state.paribhasha_gates.get("sthanivadbhava") is True


def al_gunadharmas_of_term(term: Term) -> frozenset[str]:
    """Infer *al-āśrita* locus properties of a *sthānin* (for blocker logic)."""
    out: set[str] = set()
    if not term.varnas:
        return frozenset()
    final = term.varnas[-1].slp1
    if final in {"k", "K", "g", "G", "N", "c", "C", "j", "J", "Y", "w", "W", "q", "Q",
                 "R", "t", "T", "d", "D", "n", "p", "P", "b", "B", "m", "y", "v", "r", "l",
                 "S", "z", "s", "h"}:
        out.add(HALANTATVA)
    if final == "v":
        out.add(VANTATVA)
    if final == "H":
        out.add(VISARGANTATVA)
    if final in {"y", "v", "r", "l"} or term.meta.get("yan_aditva"):
        out.add(YANADITVA)
    return frozenset(out)


def mark_sthanivat_block(term: Term, reason: str) -> None:
    term.meta[_META_STHANIVAT_BLOCK] = reason


def it_samjnas_from_markers(
    markers: Iterable[str],
    *,
    is_apit: bool = False,
) -> frozenset[str]:
    """Map *it* letters (after **1.3.9** lopa) to it-saṃjñā keys."""
    out: set[str] = set()
    for m in markers:
        key = _MARKER_TO_IT_SAMJNA.get(m)
        if key:
            out.add(key)
    if is_apit:
        out.discard(PIT_SAMJNA)
        out.add(APIT_SAMJNA)
    return frozenset(out)


def it_samjnas_of_term(term: Term) -> frozenset[str]:
    """Infer it-saṃjñā on a *sthānin* or *ādeśa* *Term*."""
    explicit = term.meta.get("it_samjnas")
    if isinstance(explicit, (set, frozenset)):
        return frozenset(explicit)
    markers = term.meta.get("it_markers")
    if not isinstance(markers, set):
        markers = set()
    is_apit = term.meta.get("is_apit") is True
    if "kngiti" in term.tags:
        return frozenset({KIT_SAMJNA}) | it_samjnas_from_markers(markers, is_apit=is_apit)
    return it_samjnas_from_markers(markers, is_apit=is_apit)


def apply_it_samjna_sthanivat(
    adesha: Term,
    snap: SthaninSnapshot,
    *,
    sutra_id: str,
) -> None:
    """Copy *it-saṃjñā* from *sthānin* onto *ādeśa* (always, unlike *al*-blockers)."""
    markers = snap.meta.get("it_markers")
    if not isinstance(markers, set):
        markers = set()
    is_apit = snap.meta.get("is_apit") is True
    samjnas = it_samjnas_from_markers(markers, is_apit=is_apit)
    if not samjnas and "kngiti" not in snap.tags:
        return
    adesha.meta.setdefault("sthanin_upadesha_slp1", snap.meta.get("upadesha_slp1"))
    adesha.meta["sthanivat_it_from"] = sutra_id
    if markers:
        prev = adesha.meta.get("it_markers")
        if isinstance(prev, set):
            prev.update(markers)
        else:
            adesha.meta["it_markers"] = set(markers)
    adesha.meta["it_samjnas"] = samjnas
    if KIT_SAMJNA in samjnas:
        adesha.tags.add("kngiti")
    if NIT_SAMJNA in samjnas:
        adesha.tags.update({"Yit", "svaritaYit"})
    if APIT_SAMJNA in samjnas:
        adesha.meta["is_apit"] = True
        adesha.meta.pop("pit", None)
    elif PIT_SAMJNA in samjnas:
        adesha.meta["pit"] = True


def term_has_it_samjna(term: Term, key: str) -> bool:
    return key in it_samjnas_of_term(term)


def term_is_apit(term: Term) -> bool:
    return APIT_SAMJNA in it_samjnas_of_term(term) or term.meta.get("is_apit") is True


def sthanivat_blocked(term: Term, *reasons: str) -> bool:
    blk = term.meta.get(_META_STHANIVAT_BLOCK)
    if blk is None:
        return False
    if not reasons:
        return True
    return blk in reasons


def gunadharmas_of_term(term: Term) -> frozenset[str]:
    """Classify which *anal-āśrita* properties the *sthānin* carries."""
    out: set[str] = set()
    tags = term.tags
    up = (term.meta.get("upadesha_slp1") or "").strip()
    orig = (term.meta.get("upadesha_slp1_original") or "").strip()

    if "dhatu" in tags:
        out.add(DHATUTVA)
    if "anga" in tags:
        out.add(ANGATVA)
    if "krt" in tags or up in _KTVATOSUN_KASUN or orig in _KTVATOSUN_KASUN:
        out.add(KRT_PRATYAYATVA)
    if "taddhita" in tags or up in {"Tak", "ik", "ika"} or orig in {"Tak", "ik", "ika"}:
        out.add(TADDHITA_PRATYAYATVA)
    if "avyaya" in tags or up in _KTVATOSUN_KASUN or orig in _KTVATOSUN_KASUN:
        out.add(AVYAYATVA)
    if "sup" in tags:
        out.add(SUP_PRATYAYATVA)
    if (
        "tin" in tags
        or "tin_adesha_3_4_78" in tags
        or is_tin_adesha(up)
        or is_sarvadhatuka_upadesha_slp1(up)
    ):
        out.add(TING_PRATYAYATVA)
    if "pada" in tags or term.meta.get("subanta_pada"):
        out.add(PADATVA)
    return frozenset(out)


@dataclass
class SthaninSnapshot:
    kind: str
    tags: frozenset[str]
    meta: dict[str, Any]
    gunadharmas: frozenset[str] = field(default_factory=frozenset)


def snapshot_sthanin(term: Term, *, gunadharmas: Iterable[str] | None = None) -> SthaninSnapshot:
    gd = frozenset(gunadharmas) if gunadharmas is not None else gunadharmas_of_term(term)
    keep_meta = {
        k: term.meta[k]
        for k in (
            "upadesha_slp1",
            "upadesha_slp1_original",
            "gana",
            "dhatu_it",
            "it_markers",
            "is_apit",
            "pit",
            "it_samjnas",
        )
        if k in term.meta
    }
    return SthaninSnapshot(
        kind=term.kind,
        tags=frozenset(term.tags),
        meta=keep_meta,
        gunadharmas=gd,
    )


def apply_sthanivat_bhava(
    adesha: Term,
    snap: SthaninSnapshot,
    *,
    sutra_id: str,
    block: str | None = None,
) -> None:
    """Copy inherited *anal-āśrita* *guṇa-dharma* onto *ādeśa* (in-place)."""
    if block:
        mark_sthanivat_block(adesha, block)
        return
    if not snap.gunadharmas:
        return
    adesha.meta[_META_STHANIN_UPADESHA] = snap.meta.get("upadesha_slp1")
    adesha.meta[_META_STHANIVAT_FROM] = sutra_id
    adesha.meta[_META_GUNADHARMAS] = snap.gunadharmas

    if DHATUTVA in snap.gunadharmas:
        adesha.tags.add("dhatu")
        if "gana" in snap.meta:
            adesha.meta["gana"] = snap.meta["gana"]
        if "dhatu_it" in snap.meta:
            adesha.meta["dhatu_it"] = snap.meta["dhatu_it"]
    if ANGATVA in snap.gunadharmas:
        adesha.tags.add("anga")
    if KRT_PRATYAYATVA in snap.gunadharmas:
        adesha.tags.update({"krt", "pratyaya"})
    if TADDHITA_PRATYAYATVA in snap.gunadharmas:
        adesha.tags.update({"taddhita", "pratyaya"})
    if AVYAYATVA in snap.gunadharmas:
        adesha.tags.add("avyaya")
    if SUP_PRATYAYATVA in snap.gunadharmas:
        adesha.tags.update({"sup", "pratyaya"})
    if TING_PRATYAYATVA in snap.gunadharmas:
        adesha.tags.update({"tin", "pratyaya"})
        if snap.meta.get("upadesha_slp1") and is_sarvadhatuka_upadesha_slp1(
            snap.meta["upadesha_slp1"]
        ):
            adesha.tags.add("sarvadhatuka_3_4_113")
    if PADATVA in snap.gunadharmas:
        adesha.tags.add("pada")


def adesha_substitute_varnas(
    term: Term,
    new_slp1: str,
    state: State,
    *,
    sutra_id: str,
    gunadharmas: Iterable[str] | None = None,
    preserve_upadesha_original: bool = True,
    sthanivat_block: str | None = None,
    sthanin_term: Term | None = None,
) -> None:
    """
    *Al-vidhi* replacement of ``term``'s tape, then **1.1.56** inheritance.

    ``sthanivat_block`` — when set (``BLOCK_AL_*`` / ``BLOCK_NIMITTA_*``), records
    why *al-āśrita* properties were **not** extended (pedagogical exceptions).

    Call only from a sūtra ``act()`` (SIG / Art. 11).
    """
    sthanin = sthanin_term if sthanin_term is not None else term
    snap = snapshot_sthanin(sthanin, gunadharmas=gunadharmas)
    if preserve_upadesha_original and "upadesha_slp1" in term.meta:
        term.meta.setdefault(
            "upadesha_slp1_original",
            term.meta["upadesha_slp1"],
        )
    term.varnas = list(parse_slp1_upadesha_sequence(new_slp1))
    term.meta["upadesha_slp1"] = new_slp1
    if sthanivat_enabled(state):
        apply_sthanivat_bhava(
            term,
            snap,
            sutra_id=sutra_id,
            block=sthanivat_block,
        )
        apply_it_samjna_sthanivat(term, snap, sutra_id=sutra_id)


def term_has_gunadharma(term: Term, key: str) -> bool:
    gd = term.meta.get(_META_GUNADHARMAS)
    if isinstance(gd, (set, frozenset)) and key in gd:
        return True
    if key == DHATUTVA and "dhatu" in term.tags:
        return True
    if key == ANGATVA and "anga" in term.tags:
        return True
    if key == KRT_PRATYAYATVA and "krt" in term.tags:
        return True
    if key == TADDHITA_PRATYAYATVA and "taddhita" in term.tags:
        return True
    if key == AVYAYATVA and "avyaya" in term.tags:
        return True
    if key == SUP_PRATYAYATVA and "sup" in term.tags:
        return True
    if key == TING_PRATYAYATVA and ("tin" in term.tags or "tin_adesha_3_4_78" in term.tags):
        return True
    if key == PADATVA and "pada" in term.tags:
        return True
    return False


def angas_halantatva_blocked(anga: Term) -> bool:
    """True when **6.1.68** must not treat the *aṅga* as *hal*-final (7.1.85 ā-ādeśa)."""
    return sthanivat_blocked(anga, BLOCK_AL_AFTER_STHANIN) or anga.meta.get(
        "7_1_85_a_adesha"
    ) is True


def term_lacks_yan_aditva_for_sandhi(term: Term) -> bool:
    """True when **6.1.114** / **8.3.17** must not treat this as *y*-initial."""
    return sthanivat_blocked(term, BLOCK_AL_BEFORE_STHANIN) or term.meta.get(
        "no_yan_aditva_inheritance"
    ) is True
