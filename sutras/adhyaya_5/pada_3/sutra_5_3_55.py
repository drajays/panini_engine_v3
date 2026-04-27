"""
5.3.55  अतिशयने तमपिष्ठनौ  —  VIDHI (narrow: *tama*+**p** / *iṣṭha*+**n** after
*atiśayana* when ``5_3_55_tamap_arm`` *meta*)

Full *Aṣṭādhyāyī* *prayoga* needs **5.3.2**–**5.3.26** *adhikāra* and *samarthya*; v3
*glass-box* *corpus* only appends a **tama**+**p**-shaped taddhita *Term* for
*piṇḍa* *prakriyā* (e.g. *kumārī* → *kumāritamā* in user ``kumari.md``).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Term
from phonology     import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("5_3_55_tamap_arm"):
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
        varnas=parse_slp1_upadesha_sequence("tamap"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "tamap"},
    )
    state.terms.append(p)
    state.meta.pop("5_3_55_tamap_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id         = "5.3.55",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = "atiSayanI tamapizWanO",
    text_dev         = "अतिशयने तमपिष्ठनौ",
    padaccheda_dev   = "अतिशयने / तमप्-इष्ठनौ",
    why_dev          = "सर्वश्रेष्ठार्थे तमप्-प्रत्ययः (ग्लास-बॉक्स्, *meta*-आर्म्ड)।",
    anuvritti_from   = ("5.3.2",),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
