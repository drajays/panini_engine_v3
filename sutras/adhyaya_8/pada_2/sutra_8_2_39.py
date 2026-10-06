"""
8.2.39  झलां जशोऽन्ते  —  VIDHI

Padaccheda: झलाम् जशः अन्ते

At pāda-end (avasāna), jhal consonants become jaś. For asmad pañcami eka,
the final 't' of "mat" (mad+at after 7.2.90) → 'd' (giving mad).

झलां जशोऽन्ते (8.2.39)

Engine implementation:
  cond:
    • a Term tagged ``pada`` whose last varṇa is a jhal that has a jaś target
    • no ``8_2_39_done`` on the Term
  act:
    • replace that final varṇa by its antaratama jaś (sthāne 'ntaratamaḥ 1.1.50):
      the 3rd letter of its own varga, ṣ → ḍ, h → g, s → d, ś → j
    • record ``8_2_39_<old>_to_<new>`` in ``samjna_registry`` and write ``__why_now_dev__``

Rivals that take the varṇa first (so it never reaches this rule in Tripāḍī order,
and is excluded here when the rule is run on its own):
    c j (+ aspirates) → ku  8.2.30 coḥ kuḥ     ś → ṣ  8.2.36 vraśca…
    h → ḍh  8.2.31 ho ḍhaḥ                      s → ru 8.2.66 sasajuṣo ruḥ

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82039 · झलां जशोऽन्ते
              padaccheda: झलाम् जशः अन्ते
              anuvṛtti:   81016: पदस्य
              adhikāra:   8.2.1
  Source #2 — Kāśikā 8.2.39 udāharaṇa:
                वाक् → वाग् (k → g)
                श्वलिट् → श्वलिड् (ṭ → ḍ)
                अग्निचित् → अग्निचिद् (t → d)
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhavat_lang.py
  Reference record: sutra_ref_out/8_2_39.json
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence

# झल् → antaratama जश् (same sthāna and ābhyantara-prayatna), SLP1.
_JHAL_TO_JAS: dict = {
    "k": "g", "K": "g", "g": "g", "G": "g",
    "c": "j", "C": "j", "j": "j", "J": "j",
    "w": "q", "W": "q", "q": "q", "Q": "q",
    "t": "d", "T": "d", "d": "d", "D": "d",
    "p": "b", "P": "b", "b": "b", "B": "b",
    "S": "j",   # ś → j
    "z": "q",   # ṣ → ḍ   (ṣaṣ → ṣaḍ)
    "s": "d",   # s → d
    "h": "g",   # h → g
}

# Taken by another pada-final rule: 8.2.30 (cu→ku), 8.2.31 (h→Q), 8.2.36 (S→z), 8.2.66 (s→ru).
_OTHER_RULE_HAS_IT = frozenset("cCjJhSs")


def _find_target(state: State):
    for i, t in enumerate(state.terms):
        if "8_2_39_done" in t.tags:
            continue
        # Only apply to merged pada terms (post-merge, pūrvatrāsiddham zone)
        if "pada" not in t.tags:
            continue
        if not t.varnas:
            continue
        last = t.varnas[-1].slp1
        if last not in _JHAL_TO_JAS or last in _OTHER_RULE_HAS_IT:
            continue
        if _JHAL_TO_JAS[last] == last:
            continue  # already jaś
        return i
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    t = state.terms[i]
    old = t.varnas[-1].slp1
    new = _JHAL_TO_JAS[old]
    t.varnas[-1] = parse_slp1_upadesha_sequence(new)[0]
    t.tags.add("8_2_39_done")
    state.samjna_registry[f"8_2_39_{old}_to_{new}"] = True
    state.meta["__why_now_dev__"] = (
        f"पदान्त-झल् ({old}) स्थाने अन्तरतमः जश् ({new}); यथा वाक् → वाग्, षष् → षड्। (८.२.३९)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.39",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'JalAM jaSonte',
    text_dev              = 'झलां जशोऽन्ते',
    samagra_slp1          = "padasya ante JalAm jaSaH",
    samagra_dev           = "पदस्य अन्ते झलाम् जशः",
    padaccheda_dev        = "झलाम् जशः अन्ते",
    why_dev               = "पदान्ते झल्-व्यञ्जनस्य स्थाने जश्-व्यञ्जनः "
                            "(सूत्रम् ८.२.३९ झलां जशोऽन्ते) — यथा वाक् → वाग्, षष् → षड्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
