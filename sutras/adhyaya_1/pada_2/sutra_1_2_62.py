"""
1.2.62  विशाखयोश्च  —  VIDHI (SAMJNA gate)

*Padaccheda:* **विशाखयोः** / **च**

And for "viśākhā" — another nakṣatra pair — the same plural/dual
treatment applies (anuvritti of the ekaśeṣa/bahuvacanam rule from
1.2.60).  The particle "ca" (and) draws in the earlier rule by
continuation.

Operational role (v3):
  - Registers the gate ``1_2_62_viSAkhayoH`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when applying plural/ekaśeṣa
    treatment to the nakṣatra name "viśākhā".

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
Pāṭha: ashtadhyayi.com data.txt row i=12062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import accent_paribhasha_gate_eligible

_GATE_KEY = "1_2_62_viSAkhayoH"


def cond(state: State) -> bool:
    return accent_paribhasha_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.62",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = 'viSAKayoSca',
    text_dev                = 'विशाखयोश्च',
    samagra_slp1            = "viSAKayoH ca anyatarasyAm nakzatre Candasi ekavacanam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev             = "विशाखयोः च अन्यतरस्याम् नक्षत्रे छन्दसि एकवचनम्",
    padaccheda_dev          = "विशाखयोः / च",
    why_dev                 = (
        "विशाखा-नक्षत्रयुगलस्यापि एकशेष-बहुवचन-विधिः अनुवर्तते — "
        "च-शब्देन फल्गुनी-प्रोष्ठपदयोः समं विशाखयोरपि ग्रहणम्।"
    ),
    anuvritti_from          = ("1.2.60",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
