"""
1.4.22  द्वि-एकयोः द्विवचन-एकवचने  —  PARIBHASHA

*Padaccheda:* *dvi-ekayoḥ* (saptamī *dvivacanam* of *dvi* and *eka* in compound), *dvivacana-ekavacane* (nominative dual).

*Śāstra* *niyama (laghu):* when *dva* is to be denoted, *divivacana* *pratyaya*; when *eka*, *ekavacana* — for *tiṅ* (**1.4.102**) and *sup* (**1.4.103**).  *Vivakṣā* is by recipe: ``1_4_22_affix_class`` ∈ {``"dvi"``, ``"eka"``} on the primary *dhātu*.

*Anuvṛtti:* **1.4.1** *ekasañjñā*.

*Engine:* ``paribhasha_gates``; **R3**-safe ``cond``; no *vākya* semantics.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import find_primary_dhatu
from sutras.adhyaya_1.pada_4.dvi_eka_1_4_22 import (
    DVI_EKA_NIMITTA_KEY,
    GATE_KEY,
    dvi_eka_22_gate_needs_update,
)


def cond(state: State) -> bool:
    return dvi_eka_22_gate_needs_update(state)


def act(state: State) -> State:
    d = find_primary_dhatu(state)
    assert d is not None
    n = d.meta.get(DVI_EKA_NIMITTA_KEY)
    assert n in ("dvi", "eka")
    state.paribhasha_gates[GATE_KEY] = {
        "active"  : True,
        "nimitta" : n,
        "pATha"   : "1.4.22",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.22",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "dvi-ekayoH divivacana-ekavacane",
    text_dev       = "द्वि-एकयोः द्विवचन-एकवचने (एकसंज्ञा १.४.१, तिङ्-१.४.१०२, सुप्-१.४.१०३)",
    padaccheda_dev = "द्वि-एकयोः (सप्तमी-द्वि) / द्विवचन-एकवचने (प्रथमा-द्वि)",
    why_dev        = (
        "द्वित्व-विवक्षायां द्वि-वचनिय-प्रत्ययः, एकत्व-विवक्षायाम् एक-वचनियः; "
        "विवक्षा अभिकल्प्य धातु-मेटा 1_4_22_affix_class इति।"
    ),
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
