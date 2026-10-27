"""pipelines/taddhita_loop.py — a taddhita word through the loop, as :mod:`pipelines.krdanta` does for a kṛdanta.

``derive_taddhita(stem, vibhakti, vacana, linga, taddhitArtha="apatya", …)``: the stem is a prātipadika (SLP1), the vivakṣā names the sense
(AMENDMENT 25); the loop picks the pratyaya (4.1.83 ff. and their apavādas), does it-lopa, vṛddhi and the rest of the aṅgakārya and sandhi, and
stops where the tripāḍī would begin; the subanta then takes the sup (the derived stem is a prātipadika, 1.2.46)."""
from __future__ import annotations

from engine.state import State


def derive_taddhita_stem(stem_slp1: str, origin_tags: set[str] | None = None, stem_linga: str | None = None, **vivaksha: str) -> tuple[str, set[str], dict]:
    from engine import origin
    from engine.tape_init.taddhita import build_taddhita_state
    from tools.autonomy_report import run_autonomously

    s = build_taddhita_state(stem_slp1, origin_tags, **vivaksha)
    if stem_linga:
        s.terms[0].tags.add(stem_linga)
    s.phase = "upadesha"
    run = run_autonomously(s, "", stem_slp1, 300, stop_before_tripadi=True)
    st = run.state
    return "".join(v.slp1 for t in st.terms for v in t.varnas), set(origin.record_from_terms(st.terms)), dict(st.meta.get("vikalpa_multi") or {})


def derive_taddhita(stem_slp1: str, vibhakti: int, vacana: int, linga: str = "pulliṅga", *, origin_tags: set[str] | None = None,
                    stem_linga: str | None = None, **vivaksha: str) -> State:
    from pipelines.subanta import build_initial_state, run_subanta_sup_attach_and_finish_scanner

    stem, tags, multi = derive_taddhita_stem(stem_slp1, origin_tags, stem_linga, **vivaksha)
    s = build_initial_state(stem, vibhakti, vacana, linga, derived_pratipadika=True)
    s.terms[0].tags |= tags
    if multi:
        s.meta["vikalpa_multi"] = multi
    return run_subanta_sup_attach_and_finish_scanner(s)
