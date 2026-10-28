"""
5.1.23  वतोरिड्वा  —  VIDHI

Padaccheda: वतोः इट् वा

वतोरिड्वा (5.1.23)
Pāṭha: ashtadhyayi.com data.txt row i=51023 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_23_vatoriqvA_23"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.23", state, "5.1.19"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.23"
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


from engine.state import Term
from phonology.varna import parse_slp1_upadesha_sequence


def _iw_site(state: State):
    i = live_taddhita(state, only_from=("5.1.22",), upadesha=("kan",))
    if i is None or i == 0 or state.meta.get("done:5.1.23") or not _ok(state):
        return None
    flat = "".join(v.slp1 for v in state.terms[i - 1].varnas)
    return i if flat.endswith("vat") else None                # vatu-ending saṃkhyā: tāvat, yāvat


def _new_cond(state: State) -> bool:
    return _iw_site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    i = _iw_site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.1.23"] = True
    if policy_pick(state, "5.1.23", 2) == 1:              # vā: no iṭ
        return state
    state.terms.insert(i, Term(kind="agama", varnas=list(parse_slp1_upadesha_sequence("iw")), tags={"agama", "upadesha"}, meta={"upadesha_slp1": "iw"}))
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vatoriqvA",
    text_dev              = "वतोरिड्वा",
    samagra_slp1          = "A-arhAt vatoH saMKyAyAH iw vA",
    samagra_dev           = "आ-अर्हात् वतोः संख्यायाः  इट्  वा",
    padaccheda_dev        = "वतोः इट् वा",
    why_dev               = "(सूत्रम् 5.1.23) वतोरिड्वा।",
    anuvritti_from        = ('5.1.19',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
