"""
6.1.8  लिटि धातोरनभ्यासस्य  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  In liṭ, duplicate the primary dhātu to form a reduplication frame:
    [abhyāsa, dhātu, …].

Teaching JSON **P036** (*nināya*): after **6.1.78** the tape is **nay** + augment **a**;
with **1.1.59** *sthānivat* the guṇa vowel **e** of **nī** is treated as present for
*abhyāsa*, so insert **ne** (not a copy of **nay**) before **nay** + **a**.

Engine:
  • default: ``state.meta['liT_dvitva_recipe']`` — copy *dhātu*.
  • **P036**: ``state.meta['P036_6_1_8_lit_sthanivat_ne_arm']``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61008 · लिटि धातोरनभ्यासस्य
              padaccheda: लिटि धातोः अन्-अभ्यासस्य
              anuvṛtti:   61001: एकाचः द्वे प्रथमस्य | 61002: अजादेः द्वितीयस्य
  Source #2 — Kāśikā 6.1.8 udāharaṇa:
                पपाच
                पपाठ प्रोर्णुनाव
                (का० ३.१.३६) इति वचनाद् ऊर्णोतेः   इत्याम् न भवति
  Cross-check — surface pinned by: tests/regression/test_anya_pullinga_gold.py, tests/regression/test_rADA_strilinga_gold.py, tests/unit/test_6_1_104_nadici_ramau.py
  Reference record: sutra_ref_out/6_1_8.json
"""
from __future__ import annotations

from copy import deepcopy

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _site_p036(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    di = _first_dhatu_index(state)
    if di is None or di + 1 >= len(state.terms):
        return False
    dh, nxt = state.terms[di], state.terms[di + 1]
    if dh.meta.get("P036_6_1_8_done"):
        return False
    if "".join(v.slp1 for v in dh.varnas) != "nAy":
        return False
    if len(nxt.varnas) != 1 or nxt.varnas[0].slp1 != "a":
        return False
    if di > 0 and "abhyasa" in state.terms[di - 1].tags:
        return False
    return True


def _structural_site(state: State) -> int | None:
    """लिटि धातोरनभ्यासस्य: the dhātu (not an abhyāsa, not yet doubled) stands before a liṭ affix — read from the
    tiṅ's own source lakāra (Art. 2). Returns the dhātu's index."""
    if _site_p036(state):        # nAy + ṇal: the P036 branch (abhyāsa ne) owns it
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("6_1_8_dvitva_done"):
            continue
        if i > 0 and "abhyasa" in state.terms[i - 1].tags:
            continue
        if any(u.kind == "pratyaya" and "tin_adesha_3_4_78" in u.tags and u.varnas
               and (u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in state.terms[i + 1:]):
            return i
    return None


def cond(state: State) -> bool:
    if _structural_site(state) is not None:
        return True
    if not state.meta.get("lakara_liT"):
        return False
    if _site_p036(state):
        return True
    if not state.meta.get("liT_dvitva_recipe"):
        return False
    di = _first_dhatu_index(state)
    if di is None:
        return False
    if di > 0 and "abhyasa" in state.terms[di - 1].tags:
        return False
    return True


def act(state: State) -> State:
    di = _structural_site(state)
    if di is not None:
        dh = state.terms[di]
        ab = Term(
            kind=dh.kind,
            varnas=[deepcopy(v) for v in dh.varnas],
            tags=set(dh.tags) | {"abhyasa"},
            meta=dict(dh.meta),
        )
        ab.tags.discard("dhatu")
        ab.meta["6_1_8_abhyasa"] = True
        state.terms.insert(di, ab)
        state.terms[di + 1].meta["6_1_8_dvitva_done"] = True
        state.meta["__why_now_dev__"] = (
            "लिटि परे अनभ्यासस्य धातोः द्वित्वम् (एकाचो द्वे प्रथमस्य ६.१.१); पूर्वोऽभ्यासः (६.१.४) — भू → भू-भू। (६.१.८)"
        )
        return state
    if _site_p036(state):
        di = _first_dhatu_index(state)
        assert di is not None
        ab = Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("ne")),
            tags={"abhyasa", "anga"},
            meta={"P036_6_1_8_abhyasa_ne": True},
        )
        state.terms.insert(di, ab)
        state.terms[di + 1].meta["P036_6_1_8_done"] = True
        return state
    if not state.meta.get("liT_dvitva_recipe"):
        return state
    di = _first_dhatu_index(state)
    if di is None:
        return state
    dh = state.terms[di]
    ab = Term(
        kind=dh.kind,
        varnas=[deepcopy(v) for v in dh.varnas],
        tags=set(dh.tags) | {"abhyasa"},
        meta=dict(dh.meta),
    )
    ab.tags.discard("dhatu")
    ab.meta["6_1_8_abhyasa"] = True
    state.terms.insert(di, ab)
    state.meta["liT_dvitva_recipe"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.8",
    sutra_type=SutraType.VIDHI,
    text_slp1='liwi DAtoranaByAsasya',
    text_dev='लिटि धातोरनभ्यासस्य',
    samagra_slp1="liwi DAtoH anaByAsasya ekAcaH praTamasya ajAdeH dvitIyasya dve",
    samagra_dev="लिटि धातोः अनभ्यासस्य एकाचः प्रथमस्य, अजादेः द्वितीयस्य द्वे",
    padaccheda_dev="लिटि / धातोः / अनभ्यासस्य",
    why_dev="लिटि धातोः द्वित्वम् (अभ्यास-प्रकरणे) — विभिदतुः / प०३६।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
