"""
5.3.70  प्रागिवात्कः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=53070):** *kādhikāraḥ* — scope through
**5.3.95** (अवक्षेपणे कन्), matching v2 ``adhikara_prakarana.json`` sequence
**45**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _legacy_cond(state: State) -> bool:
    return not any(e.get("id") == "5.3.70" for e in state.adhikara_stack)


def _legacy_act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.3.70",
        "scope_end" : "5.3.95",
        "text_dev"  : 'प्रागिवात्कः',
    })
    return state


from engine.taddhita_attach import default_site, attach_taddhita


def _new_cond(state: State) -> bool:
    return default_site(state, "5.3.70") is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    return attach_taddhita(state, "ka")      # SHORTCUT S57: only prātipadikas (the tiṅaś ca of 5.3.56 is not modelled); ka (5.3.70) is the default to 5.3.95 in the senses 5.3.73 – 86; the sense openers carry the frame


SUTRA = SutraRecord(
    sutra_id       = "5.3.70",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'prAgivAtkaH',
    text_dev       = 'प्रागिवात्कः',
    samagra_slp1   = "prAk ivAt prAtipadikAt kaH",
    samagra_dev    = "प्राक् इवात् प्रातिपदिकात् कः",
    padaccheda_dev = "प्राक् / इवात् / कः",
    why_dev        = "काधिकारः — ५.३.७० तः ५.३.९५ पर्यन्तम्।",
    anuvritti_from = (),
    also_vidhi     = True,          # the loop attaches this default from the speaker's taddhitArtha
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.3.70", "5.3.95"),
)

register_sutra(SUTRA)

