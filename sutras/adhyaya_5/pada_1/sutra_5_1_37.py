"""
5.1.37  तेन क्रीतम्  —  SAMJNA (narrow ``prakriya_43``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51037):** *tena krītam* — ``Ra`` (*ṭak*) after a stem in the sense
‘bought with / by means of that’.

Narrow v3 (**पञ्चशष्कुलम्** ``…/separated_prakriyas/prakriya_43_*.json`` ``panini_engine_pipeline``):
  • **4.1.76** *taddhita* *adhikāra* on ``adhikara_stack``.
  • ``prakriya_43_5_1_37_arm`` + ``meta['prakriya_43_tena_krItam_note']`` +
    witness ``Term`` tagged ``prakriya_43_paYcaSazkulam_demo`` →
    ``samjna_registry['5.1.37_tena_krItam_prakriya_43']``.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _taddhita_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    if not _taddhita_adhikara_open(state):
        return False
    note_ok = bool(state.meta.get("prakriya_43_tena_krItam_note")) or bool(
        state.meta.get("prakriya_P011_tena_krItam_note")
    )
    if not note_ok:
        return False
    if not state.terms:
        return False
    if not any(
        ("prakriya_43_paYcaSazkulam_demo" in t.tags) or ("prakriya_P011_paYcagoRiH_demo" in t.tags)
        for t in state.terms
    ):
        return False
    if state.samjna_registry.get("5.1.37_tena_krItam_prakriya_43"):
        return False
    return True


def _legacy_cond(state: State) -> bool:
    return _site(state)


def _legacy_act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["5.1.37_tena_krItam_prakriya_43"] = True
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


def _sense(state: State):
    if not stem_ends_tape(state):
        return None
    return True if vivaksita(state, "taddhitArtha", "krIta") and not any(e.get("id") == "5.1.37" for e in state.adhikara_stack) else None


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _sense(state) is not None:
        return open_default_frame(state, "5.1.37", "krIta", "5.1.18", "5.1.114")      # tena krītam: ṭhañ (5.1.18) is the default to 5.1.114, ṭhak (5.1.19) to 5.1.63
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id="5.1.37",
    sutra_type=SutraType.VIDHI,
    text_slp1="tena krItam",
    text_dev="तेन क्रीतम्",
    samagra_slp1="tena krItam iti samarTAnAm praTamAt paraH WaY pratyayaH",
    samagra_dev="'तेन क्रीतम्' (इति) समर्थानाम् प्रथमात् परः ठञ् प्रत्ययः",
    padaccheda_dev="तेन क्रीतम्",
    why_dev="तेन क्रीतम् इत्यर्थे ठक्-प्रत्ययः (*prakriya_43*, **पञ्चशष्कुलम्**)।",
    anuvritti_from=(),
    also_vidhi     = True,          # the loop attaches this default / opens this sense-frame from the speaker's taddhitArtha
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
