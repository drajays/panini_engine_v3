"""
5.3.55  अतिशयने तमपिष्ठनौ  —  VIDHI (narrow: *tama*+**p** / *iṣṭha*+**n** after
*atiśayana* when ``5_3_55_tamap_arm`` *meta*)

Full *Aṣṭādhyāyī* *prayoga* needs **5.3.2**–**5.3.26** *adhikāra* and *samarthya*; v3
*glass-box* *corpus* appends a **tama**+**p**-shaped taddhita *Term* when either
``5_3_55_tamap_arm`` (*strīliṅga*, e.g. *kumārī* → *kumāritamā* in ``kumari.md``)
or ``5_3_55_tamap_pullinga_arm`` (*pulliṅga*, ``prakriya_22`` *ratnadhātama*-) is set.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 53055 · अतिशायने तमबिष्ठनौ
              padaccheda: अतिशायने तमप्-इष्ठनौ
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः
  Source #2 — Kāśikā 5.3.55 udāharaṇa:
                निपातनाद् दीर्घत्वम्
                प्रकृत्यर्थविशेषणं चैतत्
                प्रकृत्यर्थविशेषणं च स्वार्थिकानां द्योत्यं भवति
  Cross-check — surface pinned by: tests/unit/test_kumAri_taddhita_pipeline.py, tests/unit/test_ratnaDAtamam.py
  Reference record: sutra_ref_out/5_3_55.json
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Term
from phonology     import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if len(state.terms) != 1:
        return None
    t0 = state.terms[0]
    if "prātipadika" not in t0.tags:
        return None
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms[1:]):
        return None
    if state.meta.get("5_3_55_tamap_arm"):
        if "strīliṅga" not in t0.tags:
            return None
        return 0
    if state.meta.get("5_3_55_tamap_pullinga_arm"):
        if "pulliṅga" not in t0.tags:
            return None
        return 0
    return None


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
    state.meta.pop("5_3_55_tamap_pullinga_arm", None)
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
