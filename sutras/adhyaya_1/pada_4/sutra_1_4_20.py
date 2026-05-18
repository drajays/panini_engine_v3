"""
1.4.20  अयस्मयादीनि च्छन्दसि  (ayasmayādīni chandasi)  —  VIDHI

**Pāṭha:** *Ayasmaya* and similar forms [are used / treated specially] in
the Vedic register (*chandas*).

v3: sets the gate ``1_4_20_ayasmayAdi_chandasi`` in
``state.paribhasha_gates`` to indicate that the ayasmayādi Vedic provision
is active.  Actual morphological effects are handled by downstream rules
consulting this gate when ``state.meta["chandas"]`` is set.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.paribhasha_gates.get("1_4_20_ayasmayAdi_chandasi") is not True


def act(state: State) -> State:
    state.paribhasha_gates["1_4_20_ayasmayAdi_chandasi"] = True
    state.samjna_registry["ayasmayAdi_chandasi"] = frozenset({"vedic_provision"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.20",
    sutra_type             = SutraType.VIDHI,
    text_slp1              = "ayasmayAdIni chandasi",
    text_dev               = "अयस्मयादीनि च्छन्दसि",
    padaccheda_dev         = "अयस्मय-आदीनि / छन्दसि",
    why_dev                = "छन्दसि अयस्मयादि-शब्दानां विशेष-विधिः प्रवर्तते।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
