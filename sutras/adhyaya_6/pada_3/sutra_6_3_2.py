"""
6.3.2  पञ्चम्याः स्तोकादिभ्यः  —  VIDHI

Padaccheda: पञ्चम्याः स्तोक-आदिभ्यः

पञ्चम्याः स्तोकादिभ्यः (6.3.2)
Pāṭha: ashtadhyayi.com data.txt row i=63002 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_2_paYcamyAH_2"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.2", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.2"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _alug_sup(state: State, vib: str, ok):
    """A samāsa tape: the pūrvapada stem (``samasa_purvapada``), its sup still on the tape (not yet luk-ed by 2.4.71), then the uttarapada.
    Returns the sup Term when ``ok(stem Term)`` holds and the sup carries the vibhakti saṃjñā ``vib``."""
    for i, t in enumerate(state.terms[:-2]):
        s = state.terms[i + 1]
        if "samasa_purvapada" not in t.tags or "sup" not in s.tags or vib not in s.tags or not s.varnas or s.meta.get("alug"):
            continue
        if any(u.varnas and "sup" not in u.tags for u in state.terms[i + 2:]) and ok(t):
            return s
    return None


# SHORTCUT S111: the stokādi list is the Kāśikā's (stoka, alpa; antika, abhyāśa; dūra, viprakṛṣṭa; kṛcchra) — the Gaṇapāṭha file has no stokādi entry
_STOKADI = frozenset({"stoka", "alpa", "antika", "aByASa", "dUra", "viprakfzwa", "kfcCra"})


def _site(state: State):
    """पञ्चम्याः स्तोकादिभ्यः: a stokādi pūrvapada keeps its pañcamī sup in the samāsa (stokānmuktaḥ, antikādāgataḥ, dūrādāgataḥ)."""
    return _alug_sup(state, "vib_panchami", lambda t: _flat(t) in _STOKADI)


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _legacy_act(state)
    s.tags.add("alug")                     # the sup stays (alug): 2.4.71's luk does not take it
    s.meta["alug"] = "6.3.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamyAH stokAdiByaH",
    text_dev              = "पञ्चम्याः स्तोकादिभ्यः",
    samagra_slp1          = "alug uttarapade paYcamyAH stokAdiByaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे पञ्चम्याः स्तोकादिभ्यः",
    padaccheda_dev        = "पञ्चम्याः स्तोक-आदिभ्यः",
    why_dev               = 'स्तोकादिभ्यः परस्याः पञ्चम्याः उत्तरपदे अलुक् — स्तोकान्मुक्तः, अन्तिकादागतः, दूरादागतः।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
