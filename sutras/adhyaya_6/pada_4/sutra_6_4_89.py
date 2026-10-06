"""
6.4.89  ऊदुपधाया गोहः  —  VIDHI

The upadhā u of गुहू (guh) becomes ū before an ac-initial affix — गूहति, गूहते, जुगूह, अगूहीत् (KV 6.4.89; Vidyut agrees). The long ū is not laghu,
so 7.3.86's laghūpadha guṇa has no site (apavāda).
Source: ashtadhyayi.com data row 64089 (anuvṛtti: अङ्गस्य, अचि).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("6_4_89_done"):
            continue
        if (dh.meta.get("upadesha_slp1") or "").strip() != "guhU~":
            continue
        vs = dh.varnas
        j = next((k for k, v in enumerate(vs) if "aT_agama_v" not in v.tags), 0)
        if len(vs) - j != 3 or vs[j + 1].slp1 != "u":
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or nxt.varnas[0].slp1 not in _AC or "kngiti" in nxt.tags:
            continue        # not before a kit/ṅit ending: जुगुहतुः (KV/Vidyut); गूहति has śap, गूहते
        if "upadesha" in nxt.tags and not nxt.meta.get("it_lopa_done"):
            continue        # its it-letters are still on it (Sap): wait for 1.3.2–9
        return dh, j + 1
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is not None:
        dh, k = hit
        dh.varnas[k] = mk("U", *dh.varnas[k].tags)
        dh.meta["6_4_89_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.89",
    sutra_type=SutraType.VIDHI,
    text_slp1="UdupaDAyA gohaH",
    text_dev="ऊदुपधाया गोहः",
    padaccheda_dev="ऊत् उपधायाः गोहः",
    why_dev="गुहू-धातोः उपधा-उकारस्य अजादौ प्रत्यये ऊकारः (गूहति)।",
    anuvritti_from=("6.4.1",),
    apavada_of=("7.3.84", "7.3.86"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
