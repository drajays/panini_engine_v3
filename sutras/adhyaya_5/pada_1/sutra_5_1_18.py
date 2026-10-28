"""
5.1.18  प्राग्वतेष्ठञ्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51018):** *prāg-vatīya ṭhañ-adhikāraḥ*
— scope through **5.1.114** (आकालिकडाद्यन्तवचने), matching v2
``adhikara_prakarana.json`` sequence **39**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _legacy_cond(state: State) -> bool:
    return not any(e.get("id") == "5.1.18" for e in state.adhikara_stack)


def _legacy_act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.1.18",
        "scope_end" : "5.1.114",
        "text_dev"  : 'प्राग्वतेष्ठञ्',
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
    return "WaY" if default_site(state, "5.1.18") is not None else None


def _new_cond(state: State) -> bool:
    return default_site(state, "5.1.18") is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.1.18", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.1.18"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id       = "5.1.18",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'prAgvatezWaY',
    text_dev       = 'प्राग्वतेष्ठञ्',
    samagra_slp1   = "prAk vateH WaY",
    samagra_dev    = "प्राक् वतेः ठञ्",
    padaccheda_dev = "प्राक् / वतेः / ठञ्",
    why_dev        = "प्राग्वतीयः ठञधिकारः — ५.१.१८ तः ५.१.११४ पर्यन्तम्।",
    anuvritti_from = (),
    also_vidhi     = True,          # the loop attaches this default / opens this sense-frame from the speaker's taddhitArtha
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.1.18", "5.1.114"),
)

register_sutra(SUTRA)

