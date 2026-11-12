"""
3.1.60  चिण् ते पदः  —  VIDHI

Kāśikā 3.1.60: "अस्माद् धातोः परस्य च्लेश्चिणादेशो भवति तशब्दे परतः। … उदपादि सस्यम्। समपादि भैक्षम्।"

Engine: after 3.1.43 the luṅ cli stands before the ātmanepada ``ta``; for the root pad it is replaced by
ciṇ (the cli → ciṇ swap is the one 3.1.66 makes for bhāva/karman, here for kartari-of-pad).  ``swap_cli_cin``
is shared with 3.1.61, which names six more roots and makes the swap optional.

Pāṭha: ashtadhyayi.com data.txt row i=31060 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def cli_before_ta(state: State, roots) -> int | None:
    """Index of the luṅ cli right after a root in ``roots`` (upadeśa without its ~) and before the tiṅ ``ta``."""
    for i, t in enumerate(state.terms[:-1]):
        if t.kind != "pratyaya" or (t.meta.get("upadesha_slp1") or "").strip() != "cli" or i == 0:
            continue
        dh, nxt = state.terms[i - 1], state.terms[i + 1]
        if "dhatu" not in dh.tags or (dh.meta.get("upadesha_slp1") or "").strip().replace("~", "") not in roots:
            continue
        if "tin_adesha_3_4_78" in nxt.tags and "".join(v.slp1 for v in nxt.varnas) == "ta":
            return i
    return None


def swap_cli_cin(state: State, i: int) -> State:
    t = state.terms[i]
    t.varnas = parse_slp1_upadesha_sequence("ciR")
    t.meta["upadesha_slp1"] = "ciR"
    t.meta["it_markers"] = {"c", "R"}
    t.tags.update({"upadesha", "ardhadhatuka", "vikarana"})
    return state


_ROOTS = frozenset({"pada"})


def cond(state: State) -> bool:
    return cli_before_ta(state, _ROOTS) is not None


def act(state: State) -> State:
    return swap_cli_cin(state, cli_before_ta(state, _ROOTS))


SUTRA = SutraRecord(
    sutra_id              = "3.1.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ciR te padaH",
    text_dev              = "चिण् ते पदः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH ciR te padaH luNi cleH",
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः चिण् ते पदः लुङि च्लेः",
    padaccheda_dev        = "चिण् ते पदः",
    why_dev               = "पद-धातोः लुङि तशब्दे परे च्लेः चिण् (उदपादि) — काशिका ३.१.६०।",
    anuvritti_from        = ("3.1.44",),
    apavada_of            = ("3.1.44",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
