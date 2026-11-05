"""
6.4.127  अर्वणस्त्रसावनञः  —  VIDHI

Padaccheda: अर्वणः तृ (लुप्तप्रथमान्तनिर्देशः) अ-सौ अन्-अञः

अर्वणस्त्रसावनञः (6.4.127)
Pāṭha: ashtadhyayi.com data.txt row i=64127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_4_127_arvaRastra_127"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.127", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.127"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _live_before(state: State, i: int):
    """The Term with sounds right before ``i``."""
    return next((state.terms[k] for k in range(i - 1, -1, -1) if state.terms[k].varnas), None)

_SU = frozenset({"vib_prathama", "vac_eka"})      # su


def _tr_site(state: State, stem: str, *, asu: bool):
    for i, t in enumerate(state.terms[:-1]):
        if "anga" not in t.tags or _flat(t) != stem or t.meta.get("6_4_127_tr_done") or not adhikara_in_effect("6.4.127", state, "6.4.1"):
            continue
        nxt = state.terms[i + 1]
        if "sup" not in nxt.tags and "pratyaya" not in nxt.tags:
            continue
        if asu and _SU <= nxt.tags:
            continue                       # asau: not before su (arvā)
        if asu:
            before = _live_before(state, i)
            if before is not None and (before.meta.get("upadesha_slp1") or "") == "naY":
                continue                   # anañaḥ: anarvāṇau
        return t
    return None


def _tr_act(t) -> None:
    """tṛ replaces the final n (1.1.52); its ṛ is an it (the ugit that 7.1.70 reads: arvantau), so t stands in the aṅga."""
    t.varnas[-1] = mk("t")
    t.tags.add("origin_it:f")
    t.meta["6_4_127_tr_done"] = True


def _site(state: State):
    """अर्वणस्त्रसावनञः: arvan takes tṛ in place of its n, except before su and after nañ (arvantau, arvataḥ, arvadbhyām; arvā; anarvāṇau)."""
    return _tr_site(state, "arvan", asu=True)


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    _tr_act(t)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arvaRastrasAvanaYaH",
    text_dev              = "अर्वणस्त्रसावनञः",
    samagra_slp1          = "aNgasya asidDavadatrABAt arvaRaH tf asO anaYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् अर्वणः तृ असौ अनञः",
    padaccheda_dev        = "अर्वणः तृ (लुप्तप्रथमान्तनिर्देशः) अ-सौ अन्-अञः",
    why_dev               = 'अर्वन्नित्यङ्गस्य तृ-आदेशः (नकारस्थाने), सौ नञः परस्य च न — अर्वन्तौ, अर्वतः; अर्वा, अनर्वाणौ।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
