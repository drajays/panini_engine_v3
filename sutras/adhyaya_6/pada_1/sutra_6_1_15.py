"""
6.1.15  वचिस्वपियजादीनां किति  —  VIDHI

Operational role (v3.6, demo slice for `1145.md`):
  - When a dhātu is in the `vaci/svapi/yaji...` set and the following kṛt
    pratyaya is `kit`, mark the dhātu's YAN-varṇa (y/v/r/l) as a samprasāraṇa
    target for **1.1.45** to map by yathāsaṅkhya.

This file is a **trigger / scheduler** in our glass-box demos. It records the
target index in `state.meta` and is form-identity-exempt by design.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import YAN
from sutras.adhyaya_1.pada_1.sutra_1_1_45 import META_TARGETS


_DHATU_UPADESHA_SET = frozenset({"vac", "svap", "yaj"})


def _is_kit_pratyaya(pr) -> bool:
    markers = pr.meta.get("it_markers") or set()
    if "k" in markers or pr.meta.get("kit") is True:
        return True
    # *kitvat* on *san* (**1.2.8** ``kngiti``) licences **6.1.15** for *vac*+*san*.
    return "kngiti" in pr.tags and "sanadi" in pr.tags


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    # Demo frame: [dhatu, pratyaya]
    dh = next((t for t in state.terms if "dhatu" in t.tags), None)
    if dh is None:
        return None
    if dh.meta.get("upadesha_slp1") not in _DHATU_UPADESHA_SET:
        return None
    pr = state.terms[-1]
    if pr.kind != "pratyaya":
        return None
    if not _is_kit_pratyaya(pr):
        return None
    if dh.meta.get("6_1_15_samprasaran_armed"):
        return None
    for vi, v in enumerate(dh.varnas):
        if v.slp1 in YAN:
            return (state.terms.index(dh), vi)
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi = hit
    state.meta[META_TARGETS] = [(ti, vi)]
    state.terms[ti].meta["6_1_15_samprasaran_armed"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.15",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="vaci-svapi-yajAdInAM kiti",
    text_dev="वचिस्वपियजादीनां किति",
    padaccheda_dev="वचि-स्वपि-यज-आदीनाम् किति",
    why_dev="कित्-प्रत्यये परे वच्/स्वप्/यज्-आदीनां यण्-वर्णस्य सम्प्रसारण-प्रसङ्गः।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

