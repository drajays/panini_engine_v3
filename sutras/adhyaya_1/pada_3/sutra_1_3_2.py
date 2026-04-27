"""
1.3.2  उपदेशेऽजनुनासिक इत्  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — assigns *it* to eligible sounds; deletion is **1.3.9**.

• **Case A — anunāsika vowel (अज् + ँ / SLP1 ``~``):** Varṇa already carries
  ``anunasika`` (from ``parse_slp1_upadesha_sequence`` / tokenizer). Tag
  ``it_candidate_anunasika`` for **1.3.9**.

• **Case B — vārttika इँर् (irit):** For a **dhātu** upadeśa whose tail is
  ``i(anunāsika) + r``, the cluster is *it* **as a unit** (not ``i~`` alone).
  Both varṇas get ``it_candidate_irit`` so **1.3.9** drops ``i`` and ``r``
  together (e.g. ``Bidi~r`` → ``Bid``).

• **Blindness (Art. 2):** Only SLP1 / Varṇa tags — never ``(vibhakti, vacana)``.

• **v2 hint:** ``~/Documents/panini_engine_v2/core`` (e.g. ``it_rules.py``) —
  v3 uses Varṇa tags +
  ``samjna_registry`` only.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import AC_DEV


def _irit_indices(state: State):
    """
    Yield (term_idx, idx_i, idx_r) for dhātu+upadeśa terms ending in i(anu)+r.
    """
    for ti, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "upadesha" not in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 2:
            continue
        i_v, r_v = vs[-2], vs[-1]
        if r_v.slp1 != "r":
            continue
        if i_v.slp1 != "i" or "anunasika" not in i_v.tags:
            continue
        yield ti, len(vs) - 2, len(vs) - 1


def _irit_pending(state: State):
    """irit positions not yet marked (avoids refiring → R2 / redundant work)."""
    for ti, ii, ir in _irit_indices(state):
        vi = state.terms[ti].varnas[ii]
        if "it_candidate_irit" not in vi.tags:
            yield ti, ii, ir


def _eligible_anunasika_vowels(state: State):
    """Yield (term_idx, varna_idx) for Case A, excluding irit ``i`` (Case B)."""
    irit_is: set[tuple[int, int]] = {(ti, ii) for ti, ii, _ in _irit_indices(state)}
    for i, t in enumerate(state.terms):
        if "upadesha" not in t.tags:
            continue
        for j, v in enumerate(t.varnas):
            # अज् — all vowel letters (incl. dīrgha); ``AC`` pratyāhāra here is short-only.
            if v.slp1 not in AC_DEV:
                continue
            if "anunasika" not in v.tags:
                continue
            if "it" in v.tags or "it_candidate_anunasika" in v.tags:
                continue
            if "it_candidate_irit" in v.tags:
                continue
            if (i, j) in irit_is:
                continue
            yield i, j


def cond(state: State) -> bool:
    if next(_irit_pending(state), None) is not None:
        return True
    return next(_eligible_anunasika_vowels(state), None) is not None


def act(state: State) -> State:
    # Case B — irit unit (इँर्)
    for ti, ii, ir in _irit_pending(state):
        vi, vr = state.terms[ti].varnas[ii], state.terms[ti].varnas[ir]
        vi.tags.add("it_candidate_irit")
        vr.tags.add("it_candidate_irit")
        state.samjna_registry[("it_irit", ti, ii, ir)] = frozenset({"i", "r"})

    # Case A — remaining अज् अनुनासिक
    for i, j in _eligible_anunasika_vowels(state):
        state.terms[i].varnas[j].tags.add("it_candidate_anunasika")
        key = ("it_anunasika", i, j)
        state.samjna_registry[key] = frozenset({state.terms[i].varnas[j].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.2",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "upadeSe ajanunAsika it",
    text_dev       = "उपदेशेऽजनुनासिक इत्",
    padaccheda_dev = "उपदेशे अज् अनुनासिकः इत्",
    why_dev        = "उपदेशावस्थायाम् अज् वर्णः अनुनासिकः चेद् इत्-संज्ञकः; "
                     "इँर्-वार्तिके पुनः द्वयोः संयुक्तः इत्। लोपः १.३.९।",
    anuvritti_from = ("1.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
