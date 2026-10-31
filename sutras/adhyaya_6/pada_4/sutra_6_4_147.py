"""
6.4.147  ढे लोपोऽकद्र्वाः  —  VIDHI

Padaccheda: ढे लोपः अकद्र्वाः

ढे लोपोऽकद्र्वाः (6.4.147)
Pāṭha: ashtadhyayi.com data.txt row i=64147 (Art. 14).

Before a taddhita that begins with ḍh (upadeśa ḍhak, ḍhañ, ḍhakañ, ḍhrak …; its ḍh is already eya by 7.1.2, the pratyaya's own upadeśa still says ḍh), the final
uvarṇa of a bha aṅga is dropped instead of taking guṇa (apavāda of 6.4.146): jambū + ḍhañ -> jāmbeya, śītabāhu + ḍhañ -> śaitabāheya, mṛkaṇḍu + ḍhak -> mārkaṇḍeya.
Not for the word kadrū: kādraveya (6.4.146 guṇa, then avādeśa).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_147_Qe_147"


def _site(state: State):
    for ti in range(len(state.terms) - 1):
        anga, pr = state.terms[ti], state.terms[ti + 1]
        if not ({"anga", "bha"} <= anga.tags and {"taddhita", "pratyaya"} <= pr.tags) or anga.meta.get("6_4_147_lopa_done"):
            continue
        org = next((x.split(":", 1)[1] for x in pr.tags if x.startswith("origin_pratyaya:")), pr.meta.get("upadesha_slp1") or "")      # eya still remembers ḍh (7.1.2)
        if not org.startswith("Q") or not anga.varnas or anga.varnas[-1].slp1 not in ("u", "U"):
            continue
        if anga.meta.get("upadesha_slp1") == "kadrU":           # akadrvāḥ (the word as given: vṛddhi has already made it kAdrU)
            continue
        return ti
    return None


def cond(state: State) -> bool:
    return _site(state) is not None or samhita_gate_eligible(state, "6.4.147", gate_key=_GATE_KEY)


def act(state: State) -> State:
    ti = _site(state)
    if ti is None:
        state.paribhasha_gates[_GATE_KEY] = True
        state.samjna_registry[_GATE_KEY]  = True
        state.meta["anga_kind"]             = "6.4.147"
        return state
    state.terms[ti].varnas.pop()
    state.terms[ti].meta["6_4_147_lopa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'Qe lopokadrvAH',
    text_dev              = 'ढे लोपोऽकद्र्वाः',
    samagra_slp1          = "oH Basya aNgasya Qe tadDite lopaH akadrvAH",
    samagra_dev           = "ओः भस्य अङ्गस्य ढे तद्धिते लोपः अकद्र्वाः",
    padaccheda_dev        = "ढे लोपः अकद्र्वाः",
    why_dev               = "(सूत्रम् 6.4.147) ढे लोपोऽकद्र्वाः।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.146',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
