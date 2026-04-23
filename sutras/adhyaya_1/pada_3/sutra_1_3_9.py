"""
1.3.9  उपदेशे इतस्य लोपः  —  VIDHI

Śāstra / engine role (CONSTITUTION Arts. 1, 2, 5 (R1), 7)
──────────────────────────────────────────────────────────
• **Type:** VIDHI — **deletes** Varṇas that have been marked as *it* (by
  **1.3.2**–**1.3.8** and related it-candidate tags). This is
  the operational *lopa* of the *it* sound — not the saṃjñā step.

• **tasya:** *Of that [it]* — anuvṛtti links to the *it* prakaraṇa opened by
  **1.3.2**; baked into ``text_slp1`` as ``itasya`` (Art. 4).

• **R1:** Not exempt — if ``cond`` is True, ``act`` must remove at least one
  Varṇa whose tags intersect ``IT_LOPA_TAGS``; otherwise *R1Violation*.

• **v2 reference:** ``~/Documents/panini_engine_v2/core/it_rules.py``
  ``cond_1_3_9`` /
  ``act_1_3_9`` — same job on a different ``State`` / Varṇa model.

• **Tags:** Only deletions listed in ``IT_LOPA_TAGS``; ``nut_agama_inserted``
  etc. are deliberately excluded (see 7.1.54 notes in repo).
"""
from __future__ import annotations

from typing import Final, FrozenSet

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.pratyahara import AC
from phonology.varna     import mk as v_mk, mk_inherent_a

# Exposed for tools/UI — single source for “what 1.3.9 strips”
IT_LOPA_TAGS: Final[FrozenSet[str]] = frozenset((
    "it",
    "it_candidate_halantyam",
    "it_candidate_anunasika",
    "it_candidate_irit",
    "it_candidate_nit_tu_du",
    "it_candidate_sha_pratyaya",
    "it_candidate_cutu",
    "it_candidate_lasaku",
))


def _has_it_varna(term) -> bool:
    return any(
        v.tags & IT_LOPA_TAGS
        for v in term.varnas
    )


def cond(state: State) -> bool:
    return any(_has_it_varna(t) for t in state.terms)


def act(state: State) -> State:
    for t in state.terms:
        removed: list[str] = []
        new_varnas = []
        for v in t.varnas:
            if not (v.tags & IT_LOPA_TAGS):
                new_varnas.append(v)
                continue
            # Dhātu upadeśa: anunāsika vowel (१.३.२) — *it* is the nasal
            # feature; the vowel letter remains (e.g. डुपचँष् → पच्, not प्-च्).
            # Sup / other pratyayas: vowel marked anunāsika is fully elided
            # (e.g. सुँ → स्).
            if "it_candidate_irit" in v.tags:
                removed.append(v.slp1)
                continue
            if (
                "dhatu" in t.tags
                and "it_candidate_anunasika" in v.tags
                and v.slp1 in AC
            ):
                removed.append(v.slp1)
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
        t.varnas = new_varnas
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.9",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "upadeSe itasya lopaH",
    text_dev       = "उपदेशे इतस्य लोपः",
    padaccheda_dev = "उपदेशे इतस्य लोपः",
    why_dev        = "ये वर्णाः ‘इत्’ संज्ञकाः (१.३.२–१.३.८), तेषां लोपः। "
                     "अयम् एव ध्वनि-अपगमः — संज्ञा-निर्देशो न।",
    anuvritti_from = (
        "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8",
    ),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
