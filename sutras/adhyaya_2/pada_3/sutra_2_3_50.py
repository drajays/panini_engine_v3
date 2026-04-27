"""
2.3.50  षष्ठी शेषे  —  SAMJNA (vibhakti-nirdhāraṇa helper)

**Pāṭha** (anuvṛtti from **2.3.1** baked in for storage; see CONSTITUTION Art. 4):
*anabhihite ṣaṣṭhī śeṣe*.

**Kāśikā (sense):** *karmādibhyo'nyo* — any relation other than *kāraka* and other
canonical vibhaktyarthas; e.g. *sva-svāmi-sambandha* (possessor–possessed),
part–whole, etc.  In such *śeṣa* relations, the 6th-case-affix (*ṣaṣṭhī*) is
used.

**Engine (glass-box):** the engine is mechanically blind to semantics.  So this
sūtra is implemented as an **opt-in** vibhakti-selection helper keyed off
``state.meta['2_3_50_sheSa_shashthi_eligible']`` (set by the caller/recipe after
doing the necessary semantic analysis outside the engine core).  When eligible
and the **2.3.1** *anabhihita* adhikāra is open, this sūtra writes
``state.meta['vibhakti_vacana'] = '6-1'`` (genitive singular) so **4.1.2** can
attach the correct *sup* (*ङस् / Nas*).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

META_SHESE_ELIGIBLE = "2_3_50_sheSa_shashthi_eligible"
META_OVERRIDE_VV    = "2_3_50_override_vibhakti_vacana"


def _adhikara_2_3_1_open(state: State) -> bool:
    return any(e.get("id") == "2.3.1" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    if not _adhikara_2_3_1_open(state):
        return False
    if not state.meta.get(META_SHESE_ELIGIBLE):
        return False
    # Avoid redundant applications once the coordinate is already set.
    return state.meta.get("vibhakti_vacana") != "6-1"


def act(state: State) -> State:
    # Default behaviour: *śeṣa* selection is a vibhakti-determiner, so it may
    # override a caller-provided coordinate unless explicitly disabled.
    override = state.meta.get(META_OVERRIDE_VV, True)
    if override or not state.meta.get("vibhakti_vacana"):
        state.meta["vibhakti_vacana"] = "6-1"
    state.samjna_registry["2.3.50_vibhakti_vacana"] = state.meta.get("vibhakti_vacana")
    # Monotonic stamp: allows repeat applications to satisfy R2 in audit flows.
    state.samjna_registry["2.3.50_apply_stamp"] = (
        int(state.samjna_registry.get("2.3.50_apply_stamp", 0)) + 1
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.3.50",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "anabhihite zazWI Seze",
    text_dev       = "अनभिहिते षष्ठी शेषे",
    padaccheda_dev = "अनभिहिते / षष्ठी / शेषे",
    why_dev        = (
        "कर्मादिभ्योऽन्यः (स्वस्वामिसंबन्धादिः) शेषः; तत्र षष्ठी विभक्तिः। "
        "इह प्रक्रियायां '६-१' इति विभक्ति-निर्णयः (सुप्-आदेशः ४.१.२)।"
    ),
    anuvritti_from = ("2.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

