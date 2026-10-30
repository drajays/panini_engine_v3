"""
6.4.161  र ऋतो हलादेर्लघोः  —  VIDHI

Padaccheda: रः ऋतः हल्-आदेः लघोः

र ऋतो हलादेर्लघोः (6.4.161)
Pāṭha: ashtadhyayi.com data.txt row i=64161 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_161_ra_161"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.161", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.161"
    return state


from engine.state import State
from phonology import mk

# SHORTCUT S86: the parigaṇana of the Kāśikā (पृथुं मृदुं भृशं चैव कृशं च दृढमेव च । परिपूर्वं वृढं चैव षडेतान् रविधौ स्मरेत्) as a set of the residues the aṅga has
# when the ṭi of 6.4.155 – 159 is gone; replacement: a gaṇa lookup of the six original stems.
_RES = frozenset(['pfT', 'mfd', 'BfS', 'kfS', 'dfQ', 'vfQ', 'pfTu', 'mfdu', 'BfSa', 'kfSa', 'dfQa', 'vfQa', 'parivfQa'])


def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        n = state.terms[i + 1]
        up = (n.meta.get("upadesha_slp1") or "").strip()
        flat = "".join(v.slp1 for v in t.varnas)
        if (flat in _RES and "anga" in t.tags and not t.meta.get("6_4_161_done") and n.kind == "pratyaya"
                and up.startswith(("izW", "iman", "Iyas"))):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    j = next(j for j, v in enumerate(t.varnas) if v.slp1 == "f")
    t.varnas[j:j + 1] = [mk("r"), mk("a")]  # पृथु → प्रथ् (प्रथिष्ठः): ṛ → ra for a hal-initial laghu aṅga
    t.meta["6_4_161_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.161",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ra fto halAderlaGoH",
    text_dev              = "र ऋतो हलादेर्लघोः",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya raH ftaH halAdeH laGoH izWa-iman-Iyassu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य रः ऋतः हलादेः लघोः इष्ठ-इमन्-ईयस्सु",
    padaccheda_dev        = "रः ऋतः हल्-आदेः लघोः",
    why_dev               = "हलादेः लघोः ऋकारस्य इष्ठ-इमन्-ईयस्सु रः — प्रथिष्ठः, प्रथिमा, प्रथीयान्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
