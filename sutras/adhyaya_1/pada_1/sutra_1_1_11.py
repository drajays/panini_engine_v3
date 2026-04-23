"""
1.1.11  ईदूदेद्द्विवचनं प्रगृह्यम्  (IdUdeddvivacanaM pragfhyam)  —  SAMJNA

**Śāstra (GRETIL pāṭha):** a *dvivacana* (dual) *pada* whose *anta* (in the *anuvṛtti*
scope of this *ūha*) is *ī, ū, e, ai, o, or au* is called *pragṅhya* (to be
“held” – no *lopa* of final vowel in certain *sandhi* contexts that name *pragṅhya*).

v3: **R2** — ``act`` writes the definiens to ``samjna_registry['pragrahya']`` (vowel
phonemes, SLP1) *and*, in ``act`` only, may add the ``pragrahya`` tag to *prātipadika*/*aṅga*
**Term**s when ``state.meta['vibhakti_vacana']`` encodes *dvivacana* (see ``pipelines/subanta``).
``cond`` does **not** read *vibhakti* / *vacana* (CONSTITUTION Art. 2).

See also **1.1.12** (``sutra_1_1_12``) — *adaso māt* (paribhāṣā for *a*ś *it* on
*etad* / *adas* *aṅga*, with **1.1.11** *pragṛhya* in *dvivacana*);
**1.1.13** (``sutra_1_1_13``) for *śe* ( *aś* / *ś* locus, *Kāśikā* *vṛtti* on *pragṛhya* *prayoga* off);
**1.1.14** (``sutra_1_1_14``) for *nipāta ekājanāṅ* ( *pragṛhya* for one-vowel *nipāta*, not *ā*ṅ);
**1.1.100** (``sutra_1_1_100``) — *Kāśikā* *na mātrā samāse* ( *vṛtti* extension, not the Pāṇini *1.1.14* pāṭha);
**1.1.19** (``sutra_1_1_19``) for *Ī* / *Ū* + *tau* with *saptamī*-*artha* (ashtadhyayi *i* 11019).
"""
from __future__ import annotations

from typing import FrozenSet

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# ī, ū, e, ai, o, au — SLP1 (E, O align with 1.1.1 for *ai* / *au* diphthongs).
PRAGHYA_VOWEL_SLP1: FrozenSet[str] = frozenset({"I", "U", "e", "E", "o", "O"})

# Term-level *pragṛhya* mark (when **1.1.11** *prayoga* applies in *dvivacana*).
PRAGHYA_TERM_TAG: str = "pragrahya"


def is_pragrahya_slp1_vowel(slp1: str) -> bool:
    """True iff ``slp1`` is one of the *ī, ū, e, ai, o, au* definienda (1.1.11)."""
    return slp1 in PRAGHYA_VOWEL_SLP1


def pragrahya_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get("pragrahya") == PRAGHYA_VOWEL_SLP1


def _vacana_from_meta(state: State) -> int | None:
    """*Vacana* digit from ``vibhakti_vacana`` in ``act`` only (e.g. ``'1-2'`` → ``2``)."""
    raw = state.meta.get("vibhakti_vacana")
    if not raw or not isinstance(raw, str) or "-" not in raw:
        return None
    try:
        return int(raw.rsplit("-", 1)[1])
    except (ValueError, IndexError):
        return None


def _tag_dvivacana_praghy_terms(state: State) -> None:
    if _vacana_from_meta(state) != 2:  # dvivacana
        return
    for t in state.terms:
        if not ({"prātipadika", "anga"} & t.tags):
            continue
        fin = t.final_varna
        if fin and is_pragrahya_slp1_vowel(fin.slp1):
            t.tags.add(PRAGHYA_TERM_TAG)


def cond(state: State) -> bool:
    return not pragrahya_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry["pragrahya"] = PRAGHYA_VOWEL_SLP1
    _tag_dvivacana_praghy_terms(state)
    return state


_WHY = (
    "द्विवचनान्ते ई-कार-ऊ-कार-ए-ऐ-ओ-औ, ते 'प्रगृह्य' संज्ञिनः; "
    "सन्धौ न लोप-ग्रहः (उत्सर्ग-नियमः)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.11",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "IdUdeddvivacanaM pragfhyam",
    text_dev       = "ईदूदेद्द्विवचनं प्रगृह्यम्",
    padaccheda_dev = "द्विवचनं ईदूदैदौ प्रगृह्यम्",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
