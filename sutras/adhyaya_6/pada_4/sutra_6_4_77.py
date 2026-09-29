"""
6.4.77  अचि श्नु धातुभ्रुवां य्वोरियुवङौ  —  VIDHI 

Glass-box scope for `loluv`:
  When a dhātu ends in ū (U) and an a-initial pratyaya follows, replace that U
  with the sequence "uv" (u + v).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_AC = frozenset("aAiIuUfFxXeEoO")
_IYUV = {"i": "iy", "I": "iy", "u": "uv", "U": "uv"}


def _find(state: State):
    """A dhātu ending in इ/उ-varṇa before a vowel-initial pratyaya: इयङ्/उवङ्
    (नु+अ → नुव, प्रि+अ → प्रिय, लू+उस् …). 6.4.81 इणो यण् (the root इ) is excepted."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("6_4_77_uvang_done"):
            continue
        pr = state.terms[i + 1]
        if pr.kind != "pratyaya" or not pr.varnas or pr.varnas[0].slp1 not in _AC:
            continue
        if not dh.varnas or dh.varnas[-1].slp1 not in _IYUV:
            continue
        if len(dh.varnas) == 1 and dh.varnas[0].slp1 == "i":
            continue                                   # 6.4.81 इणो यण्
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    dh = state.terms[i]
    a, b = _IYUV[dh.varnas[-1].slp1]
    dh.varnas[-1] = mk(a)
    dh.varnas.append(mk(b))
    dh.meta["6_4_77_uvang_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.77",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "aci SnU-DAtuBruvAM yvor iyuvaNgO",
    text_dev       = "अचि श्नु धातुभ्रुवां य्वोरियुवङौ",
    padaccheda_dev = "अचि / श्नु-धातु-भ्रुवाम् / य्वोः / इयु-वङौ",
    why_dev        = "धातोः इवर्ण-उवर्णयोः अचि परे इयङ्-उवङौ (नुवति, म्रियते)।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

