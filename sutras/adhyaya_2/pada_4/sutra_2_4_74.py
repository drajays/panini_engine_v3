"""
2.4.74  यङोऽचि च  —  VIDHI (narrow: delete yaG's y before ac)

Glass-box scope for `loluv`:
  When a yaG-derived dhātu has a trailing 'y' immediately before an
  ardhadhātuka ac-pratyaya 'a', delete that 'y' (luk) and tag the dhātu with
  ``dhatulopa`` so 1.1.4 can block 7.3.84 guṇa in that locus.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State):
    if len(state.terms) < 2:
        return None
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags:
            continue
        pr = state.terms[i + 1]
        if pr.kind != "pratyaya":
            continue
        if not pr.varnas or pr.varnas[0].slp1 != "a":
            continue
        if "ardhadhatuka" not in pr.tags:
            continue
        if not dh.varnas or dh.varnas[-1].slp1 != "y":
            continue
        if dh.meta.get("2_4_74_yang_luk_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return bool(state.meta.get("2_4_74_yang_luk_arm")) and _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    dh = state.terms[i]
    del dh.varnas[-1]
    dh.tags.add("dhatulopa")
    dh.meta["2_4_74_yang_luk_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.74",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "yaGo aci ca",
    text_dev       = "यङोऽचि च",
    padaccheda_dev = "यङः / अचि / च",
    why_dev        = "यङन्त-धातोः अचि परे अन्त्य-यकारस्य लुक् (लोप-टैग सह)।",
    anuvritti_from = ("2.4.58",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

