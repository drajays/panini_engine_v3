"""
1.3.2  उपदेशेऽजनुनासिक इत्  —  SAMJNA

Sources consulted:
- ashtadhyayi.com data.txt row i=13002
- Kāśikā: "तत्र योऽच् अनुनासिकः स इत्संज्ञो भवति" — एधँ → एध, स्पर्धँ → स्पर्ध
- Cross-validation: regression tests tests/unit/test_it_prakarana.py
  (गमॢँ → गम्, सुँ → स्, भिदिँर् → भिद्), tests/unit/test_tinanta_pathati_lat.py

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — assigns *it* to eligible sounds; deletion is **1.3.9**.

• **Case A — anunāsika vowel (अच् + ँ / SLP1 ``~``):** Varṇa already carries
  ``anunasika`` (from ``parse_slp1_upadesha_sequence`` / tokenizer). Tag
  ``it_candidate_anunasika`` for **1.3.9**.

• **Case B — vārttika इर इत्संज्ञा वाच्या (irit):** For a **dhātu** upadeśa whose
  tail is ``i(anunāsika) + r``, the cluster is *it* **as a unit** (not ``i~``
  alone).  Both varṇas get ``it_candidate_irit`` so **1.3.9** drops them together
  and records one *irit* (3.1.57 *irito vā*), e.g. ``Bidi~r`` → ``Bid``.

• **Upadeśa only:** a Term already through **1.3.9** (``it_lopa_already_done``)
  is no longer in its aupadeśika form and is not re-examined.

• **Blindness (Art. 2):** Only SLP1 / Varṇa tags — never ``(vibhakti, vacana)``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_samjna import TAG_ANUNASIKA, TAG_IRIT, it_lopa_already_done, register_candidate_tag
from engine.state  import State
from phonology.varna import AC_DEV


def _in_upadesha(t) -> bool:
    return "upadesha" in t.tags and not it_lopa_already_done(t)


def _irit_pair(t):
    """(idx_i, idx_r) when the dhātu upadeśa ends in इँर्, else None."""
    if "dhatu" not in t.tags or not _in_upadesha(t):
        return None
    vs = t.varnas
    if len(vs) < 2:
        return None
    i_v, r_v = vs[-2], vs[-1]
    if r_v.slp1 != "r" or i_v.slp1 != "i" or "anunasika" not in i_v.tags:
        return None
    return len(vs) - 2, len(vs) - 1


def term_candidates(state: State, ti: int) -> list[int]:
    """Varṇa indices of ``terms[ti]`` this sūtra (or its vārttika) still has to name *it*."""
    t = state.terms[ti]
    if not _in_upadesha(t):
        return []
    out: list[int] = []
    pair = _irit_pair(t)
    if pair is not None and "it_candidate_irit" not in t.varnas[pair[0]].tags:
        out.extend(pair)
    irit_i = pair[0] if pair is not None else None
    for j, v in enumerate(t.varnas):
        if j == irit_i or v.slp1 not in AC_DEV or "anunasika" not in v.tags:
            continue
        if v.tags & {"it", "it_candidate_anunasika", "it_candidate_irit"}:
            continue
        out.append(j)
    return out


def cond(state: State) -> bool:
    return any(term_candidates(state, ti) for ti in range(len(state.terms)))


def act(state: State) -> State:
    for ti, t in enumerate(state.terms):
        cands = term_candidates(state, ti)
        if not cands:
            continue
        pair = _irit_pair(t)
        for j in cands:
            v = t.varnas[j]
            if pair is not None and j in pair:
                v.tags.add("it_candidate_irit")
                continue
            v.tags.add("it_candidate_anunasika")
            state.samjna_registry[("it_anunasika", ti, j)] = frozenset({v.slp1})
        if pair is not None and pair[0] in cands:
            state.samjna_registry[("it_irit", ti, pair[0], pair[1])] = frozenset({"i", "r"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.2",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'upadeSejanunAsika it',
    text_dev       = 'उपदेशेऽजनुनासिक इत्',
    padaccheda_dev = "उपदेशे अज् अनुनासिकः इत्",
    why_dev        = "उपदेशावस्थायाम् अज् वर्णः अनुनासिकः चेद् इत्-संज्ञकः; "
                     "इँर्-वार्तिके पुनः द्वयोः संयुक्तः इत्। लोपः १.३.९।",
    anuvritti_from = ("1.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
register_candidate_tag(TAG_ANUNASIKA, SUTRA.sutra_id)
register_candidate_tag(TAG_IRIT, SUTRA.sutra_id + "-vārttika")
