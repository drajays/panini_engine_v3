"""
6.1.111  ऋत उत्  —  VIDHI

After an aṅga ending in ṛ, the a of ṅasi / ṅas (the ablative and genitive singular) and the ṛ become one ut (u, then rapara by
1.1.51): पितृ + ङसिँ / ङस् → पितुः, मातुः, भ्रातुः, कर्तुः. (ङे and ङि take guṇa instead — पित्रे by yaṇ, पितरि by 7.3.110; 6.1.110
ङसिङसोश्च is the neighbouring rule for e / o.)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 6.1.111 (padaccheda: ऋतः उत्; anuvṛtti: ङसिङसोः 6.1.110, अति)
  Source #2 — ashtadhyayi.com subanta table, ṛ-stems 5-1 / 6-1: पितुः, मातुः, भ्रातुः, भवितुः ; engine docs sutra_1_1_51 (पितृ + ङसिँ → पित् उ र् स्)

Engine: structural — an ṛ-final aṅga followed by the ṅasi / ṅas sup (by upadeśa identity), whose first varṇa is the a. The ṛ becomes u
with the rapara marker 1.1.51 consumes; the a is absorbed into the ekādeśa (the sup keeps its s).

DEBT (Art. 16): this file also carries, below, an older glass-box branch that is *not* 6.1.111 — it deletes the t of ktavatu in
भिन्नवान् and fires structurally (``n n`` + ``t``-initial krt). It predates the real rule and is kept only so that derivation stays
green; the honest derivation is 8.2.42 (the t of niṣṭhā becomes n).
Pāṭha: ashtadhyayi.com data.txt row i=61111 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_SUPS = frozenset({"Nas", "Nasi", "Nasi~"})


def _site(state: State):
    for i, ang in enumerate(state.terms[:-1]):
        sup = state.terms[i + 1]
        if "prātipadika" not in ang.tags or ang.meta.get("fta_ut_6_1_111_done") or not ang.varnas:
            continue
        if "sup" not in sup.tags or (sup.meta.get("upadesha_slp1") or "").strip() not in _SUPS:
            continue
        # ऋत् is taparaḥ (1.1.70): the short ṛ (and its savarṇa ḷ) only — the long ṝ-stems (कॄ, तॄ) keep their own forms
        if ang.varnas[-1].slp1 in ("f", "x") and sup.varnas and sup.varnas[0].slp1 == "a":
            return ang, sup
    return None


def _nn_t_demo(state: State) -> bool:     # the older, mislabelled branch (see DEBT above)
    if len(state.terms) != 2:
        return False
    a0, pr = state.terms[0], state.terms[1]
    vs0, vs1 = a0.varnas, pr.varnas
    if len(vs0) < 2 or len(vs1) < 2:
        return False
    if vs0[-2].slp1 != "n" or vs0[-1].slp1 != "n" or vs1[0].slp1 != "t" or "krt" not in pr.tags:
        return False
    return not pr.meta.get("6_1_111_t_lopa_done")


def cond(state: State) -> bool:
    return _site(state) is not None or _nn_t_demo(state)


def act(state: State) -> State:
    site = _site(state)
    if site is not None:
        ang, sup = site
        ang.varnas[-1] = mk("u")
        ang.meta["urN_rapara_pending"] = "r"
        ang.meta["urN_rapara_after_index"] = len(ang.varnas) - 1
        ang.meta["fta_ut_6_1_111_done"] = True
        del sup.varnas[0]                  # the a is part of the ekādeśa
        return state
    if _nn_t_demo(state):
        pr = state.terms[1]
        del pr.varnas[0]
        pr.meta["6_1_111_t_lopa_done"] = True
        state.samjna_registry["6.1.111_nn_t_lopa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.111",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'fta ut',
    text_dev       = 'ऋत उत्',
    samagra_slp1   = "ftaH NasiNasoH ati pUrvaparayoH ekaH ut",
    samagra_dev    = "ऋतः ङसिङसोः अति पूर्वपरयोः एकः उत्",
    padaccheda_dev = "ऋतः उत्",
    why_dev        = "ऋकारान्त अङ्ग और ङसि / ङस् के अ के स्थान में उ (रपर) एकादेश: पितुः, मातुः।",
    anuvritti_from = ("6.1.110",),
    apavada_of     = ("6.1.77",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
