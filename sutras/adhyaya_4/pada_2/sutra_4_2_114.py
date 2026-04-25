"""
4.2.114  वृद्धाच्छः  —  SAMJNA (*vṛddhāc chaḥ* — *śaiṣika* *śeṣa*)

**Pāṭha (baked *anuvṛtti*):** after **4.2.92** *śeṣe*, carrying **3.1.1–3.1.3**,
**4.1.1**, **4.1.76**, **4.1.82**, **4.1.83** — *śaiṣika* *Cha* after a *vṛddha*
*pada* (**1.1.73**), in senses other than the *apatyādi* … *catur-artha* block
already taught (*Kāśikā:* *vṛddhāt prātipadikāc chaḥ pratyayo bhavati śaiṣikaḥ;
aṇo ’pavādaḥ*).  *Gotra* does **not** *anuvṛtti* here (*sāmānyena vidhānam*).
Later *paratva* rules (e.g. **4.2.104**, **106**, **109**, **110**) may block this
*vidhi* where applicable.

*Engine:* ``samjna_registry[SAMJNA_KEY]`` = intersection of (a) indices the
recipe marks *śaiṣika*-*śeṣa*-eligible via ``state.meta[META_ELIGIBLE_INDICES]``
and (b) **1.1.73** *vṛddha-pada* indices.  No *Cha* segment is inserted here
(*vidhi* / *prakriyā* pending).  **4.2.92** *adhikāra* must be open.
"""
from __future__ import annotations

from typing import FrozenSet

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

from sutras.adhyaya_1.pada_1.sutra_1_1_73 import VRIDDHAM_INDICES_KEY

SAMJNA_KEY = "4.2.114_vrddhAc_cha_eligible_term_indices"
META_ELIGIBLE_INDICES = "4_2_114_saiSsika_sheSa_term_indices"


def _requested_indices(state: State) -> FrozenSet[int]:
    raw = state.meta.get(META_ELIGIBLE_INDICES)
    if raw is None:
        return frozenset()
    if isinstance(raw, frozenset):
        seq = raw
    elif isinstance(raw, (set, tuple, list)):
        seq = raw
    else:
        return frozenset()
    out: list[int] = []
    for x in seq:
        try:
            out.append(int(x))
        except (TypeError, ValueError):
            continue
    n = len(state.terms)
    return frozenset(i for i in out if 0 <= i < n)


def _vrddham_indices(state: State) -> FrozenSet[int]:
    v = state.samjna_registry.get(VRIDDHAM_INDICES_KEY)
    if isinstance(v, frozenset):
        return v
    if v is None:
        return frozenset()
    return frozenset()


def proposed_cha_eligible_indices(state: State) -> FrozenSet[int]:
    """*Cha* licence only where recipe requests **and** **1.1.73** *vṛddham*."""
    return _requested_indices(state) & _vrddham_indices(state)


def cond(state: State) -> bool:
    if not adhikara_in_effect("4.2.114", state, "4.2.92"):
        return False
    new = proposed_cha_eligible_indices(state)
    old = state.samjna_registry.get(SAMJNA_KEY)
    if old is None:
        old = frozenset()
    return new != old


def act(state: State) -> State:
    state.samjna_registry[SAMJNA_KEY] = proposed_cha_eligible_indices(state)
    return state


SUTRA = SutraRecord(
    sutra_id        = "4.2.114",
    sutra_type      = SutraType.SAMJNA,
    text_slp1       = (
        "samarthAnAm prathamAt NyAp prAtipadikAt paraH AdyudAttaH "
        "taddhitaH vA prAg dIvyataH aR Seze vfdDAt CaH"
    ),
    text_dev        = (
        "समर्थानां प्रथमात् ङ्याप्प्रातिपदिकात् परः आद्युदात्तस्तद्धितो वा "
        "प्राग्दीव्यतोऽण् शेषे वृद्धात् छः"
    ),
    padaccheda_dev  = "वृद्धात् (पञ्चमी-एकवचनम्) / छः (प्रथमा-एकवचनम्)",
    why_dev         = (
        "वृद्ध-प्रातिपदिकात् शैषिके शेषार्थे छ-प्रत्ययः, अण्-बाधकः; "
        "गोत्र-शब्दोऽत्रानुवर्तते न। परत्वेन ४.२.१०४ादयो यत्र प्रवृत्ताः, तत्र बाधः।"
    ),
    anuvritti_from  = (
        "3.1.1",
        "3.1.2",
        "3.1.3",
        "4.1.1",
        "4.1.76",
        "4.1.82",
        "4.1.83",
        "4.2.92",
    ),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)
