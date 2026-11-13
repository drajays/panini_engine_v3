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
    parts: tuple = ()       # a compound's members, pūrvapada(s) first: (slp1, tags) — the seam the tripāḍī (8.4.12, 5.4.69) reads


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
    if stem.parts:      # a compound: the strī pratyaya follows its last member; the pūrvapada(s) keep their seam (paYcan | pUla → paYca-pUlī)
        last, last_tags = stem.parts[-1]
        s, tags = derive_stri_stem(last, set(stem.tags), **vivaksha)
        parts = stem.parts[:-1] + ((s, last_tags),)
        return Stem("".join(p for p, _ in parts), frozenset(tags), stem.multi, "strīliṅga", stem.trace + (_fired("strI"),), parts)
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


_SAMASA_TAGS = ("dvigu", "tatpurusha", "bahuvrihi", "dvandva", "avyayibhava", "samAnADikaraRa")


def _samasa_done(x: State) -> bool:
    """The compound stem is ready: its members' sups are gone (2.4.71) and the sūtra that gives its liṅga has spoken (2.4.17 / 2.4.26 for a tatpuruṣa or
    dvandva, 2.4.18 for an avyayībhāva; a bahuvrīhi takes the liṅga of what it names, the speaker's)."""
    if not x.meta.get("2_4_71_luk"):
        return False
    kind = x.meta.get("samasa_kind", "").split(" ")[0]
    if kind in ("tatpurusha", "dvandva"):
        return any(a.startswith("samasa_linga:") for t in x.terms for a in t.tags)
    return kind != "avyayibhava" or bool(x.samjna_registry.get("2_4_18_avyayibhava_napuMsaka"))


def samasa(members: list[tuple], **vivaksha: str) -> Stem:
    """The vākya (each member: stem, vibhakti, vacana[, lexical tags[, liṅga]]) → one compound stem: the 2.1.x / 2.2.x sūtras make the members a samāsa,
    2.4.71 takes the members' sups away, 2.4.26 gives the liṅga. The members stay apart on ``parts`` (docs/SAMASA_MACHINE.md)."""
    import sutras  # noqa: F401
    from engine.tape_init.samasa import build_samasa_state
    from tools.autonomy_report import run_autonomously

    s = build_samasa_state(members, **vivaksha)
    s.phase = "upadesha"
    st = run_autonomously(s, "", "".join(m[0] for m in members), 300, stop_before_tripadi=True, stop_when=_samasa_done).state
    if "samasa_kind" not in st.meta:
        raise ValueError("no samāsa sūtra applied to " + " + ".join(m[0] for m in members))
    ms = [t for t in st.terms if "samasa_member" in t.tags]
    last = ms[-1]
    linga = next((x.split(":", 1)[1] for x in last.tags if x.startswith("samasa_linga:")), None) \
        or ("napuṃsaka" if st.samjna_registry.get("2_4_18_avyayibhava_napuMsaka") else None)
    keep = lambda t: frozenset(x for x in t.tags if x.startswith("lex:") or x in _SAMASA_TAGS)       # the saṃjñā and lexical facts, not the loop's origin record of a lukt sup
    tags = frozenset().union(*(keep(t) for t in ms)) | frozenset({"lex:samAsa"})
    parts = tuple(("".join(v.slp1 for v in t.varnas), keep(t)) for t in ms)
    return Stem("".join(p for p, _ in parts), tags, (), linga, (_fired("samasa"),), parts)


def sup(stem: Stem, vibhakti: int, vacana: int, linga: str | None = None) -> State:
    from pipelines.subanta import build_initial_state, run_subanta_sup_attach_and_finish_scanner
    linga = next((x.split(":", 1)[1] for x in stem.tags if x.startswith("yuktavad_linga:")), linga or stem.linga or "pulliṅga")
    s = build_initial_state(stem.slp1, vibhakti, vacana, linga, derived_pratipadika=True)
    s.terms[0].tags |= set(stem.tags)
    if stem.parts:          # the compound's pūrvapada(s) stay Terms of their own: the seam is a samāsa seam, not a samānapada one
        from engine.state import Term
        from phonology.varna import parse_slp1_upadesha_sequence
        last = s.terms[0]
        last.varnas = list(parse_slp1_upadesha_sequence(stem.parts[-1][0]))
        last.meta["upadesha_slp1"] = stem.slp1
        last.tags |= {"samasa_uttarapada", "samasa_member"}
        s.terms = [Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence(p)), tags={"samasa_purvapada", "samasa_member", "prātipadika"} | set(pt),
                        meta={"upadesha_slp1": p}) for p, pt in stem.parts[:-1]] + [last]
    if stem.multi:
        s.meta["vikalpa_multi"] = dict(stem.multi)
    return run_subanta_sup_attach_and_finish_scanner(s)


def tinanta(dhatu: Dhatu, lakara: str, purusha: int, vacana: int, *, pada: str = "parasmai") -> State:
    """dhātu —(lakāra, tiṅ, vikaraṇa)→ kriyāpada, for a derived dhātu."""
    from pipelines.cycle_loop import derive_tinanta
    return derive_tinanta(list(dhatu.terms), lakara, purusha, vacana, pada=pada)
