"""
7.3.113  आपः  —  VIDHI (narrow slice: *yāṭ* before **ṅe** when **not** sarvanāma)

अनुवृत्तिः  ङिति 7.3.111 (engine: same *ṅit* *sup* set as **7.3.114**).

अधिकारः  अङ्गस्य 6.4.1

When the *aṅga* is **ā**‑banta (final SLP1 ``A``) but **not** tagged ``sarvanama``,
before **Ne**: insert **yāṭ** residue **y** + **ā** before **e** (ṅ dropped).  The
*aṅga* is **not** shortened here (contrast **7.3.114**).  **6.1.88** then applies
to the **ā** + **e** contact (…**y** is intervening only in the varṇa stream;
the operational *vṛddhi* pair is the **A** immediately before **e** in the
pratyaya slice).

Mutually exclusive with **7.3.114** (*sarvanāmnaḥ syāṭ* …).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.ngit_sup_locator import indices_last_anga_before_ngit_sup
from engine.state  import State, Term
from phonology     import mk
from phonology.sarvanama_syat_7_3_114 import is_abanta_flat, ngit_sup_match


def _matches(state: State) -> bool:
    if not adhikara_in_effect("7.3.113", state, "6.4.1"):
        return False
    hit = indices_last_anga_before_ngit_sup(state)
    if hit is None:
        return False
    _ai, _pj = hit
    anga = state.terms[_ai]
    pr = state.terms[_pj]
    if "anga" not in anga.tags or "sarvanama" in anga.tags:
        return False
    if "ghi" in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "Ne":
        return False
    if pr.meta.get("yad_ap_7_3_113_done"):
        return False
    if not anga.varnas or not pr.varnas:
        return False
    flat = "".join(v.slp1 for v in anga.varnas)
    if not is_abanta_flat(flat):
        return False
    return anga.varnas[-1].slp1 == "A"


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    hit = indices_last_anga_before_ngit_sup(state)
    if hit is None:
        return state
    _ai, pj = hit
    pr = state.terms[pj]
    pr.varnas = [mk("y"), mk("A"), mk("e")]
    pr.meta["yad_ap_7_3_113_agama"] = "yAw"
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1", "Ne")
    pr.meta["upadesha_slp1"] = "yAe"
    pr.meta["yad_ap_7_3_113_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.113",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ApaH Niti supi",
    text_dev       = "आपः ङिति सुपि",
    padaccheda_dev = "आपः (सप्तम्येकवचनम्), ङिति (सप्तम्येकवचनम्), सुपि (सप्तम्येकवचनम्)",
    why_dev        = (
        "आबन्तात् न-सर्वनाम्नः परे ङिति ङे याट्-आगमः; अङ्गे ह्रस्वो न भवति।"
    ),
    anuvritti_from = ("7.3.111",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
