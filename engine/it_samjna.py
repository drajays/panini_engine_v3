"""
engine/it_samjna.py — *it-saṃjñā prakaraṇa* (**1.3.2**–**1.3.9**): order, records, predicates.

Pāṇini's procedure on every *upadeśa* (dhātu, pratyaya, ādeśa, āgama) as first
uttered (*ādyoccāraṇa*):

    1.3.2  उपदेशेऽजनुनासिक इत्     anunāsika vowel                 (+ vārttika इर इत्संज्ञा वाच्या)
    1.3.3  हलन्त्यम्                 final hal
    1.3.4  न विभक्तौ तुस्माः          … except tu-varga / s / m ending a vibhakti
    1.3.5  आदिर्ञिटुडवः              initial ñi / ṭu / ḍu of a dhātu
    1.3.6  षः प्रत्ययस्य             initial ṣ of a pratyaya
    1.3.7  चुटू                     initial cu / ṭu of a pratyaya
    1.3.8  लशक्वतद्धिते              initial l / ś / ku of a non-taddhita pratyaya
    1.3.9  तस्य लोपः                lopa of everything marked *it*

The saṃjñā sūtras only tag Varṇas; **1.3.9** deletes them and, through
``record_it_lopa``, leaves a permanent record on the ``Term`` of *which* letter
was *it*, *which sūtra* named it, and the Pāṇinian class name it confers
(*kit*, *ṅit*, *ñit*, *ṇit*, *pit*, *śit*, *ṣit*, *ñīt*, *ṭvit*, *ḍvit*, *irit*,
*udit*, *idit*, *ṛdit*, *ḷdit*, *odit* …).  Later rules (1.1.5 *kṅiti ca*, 7.2.115
*aco ñṇiti*, 7.3.84 vs 1.2.4 *pit*/*apit*, 7.1.58 *idito num dhātoḥ*, 3.1.57
*irito vā*, 3.2.187 *ñītaḥ ktaḥ*, 3.3.88 *ḍvitaḥ ktriḥ*, 3.3.89 *ṭvito 'thuc*, 4.1.41
*ṣidgaurādibhyaś ca* …) read those names via ``has_it`` / the ``it:<name>`` tag.

The ordered run is scheduled by ``pipelines.it_prakarana.run_it_prakarana``.
This module never names a sūtra itself: each saṃjñā sūtra registers its own
candidate tag via ``register_candidate_tag`` (so the record's ``sutra`` field is
the registering ``SutraRecord.sutra_id``).
"""
from __future__ import annotations

from typing import Any, Dict, FrozenSet, Iterable, List, Optional, Tuple

from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from phonology.varna import AC_DEV, HAL_DEV

# Varṇa candidate tags, keyed by the kind of it they confer.
TAG_ANUNASIKA = "it_candidate_anunasika"
TAG_IRIT = "it_candidate_irit"
TAG_HALANTYAM = "it_candidate_halantyam"
TAG_NIT_TU_DU = "it_candidate_nit_tu_du"
TAG_SHA = "it_candidate_sha_pratyaya"
TAG_CUTU = "it_candidate_cutu"
TAG_LASAKU = "it_candidate_lasaku"
TAG_OVARGA = "it_candidate_ovarga_anubandha"

# Unit its (इर्, ञि/टु/डु) outrank a letter-level tag on the same Varṇa.
_UNIT_TAGS: Tuple[str, ...] = (TAG_IRIT, TAG_NIT_TU_DU)
_LETTER_TAGS: Tuple[str, ...] = (
    TAG_ANUNASIKA, TAG_HALANTYAM, TAG_SHA, TAG_CUTU, TAG_LASAKU, TAG_OVARGA,
)

# Candidate tag → sūtra id, filled by the saṃjñā sūtras at import time.
CANDIDATE_TAG_SUTRA: Dict[str, str] = {}


def register_candidate_tag(tag: str, sutra_id: str) -> None:
    CANDIDATE_TAG_SUTRA[tag] = sutra_id

TAG_PREFIX = "it:"
TAG_PREFIX_STHANIVAT = "sthanivat_it:"
META_RECORDS = "it_records"
META_NAMES = "it_samjna_names"
META_LOPA_DONE = "it_lopa_done"
META_IT_LOPA_LOG = "it_lopa_log"      # state.meta: every record of the derivation, in order

