"""
1.3.3  उपदेशेऽन्त्यं हलन्त्यम्  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — final **hal** of an upadeśa gets the name *it* (via
  candidate tag); deletion is **1.3.9**, not here.

• **1.3.4 (न विभक्तौ तुस्माः):** A **sup** pratyaya whose final **hal** is in
  **tusma** does **not** get halantyam (structural ``sup`` + ``TUSMA``; see
  ``sutra_1_3_4``). The ``has_halant_it`` tag (from ``sup_upadesha.json``
  ``_meta``) still gates which affixes participate in halantyam at all.
  The same *tusma*-final exclusion applies to **tiṅ** *ādeśa* *vibhakti* *Terms*
  (``is_tin_vibhakti_pratyaya`` — e.g. *tas*, *mas*).

• **Anuvṛtti (Art. 4):** ``upadeśe`` and ``it`` are baked into ``text_*``;
  ``anuvritti_from`` points at **1.3.2** for the *upadeśe* anchor.

• **Blindness:** No paradigm coordinates in ``cond`` (Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import HAL, TUSMA

from sutras.adhyaya_1.pada_4.vibhakti_samjna_1_4_104 import is_tin_vibhakti_pratyaya


def _eligible_terms(state: State):
    """Yield (index, term) with an unmarked final hal in upadeśa (when allowed)."""
    for i, t in enumerate(state.terms):
        if "upadesha" not in t.tags:
            continue
        if "sup" in t.tags and "has_halant_it" not in t.tags:
            continue
        if not t.varnas:
            continue
        last = t.varnas[-1]
        if last.slp1 not in HAL:
            continue
        if "sup" in t.tags and last.slp1 in TUSMA:
            continue
        up_tin = (t.meta.get("upadesha_slp1") or "").strip()
        # **tām** (narrow **3.4.101** output): final nasal *m* is not *halantyam-it*.
        if up_tin == "tAm" and last.slp1 == "m":
            continue
        # *na vibhaktau tusmāḥ* (1.3.4) — *tiṅ* *ādeśa* *vibhakti* finals in *tusma*
        # are likewise not *halantyam-it* (e.g. *tas*, *mas*).
        if is_tin_vibhakti_pratyaya(t) and last.slp1 in TUSMA:
            continue
        if "it" in last.tags or "it_candidate_halantyam" in last.tags:
            continue
        yield i, t


def cond(state: State) -> bool:
    return next(_eligible_terms(state), None) is not None


def act(state: State) -> State:
    for i, t in _eligible_terms(state):
        t.varnas[-1].tags.add("it_candidate_halantyam")
        # Back-compat: keep the historical index-only key expected by some tests.
        # Also keep a stable key that survives later structural insertions.
        state.samjna_registry[("it_halantyam", i)] = frozenset({t.varnas[-1].slp1})

        up = (t.meta.get("upadesha_slp1") or "").strip()
        key = ("it_halantyam", i, up)
        state.samjna_registry[key] = frozenset({t.varnas[-1].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.3",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "upadeSe hal antyam it",
    text_dev       = "उपदेशेऽन्त्यं हलन्त्यम् इत्",
    padaccheda_dev = "उपदेशे अन्त्यं हलन्त्यम्",
    why_dev        = "उपदेशे अन्त्यः हल् वर्णः ‘इत्’ संज्ञां लभते; "
                     "तुस्मान्त-विभक्तौ निषेधः १.३.४। लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
