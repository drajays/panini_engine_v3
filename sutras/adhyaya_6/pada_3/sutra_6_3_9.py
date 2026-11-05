"""
6.3.9  हलदन्तात् सप्तम्याः संज्ञायाम्  —  VIDHI

Padaccheda: हल्-अत्-अन्तात् सप्तम्याः संज्ञायाम्

हलदन्तात् सप्तम्याः संज्ञायाम् (6.3.9)
Pāṭha: ashtadhyayi.com data.txt row i=63009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from engine.vivaksha import vivaksita

_GATE_KEY: str = "6_3_9_haladantAt_9"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.9", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.9"
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


_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")


def _site(state: State):
    """हलदन्तात् सप्तम्याः संज्ञायाम्: a hal-final or a-final pūrvapada keeps its saptamī sup when the compound is a name (kaṇṭhekālaḥ, yudhiṣṭhiraḥ, vanekiṃśukāḥ)."""
    if not vivaksita(state, "arthaViSeSa", "saMjYA"):
        return None
    return _alug_sup(state, "vib_saptami", lambda t: bool(t.varnas) and (t.varnas[-1].slp1 in _HAL or t.varnas[-1].slp1 == "a"))


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _legacy_act(state)
    s.tags.add("alug")                     # the sup stays (alug): 2.4.71's luk does not take it
    s.meta["alug"] = "6.3.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "haladantAt saptamyAH saMjYAyAm",
    text_dev              = "हलदन्तात् सप्तम्याः संज्ञायाम्",
    samagra_slp1          = "alug uttarapade haladantAt saptamyAH saMjYAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे हलदन्तात् सप्तम्याः संज्ञायाम्",
    padaccheda_dev        = "हल्-अत्-अन्तात् सप्तम्याः संज्ञायाम्",
    why_dev               = 'संज्ञायां हलन्ताद् अदन्ताच्च परस्याः सप्तम्याः उत्तरपदे अलुक् — कण्ठेकालः, युधिष्ठिरः, वनेकिंशुकाः।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
