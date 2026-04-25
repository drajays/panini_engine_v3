"""
2.3.36  सप्तम्यधिकरणे च  —  SAMJNA (glass-box: *kāraka* / *vibhaktyartha* audit)

**Pāṭha (short):** *kārake* + *saptamyadhikaraṇe ca* (full *anuvṛtti* in teaching
editions).  This file records a *śālīya*-only *prayoga* note, not a second *sup*
pass.

*Engine (narrow):* when ``meta['prakriya_sAlIya']`` and **1.4.45** has
registered a locus index, and ``meta['2_3_36_sAlIya_locative_slp1']`` holds
the SLP1 string for the pedagogical *śālāyām* *prayoga* (set by
``pipelines/taddhita_salIya`` only), copy that string into
``samjna_registry[REGISTRY_KEY]`` for trace/UI.  Does **not** reattach *sup* or
mutate the running *śālīya* *prakriyā* (still *prathama* *samartha* for
**4.1.82** per recipe).  ``cond`` does not read (vibhakti, vacana) (Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_4.sutra_1_4_45 import SAMJNA_KEY as REG_1_4_45_ADH

REGISTRY_KEY = "2.3.36_sAlIya_adhikaraNa_saptamI_slp1"
META_LOCATIVE  = "2_3_36_sAlIya_locative_slp1"
META_AUTO_SET_VIBHAKTI_VACANA = "2_3_36_auto_set_vibhakti_vacana"
REGISTRY_KEY_AUTO_VV = "2.3.36_auto_vibhakti_vacana"


def cond(state: State) -> bool:
    # Generic helper (opt-in): if caller wants vibhakti selection from adhikaraṇa,
    # set vibhakti-vacana for **4.1.2** sup attachment.
    #
    # This keeps the default engine policy unchanged (recipes typically supply
    # vibhakti-vacana explicitly).  Here, 2.3.36 is allowed to *write* meta but
    # never *read* paradigm coordinates (CONSTITUTION Art. 2).
    if (
        state.meta.get(META_AUTO_SET_VIBHAKTI_VACANA)
        and not state.meta.get("vibhakti_vacana")
        and isinstance(state.samjna_registry.get(REG_1_4_45_ADH), frozenset)
        and state.samjna_registry.get(REG_1_4_45_ADH)
    ):
        return True
    if not state.meta.get("prakriya_sAlIya"):
        return False
    prev = state.samjna_registry.get(REG_1_4_45_ADH)
    if not isinstance(prev, frozenset) or not prev:
        return False
    loc = state.meta.get(META_LOCATIVE)
    if not loc or not isinstance(loc, str):
        return False
    if state.samjna_registry.get(REGISTRY_KEY) == loc:
        return False
    return True


def act(state: State) -> State:
    if (
        state.meta.get(META_AUTO_SET_VIBHAKTI_VACANA)
        and not state.meta.get("vibhakti_vacana")
        and isinstance(state.samjna_registry.get(REG_1_4_45_ADH), frozenset)
        and state.samjna_registry.get(REG_1_4_45_ADH)
    ):
        # adhikaraṇa → saptamī ekavacana (ङि) for sup attachment by 4.1.2
        state.meta["vibhakti_vacana"] = "7-1"
        state.samjna_registry[REGISTRY_KEY_AUTO_VV] = "7-1"
        return state
    loc = state.meta.get(META_LOCATIVE)
    assert isinstance(loc, str) and loc
    state.samjna_registry[REGISTRY_KEY] = loc
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.3.36",
    sutra_type     = SutraType.SAMJNA,
    # Short *pāṭha* head; *anuvṛtti* of **2.3.1** *kārake* is metalinguistic here.
    text_slp1      = "kArake saptamI adhikaraRe ca",
    text_dev       = "कारके सप्तम्यधिकरणे च",
    padaccheda_dev = "सप्तमी / अधिकरणे / च",
    why_dev        = (
        "अधिकरणे कारके सप्तमी-स्मरणम् — *śālīya* प्रक्रियायां केवल ऑडिट्; "
        "विभक्ति-निर्वाहः स्वतत्र न।"
    ),
    anuvritti_from = ("2.3.1", "1.4.45"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
