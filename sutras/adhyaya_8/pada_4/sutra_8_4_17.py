"""
8.4.17  नेर्गदनदपतपदघुमास्य…  —  VIDHI (narrow: *neḥ* of *ni* → *ṇ* + *ghu*)

*Śāstra-pāṭha (machine index i=34017; SLP1 row on ashtadhyayi-com):* **neH**
before the listed ārya-roots, including **घु**-dhātus.  This engine implements
only the **घु** *śākhā* in terms of `dhatu_upadesha_slp1_is_ghu` (``1.1.20``):
after a **pra-** or **pary-**-class *upasarga* (*recipes* use flat ``"pra"``,
``"pari"`` + tags) the initial **n** of the *upasarga* **ni** (varṇa row ``n i``)
becomes **R** (ण्) when the *śāstrīya* *dhātu* **upadeśa** is a **ghu** member
(*e.g.* *pra*+*ni*+**dada+ti** → *pra*+*R*+*i*+…, **प्रणिददाति** style, or
**7.3.78** *yacC*+**a**+**ti** with ``upadesha_slp1`` still **da~da** and **1.1.20**
*ghu*, **प्रणियच्छति** style, or *deN*+**6.1.78** **dayate** with ``de~N`` *ghu*,
**प्रणिदयते** style).

*Tripāḍī* (``state.tripadi_zone``) **or** ``state.meta["8_4_17_pre_tripadi_arm"]``,
analogous to **8.4.40** pre-**8.2.1** demos.  *Vyāya* full *gadādi* *liṣṭa* is
future work: **cond** is intentionally narrow (R1-safe on this *corpus*).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Term
from phonology     import mk

from sutras.adhyaya_1.pada_1.sutra_1_1_20 import dhatu_upadesha_slp1_is_ghu

# *Upasarga* ``Term`` whose *saṃsṛṣṭi* with **ni** licenses **8.4.17** in
# *Kāśikā-style* *pra* / *pari* examples.  (Extend when broadening *ner*.)
_GHU_NER_PRAK_UPAS: frozenset[str] = frozenset(
    {
        "pra",   # प्र +
        "pari",  # परि + (Kāś.: परिणिगदति-style)
    }
)


def _flat_t(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas if v is not None)


def _is_ni_upasarga(ni_t: Term) -> bool:
    if "upasarga" not in ni_t.tags or len(ni_t.varnas) < 2:
        return False
    return (
        ni_t.varnas[0].slp1 == "n"
        and ni_t.varnas[1].slp1 == "i"
    )


def _ghu_anga_after_ni(
    state: State,
    ni_idx: int,
) -> bool:
    for j in range(ni_idx + 1, len(state.terms)):
        t = state.terms[j]
        if "dhatu" not in t.tags:
            continue
        u = (t.meta.get("upadesha_slp1") or "").strip()
        return bool(u) and dhatu_upadesha_slp1_is_ghu(state, u)
    return False


def _find(state: State) -> int | None:
    if not (state.tripadi_zone or state.meta.get("8_4_17_pre_tripadi_arm")):
        return None
    if not state.terms or len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        t0 = state.terms[i]
        t1 = state.terms[i + 1]
        if t1.meta.get("8_4_17_ner_done"):
            continue
        if "upasarga" not in t0.tags or "upasarga" not in t1.tags:
            continue
        if not _is_ni_upasarga(t1):
            continue
        if _flat_t(t0) not in _GHU_NER_PRAK_UPAS:
            continue
        if not _ghu_anga_after_ni(state, i + 1):
            continue
        return i + 1
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    ti = _find(state)
    if ti is None:
        return state
    t = state.terms[ti]
    t.varnas[0] = mk("R")
    t.meta["8_4_17_ner_done"] = True
    return state


# Full *pāṭha* SLP1: *neH* + *gadādi* liṣṭa *śabda* (i=34017, ashtadhyayi-com *s*).
# Devanagarī: नेर्गदनदपतपदघु…चनो…देग्धिषु च
_TEXT_SLP1 = (
    "neH gadanadapatapadaghumAsyatihantiyAtivAtidrAtipsAtivapativahati"
    "SAmyaticinotidegDizica"
)

SUTRA = SutraRecord(
    sutra_id         = "8.4.17",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = _TEXT_SLP1,
    text_dev         = "नेर्गदनदपतपदघुमास्य…चिनो…देग्धिषु च",
    padaccheda_dev   = "नेः / गद-… / च",
    why_dev          = (
        "उपसर्ग-स्थानिकस्य नि-उपसर्गे नकारं गदादिघोः परतः णादेशो "
        "(*त्रिपादी*; *प्र* + *नि* + *घु* *धा* = प्रणि- + ददाति)।"
    ),
    anuvritti_from   = ("8.2.1", "8.2.108"),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
