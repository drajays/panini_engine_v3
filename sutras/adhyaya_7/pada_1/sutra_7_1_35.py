"""
7.1.35  तुह्योस्तातङ्ङाशिष्यन्यतरस्याम्  —  VIBHASHA

Padaccheda: तु-ह्योः तातङ् आशिषि अन्यतरस्याम्   Anuvṛtti: अङ्गस्य 6.4.1

In the sense of a blessing (आशिषि), the loṭ ādeśas ``tu`` (3.4.86, तिप् → ति → तु) and ``hi`` (3.4.87,
सिप् → हि) are optionally replaced by ``tAta~N`` — तातँङ्, the अँ and the ङ् are both it (1.3.2, 1.3.3), so ``tāt`` remains: भवतु / भवतात्, भव / भवतात्.
Both readings are valid (अन्यतरस्याम्), so this is a VIBHASHA and every branch is an output.

The blessing sense is an *input*, like puruṣa and vacana: the dhātu carries the tag ``ashis`` (the caller
proposes it from the sentence; the engine does not read meaning). Without it the sūtra has nothing to do.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 71035 · तुह्योः तातङ् आशिषि अन्यतरस्याम्   anuvṛtti: 64001: अङ्गस्य
  Source #2 — Kāśikā 7.1.35 udāharaṇa:
                जीवताद् भवान्
                जीवतात् त्वम्
                जीवतु भवान्
                जीव त्वम्
  Source #3 — user-supplied prakriyā for भू (भूसत्तायाम्), 2026-10-03:
                भू+अ+तु → तातँङ् (७.१.३५) → भो+अ+तात् → भव्+अ+तात् → ताद् (८.२.३९) → तात् (८.४.५६)
                भू+अ+हि → तातँङ् (७.१.३५) → … भवतात् / भवताद्; the other branch: हि → 6.4.105 → भव
  Cross-check — tests/unit/test_sutra_7_1_35_tAtaN.py
  Reference record: sutra_ref_out/7_1_35.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.sthanivat import TING_PRATYAYATVA, adesha_substitute_varnas

_TU_HI = frozenset({"tu", "hi"})


def _site(state: State):
    if not any("dhatu" in t.tags and "ashis" in t.tags for t in state.terms):
        return None
    for t in state.terms:
        if t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags:
            continue
        if (t.meta.get("source_lakara_upadesha") or "").strip() != "loT":
            continue
        if t.meta.get("7_1_35_done"):
            continue
        if "".join(v.slp1 for v in t.varnas) in _TU_HI:
            return t
    return None


def cond(state: State) -> bool:
    return adhikara_in_effect("7.1.35", state, "6.4.1") and _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    adesha_substitute_varnas(t, "tAta~N", state, sutra_id="7.1.35", gunadharmas=frozenset({TING_PRATYAYATVA}))
    t.meta["7_1_35_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.35",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = True,       # the blessing reading is taken; vikalpa.choose({"7.1.35": False}) takes the other
    text_slp1             = 'tuhyostAtaNNASizyanyatarasyAm',
    text_dev              = 'तुह्योस्तातङ्ङाशिष्यन्यतरस्याम्',
    padaccheda_dev        = "तु-ह्योः तातङ् आशिषि अन्यतरस्याम्",
    why_dev               = "आशिषि लोटः तु-हि-स्थाने विकल्पेन तातङ् (भवतात्, भवताद्)।",
    anuvritti_from        = ('6.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
