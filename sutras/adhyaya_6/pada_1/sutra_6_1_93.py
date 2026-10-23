"""
6.1.93  औतोऽम्शसोः  —  VIDHI

The JSON spine for ``split_prakriyas_11/P013.json`` includes **6.1.93** as a
no-op placeholder step.  This repository does not currently implement the full
6.1.93 sandhi family; for this demo we provide an **anuvāda audit step** that
records the invocation when recipe-armed.
Pāṭha: ashtadhyayi.com data.txt row i=61093 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup
from engine.state import State
from phonology import mk


# ओतः + अम् / शस् (अचि): the o and the a become one आ — गां, गाः, द्याम्, द्याः. Kāśikā: this आ is made where vṛddhi (7.2.115, from the
# ṇit of 7.1.90) would otherwise come, and takes it away (apavāda); अम् is the dvitīyā ekavacana (शस् keeps it company).
def _site(state: State):
    hit = anga_and_sup(state)
    if hit is None:
        return None
    anga, sup = hit
    if anga.varnas[-1].slp1 != "o" or sup.meta.get("6_1_93_done"):
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() not in {"am", "Sas", "am~", "Sas~"} or not sup.varnas or sup.varnas[0].slp1 != "a":
        return None
    return anga, sup


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga, sup = _site(state)
    anga.varnas[-1] = mk("A")
    del sup.varnas[0]
    sup.meta["6_1_93_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.93",
    sutra_type     = SutraType.VIDHI,
    apavada_of     = ("7.2.115",),     # Kāśikā 6.1.93: it takes away the vṛddhi the ṇit of 7.1.90 would bring
    text_slp1      = 'OtomSasoH',
    text_dev       = 'औतोऽम्शसोः',
    samagra_slp1   = "otaH am-SasoH aci ekaH pUrvaparayoH A",
    samagra_dev    = "ओतः अम्-शसोः अचि एकः पूर्वपरयोः आ",
    padaccheda_dev = "ओम् / आङोः / च",
    why_dev        = "P013 JSON placeholder (no mutation in this narrow demo).",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

