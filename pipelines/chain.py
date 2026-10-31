"""pipelines/chain.py — the Aṣṭādhyāyī cycle as composable stages (prātipadika ↔ dhātu, then sup).

A stage takes the previous stage's result (a :class:`Stem`: the SLP1 stem, its origin record, its gender and its side-by-side choices) and
returns the next; each stage is the existing loop-driven entry point (krdanta / taddhita_loop), so no stage knows a form.
    krt(dhatu_ref, krt=…, kala=…) → taddhita(stem, taddhitArtha=…) → … → sup(stem, vibhakti, vacana)
Stages not yet loop-driven (strī, sanādi, nāmadhātu) are listed in docs/V4_CYCLE.md and are NOT faked here."""
from __future__ import annotations

from dataclasses import dataclass, field

from engine.state import State


@dataclass(frozen=True)
class Stem:
    slp1: str
    tags: frozenset = field(default_factory=frozenset)      # the vyutpatti record (engine/origin.py) the next stage and the sup read
    multi: tuple = ()                                      # vikalpa_multi: the side-by-side choices, kept visible to explore()
    linga: str | None = None


def krt(dhatu_ref: str, *, upapada: tuple[str, str] | None = None, **vivaksha: str) -> Stem:
    from pipelines.krdanta import derive_krdanta_stem
    s, tags, multi = derive_krdanta_stem(dhatu_ref, upapada=upapada, **vivaksha)
    return Stem(s, frozenset(tags), tuple(sorted(multi.items())))


def taddhita(stem: Stem, **vivaksha: str) -> Stem:
    from pipelines.taddhita_loop import derive_taddhita_stem
    s, tags, multi = derive_taddhita_stem(stem.slp1, set(stem.tags), stem.linga, **vivaksha)
    return Stem(s, frozenset(tags), tuple(sorted({**dict(stem.multi), **multi}.items())))


def sup(stem: Stem, vibhakti: int, vacana: int, linga: str = "pulliṅga") -> State:
    from pipelines.subanta import build_initial_state, run_subanta_sup_attach_and_finish_scanner
    linga = next((x.split(":", 1)[1] for x in stem.tags if x.startswith("yuktavad_linga:")), linga)
    s = build_initial_state(stem.slp1, vibhakti, vacana, linga, derived_pratipadika=True)
    s.terms[0].tags |= set(stem.tags)
    if stem.multi:
        s.meta["vikalpa_multi"] = dict(stem.multi)
    return run_subanta_sup_attach_and_finish_scanner(s)
