"""
3.3.115  ल्युट् च  —  ANUVADA (narrow **corrected-v2 P006**)

**Pāṭha:** *lyuṭ ca* — *lyuṭ* is taught (among other affixes) in *bhāva* and
related senses.

Engine role: trace-only stamp on the **चिञ्** → *cayana* (*lyuṭ*) spine when the
recipe arms ``corrected_v2_P006_3_3_115_arm`` (CONSTITUTION Art. 7).  Affixation
still proceeds via **3.4.68** + **3.1.133** (*lyuw*).
Pāṭha: ashtadhyayi.com data.txt row i=33115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return bhava_site(state, vivaksita(state, "artha", "BAva"), vivaksita(state, "linga", "napuMsaka"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "lyuw")


SUTRA = SutraRecord(
    sutra_id="3.3.115",
    sutra_type=SutraType.ANUVADA,
    text_slp1="lyuw ca",
    text_dev="ल्युट् च",
    samagra_slp1="pratyayaH paraSca AdyudAttaSca DAtoH lyuw ca kft napuMsake BAve",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="प्रत्ययः परश्च आद्युदात्तश्च धातोः ल्युट् च कृत् नपुंसके भावे",
    padaccheda_dev="ल्युट् च",
    why_dev="भावादौ धातोः ल्युट्-विधानम् — अनुवादः (प००६ आर्म्)।",
    anuvritti_from=("3.1.91",),
    apavada_of     = ("3.3.18",),
    cond=cond,
    also_vidhi=True,          # ANUVADA in the pāṭha, and the vidhi of lyuṭ in napuṃsake bhāve
    act=act,
)

register_sutra(SUTRA)
