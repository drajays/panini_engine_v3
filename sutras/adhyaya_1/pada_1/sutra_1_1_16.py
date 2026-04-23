"""
1.1.16  सम्बुद्धौ शाकल्यस्येतावनार्षे  —  SAMJNA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11016, ``e`` = *sambuddhaushaakalyasyetaavanaarshe*):**
*Kāśikā* *vṛtti*: in *sambuddhi* (8), *Śākalya* *mata* for *o* and *t* in *it* in *anarṣa* *prayoga* —
*pragṅhya* extension with *anuvṛtti* from **1.1.11** and **1.1.15** (*ot*).

v3: **R2** — ``samjna_registry['pragrahya_sambuddhau_shAkalya'] = True``; *sambuddhi* is **not** read
in *cond* here; *vibhakti* firewall per Art. 2.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

SAMJNA_KEY: str = "pragrahya_sambuddhau_shAkalya"

# Spaced SLP1 aligned with the index ``e``-field segmentation (see ``text_dev`` + Kāśikā *padaccheda*).
TEXT_SLP1: str = "sambuddhau SAkalyasya itA avan Arze"


def sambuddhau_shakalya_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(SAMJNA_KEY) is True


def sambuddhau_shakalya_gate_is_set(state: State) -> bool:
    """Back-compat name; **1.1.16** is a SAMJNA, not a paribhāṣā *gate*."""
    return sambuddhau_shakalya_samjna_is_registered(state)


def cond(state: State) -> bool:
    return not sambuddhau_shakalya_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry[SAMJNA_KEY] = True
    return state


_WHY = (
    "सम्बुद्ध-औ-त-चर्चा, शाकल्य-मत-नियम, अनार्ष-काले, प्रगृह्य-संज्ञा, इति।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.16",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = TEXT_SLP1,
    text_dev       = "सम्बुद्धौ शाकल्यस्येतावनार्षे",
    padaccheda_dev = "सम्बुद्धौ / शाकल्यस्य / इतौ / अनार्षे",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11", "1.1.15"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