# 3.2.187 ñītaḥ, 3.3.89 ṭvitaḥ, 3.3.88 ḍvitaḥ — the ādi cluster names (1.3.5).
_ADI_CLUSTER_NAME = {"Yi": "YIt", "wu": "wvit", "qu": "qvit"}
_CLUSTER_NAME_DEV = {
    "YIt": "ञीत्", "wvit": "ट्वित्", "qvit": "ड्वित्", "irit": "इरित्",
}

_PRATYAYA_TAGS: FrozenSet[str] = frozenset({
    "pratyaya", "sup", "tin", "krt", "taddhita", "vikarana",
    "stri_pratyaya", "tin_adesha_3_4_78",
})


# ─────────────────────────────────────────────────────────────────────────────
# Term-class predicates (the "which upadeśa" question of the flow-chart)
# ─────────────────────────────────────────────────────────────────────────────

def is_agama(t: Any) -> bool:
    return t.kind == "agama" or any(
        tag == "agama" or tag.endswith("_agama") for tag in t.tags
    )


def is_dhatu_upadesha(t: Any) -> bool:
    """Dhātu as taught in the dhātupāṭha (scope of **1.3.5**)."""
    if "upadesha" not in t.tags or is_agama(t):
        return False
    if "dhatu" in t.tags:
        return True
    return t.kind == "prakriti" and "prātipadika" not in t.tags and not (
        t.tags & _PRATYAYA_TAGS
    )


def is_pratyaya_upadesha(t: Any) -> bool:
    """Pratyaya (or pratyaya-ādeśa) as taught (scope of **1.3.6**–**1.3.8**)."""
    if "upadesha" not in t.tags or "dhatu" in t.tags:
        return False
    if t.kind in ("upasarga", "nipata") or "upasarga" in t.tags or is_agama(t):
        return False
    if LUK_LOPA_GHOST_TAG in t.tags:
        return False
    return t.kind == "pratyaya" or bool(t.tags & _PRATYAYA_TAGS)


def it_lopa_already_done(t: Any) -> bool:
    """
    True once **1.3.9** has run on this exact upadeśa and the tape is unchanged
    since: the residue (गम् of गमॢँ, स् of सिच्) is no longer *aupadeśika*, so
    **1.3.2**–**1.3.8** must not name its letters *it* a second time.
    """
    done = t.meta.get(META_LOPA_DONE)
    if not done:
        return False
    up, residue = done
    return (
        up == (t.meta.get("upadesha_slp1") or "").strip()
        # an āgama grown into the term (7.2.35's iṭ) is not part of the upadeśa residue
        and residue == "".join(v.slp1 for v in t.varnas if "it_agama" not in v.tags)
    )


# ─────────────────────────────────────────────────────────────────────────────
# Names
# ─────────────────────────────────────────────────────────────────────────────

def it_name(letters: str, kind: Optional[str]) -> Optional[str]:
    """
    Pāṇinian class name for an it-letter (SLP1) given its candidate tag:
    ``k`` → ``kit``, ``u`` (anunāsika) → ``udit``, ``Yi`` (1.3.5) → ``YIt``.
    """
    if kind == TAG_IRIT:
        return "irit"
    if kind == TAG_NIT_TU_DU:
        return _ADI_CLUSTER_NAME.get(letters)
    if len(letters) != 1:
        return None
    if letters in HAL_DEV:
        return f"{letters}it"
    if letters in AC_DEV and kind in (TAG_ANUNASIKA, TAG_OVARGA):
        return f"{letters}dit"
    return None


def it_name_dev(name: str) -> str:
    if name in _CLUSTER_NAME_DEV:
        return _CLUSTER_NAME_DEV[name]
    if name.endswith("dit") and name[:-3] in AC_DEV:
        return AC_DEV[name[:-3]] + "दित्"
    if name.endswith("it") and name[:-2] in HAL_DEV:
        return HAL_DEV[name[:-2]].rstrip("्") + "ित्"
    return name


def _letters_dev(varnas: List[Any]) -> str:
    from phonology.joiner import slp1_to_devanagari

    return slp1_to_devanagari(varnas)


# ─────────────────────────────────────────────────────────────────────────────
# Records (written by 1.3.9)
# ─────────────────────────────────────────────────────────────────────────────

