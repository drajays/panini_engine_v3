"""
5.1.19  आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51019):** *prāg-ārhīya ṭhag-adhikāraḥ*
— scope through **5.1.63** (तद् अर्हति), matching v2
``adhikara_prakarana.json`` sequence **40**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _legacy_cond(state: State) -> bool:
    return not any(e.get("id") == "5.1.19" for e in state.adhikara_stack)


def _legacy_act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.1.19",
        "scope_end" : "5.1.63",
        "text_dev"  : 'आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्',
    })
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
    t = default_site(state, "5.1.18", _ARHIYA)
    if t is None or any(f"lex:{x}" in t.tags for x in ("gopucCAdi", "saMKyA", "parimARa")):      # gopucchādi, saṃkhyā and parimāṇa keep the ṭhañ of 5.1.18
        return None
    return "Wak"


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.1.19")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.19", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.19"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id       = "5.1.19",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'ArhAdagopucCasaMKyAparimARAwWak',
    text_dev       = 'आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्',
    samagra_slp1   = "A-arhAt prAg vateH a-gopucCa-saMKyA-parimARAt Wak",
    samagra_dev    = "आ-अर्हात् प्राग् वतेः अ-गोपुच्छ-संख्या-परिमाणात् ठक्",
    padaccheda_dev = "आ / अर्हात् / अ-गोपुच्छ-संख्या-परिमाणात् / ठक्",
    why_dev        = "प्रागार्हीयः ठगधिकारः — ५.१.१९ तः ५.१.६३ पर्यन्तम्।",
    anuvritti_from = (),
    apavada_of     = ('5.1.18',),
    also_vidhi     = True,          # the loop attaches this default / opens this sense-frame from the speaker's taddhitArtha
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.1.19", "5.1.63"),
)

register_sutra(SUTRA)

