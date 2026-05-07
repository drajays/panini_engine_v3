"""
6.4.71  लुङ्लङ्लृङ्क्ष्वडुदात्तः  —  VIDHI (narrow: aṭ augment)

Engine: in luṅ/laṅ/lṛṅ contexts, prepend 'a' to the dhātu term as aṭ-āgama
(ṭ-it handled by 1.3.3/1.3.9 elsewhere). No pipeline-side forcing flag.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

AT_AGAMA_CONTEXT_TAG = "aT_agama_context"


def _find_dhatu_term(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def _find_at_agama_site(state: State):
    dh = _find_dhatu_term(state)
    if dh is None:
        return None
    if dh.meta.get("aT_agama_6_4_71_done"):
        return None
    if AT_AGAMA_CONTEXT_TAG not in dh.tags:
        return None
    return dh


def cond(state: State) -> bool:
    return _find_at_agama_site(state) is not None


def act(state: State) -> State:
    dh = _find_at_agama_site(state)
    if dh is None:
        return state
    dh.varnas.insert(0, mk("a"))
    dh.meta["aT_agama_6_4_71_done"] = True
    dh.tags.discard(AT_AGAMA_CONTEXT_TAG)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.71",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "luG-laG-lRG-kzu aT udAttaH",
    text_dev       = "लुङ्लङ्लृङ्क्ष्वडुदात्तः",
    padaccheda_dev = "लुङ्-लङ्-लृङ्-क्षु / अट् / उदात्तः",
    why_dev        = (
        "लुङ्/लङ्/लृङ्-लकारे धातोः पूर्वं अट्-आगमः; "
        "P014: लिटि अनुप्रयोग-कृ-यण्-मूर्तौ ``kr`` पूर्वम् ``a`` (आगम-समान-कार्यम्)।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

