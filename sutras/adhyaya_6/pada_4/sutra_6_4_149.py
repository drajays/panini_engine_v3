"""
6.4.149  सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः  —  VIDHI

Padaccheda: सूर्य-तिष्य-अगस्त्य-मत्स्यानाम् यः उपधायाः

सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः (6.4.149)
Pāṭha: ashtadhyayi.com data.txt row i=64149 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from engine.vartika import Vartika

_GATE_KEY: str = "6_4_149_sUryatizyA_149"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.149", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.149"
    return state


# Art. 25 / AMENDMENT 29: the vārttika of 6.4.149 lives here. Kātyāyana (Kāśikā 6.4.149): tiṣyapuṣyayor nakṣatrāṇi yalopa iti vācyam — the ya of the
# nakṣatra words tiṣya, puṣya goes before a taddhita (pauṣa, taiṣa). After 6.4.148 took the a, the ya stands last (pauṣya -> pauṣy -> pauṣ).
def _tp_site(state: State):
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if not ({"bha", "anga"} <= t.tags and {"taddhita", "pratyaya"} <= pr.tags) or t.meta.get("6_4_149_v3_done"):
            continue
        if t.meta.get("upadesha_slp1") in ("tizya", "puzya") and "lex:nakzatra" in t.tags and t.meta.get("6_4_148_lopa_done") \
                and t.varnas and t.varnas[-1].slp1 == "y":
            return t
    return None


def _tp_cond(state: State) -> bool:
    return _tp_site(state) is not None


def _tp_act(state: State) -> State:
    t = _tp_site(state)
    t.varnas.pop()
    t.meta["6_4_149_v3_done"] = True
    return state


VARTIKAS = (
    Vartika(id="6.4.149.v3", source="Kātyāyana vā. 3 on 6.4.149 (Kāśikā 6.4.149; Kaumudī)", tier="T1", relation="apavada",       # the host is gate-only here: its own cond holds, so the vārttika must displace its act
            text_dev="तिष्यपुष्ययोर्नक्षत्राणि यलोप इति वाच्यम्", cond=_tp_cond, act=_tp_act),
)

SUTRA = SutraRecord(
    sutra_id              = "6.4.149",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sUryatizyAgastyamatsyAnAM ya upaDAyAH",
    text_dev              = "सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya sUrya-tizya-agastya-matsyAnAm yaH upaDAyAH tadDite lopaH Iti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य सूर्य-तिष्य-अगस्त्य-मत्स्यानाम् यः उपधायाः तद्धिते लोपः ईति",
    padaccheda_dev        = "सूर्य-तिष्य-अगस्त्य-मत्स्यानाम् यः उपधायाः",
    why_dev               = "(सूत्रम् 6.4.149) सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः।",
    anuvritti_from        = ('6.1.1',),
    vartikas              = VARTIKAS,
    cond                 = cond,
    act                   = act,
)

register_sutra(SUTRA)
