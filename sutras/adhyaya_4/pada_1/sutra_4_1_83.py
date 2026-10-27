"""
4.1.83  प्राग्दीव्यतोऽण्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41083):** *prāg-dīvyatīya aṇ-adhikāraḥ*
— scope through **4.3.168** (कंसीयपरशव्ययोर्यञञौ लुक् च), matching v2
``adhikara_prakarana.json`` sequence **34**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state)


def _open(state: State) -> bool:
    return not any(e.get("id") == "4.1.83" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return _open(state) or _site(state) is not None


def act(state: State) -> State:
    if _open(state):
        state.adhikara_stack.append({"id": "4.1.83", "scope_end": "4.3.168", "text_dev": "प्राग्दीव्यतोऽण्"})
    if _site(state) is not None:
        return attach_taddhita(state, "aR")
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.83",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'prAgdIvyatoR',
    text_dev       = 'प्राग्दीव्यतोऽण्',
    samagra_slp1   = "prAk-dIvyataH samarTAnAM praTamAt aR tadDitaH pratyayaH paraH vA",
    samagra_dev    = "प्राक्-दीव्यतः समर्थानां प्रथमात् अण् तद्धितः प्रत्ययः परः वा",
    padaccheda_dev = "प्राक् / दीव्यतः / अण्",
    why_dev        = "प्राग्दीव्यतीयः अणधिकारः — ४.१.८३ तः ४.३.१६८ पर्यन्तम्।",
    anuvritti_from = (),
    also_vidhi     = True,          # the adhikāra of aṇ is also its vidhi (prāg dīvyato 'ṇ)
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.83", "4.3.168"),
)

register_sutra(SUTRA)

