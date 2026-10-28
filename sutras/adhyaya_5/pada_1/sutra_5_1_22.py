"""
5.1.22  संख्याया अतिशदन्तायाः कन्  —  VIDHI

Padaccheda: संख्याया अ-ति-शत्-अन्तायाः कन्

संख्याया अतिशदन्तायाः कन् (5.1.22)
Pāṭha: ashtadhyayi.com data.txt row i=51022 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_22_saMKyAyA_22"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.22", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.22"
    return state


from engine.taddhita_attach import frame_in, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
from engine.luk import live_taddhita, take_away

_ARHIYA = ("5.1.37", "5.1.63")     # the senses of the ārhīya group (tena krītam … tadarhati), where 5.1.18's ṭhañ gives way to 5.1.19's ṭhak
_FROM = ("5.1.18", "5.1.19", "5.1.20", "5.1.21", "5.1.22", "5.1.23", "5.1.24", "5.1.25", "5.1.26", "5.1.27")     # the ārhīya pratyayas that 5.1.28 – 31 take away


def _ok(state: State) -> bool:
    return frame_in(state, "5.1.18", _ARHIYA)


def _tsite(state: State, **kw):
    return taddhita_site(state, None, ok=_ok(state), **kw)


def _compound(state: State, last: tuple[str, ...], *tags: str):
    """S27: the saṃkhyāpūrva / dvigu stem is a flat lexical item carrying the caller's tag; tadantavidhi is read off its final letters."""
    t = _tsite(state, tag=tags[0], final=lambda f: f.endswith(last))
    return t if t is not None and all(f"lex:{x}" in t.tags for x in tags) else None


def _attach(state: State):
    # atiśadantāyāḥ: not a saṃkhyā ending in ti or śat — the arthavat ti only (kati, a ḍati, is not excluded)
    t = _tsite(state, tag="saMKyA", final=lambda f: not ((f.endswith("ti") and f != "kati") or f.endswith("Sat")))
    return "kan" if t is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.22")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.22", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.22"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.1.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyAyA atiSadantAyAH kan",
    text_dev              = "संख्याया अतिशदन्तायाः कन्",
    samagra_slp1          = "A-arhAt saNKyAyAH a-ti-Sad-antAyAH kan",
    samagra_dev           = "आ-अर्हात् सङ्ख्यायाः अ-ति-शद्-अन्तायाः कन्",
    padaccheda_dev        = "संख्याया अ-ति-शत्-अन्तायाः कन्",
    why_dev               = "(सूत्रम् 5.1.22) संख्याया अतिशदन्तायाः कन्।",
    anuvritti_from        = ('5.1.19',),
    apavada_of     = ('5.1.18', '5.1.19'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
