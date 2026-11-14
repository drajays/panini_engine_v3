"""
8.4.68  अ अ  —  ANUVADA

Padaccheda: अ · अ · इति

Mahābhāṣya: vivṛta short *a* of the prakriyā is restored to saṃvṛta for prayoga
(*akārasya vivṛtasya saṃvṛtāpratyāpattiḥ*). Surface SLP1 stays ``a``; the varṇa is
tagged ``samvrta``. Fires once at the end of the tripāḍī (gate), whenever the
derivation has reached that stratum.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84068 · अ अ इति
              padaccheda: अ · अ · इति
  Source #2 — Kāśikā 8.4.68 udāharaṇa:
                अअ
                अआ
                आअ
  Cross-check — surface pinned by: tests/constitutional/test_astadhyayi_kram_respected.py, tests/test_bhavati_glassbox.py, tests/unit/test_autonomous_vs_recipe.py
  Reference record: sutra_ref_out/8_4_68.json
  Concept: Pushpa Dixit C-053 (ābhyantara prayatna; hrasva a saṃvṛta in prayoga).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_68_a_68"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.68", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]         = "8.4.68"
    n = 0
    for t in state.terms:
        for v in t.varnas:
            if v.slp1 == "a" and "samvrta" not in v.tags:
                v.tags.add("samvrta")
                n += 1
    state.meta["__why_now_dev__"] = (
        "प्रक्रियायां विवृतः ह्रस्वः अकारः प्रयोगे संवृतः भवति (अ अ इति)।"
        + (f" संवृत-वर्णाः: {n}।" if n else "")
    )
    return state


SUTRA = SutraRecord(
    sutra_id                = "8.4.68",
    sutra_type              = SutraType.ANUVADA,
    r1_form_identity_exempt = True,
    text_slp1               = 'a a',
    text_dev                = 'अ अ',
    samagra_slp1            = "a a",
    samagra_dev             = "अ अ",
    padaccheda_dev          = "अ · अ · इति",
    why_dev                 = "प्रक्रियायां विवृतः ह्रस्वः अकारः प्रयोगे संवृतः (अ अ इति)।",
    anuvritti_from          = ('8.1.1',),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)
