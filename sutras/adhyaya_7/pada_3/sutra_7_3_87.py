"""
7.3.87  नाभ्यस्तस्याचि पिति सार्वधातुके  —  VIDHI

Padaccheda: न अभ्यस्तस्य अचि पिति सार्वधातुके

नाभ्यस्तस्याचि पिति सार्वधातुके (7.3.87)
Pāṭha: ashtadhyayi.com data.txt row i=73087 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.declension import vowel_initial

_BLOCKS = ("7.3.86",)      # pugantalaghūpadhasya ca; 7.3.84 credits the laghūpadha guṇa too (ponytail there), so the aṅga is marked: ``7_3_87_barred``


def _site(state: State):
    """An abhyasta aṅga (abhyāsa + dhātu) before an ac-initial pit sārvadhātuka (the āṭ of the loṭ uttama is part of it, 1.1.46: nij + āni)."""
    if not adhikara_in_effect("7.3.87", state, "6.4.1"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or i == 0 or "abhyasa" not in state.terms[i - 1].tags or t.meta.get("7_3_87_barred"):
            continue
        rest = state.terms[i + 1:]
        tin = next((u for u in rest if "agama" not in u.tags), None)
        if tin is not None and vowel_initial(rest[0]) \
                and "it:pit" in tin.tags and any(g.startswith("sarvadhatuka") for g in tin.tags):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).meta["7_3_87_barred"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.87",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nAByastasyAci piti sArvaDAtuke",
    text_dev              = "नाभ्यस्तस्याचि पिति सार्वधातुके",
    samagra_slp1          = "aNgasya na aByastasya aci piti sArvaDAtuke guRaH pugantalaGUpaDasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न अभ्यस्तस्य अचि पिति सार्वधातुके गुणः पुगन्तलघूपधस्य",
    padaccheda_dev        = "न अभ्यस्तस्य अचि पिति सार्वधातुके",
    why_dev               = "नाभ्यस्तस्याचि पिति सार्वधातुके — लघूपधगुणः न (नेनिजानि)।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
