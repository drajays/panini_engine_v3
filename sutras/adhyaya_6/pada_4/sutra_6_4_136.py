"""
6.4.136  विभाषा ङिश्योः  —  VIDHI

Padaccheda: विभाषा ङि-श्योः

विभाषा ङिश्योः (6.4.136)
Pāṭha: ashtadhyayi.com data.txt row i=64136 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from sutras.adhyaya_6.pada_4.sutra_6_4_137 import samyogad_vamanta

def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _live_before(state: State, i: int):
    """The Term with sounds right before ``i``."""
    return next((state.terms[k] for k in range(i - 1, -1, -1) if state.terms[k].varnas), None)


def _site(state: State):
    """विभाषा ङिश्योः: the a of an an-aṅga in bha goes, or stays, before ṅi and śī (rājñi, rājani; sāmni, sāmani; sāmnī, sāmanī). 6.4.137 holds here too (karmaṇi)."""
    for i, t in enumerate(state.terms[:-1]):
        if "anga" not in t.tags or "bha" not in t.tags or t.meta.get("6_4_136_done") or len(t.varnas) < 2:
            continue
        nxt = state.terms[i + 1]
        if (nxt.meta.get("upadesha_slp1") or "") not in ("Ni", "SI") or "sup" not in nxt.tags:
            continue
        if t.varnas[-1].slp1 != "n" or t.varnas[-2].slp1 != "a" or samyogad_vamanta([v.slp1 for v in t.varnas]):
            continue
        if adhikara_in_effect("6.4.136", state, "6.4.1") and adhikara_in_effect("6.4.136", state, "6.4.129"):
            return t
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    del t.varnas[-2]                       # the a of an (the vā takes this reading; the other is 6.4.134 held back, rājani)
    t.meta["6_4_136_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.136",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA NiSyoH",
    text_dev              = "विभाषा ङिश्योः",
    samagra_slp1          = "anaH Basya aNgasya at NiSyoH viBAzA lopaH",
    samagra_dev           = "अनः भस्य अङ्गस्य अत् ङिश्योः विभाषा लोपः",
    padaccheda_dev        = "विभाषा ङि-श्योः",
    why_dev               = 'ङौ शी-आदेशे च परे भस्य अनः अकारस्य विकल्पेन लोपः — राज्ञि, राजनि; साम्नी, सामनी।',
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    vibhasha_scope        = _new_cond,
    apavada_of            = ('6.4.134',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
