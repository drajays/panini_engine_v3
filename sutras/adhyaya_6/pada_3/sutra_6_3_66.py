"""
6.3.66  खित्यनव्ययस्य  —  VIDHI

Padaccheda: खिति अन्-अव्ययस्य

खित्यनव्ययस्य (6.3.66)
Pāṭha: ashtadhyayi.com data.txt row i=63066 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_66_Kityanavya_66"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.66", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.66"
    return state



_LONG = {"A": "a", "I": "i", "U": "u", "F": "f"}


def _khit_present(state: State) -> bool:
    """A khit pratyaya follows: khaś (3.2.28, 3.2.83 …), Kac …; the same reading as 6.3.67."""
    return any((t.meta.get("upadesha_slp1") or "").strip() in ("Kac", "Kas", "KaS") or t.meta.get("khit") is True or "K" in (t.meta.get("it_markers") or set())
               for t in state.terms)


def _site(state: State):
    """(Term, index of its long vowel) for an anavyaya upapada before a khit uttarapada; 6.3.67's mum may already stand after the vowel (kālim-)."""
    if not _khit_present(state):
        return None
    for t in state.terms:
        if "dhatu" in t.tags or t.kind == "pratyaya" or "avyaya" in t.tags or not t.varnas or t.meta.get("6_3_66_done"):
            continue
        j = len(t.varnas) - 1
        if t.varnas[j].slp1 == "m" and t.meta.get("6_3_67_mum_done") and j > 0:
            j -= 1
        if t.varnas[j].slp1 in _LONG:
            return t, j
        return None
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _legacy_act(state)
    t, j = s
    t.varnas[j] = mk(_LONG[t.varnas[j].slp1])
    t.meta["6_3_66_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Kityanavyayasya",
    text_dev              = "खित्यनव्ययस्य",
    samagra_slp1          = "uttarapade Kiti anavyayasya treH hrasvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे खिति अनव्ययस्य त्रेः ह्रस्वः",
    padaccheda_dev        = "खिति अन्-अव्ययस्य",
    why_dev               = "खित्-परे उत्तरपदे अनव्यय-पूर्वपदस्य ह्रस्वः (कालिम्मन्या, हरिणिम्मन्या; मुम् ६.३.६७ ह्रस्वं न बाधते)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
