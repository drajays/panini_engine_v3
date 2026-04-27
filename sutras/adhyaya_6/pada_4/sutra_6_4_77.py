"""
6.4.77  अचि श्नु धातुभ्रुवां य्वोरियुवङौ  —  VIDHI (narrow: ū → uv before a)

Glass-box scope for `loluv`:
  When a dhātu ends in ū (U) and an a-initial pratyaya follows, replace that U
  with the sequence "uv" (u + v).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    if len(state.terms) < 2:
        return None
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags:
            continue
        pr = state.terms[i + 1]
        if pr.kind != "pratyaya" or not pr.varnas or pr.varnas[0].slp1 != "a":
            continue
        if not dh.varnas or dh.varnas[-1].slp1 != "U":
            continue
        if dh.meta.get("6_4_77_uvang_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    dh = state.terms[i]
    # Replace final U with u + v.
    dh.varnas[-1] = mk("u")
    dh.varnas.append(mk("v"))
    dh.meta["6_4_77_uvang_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.77",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "aci SnU-DAtuBruvAM yvor iyuvaNgO",
    text_dev       = "अचि श्नु धातुभ्रुवां य्वोरियुवङौ",
    padaccheda_dev = "अचि / श्नु-धातु-भ्रुवाम् / य्वोः / इयु-वङौ",
    why_dev        = "ऊ-स्थानि अचि परे उवङ्-आदेशः (ग्लास-बॉक्स्: U→uv)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

