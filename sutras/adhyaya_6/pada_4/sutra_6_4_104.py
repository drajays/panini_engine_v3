"""
6.4.104  चिणो लुक्  —  VIDHI

Padaccheda: चिणः लुक्

Sources consulted:
- ashtadhyayi.com data.txt row i=64104 (siddhārtha: चिणः लुक्)
- Kāśikā: "अकारि, अहारि, अलावि, अपाचि"
- Cross-validation: Vidyut / ashtadhyayi.com karmaṇi luṅ 3sg अभावि, अपाचि;
  regression test tests/unit/test_upadesha_inputs.py

What follows चिण् (3.1.66) — the tiṅ त — is deleted by luk. The term stays on
the tape with no varṇas so that, by 1.1.62 प्रत्ययलोपे प्रत्ययलक्षणम्, the
word is still tiṅanta for 1.4.14; 1.1.63 न लुमताङ्गस्य keeps the deleted त
from conditioning aṅgakārya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if (t.meta.get("upadesha_slp1") or "").strip() != "ciR":
            continue
        nxt = state.terms[i + 1]
        if nxt.kind == "pratyaya" and nxt.varnas:
            return i + 1
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    j = _site(state)
    if j is None:
        return state
    t = state.terms[j]
    t.varnas = []
    t.tags.add("luk")
    t.meta["luk_6_4_104"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.104",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ciRo luk",
    text_dev       = "चिणो लुक्",
    samagra_slp1   = "ciRaH luk",
    samagra_dev    = "चिणः लुक्",
    padaccheda_dev = "चिणः लुक्",
    why_dev        = "चिणः परस्य तशब्दस्य लुक् (अभावि, अपाचि)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
