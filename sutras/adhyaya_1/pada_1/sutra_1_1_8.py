"""
1.1.8  मुखनासिकावचनोऽनुनासिकः  (mukhanAsikAvacano anunAsikaH)  —  SAMJNA

**Śāstra-artha:** यस्य वर्णस्य उच्चारणे मुखेन सह नासिकायाः अपि प्रयोगः भवति,
सः वर्णः **अनुनासिक-संज्ञकः**।  'अनुनासिकः' इति पृथक् वर्णः नास्ति; विद्यमानस्य
वर्णस्यैव नासिकया सह उच्चारणे (चन्द्रबिन्दु-निर्देशे) एषा संज्ञा भवति।

**अनुनासिक-संज्ञायाः सूत्रेषु साक्षात् प्रयोगः (११):**

1) 1.3.2  उपदेशेऽजनुनासिक इत्
2) 6.1.126  आङोऽनुनासिकश्छन्दसि
3) 6.4.15  अनुनासिकस्य क्विझलोः क्ङिति
4) 6.4.19  च्छ्वोः शूडनुनासिके च
5) 6.4.37  अनुदात्तोपदेशवनतितनोत्यादीनामनुनासिक लोपो झलि क्ङिति
6) 6.4.41  विड्वनोरनुनासिकस्यात्
7) 7.4.45  नुगतोऽनुनासिकान्तस्य
8) 8.3.2  अत्रानुनासिकः पूर्वस्य तु वा
9) 8.3.4  अनुनासिकात् परोऽनुस्वारः
10) 8.4.45  यरोऽनुनासिकेऽनुनासिको वा
11) 8.4.57  अणोऽप्रगृह्यस्यानुनासिकः

अनुवृत्तिरूपेण तु अन्येषु सूत्रेषु अपि अस्याः संज्ञायाः प्रयोगः भवितुम् अर्हति।

v3: registers the global *anunāsika* saṃjñā in ``samjna_registry`` (R2).  **Operational**
marking of varṇas is by the ``anunasika`` tag (see ``1.3.2``, ``phonology.tokenizer``,
``phonology/joiner``) — this sūtra is the *śāstrīya* anchor; *vidhi* sūtras read tags +
``pratyahara``/``Varna.slp1`` only (CONSTITUTION Art. 2).

See also **1.1.9** (``sutra_1_1_9``) for *savarṇa*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Varna

# R2: canonical value after ``apply_rule("1.1.8", ...)`` .
ANUNASIKA_REGISTER_VALUE: frozenset[str] = frozenset({"1.1.8_mukhanasikA"})


def is_varna_tagged_anunAsika(v: Varna) -> bool:
    """True iff this varṇa carries the engine's *anunāsika* tag (1.1.8 scope in prakriyā)."""
    return "anunasika" in v.tags


def is_anusvara_slp1(slp1: str) -> bool:
    """``M`` = anusvāra (ं) in SLP1 surface encoding (separate varṇa; not chandrabindu)."""
    return slp1 == "M"


def anunAsika_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get("anunAsika") == ANUNASIKA_REGISTER_VALUE


# ════════════════════════════════════════════════════════════
# Sūtra — *anunāsika* definiens once (like 1.1.1 / 1.1.7)
# ════════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    return not anunAsika_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry["anunAsika"] = ANUNASIKA_REGISTER_VALUE
    return state


_WHY = (
    "यस्य वर्णस्य उच्चारणार्थं मुखेन सह नासिकायाः अपि प्रयोगः भवति, "
    "सः वर्णः 'अनुनासिक' इति संज्ञां प्राप्नोति।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.8",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "mukhanAsikAvacano anunAsikaH",
    text_dev       = "मुखनासिकावचनोऽनुनासिकः",
    padaccheda_dev = "मुख-नासिका-वचनः / अनुनासिकः",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
