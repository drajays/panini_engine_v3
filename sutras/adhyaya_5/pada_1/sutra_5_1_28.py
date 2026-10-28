"""
5.1.28  अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्  —  SAMJNA (narrow ``prakriya_43``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51028):** *adhyardhapūrvadvigor lug saṃjñāyām* — *luk* of ``ṭak``
when the prior formation is a *dvigu* (under **संज्ञा**, not a proper-name reading).

Narrow v3 (**पञ्चशष्कुलम्** ``panini_engine_pipeline``): after **5.1.37** has registered *ṭak* intent,
``prakriya_43_5_1_28_arm`` + ``meta['prakriya_43_dvigu_Tak_luk_note']`` + witness ``prakriya_43_paYcaSazkulam_demo``
→ ``samjna_registry['5.1.28_advigu_Tak_luk_prakriya_43']``.

Requires ``samjna_registry['5.1.37_tena_krItam_prakriya_43']`` from **5.1.37** on the same spine.

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
    note_ok = bool(state.meta.get("prakriya_43_dvigu_Tak_luk_note")) or bool(
        state.meta.get("prakriya_P011_dvigu_Tak_luk_note")
    )
    if not note_ok:
        return False
    if not state.samjna_registry.get("5.1.37_tena_krItam_prakriya_43"):
        return False
    if not state.terms:
        return False
    if not any(
        ("prakriya_43_paYcaSazkulam_demo" in t.tags) or ("prakriya_P011_paYcagoRiH_demo" in t.tags)
        for t in state.terms
    ):
        return False
    if state.samjna_registry.get("5.1.28_advigu_Tak_luk_prakriya_43"):
        return False
    return True


def _legacy_cond(state: State) -> bool:
    return _site(state)


def _legacy_act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["5.1.28_advigu_Tak_luk_prakriya_43"] = True
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


def _luk_site(state: State):
    i = live_taddhita(state, only_from=_FROM)
    if i is None or i == 0 or not _ok(state) or not not vivaksita(state, "arthaViSeSa", "saMjYA"):
        return None
    t = state.terms[i - 1]
    flat = "".join(v.slp1 for v in t.varnas)
    if "lex:aDyarDapUrvadvigu" not in t.tags or flat.endswith(("kArzApaRa", "sahasra")) or ("lex:dvitripUrva" in t.tags and flat.endswith(("nizka", "bista"))):
        return None                    # 5.1.29 – 31 teach the vibhāṣā luk for these
    return i


def _new_cond(state: State) -> bool:
    return _luk_site(state) is not None and not state.meta.get("done:5.1.28")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    i = _luk_site(state) if _new_cond(state) else None
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.1.28"] = True
    if False and policy_pick(state, "5.1.28", 2) == 1:       # विभाषा: the pratyaya stays
        return state
    return take_away(state, i, "luk")


SUTRA = SutraRecord(
    sutra_id="5.1.28",
    sutra_type=SutraType.VIDHI,
    text_slp1='aDyarDapUrvadvigorlugasaMjYAyAm',
    text_dev='अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्',
    samagra_slp1="A arhAt aDyarDapUrva-dvigoH a-saMjYAyAm luk",
    samagra_dev="आ अर्हात् अध्यर्धपूर्व-द्विगोः असंज्ञायाम् लुक्",
    padaccheda_dev="अध्यर्ध-पूर्व-द्विगोः / लुक् / संज्ञायाम्",
    why_dev="द्विगोः परस्य ठकि लुक् (*saṃjñā*, *prakriya_43*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
