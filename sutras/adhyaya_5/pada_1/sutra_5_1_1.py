"""
5.1.1  प्राक् क्रीताच्छः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51001):** *prāk-krītīya chādhikāraḥ*
— scope through **5.1.17** (परिखाया ढञ्), matching v2
``adhikara_prakarana.json`` sequence **38**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _legacy_cond(state: State) -> bool:
    return not any(e.get("id") == "5.1.1" for e in state.adhikara_stack)


def _legacy_act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.1.1",
        "scope_end" : "5.1.17",
        "text_dev"  : 'प्राक् क्रीताच्छः',
    })
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, group_open, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _new_cond(state: State) -> bool:
    return default_site(state, "5.1.1") is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        return attach_taddhita(state, "Ca")
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id       = "5.1.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'prAk krItAcCaH',
    text_dev       = 'प्राक् क्रीताच्छः',
    samagra_slp1   = "prAk-krItAt CaH",
    samagra_dev    = "प्राक्-क्रीतात् छः",
    padaccheda_dev = "प्राक् / क्रीतात् / छः",
    why_dev        = "प्राक्क्रीतीयः छाधिकारः — ५.१.१ तः ५.१.१७ पर्यन्तम्।",
    anuvritti_from = (),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.1.1", "5.1.17"),
)

register_sutra(SUTRA)

