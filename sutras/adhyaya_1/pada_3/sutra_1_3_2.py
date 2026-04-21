"""
1.3.2  उपदेशेऽजनुनासिक इत्  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — assigns the technical name *it* to eligible sounds; does
  not delete them (that is **1.3.9** *tasya lopaḥ*).

• **Blindness:** ``cond`` / ``act`` inspect only Varṇa tags / ``AC`` / the
  ``upadesha`` term tag — never ``(vibhakti, vacana)`` (Art. 2).

• **Anuvṛtti (Art. 4):** Baked into ``text_slp1`` / ``text_dev``; the engine
  does not compute anuvṛtti at runtime. ``anuvritti_from`` is metadata only.

• **v2 reference:** panini_engine_v2/core/it_rules.py ``cond_1_3_2`` /
  ``act_1_3_2`` — anunāsika vowels in upadeśa; v3 uses tag ``anunasika`` on
  ``Varna`` plus ``upadesha`` on the Term (from 4.1.2 sup attachment).

Operational sketch
──────────────────
  sup / pratyaya upadeśa ``s~`` → ``[s, u(anunāsika)]`` → this rule tags the
  vowel with ``it_candidate_anunasika`` → **1.3.9** removes it.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import AC


def _eligible_vowels(state: State):
    """Yield (term_idx, varna_idx) of anunāsika-marked vowels in upadeśa."""
    for i, t in enumerate(state.terms):
        if "upadesha" not in t.tags:
            continue
        for j, v in enumerate(t.varnas):
            if v.slp1 not in AC:
                continue
            if "anunasika" not in v.tags:
                continue
            if ("it" in v.tags or
                "it_candidate_anunasika" in v.tags):
                continue
            yield i, j


def cond(state: State) -> bool:
    return next(_eligible_vowels(state), None) is not None


def act(state: State) -> State:
    for i, j in _eligible_vowels(state):
        state.terms[i].varnas[j].tags.add("it_candidate_anunasika")
        key = ("it_anunasika", i, j)
        state.samjna_registry[key] = frozenset({state.terms[i].varnas[j].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.2",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "upadeSe ajanunAsika it",
    text_dev       = "उपदेशेऽजनुनासिक इत्",
    padaccheda_dev = "उपदेशे अज्-अनुनासिकः इत्",
    why_dev        = "उपदेशे अनुनासिक अच्-वर्णः ‘इत्’ संज्ञां लभते; "
                     "लोपः न अत्र अपि तु १.३.९ इत्यनेन।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
