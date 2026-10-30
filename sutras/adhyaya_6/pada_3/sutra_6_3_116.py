"""
6.3.116  नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ  —  VIDHI

Padaccheda: नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ

नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ (6.3.116)
Pāṭha: ashtadhyayi.com data.txt row i=63116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_116_nahivftivf_116"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.116", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.116"
    return state



# the seven dhātus of the sūtra (nahi, vṛti, vṛṣi, vyadhi, ruci, sahi, tani) by upadeśa; the kvip is the pratyaya they end in
_DHATU = frozenset({"Raha~", "vftu~", "vfzu~", "vyaDa~", "ruca~", "zaha~", "tanu~"})
_LONG = {"a": "A", "i": "I", "u": "U", "f": "F"}


def _kvip_present(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "") == "kvip" or "origin_pratyaya:kvip" in t.tags for t in state.terms)


def _site(state: State):
    """The pūrvapada Term (upasarga / upapada) standing right before one of the seven dhātus, the kvip being the uttarapada's pratyaya."""
    if not _kvip_present(state):
        return None
    for i in range(len(state.terms) - 1):
        t, d = state.terms[i], state.terms[i + 1]
        if "dhatu" in t.tags or t.kind == "pratyaya" or not t.varnas or t.meta.get("6_3_116_done"):
            continue
        if "dhatu" in d.tags and (d.meta.get("upadesha_slp1") or "") in _DHATU and t.varnas[-1].slp1 in _LONG:
            return t
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    t.varnas[-1] = mk(_LONG[t.varnas[-1].slp1])
    t.meta["6_3_116_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nahivftivfzivyaDirucisahitanizu kvO",
    text_dev              = "नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ",
    samagra_slp1          = "uttarapade saMhitAyAm nahi-vfti-vfzi-vyaDi-ruci-sahi-tanizu kvO dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ दीर्घः",
    padaccheda_dev        = "नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ",
    why_dev               = "नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्विबन्तेषु उत्तरपदेषु पूर्वपदस्य दीर्घः (उपानत्, नीरुक्, प्रावृट्)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
