"""
1.4.18  असर्वनामस्थाने सुँ-आदिषु यचि भम्  —  SAMJNA (*bha*)

*Padaccheda (śāstra):* **यचि** (saptamī-ekavacana), **भम्**
(prathamā-ekavacana).

*Anuvṛtti:* from **1.4.17** — *svādiṣu*, *asarvanāmasthāne*; *adhikāra*
**1.4.1** (*ā kaḍārād ekā saṃjñā*).

*Bādhyabādaka:* *bha* from this rule **bādhate** *pada* from **1.4.17** on the
same *prakṛti* (so *pada*-keyed operations such as **8.2.7** do not misfire on
*bha*-stems like *rājan* + *śas*).  Conversely, when **1.4.16** (*siti ca*) has
assigned ``pada_1_4_16``, *bha* does not apply (*ūrṇā* + *yus*).

Operational: tag the *aṅga* ``Term`` with ``bha`` and record indices under
``samjna_registry['1.4.18_bha_anga_indices']``; strip ``pada_1_4_17`` when *bha*
wins.

*Case B (``pipelines/taddhita_salIya``):* after **7.1.2** the *taddhita* may be *Iya*
(*Ī*-*ādi*).  ``yaci_onset_loose`` uses ``AC`` without long ``I``/``A``/``U``; for *Iya* we
also allow an initial dīrgha in ``_taddhite_yaci_anga_ok``.  The *aṅga* *before* that
*pratyaya* is tagged *bha* for the *śālīya* *trace* and **6.4.148** pedagogy.
*Case C* (``prakriya_itika_phak``; ``pipelines/taddhita_itika_etikAyana``): after
**7.1.2** the *taddhita* is *Āyana* (*A*-*ādi*); *bha* for **6.4.148** + **1.1.60** *trace*.

First sound of the affix is read from ``Term.varnas[0]`` after the engine's
*it*-pass (**1.3.9**).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_4.samjna_sup_prakriti_1_4 import (
    is_sarvanamasthana_sup,
    yaci_onset_loose,
)

_REGISTRY_BHA_INDICES = "1.4.18_bha_anga_indices"

# Engine ``AC`` in ``pratyahara`` is *a*..*e* (no separate long ``I`` / ``U`` / ``A``),
# so *Iya*'s *Ī*-*ādi* fails ``yaci_onset_loose``; *śikṣ* *yaci* includes dīrgha *ac* here.
# Long-vowel *ac* onsets not present in the engine’s ``pratyahara.AC`` bitvector.
_DĪRGHĀC_FIRST = frozenset({"A", "I", "U"})


def _taddhite_yaci_anga_ok(pr) -> bool:
    if yaci_onset_loose(pr):
        return True
    if not pr.varnas:
        return False
    return pr.varnas[0].slp1 in _DĪRGHĀC_FIRST


def _eligible_anga_indices(state: State):
    for i in range(len(state.terms) - 1):
        anga, pr = state.terms[i], state.terms[i + 1]
        if "anga" not in anga.tags:
            continue
        if "sup" in pr.tags:
            if "pada_1_4_16" in anga.tags:
                continue
            if is_sarvanamasthana_sup(pr, anga):
                continue
            if not yaci_onset_loose(pr):
                continue
            if "bha" in anga.tags:
                continue
            yield i
            continue
        if (
            state.meta.get("prakriya_sAlIya")
            and "taddhita" in pr.tags
            and "pratyaya" in pr.tags
        ):
            if "pada_1_4_16" in anga.tags:
                continue
            if not _taddhite_yaci_anga_ok(pr):
                continue
            if "bha" in anga.tags:
                continue
            yield i
            continue
        if (
            state.meta.get("prakriya_itika_phak")
            and "taddhita" in pr.tags
            and "pratyaya" in pr.tags
        ):
            if "pada_1_4_16" in anga.tags:
                continue
            if not _taddhite_yaci_anga_ok(pr):
                continue
            if "bha" in anga.tags:
                continue
            yield i


def cond(state: State) -> bool:
    return next(_eligible_anga_indices(state), None) is not None


def act(state: State) -> State:
    prev = state.samjna_registry.get(_REGISTRY_BHA_INDICES)
    if not isinstance(prev, frozenset):
        prev = frozenset()
    new_idx: set[int] = set(prev)
    for i in _eligible_anga_indices(state):
        anga = state.terms[i]
        anga.tags.add("bha")
        anga.tags.discard("pada_1_4_17")
        anga.tags.discard("pada_1_4_16")
        new_idx.add(i)
    state.samjna_registry[_REGISTRY_BHA_INDICES] = frozenset(new_idx)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.18",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "asarvanAmasthAne su~Adizu yaci Bham",
    text_dev       = "असर्वनामस्थाने सुँआदिषु यचि भम्",
    padaccheda_dev = "असर्वनामस्थाने सुँ-आदिषु यचि भम्",
    why_dev        = (
        "स्वादि-प्रत्यये असर्वनामस्थानके यकारादौ वा अजादौ आदौ च परे "
        "प्रकृतेः भ-संज्ञा; पद-संज्ञां (१.४.१७) बाधते।"
    ),
    anuvritti_from = ("1.4.1", "1.4.17"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
