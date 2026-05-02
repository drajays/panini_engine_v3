"""
2.4.75  जुहोत्यादिभ्यः श्लुः  —  VIDHI (narrow: **P040** *juhoti*)

*Śāstra (laghu):* for *juhotyādi* (*hu* …), *śap* is replaced by *śluḥ* — the
*ślu*-named *pratyaya-lopa* of *śap*, which **6.1.10** *ślau* follows with *dhātu*
*dvi*tva (*dadāti*, *juhoti*, …).

Engine (recipe-armed only):
  - ``state.meta['P040_2_4_75_arm']``
  - witness *dhātu* ``Term`` tagged ``P040_juhotyadi`` with ``upadesha_slp1`` ``hu``,
    immediately followed by *tiṅ* ``ti`` (after **3.4.78** + *it*-*lopa*).
  - inserts a ``Slu`` *pratyaya* ``Term`` (``S`` + ``l`` + ``u`` in SLP1) tagged
    ``P040_slu_placeholder`` so the recipe can apply **1.1.60**/**1.1.61** and then
    remove the placeholder structurally (JSON ``hu+0+ti``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("P040_2_4_75_arm"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "P040_juhotyadi" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "hu":
            continue
        nxt = state.terms[i + 1]
        if nxt.kind != "pratyaya":
            continue
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        # After **3.4.78** + *it*-*lopa*, *upadeśa* id may remain ``tip`` while *varṇa*s are ``t``+``i``.
        if up not in {"ti", "tip"}:
            continue
        return i
    return None


def _already_has_slu(state: State) -> bool:
    return any("P040_slu_placeholder" in t.tags for t in state.terms)


def cond(state: State) -> bool:
    return _site(state) is not None and not _already_has_slu(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    slu = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Slu")),
        tags={"pratyaya", "upadesha", "P040_slu_placeholder"},
        meta={"upadesha_slp1": "Slu"},
    )
    state.terms.insert(i + 1, slu)
    state.meta.pop("P040_2_4_75_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.75",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "juhotyAdibhyaH SluH (narrow P040)",
    text_dev       = "जुहोत्यादिभ्यः श्लुः — P040 संक्षेपः",
    padaccheda_dev = "जुहोत्यादिभ्यः / श्लुः",
    why_dev        = "जुहोत्यादि-गणात् शप्-स्थाने श्लुः (२.४.७५) — P040।",
    anuvritti_from = ("2.4.58",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
