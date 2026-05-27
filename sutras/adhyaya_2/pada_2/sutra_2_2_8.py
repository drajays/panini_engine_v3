"""
2.2.8  षष्ठी  —  VIDHI

पदच्छेदः  षष्ठी

अनुवृत्तिः  (समास 2.1.3; सुप्सुपा 2.1.4)

Kāśikā summary: a genitive (*ṣaṣṭhī*) subanta compounds with another subanta
to form a tatpuruṣa (the *ṣaṣṭhī-tatpuruṣa*).  This is the most general of
the tatpuruṣa rules.  Examples: *rājñaḥ puruṣaḥ* → *rājapuruṣaḥ*,
*devānāṃ priyaḥ* → *devapriyaḥ*.

Engine (narrow, mechanically blind):
  Gate key ``2_2_8_sasthi_gate``.  Recipe arms ``state.meta['2_2_8_arm']``
  and tags a Term with ``sasthi_samasa`` indicating the genitive tatpuruṣa
  context.  Gate is raised on first fire.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_8_sasthi_gate") is True:
        return False
    return any("sasthi_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates["2_2_8_sasthi_gate"] = True
    state.samjna_registry["2_2_8_sasthi_tatpurusa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.8",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="zazWI",
    text_dev="षष्ठी",
    padaccheda_dev="षष्ठी",
    why_dev=(
        "षष्ठ्यन्तं सुबन्तेन समस्यते — राजपुरुषः, देवप्रियः इत्यादि षष्ठी-तत्पुरुषः।"
    ),
    anuvritti_from=("2.1.3", "2.1.4"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
