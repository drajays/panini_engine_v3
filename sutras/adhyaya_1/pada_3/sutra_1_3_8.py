"""
1.3.8  उपदेशे लशक्वतद्धिते  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — initial **ḷ**-**ś**-**ku** (ल्·श्·कवर्ग) of a **non-taddhita**
  pratyaya in upadeśa gets *it* (then **1.3.9** deletes).

• **v3 representative encoding:** Classical लशक्व is implemented for the
  **sup** inventory by tagging initial **ṅ** (SLP1 ``N``) when ``has_initial_n_it``
  is set on the pratyaya Term — see ``sutra_4_1_2`` + ``_meta`` in
  ``data/inputs/sup_upadesha.json``. This keeps phoneme logic in sūtra files
  and inventory policy in **data/inputs/** (Art. 6 — engine never reads gold corpora).

• **v2 reference:** ``~/Documents/panini_engine_v2/core/sutra_1_3_8.py`` +
  ``it_rules.py``
  ``_terms_sup_or_primary_upadesh`` family — different Term model; same idea:
  first-hal it for eligible affixes.

• **Blindness:** ``cond`` reads tags / first Varṇa only — not paradigm coords.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _eligible_terms(state: State):
    for i, t in enumerate(state.terms):
        if "has_initial_n_it" not in t.tags:
            continue
        if not t.varnas:
            continue
        first = t.varnas[0]
        if first.slp1 != "N":
            continue
        if ("it" in first.tags or
            "it_candidate_lasaku" in first.tags):
            continue
        yield i


def cond(state: State) -> bool:
    return next(_eligible_terms(state), None) is not None


def act(state: State) -> State:
    for i in _eligible_terms(state):
        state.terms[i].varnas[0].tags.add("it_candidate_lasaku")
        key = ("it_lasaku", i)
        state.samjna_registry[key] = frozenset({state.terms[i].varnas[0].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.8",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "upadeSe laSakv ataddhite it",
    text_dev       = "उपदेशे लशक्वतद्धिते इत्",
    padaccheda_dev = "उपदेशे लशकु-अतद्धिते इत्",
    why_dev        = "अतद्धिते प्रत्ययस्य आदौ ल्-श्-कु-वर्णानाम् इत्-संज्ञा; "
                     "अत्र ङ्-आदिः प्रातिनिध्येन ‘has_initial_n_it’ द्वारा निर्दिष्टः। "
                     "लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
