"""
5.3.57  द्विवचनविभज्योपपदे तरबीयसुनौ  —  VIDHI (narrow: *tar*+**p** with ``5_3_57_tarab_arm``)

Full *Aṣṭādhyāyī* *prayoga* needs the **5.3.2** *adhikāra*, *samarthya* …; v3 *glass-box* only
*appends* a **tara**+**p**-upadeśa *taddhita* *Term* for *kumArI*+… *śāstra* demos
(``kumari.md``: *kumAritarA*).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Term
from phonology     import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("5_3_57_tarab_arm"):
        return None
    if len(state.terms) != 1:
        return None
    t0 = state.terms[0]
    if "prātipadika" not in t0.tags or "strīliṅga" not in t0.tags:
        return None
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms[1:]):
        return None
    return 0


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    p = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("tarap"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "tarap"},
    )
    state.terms.append(p)
    state.meta.pop("5_3_57_tarab_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id         = "5.3.57",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = "dvivacanavibhajyopapade tarabIyasunO",
    text_dev         = "द्विवचनविभज्योपपदे तरबीयसुनौ",
    padaccheda_dev   = "द्विवचन-विभज्य-उपपदे / तर-बी-यसु-नौ",
    why_dev          = "उपमान-तुल्यार्थे *तरप*/*ईयसुन्* (ग्लास-बॉक्स्)।",
    anuvritti_from   = ("5.3.2",),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
