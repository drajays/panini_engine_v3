"""
1.4.17  स्वादिष्वसर्वनामस्थाने  —  SAMJNA (*pada* on *prakṛti*)

*Anuvṛtti* **1.4.1** (*ā kaḍārād ekā saṃjñā*); reading: *svādiṣv asarvanāmasthāne*
— before a non-*sarvanāmasthāna* *svādi* affix, the *prātipadika* / *aṅga*
receives *pada* tagging ``pada_1_4_17``.

This *pada* is **bādhyate** by *bha* from **1.4.18** when **1.4.18** also
applies (e.g. *rājan* + *śas* — *bha* blocks unwanted *pada*-driven **8.2.7**
*n*-lopa in fuller Tripāḍī scope).
Pāṭha: ashtadhyayi.com data.txt row i=14017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state  import State
from engine.samjna_sup_prakriti import (
    yaci_onset_loose,
    is_asarvanamasthana_svadi_sup,
)


_REGISTRY = "1.4.17_pada_anga_indices"


def _wit_agama_of_taddhita(state: State, i: int) -> bool:
    """A ṭit āgama is the first part of the pratyaya it stands before (1.1.46): maṭ of ḍaṭ (5.2.49) makes pañcan pada before the m."""
    pr = state.terms[i + 1]
    return ("agama" in pr.tags and "it:wit" in pr.tags and bool(pr.varnas) and i + 2 < len(state.terms)
            and {"taddhita", "pratyaya"} <= state.terms[i + 2].tags)


def _adesha_pending(state: State) -> bool:
    from engine.registry import get_sutra
    return any(get_sutra(sid).cond(state) for sid in ("7.1.2", "7.3.50", "7.3.51"))


def _eligible(state: State):
    for i in range(len(state.terms) - 1):
        anga, pr = state.terms[i], state.terms[i + 1]
        if not (is_asarvanamasthana_svadi_sup(pr, anga) or ("anga" in anga.tags and _wit_agama_of_taddhita(state, i))):
            continue
        if "pada_1_4_17" in anga.tags:
            continue
        if "taddhita" in pr.tags and "sup" not in pr.tags and _adesha_pending(state):
            continue    # the deck: it-lopa, then any ādeśa of the pratyaya (ṭhasyekaḥ 7.3.50, isusuktāntāt kaḥ 7.3.51, āyaneyīnīyiyaḥ 7.1.2), then decide pada / bha on what stands
        if "pada_1_4_16" in anga.tags:
            continue
        if "bha" in anga.tags:  # 1.4.18 is apavāda: bha blocks pada re-entry
            continue
        # आ कडारादेका संज्ञा (1.4.1) + विप्रतिषेधे परं कार्यम् (1.4.2): before a
        # yac-initial pratyaya 1.4.18 भ is the one saṃjñā — pada never applies
        if yaci_onset_loose(pr) and not ("sup" in pr.tags and pr.varnas[0].slp1 in ("z", "s")):
            continue    # su (loc. pl.) is not yaci (as in 1.4.18): its stem is pada by this sūtra, rājasu
        yield i


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    prev = state.samjna_registry.get(_REGISTRY)
    if not isinstance(prev, frozenset):
        prev = frozenset()
    new_idx: set[int] = set(prev)
    for i in _eligible(state):
        state.terms[i].tags.add("pada_1_4_17")
        state.terms[i].tags.add("pada")        # needed for 8.2.66 pre-merge rutva
        new_idx.add(i)
    state.samjna_registry[_REGISTRY] = frozenset(new_idx)
    state.meta["__why_now_dev__"] = (
        "असर्वनामस्थान-स्वादि-प्रत्यये परे प्रातिपदिकम् 'पद'-संज्ञां प्राप्नोति; "
        "अनया पदाश्रित-कार्याणि (यथा ८.२.७ न-लोपः) प्रवर्तन्ते। (१.४.१७)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.17",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'svAdizvasarvanAmasTAne',
    text_dev       = 'स्वादिष्वसर्वनामस्थाने',
    samagra_slp1   = "asarvanAmasTAne su~-Adizu padam",
    samagra_dev    = "असर्वनामस्थाने सुँ-आदिषु   पदम्",
    padaccheda_dev = "स्वादिषु असर्वनामस्थाने",
    why_dev        = "असर्वनामस्थान-स्वादि-प्रत्यये परे प्रातिपदिकस्य पदसंज्ञा।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
