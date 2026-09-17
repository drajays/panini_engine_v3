"""
engine/phases/pada_merger — Universal structural pada-merge.

``pada_merge(state)`` replaces every ``_pada_merge()`` copy that was
duplicated across ``pipelines/tinanta.py``, ``pipelines/subanta.py``, and
``pipelines/krdanta.py``.  It is a structural book-keeping step, NOT a sūtra
— recorded in ``State.trace`` with ``sutra_id == "__MERGE__"``.

Semantic tags preserved across the merge (superset of all previous versions):
  - tinganta   (from tinanta derivations — "tin" tag on suffix term)
  - prātipadika
  - bha
  - anga
  - strīliṅga / napuṃsaka / pulliṅga
  - krt_tfc
  - pragṛhya  (from 1.1.11 — needed for sentence-level sandhi rules)
"""
from __future__ import annotations

from typing import List

from engine.state import State, Term


def pada_merge(state: State) -> None:
    """
    Structural merge: all Terms → single pada-tagged Term.

    Must be called BEFORE ``execute_tripadi_phase()``.
    Pre-merge Tripāḍī rules (8.2.1, 8.4.54, 8.2.29 …) that need to see
    individual terms must be called explicitly by the pipeline BEFORE this.

    Idempotent: if ``state.terms`` is already a single pada-tagged Term,
    the merge is still applied (re-flattening varṇas) to ensure the trace
    entry is recorded — but callers should not double-merge.
    """
    if not state.terms:
        return

    # Import lazily to avoid circular dependencies at module load time.
    try:
        from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG  # type: ignore
    except ImportError:
        PRAGHYA_TERM_TAG = "__pragrhya__"

    terms = state.terms

    # ── Collect semantic tags to preserve ────────────────────────────────────
    keep_tinganta = any(
        "tinganta" in t.tags or "tin" in t.tags for t in terms
    )
    keep_pragrahya = any(PRAGHYA_TERM_TAG in t.tags for t in terms)
    keep_bha = any("bha" in t.tags for t in terms)
    keep_pratipadika = any("prātipadika" in t.tags for t in terms)
    keep_anga = any("anga" in t.tags for t in terms)
    keep_krt_tfc = any("krt_tfc" in t.tags for t in terms)
    keep_an_pratipadika = any("an_pratipadika" in t.tags for t in terms)
    keep_sambuddhi = any("sambuddhi" in t.tags for t in terms)
    keep_ngi = any("ngi" in t.tags for t in terms)
    keep_linga = (
        "strīliṅga" if any("strīliṅga" in t.tags for t in terms)
        else "napuṃsaka" if any("napuṃsaka" in t.tags for t in terms)
        else "pulliṅga" if any("pulliṅga" in t.tags for t in terms)
        else None
    )

    # ── Flatten varṇa tapes ───────────────────────────────────────────────────
    form_before = state.flat_slp1()
    all_varnas: List = []
    for t in terms:
        all_varnas.extend(t.varnas)

    # ── Build merged Term ─────────────────────────────────────────────────────
    tags = {"pada"}
    if keep_tinganta:
        tags.add("tinganta")
    if keep_pragrahya:
        tags.add(PRAGHYA_TERM_TAG)
    if keep_bha:
        tags.add("bha")
    if keep_pratipadika:
        tags.add("prātipadika")
    if keep_anga:
        tags.add("anga")
    if keep_krt_tfc:
        tags.add("krt_tfc")
    if keep_an_pratipadika:
        tags.add("an_pratipadika")
    if keep_sambuddhi:
        tags.add("sambuddhi")
    if keep_ngi:
        tags.add("ngi")
    if keep_linga:
        tags.add(keep_linga)

    pada = Term(kind="pada", varnas=all_varnas, tags=tags, meta={})
    state.terms = [pada]

    state.emit_structural(
        "__MERGE__",
        form_before=form_before,
        form_after=state.flat_slp1(),
        why_dev="पद-रचना — सर्व-धातु/सुबन्त/कृदन्त-संयोजनम् (संरचनात्मकं, न सूत्रम्)।",
        type_label="पद-मेलनम्",
        event="MERGE",
    )
