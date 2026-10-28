"""
5.1.39  गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्  —  VIDHI

Padaccheda: गो-द्वि-अचः अ-संख्या-परिमाण-अश्व-आदेः यत्

गोद्व्यचोरसंख्यापरिमाणाश्वादेर्यत् (5.1.39)
Pāṭha: ashtadhyayi.com data.txt row i=51039 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_39_godvyacora_39"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.39", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.39"
    return state


from engine.taddhita_attach import arhiya_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine import gana


_AC = "aAiIuUfFxXeEoO"


def _attach(state: State):
    t = arhiya_site(state, "5.1.38", lacks=("saMKyA", "parimARa"))
    if t is None:
        return None
    flat = "".join(v.slp1 for v in t.varnas)
    name = t.meta.get("upadesha_slp1") or flat
    dvyac = sum(c in _AC for c in flat) == 2
    return "yat" if (name == "go" or dvyac) and not gana.in_gana("aSvAdiH#5.1.39", name) else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.39")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.39", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.39"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'godvyacosaMKyAparimARASvAderyat',
    text_dev              = 'गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्',
    samagra_slp1          = "tasya nimittaM saMyogotpAtO iti go-dvyacaH asaMKyA-parimARa-aSvAdeH yat",
    samagra_dev           = "'तस्य निमित्तं संयोगोत्पातौ' इति गो-द्व्यचः असंख्या-परिमाण-अश्वादेः यत्",
    padaccheda_dev        = "गो-द्वि-अचः अ-संख्या-परिमाण-अश्व-आदेः यत्",
    why_dev               = "(सूत्रम् 5.1.39) गोद्व्यचोरसंख्यापरिमाणाश्वादेर्यत्।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
