"""
5.4.91  राजाहःसखिभ्यष्टच्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=54091
- Kāśikā: "राजः, अह्नः, सखः।" (समासान्त टच्)
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (विबुधसखः)

राजन्/अहन्/सखि-final samāsa takes **टच्**. Then **6.4.148** drops सखि's इ.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "5_4_91_rAjAhassa_91"
_TAILS = ("saKi", "sakhi", "rAjan", "ahan", "ahan")


def _sakhi_or_rajan_ahan(state: State) -> bool:
    for t in reversed(state.terms):
        if not t.varnas:
            continue
        flat = "".join(v.slp1 for v in t.varnas)
        if any(flat.endswith(tail) for tail in ("saKi", "rAjan", "ahan")):
            return True
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"saKi", "saki", "rAjan", "ahan"}:
            return True
    return False


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any(e.get("id") == "5.4.68" for e in state.adhikara_stack):
        return False      # inside the loop (5.4.68 open) the new site above decides; the legacy recipe states its compound without it
    if any((t.meta.get("upadesha_slp1") or "").strip() == "wac" for t in state.terms):
        return False
    if not _sakhi_or_rajan_ahan(state):
        return False
    return True


def _legacy_act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("wac")),
        tags={"pratyaya", "taddhita", "upadesha", "samasanta"},
        meta={"upadesha_slp1": "wac", "it_markers": {"w", "c"}},
    )
    state.terms.append(pr)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["taddhita_kind"] = "5.4.91"
    return state


import re
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_RX = re.compile(r"[a-zA-Z]+(saKi|rAjan|ahan)$")      # SHORTCUT S62: the compound is one Term (S30 / S36); its kind and its last member are read off the lex: tags and the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.91", state, "5.4.68") or False:
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: _RX.search(f) is not None)
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('tatpuruza',)):
        return None
    return 'wac'


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.91")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.91", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.4.91"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].tags.add("samasanta")
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.91",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'rAjAhassaKiByazwac',
    text_dev              = 'राजाहस्सखिभ्यष्टच्',
    samagra_slp1          = "tatpuruzasya rAjA-ahan-saKiByaH wac",
    samagra_dev           = "तत्पुरुषस्य राजा-अहन्-सखिभ्यः टच्",
    padaccheda_dev        = "राज-अहः-सखिभ्यः टच्",
    why_dev               = "राजन्-अहन्-सखि-अन्ते समासे टच् (विबुधसखः)।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
