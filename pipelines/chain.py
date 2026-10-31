"""pipelines/chain.py — the Aṣṭādhyāyī cycle as composable stages (prātipadika ↔ dhātu, then sup).

A stage takes the previous stage's result (a :class:`Stem`: the SLP1 stem, its origin record, its gender and its side-by-side choices; or a
:class:`Dhatu`: the live Terms of a derived dhātu) and returns the next; each stage is the existing loop-driven entry point, so no stage knows a form.
    strI(stem) → nama_dhatu(stem, …) → sanadi(dhatu, …) → krt(dhatu, …) → taddhita(stem, taddhitArtha=…) → … → sup(stem, vibhakti, vacana)
    and from a dhātu: tinanta(dhatu, lakara, purusha, vacana)
Every result carries ``trace``: (stage, sūtras the loop fired in it), cumulative, so a test can see which sūtra did which arrow."""
from __future__ import annotations

from dataclasses import dataclass, field

from engine.state import State


@dataclass(frozen=True)
class Stem:
    slp1: str
    tags: frozenset = field(default_factory=frozenset)      # the vyutpatti record (engine/origin.py) the next stage and the sup read
    multi: tuple = ()                                      # vikalpa_multi: the side-by-side choices, kept visible to explore()
    linga: str | None = None
    trace: tuple = ()


@dataclass(frozen=True)
class Dhatu:
    """A derived dhātu (kyac-anta, ṇic-anta …): the live Terms the loop left, as a krt or tiṅ stage takes them. A Term list, not a string: 6.4.51 and 7.4.1 read its meta."""
    slp1: str
    terms: tuple = ()
    multi: tuple = ()
    trace: tuple = ()


def _fired(stage: str) -> tuple:
    """(stage, the sūtras the last loop run applied)."""
    from tools import autonomy_report
    run = autonomy_report.LAST_RUN
    return (stage, tuple(x[0] for x in run.steps) if run is not None else ())


def strI(stem: Stem, **vivaksha: str) -> Stem:
    """prātipadika → prātipadika (4.1.3 striyām, 4.1.4 ṭāp …), vivakṣā linga=strI."""
    from pipelines.cycle_loop import derive_stri_stem
    s, tags = derive_stri_stem(stem.slp1, set(stem.tags), **vivaksha)
    return Stem(s, frozenset(tags), stem.multi, "strīliṅga", stem.trace + (_fired("strI"),))


def nama_dhatu(stem: Stem, vibhakti: int = 2, vacana: int = 1, **vivaksha: str) -> Dhatu:
    """prātipadika → dhātu (3.1.8 kyac, vivakṣā icCA). ``vibhakti``/``vacana``: the sup the stem has in the speaker's sentence (putram: 2-1), which kyac follows and 2.4.71 lugs."""
    from pipelines.cycle_loop import derive_nama_dhatu
    terms = derive_nama_dhatu(stem.slp1, set(stem.tags) | ({stem.linga} if stem.linga else set()), vibhakti, vacana, icCA="icCA", **vivaksha)
    return Dhatu("".join(v.slp1 for t in terms for v in t.varnas), tuple(terms), stem.multi, stem.trace + (_fired("nama_dhatu"),))


def sanadi(dhatu: Dhatu, **vivaksha: str) -> Dhatu:
    """dhātu → dhātu: ṇic (3.1.26) when the speaker intends a prompting agent (``hetumat="hetumat"``)."""
    from pipelines.cycle_loop import derive_sanadi
    terms = derive_sanadi(list(dhatu.terms), **vivaksha)
    return Dhatu("".join(v.slp1 for t in terms for v in t.varnas), tuple(terms), dhatu.multi, dhatu.trace + (_fired("sanadi"),))


def krt(dhatu_ref: "str | Dhatu", *, upapada: tuple[str, str] | None = None, **vivaksha: str) -> Stem:
    from pipelines.krdanta import derive_krdanta_stem
    s, tags, multi = derive_krdanta_stem(dhatu_ref, upapada=upapada, **vivaksha)
    old = dict(getattr(dhatu_ref, "multi", ()))
    return Stem(s, frozenset(tags), tuple(sorted({**old, **multi}.items())), None, getattr(dhatu_ref, "trace", ()) + (_fired("krt"),))


def taddhita(stem: Stem, **vivaksha: str) -> Stem:
    from pipelines.taddhita_loop import derive_taddhita_stem
    s, tags, multi = derive_taddhita_stem(stem.slp1, set(stem.tags), stem.linga, **vivaksha)
    return Stem(s, frozenset(tags), tuple(sorted({**dict(stem.multi), **multi}.items())), None, stem.trace + (_fired("taddhita"),))


def sup(stem: Stem, vibhakti: int, vacana: int, linga: str | None = None) -> State:
    from pipelines.subanta import build_initial_state, run_subanta_sup_attach_and_finish_scanner
    linga = next((x.split(":", 1)[1] for x in stem.tags if x.startswith("yuktavad_linga:")), linga or stem.linga or "pulliṅga")
    s = build_initial_state(stem.slp1, vibhakti, vacana, linga, derived_pratipadika=True)
    s.terms[0].tags |= set(stem.tags)
    if stem.multi:
        s.meta["vikalpa_multi"] = dict(stem.multi)
    return run_subanta_sup_attach_and_finish_scanner(s)


def tinanta(dhatu: Dhatu, lakara: str, purusha: int, vacana: int, *, pada: str = "parasmai") -> State:
    """dhātu —(lakāra, tiṅ, vikaraṇa)→ kriyāpada, for a derived dhātu."""
    from pipelines.cycle_loop import derive_tinanta
    return derive_tinanta(list(dhatu.terms), lakara, purusha, vacana, pada=pada)
