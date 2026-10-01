"""
1.3.9  तस्य लोपः  —  VIDHI

Śāstra / engine role (CONSTITUTION Arts. 1, 2, 5 (R1), 7)
──────────────────────────────────────────────────────────
• **Type:** VIDHI — **deletes** Varṇas that have been marked as *it* (by
  **1.3.2**–**1.3.8** and related it-candidate tags). This is
  the operational *lopa* of the *it* sound — the **saṃjñā** *lopa* (“*adarśanam*”
  in *sthāne* — **1.1.60** with *sthāne* anuv.* **1.1.50**) is registered separately;
  **1.3.9** does not re-invoke **1.1.60** in ``cond`` (recipes preflight **1.1.60**).

• **tasya:** *Of that [it]* — anuvṛtti links to the *it* prakaraṇa opened by
  **1.3.2**; baked into ``text_slp1`` as ``itasya`` (Art. 4).

• **R1 / vacuous:** If *it* is tagged, ``act`` must remove the corresponding
  rows and ``form_before`` may differ from ``form_after``.  If there is no *it* to
  *lop*, the dispatcher records **APPLIED_VACUOUS** (checked *śūnya* *lopa*), not
  **SKIPPED (COND-FALSE)**.

• **v2 reference:** ``~/Documents/panini_engine_v2/core/it_rules.py``
  ``cond_1_3_9`` /
  ``act_1_3_9`` — same job on a different ``State`` / Varṇa model.

• **Tags:** Only deletions listed in ``IT_LOPA_TAGS``; ``nut_agama_inserted``
  etc. are deliberately excluded (see 7.1.54 notes in repo).

• **What the lopa leaves behind (``engine.it_samjna.record_it_lopa``):** one
  record per *it* — letter(s), the sūtra that named it, ādi/antya position and
  the class name (*kit*, *ṅit*, *pit*, *śit*, *ḍvit*, *irit*, *udit* …) — in
  ``Term.meta["it_records"]``, the Term tag ``it:<name>``, and the derivation-wide
  ``state.meta["it_lopa_log"]``.  The trace row's ``why_now_dev`` lists them.
  When no sūtra of 1.3.2–1.3.8 has an unmarked candidate left on a Term, the
  Term is stamped ``it_lopa_done`` so its residue is never re-analysed.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 13009 · तस्य लोपः
              padaccheda: तस्य · लोपः
  Source #2 — Kāśikā 1.3.9 udāharaṇa:
                हुँ (उँ इत्) → हु
                दिवुँ (उँ इत्) → दिव्
                तथा चैवोदाहृतम्
  Gloss (sa) — तस्य (इत्संज्ञकस्य) लोपः।
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_pacaka.py, tests/unit/test_Bavitavyam_split_prakriyas.py, tests/unit/test_Bavitum_split_prakriyas.py
  Reference record: sutra_ref_out/1_3_9.json
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_phonetic import IT_LOPA_TAGS
from engine.it_samjna import META_IT_LOPA_LOG, META_LOPA_DONE, record_it_lopa
from engine.state  import State
from phonology.joiner import slp1_to_devanagari
from phonology.pratyahara import is_dirgha
from phonology.varna     import AC_DEV, mk as v_mk, mk_inherent_a

# Re-export for sibling sūtras (``1.3.5``–``1.3.7``); canonical set: ``engine.it_phonetic``.


def _has_it_varna(term) -> bool:
    return any(
        v.tags & IT_LOPA_TAGS
        for v in term.varnas
    )


def _only_it_varnas_after(term, j: int) -> bool:
    """True iff every varṇa strictly after ``j`` already bears an *it* lopa tag."""
    for k in range(j + 1, len(term.varnas)):
        if not (term.varnas[k].tags & IT_LOPA_TAGS):
            return False
    return True


def cond(state: State) -> bool:
    return any(_has_it_varna(t) for t in state.terms)


def _it_samjna_exhausted(state: State, ti: int) -> bool:
    """No sūtra of 1.3.2–1.3.8 still has an unmarked *it* candidate in ``terms[ti]``."""
    from sutras.adhyaya_1.pada_3 import (
        sutra_1_3_2, sutra_1_3_3, sutra_1_3_5, sutra_1_3_6, sutra_1_3_7, sutra_1_3_8,
    )
    return not any(
        m.term_candidates(state, ti)
        for m in (sutra_1_3_2, sutra_1_3_3, sutra_1_3_5, sutra_1_3_6, sutra_1_3_7, sutra_1_3_8)
    )


def act(state: State) -> State:
    exhausted = {
        ti for ti, t in enumerate(state.terms)
        if "upadesha" in t.tags and _it_samjna_exhausted(state, ti)
    }
    new_log: list[dict] = []
    summary: list[str] = []
    for ti, t in enumerate(state.terms):
        removed: list[str] = []
        removed_at: list[tuple[int, object]] = []
        n_before = len(t.varnas)
        new_varnas = []
        for j, v in enumerate(t.varnas):
            if not (v.tags & IT_LOPA_TAGS):
                new_varnas.append(v)
                continue
            removed_at.append((j, v))
            # Dhātu upadeśa: anunāsika vowel (१.३.२) — *it* is the nasal
            # feature; the vowel letter remains (e.g. डुपचँष् → पच्, not प्-च्).
            # Sup / other pratyayas: vowel marked anunāsika is fully elided
            # (e.g. सुँ → स्).
            if "it_candidate_irit" in v.tags:
                removed.append(v.slp1)
                # After all irit varnas drop, mark the dhātu as "irit" (iñr vārttika).
                # Done outside loop (below) after we know all irit were removed.
                continue
            if (
                "dhatu" in t.tags
                and "it_candidate_anunasika" in v.tags
                and v.slp1 in AC_DEV
            ):
                removed.append(v.slp1)
                # An anunāsika *i* that is *it* makes the dhātu *idit* (वदिँ → वद्),
                # the condition of 7.1.58. The *i* of ādi ñi (1.3.5) and of इँर्
                # (irit, above) never reach this branch.
                if v.slp1 == "i":
                    t.tags.add("idit")
                # Final anunāsika vowel (e.g. "…A~") or vowel whose only tail material
                # is *it* (e.g. ``mFjU~z``: ``U`` before hal-it ``z``) — full elision.
                # An upadeśa-initial anunāsika vowel is a whole marker (ओँविजीँ → विज्,
                # टुओँश्वि → श्वि: only markers precede it).
                if j < len(t.varnas) - 1 and all(x.tags & IT_LOPA_TAGS for x in t.varnas[:j]):
                    continue
                if j == len(t.varnas) - 1 or _only_it_varnas_after(t, j):
                    # ``dIDI~N``-class dhātus: dīrgha ``I``/``U``/``F`` before final
                    # ``N`` (halantyam it) — keep the vowel, drop only anunāsika
                    # (contrast ``mFjU~z`` where tail is ``z``, not ``N``).
                    if (
                        "dhatu" in t.tags
                        and is_dirgha(v.slp1)
                        and j + 1 == len(t.varnas) - 1
                        and t.varnas[-1].slp1 == "N"
                        and "it_candidate_halantyam" in t.varnas[-1].tags
                    ):
                        if v.slp1 == "a" and v.dev == "":
                            new_varnas.append(mk_inherent_a())
                        else:
                            new_varnas.append(v_mk(v.slp1))
                        continue
                    continue
                # Otherwise, nasalization is the it-feature; the vowel letter remains.
                if v.slp1 == "a" and v.dev == "":
                    new_varnas.append(mk_inherent_a())
                else:
                    new_varnas.append(v_mk(v.slp1))
                continue
            removed.append(v.slp1)
            # fall through: delete varna (do not append)
        if removed:
            # Preserve it-markers for downstream rules that depend on them
            # (e.g. 7.2.116 checks for ṇit in a kṛt pratyaya).
            prev = t.meta.get("it_markers")
            if isinstance(prev, set):
                prev.update(removed)
            else:
                t.meta["it_markers"] = set(removed)
            # iñr vārttika: if both 'i' and 'r' were irit-lopped from a dhātu,
            # mark it "irit" so 3.1.57 can fire and 7.1.58 (idit num) stays silent.
            if "dhatu" in t.tags and "i" in removed and "r" in removed:
                t.tags.add("irit")
            upadesha_dev = slp1_to_devanagari(t.varnas)
            recs = record_it_lopa(t, removed_at, n_before)
            new_log.extend(dict(r, term_index=ti) for r in recs)
            summary.append(upadesha_dev + " — " + ", ".join(
                f"{r['letters_dev']} → {r['name_dev'] or 'इत्'} ({_dev_digits(r['sutra'] or '')})"
                for r in recs
            ))
        t.varnas = new_varnas
        if ti in exhausted:
            t.meta[META_LOPA_DONE] = (
                (t.meta.get("upadesha_slp1") or "").strip(),
                "".join(v.slp1 for v in new_varnas),
            )
    if new_log:
        state.meta[META_IT_LOPA_LOG] = list(state.meta.get(META_IT_LOPA_LOG) or ()) + new_log
    state.meta["__why_now_dev__"] = (
        "इत्-संज्ञक-वर्णानां लोपः (तस्य लोपः): " + "; ".join(summary) + "। (१.३.९)"
    )
    return state


_DEV_DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")


def _dev_digits(s: str) -> str:
    return s.replace("-vārttika", " वार्तिकम्").translate(_DEV_DIGITS)


SUTRA = SutraRecord(
    sutra_id       = "1.3.9",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'tasya lopaH',
    text_dev       = 'तस्य लोपः',
    padaccheda_dev = "उपदेशे इतस्य लोपः",
    why_dev        = "ये वर्णाः ‘इत्’ संज्ञकाः (१.३.२–१.३.८), तेषां लोपः। "
                     "अयम् एव ध्वनि-अपगमः — संज्ञा-निर्देशो न।",
    anuvritti_from = (
        "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8",
    ),
    cond           = cond,
    act            = act,
    why_dev_vacuous = "इत्-संज्ञक-वर्णाः न सन्ति, अतः लोपः शून्यः; "
                      "तथापि नियम-परीक्षा अनिवार्या (१.३.९)।",
)

register_sutra(SUTRA)
