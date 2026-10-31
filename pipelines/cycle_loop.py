"""pipelines/cycle_loop.py — the arrows strī, nāmadhātu and sanādi (docs/V4_CYCLE.md), driven by the loop and no recipe.

    derive_stri_stem(stem, …)    prātipadika →(4.1.3 striyām, 4.1.4 ṭāp, 6.1.101)→ prātipadika            (vivakṣā linga=strI)

    derive_nama_dhatu(stem, …)   prātipadika + sup  →(3.1.8 kyac, 2.4.71 luk, 3.1.32, 7.4.33 …)→ dhātu   (vivakṣā icCA)
    derive_sanadi(terms, …)      dhātu →(3.1.26 ṇic, 3.1.32 …)→ dhātu                                  (vivakṣā hetumat)

Both return the live Terms the loop left (a dhātu is a Term list, not a string: the ṇic that a later 6.4.51 removes must still be a Term)."""
from __future__ import annotations

from engine.state import State, Term
from engine.tape_init.krdanta import build_krdanta_state


def _run(state: State, case: str) -> list[Term]:
    from tools.autonomy_report import run_autonomously

    state.phase = "pratyaya"
    return [t.clone() for t in run_autonomously(state, "", case, 300, stop_before_tripadi=True).state.terms]


def _merge_one_dhatu(terms: list[Term]) -> Term:
    """SHORTCUT S105 — structural (not a sūtra): 3.1.32 makes the whole sanādyanta one dhātu; the Terms that still have letters become its one Term, as ``_kyaz_merge`` did."""
    from engine import origin

    live = [t for t in terms if t.varnas]
    flat = "".join(v.slp1 for t in live for v in t.varnas)
    rec = set(origin.record_from_terms(live)) - {origin.DHATU + (t.meta.get("upadesha_slp1") or "") for t in live if t.kind == "pratyaya"}   # 3.1.32 tagged the kyac Term dhatu too
    return Term(kind="prakriti", varnas=[v.clone() for t in live for v in t.varnas], tags={"dhatu", "anga", "sanadi"} | rec,
                meta={"upadesha_slp1": flat, "sanadi_pratyayanta": True, **({"nijanta": True} if any("nic" in t.tags for t in live) else {})})   # the convention 6.4.51, 7.4.1, 7.4.93 read


def derive_stri_stem(stem_slp1: str, origin_tags: set[str] | None = None, **vivaksha: str) -> tuple[str, set[str]]:
    import sutras  # noqa: F401
    from engine import origin
    from engine.tape_init.taddhita import build_taddhita_state
    from tools.autonomy_report import run_autonomously

    s = build_taddhita_state(stem_slp1, set(origin_tags or ()) | {"strīliṅga"}, linga="strI", **vivaksha)   # SHORTCUT S104: the strīliṅga tag 4.1.4 reads is the caller's linga=strI, put on the stem here
    s.phase = "upadesha"
    st = run_autonomously(s, "", stem_slp1, 300, stop_before_tripadi=True).state
    return "".join(v.slp1 for t in st.terms for v in t.varnas), set(origin.record_from_terms(st.terms)) | {"strīliṅga"}


def derive_nama_dhatu(stem_slp1: str, origin_tags: set[str], vibhakti: int, vacana: int, **vivaksha: str) -> list[Term]:
    """The stem stands with the sup its role in the speaker's sentence gives it (putram: dvitīyā); kyac is taken after that sup (supaḥ) and 2.4.71 removes it.
    SHORTCUT S102: (vibhakti, vacana) are the caller's — the kāraka-vibhakti sūtras (2.3.x) do not choose the sup here."""
    import sutras  # noqa: F401
    from engine import apply_rule
    from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7

    s = build_initial_state(stem_slp1, vibhakti, vacana, next((t for t in ("strīliṅga", "napuṃsakaliṅga") if t in origin_tags), "pulliṅga"), derived_pratipadika=True)
    s.terms[0].tags |= set(origin_tags)
    s = apply_rule("4.1.2", run_subanta_preflight_through_1_4_7(s))
    from engine.tape_init.sanadi import with_vivaksha

    return [_merge_one_dhatu(_run(with_vivaksha(s, **vivaksha), stem_slp1))]


def derive_sanadi(terms: list[Term], **vivaksha: str) -> list[Term]:
    s = build_krdanta_state([t.clone() for t in terms], **vivaksha)
    return [_merge_one_dhatu(_run(s, "".join(v.slp1 for t in terms for v in t.varnas)))]


def derive_tinanta(terms: list[Term], lakara: str, purusha: int, vacana: int, *, pada: str = "parasmai", prayoga: str = "kartari") -> State:
    """The tiṅanta arrow of a derived dhātu: the dhātu Term as the sanādi stage left it (a ṇijanta is bhvādi-like, 3.1.32), then the loop of tools/autonomy_report.
    SHORTCUT S103: ``pada`` is the caller's vivakṣā (1.3.74 would choose for a ṇic-anta); the Term's gaṇa 1 is set here, not read from the dhātupāṭha."""
    import sutras  # noqa: F401
    from engine.tape_init.tinanta import _LAKARA_TAG, _record_vivaksha
    from tools.autonomy_report import _tinanta_attach, run_autonomously

    dh = terms[0].clone()
    dh.tags |= {"upadesha", prayoga, _LAKARA_TAG[lakara]}
    dh.meta.setdefault("gana", 1)
    s = State(terms=[dh], meta={"derivation_class": "tinanta", "lakara": lakara, "prayoga": prayoga}, trace=[])
    _record_vivaksha(s, prayoga)
    s = _tinanta_attach(s, lakara, pada, purusha, vacana)
    return run_autonomously(s, "", dh.meta["upadesha_slp1"], 300).state