def _kind_of(tags: Iterable[str]) -> Optional[str]:
    tags = set(tags)
    for tag in _UNIT_TAGS + _LETTER_TAGS:
        if tag in tags:
            return tag
    return None


def record_it_lopa(term: Any, removed: List[Tuple[int, Any]], n_before: int) -> List[dict]:
    """
    Build the it-records for one ``Term`` from the Varṇas **1.3.9** deletes.

    ``removed`` — ``(index_in_upadesha, varna)`` pairs, in tape order.
    The ñi/ṭu/ḍu unit (1.3.5) and the इर् unit (vārttika) are single *it*s.
    """
    upadesha = (term.meta.get("upadesha_slp1") or "").strip()
    out: List[dict] = []
    k = 0
    while k < len(removed):
        idx, v = removed[k]
        kind = _kind_of(v.tags)
        letters = v.slp1
        unit = [v]
        span_end = idx
        if kind in _UNIT_TAGS and k + 1 < len(removed):
            nidx, nv = removed[k + 1]
            if nidx == idx + 1 and _kind_of(nv.tags) == kind:
                letters += nv.slp1
                unit.append(nv)
                span_end = nidx
                k += 1
        if idx == 0:
            position = "adi"
        elif span_end == n_before - 1:
            position = "antya"
        else:
            position = "madhya"
        name = it_name(letters, kind)
        out.append({
            "letters": letters,
            "letters_dev": _letters_dev(unit),
            "sutra": CANDIDATE_TAG_SUTRA.get(kind) if kind else None,
            "position": position,
            "name": name,
            "name_dev": it_name_dev(name) if name else None,
            "upadesha": upadesha,
        })
        k += 1
    if out:
        prev = term.meta.get(META_RECORDS)
        term.meta[META_RECORDS] = (list(prev) if prev else []) + out
        names = set(term.meta.get(META_NAMES) or ())
        for r in out:
            if r["name"]:
                names.add(r["name"])
                term.tags.add(TAG_PREFIX + r["name"])
        term.meta[META_NAMES] = frozenset(names)
    return out


def inherit_it_records(adesha: Any, records: Iterable[dict], *, sutra_id: str,
                       drop: FrozenSet[str] = frozenset()) -> None:
    """**1.1.56** — copy the sthānin's it-records onto the ādeśa, kept distinct from its own."""
    inherited = [dict(r, sthanivat_from=sutra_id) for r in records if r.get("name") not in drop]
    if not inherited:
        return
    prev = adesha.meta.get(META_RECORDS)
    adesha.meta[META_RECORDS] = (list(prev) if prev else []) + inherited
    for r in inherited:
        if r["name"]:
            adesha.tags.add(TAG_PREFIX_STHANIVAT + r["name"])


def it_records(term: Any) -> List[dict]:
    return list(term.meta.get(META_RECORDS) or ())


def it_names(term: Any, *, include_sthanivat: bool = True) -> FrozenSet[str]:
    out = set()
    for r in it_records(term):
        if r.get("name") and (include_sthanivat or "sthanivat_from" not in r):
            out.add(r["name"])
    return frozenset(out)


def has_it(term: Any, name: str, *, include_sthanivat: bool = True) -> bool:
    """``has_it(t, "kit")`` — the Term's upadeśa had a k-it (or inherits one, 1.1.56)."""
    return name in it_names(term, include_sthanivat=include_sthanivat)


__all__ = [
    "CANDIDATE_TAG_SUTRA",
    "register_candidate_tag",
    "TAG_ANUNASIKA",
    "TAG_IRIT",
    "TAG_HALANTYAM",
    "TAG_NIT_TU_DU",
    "TAG_SHA",
    "TAG_CUTU",
    "TAG_LASAKU",
    "TAG_OVARGA",
    "TAG_PREFIX",
    "TAG_PREFIX_STHANIVAT",
    "META_RECORDS",
    "META_NAMES",
    "META_LOPA_DONE",
    "META_IT_LOPA_LOG",
    "is_agama",
    "is_dhatu_upadesha",
    "is_pratyaya_upadesha",
    "it_lopa_already_done",
    "it_name",
    "it_name_dev",
    "record_it_lopa",
    "inherit_it_records",
    "it_records",
    "it_names",
    "has_it",
]
