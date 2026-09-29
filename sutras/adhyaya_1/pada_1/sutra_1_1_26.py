"""
1.1.26  क्तक्तवतू निष्ठा  —  SAMJNA

Operational role (v3.6, demos):
  - Tag kṛt-pratyayas `kta` and `ktavatu~` as `nistha`.

This is used as a clear glass-box marker in demo prakriyās (e.g. उक्तः / उक्तवान्),
but downstream rules in v3 typically key off `krt` / it-markers rather than
paradigm coordinates.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


_TARGETS = frozenset({"kta", "ktavatu"})


def _eligible(state: State):
    for t in state.terms:
        if t.kind != "pratyaya" or "krt" not in t.tags:
            continue
        if t.meta.get("upadesha_slp1") not in _TARGETS:
            continue
        if "nistha" in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.add("nistha")
    state.samjna_registry["1.1.26_nistha"] = frozenset(_TARGETS)
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.26",
    sutra_type=SutraType.SAMJNA,
    text_slp1='ktaktavatU nizWA',
    text_dev='क्तक्तवतू निष्ठा',
    padaccheda_dev="क्त-क्तवतु निष्ठा",
    why_dev="क्त/क्तवतु-प्रत्यययोः निष्ठा-संज्ञा।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

