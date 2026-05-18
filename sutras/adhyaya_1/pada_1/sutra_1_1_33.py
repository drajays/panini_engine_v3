"""
1.1.33  prathamacamatayālpārdhakatipayanemāśca  —  SAMJNA

*Anuvṛtti*: sarvanāma from **1.1.27**.

**Pāṭha:** prathama, carama, taya, alpa, ardha, katipaya, nema — these (*ca*)
also receive *sarvanāma*-saṃjñā (in addition to the *sarvādi*-gaṇa words of
**1.1.27**).

This extends the *sarvanāma*-saṃjñā to the *prathamādi*-group: stems that are
not in the *sarvādi* gaṇa-pāṭha but behave like *sarvanāma*s for the purpose
of sup-vibhakti operations (e.g. **7.1.16** *jasaḥ śī*).

v3:
  - Module-level frozenset ``PRATHAMADI_SLP1`` contains the seven SLP1 forms.
  - ``cond``: any *aṅga* + *prātipadika* Term whose ``upadesha_slp1`` is in the
    set and does not yet have tag ``sarvanama``.
  - ``act``: add ``sarvanama`` tag; set ``samjna_registry['1_1_33_praTamAdi']``.
  - ``r1_form_identity_exempt=True`` — no surface change.

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only ``Term.meta['upadesha_slp1']`` and Term.tags.
  - No paradigm coordinates, no Devanāgarī strings.
"""
from __future__ import annotations

from typing import FrozenSet

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# SLP1 prātipadika forms of the prathamādi-group (1.1.33).
PRATHAMADI_SLP1: FrozenSet[str] = frozenset({
    "praTama",   # प्रथम
    "carama",    # चरम
    "taya",      # तय
    "alpa",      # अल्प
    "arDa",      # अर्ध
    "katipaya",  # कतिपय
    "nema",      # नेम
})

# Registry key for this rule.
REGISTRY_KEY: str = "1_1_33_praTamAdi"


def _eligible(state: State):
    """Yield aṅga+prātipadika Terms in the prathamādi set not yet tagged sarvanama."""
    for t in state.terms:
        if "anga" not in t.tags:
            continue
        if "prātipadika" not in t.tags:
            continue
        if "sarvanama" in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if not isinstance(upa, str):
            continue
        if upa in PRATHAMADI_SLP1:
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry[REGISTRY_KEY] = PRATHAMADI_SLP1
    for t in _eligible(state):
        t.tags.add("sarvanama")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.33",
    sutra_type     = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1      = "praTamacaramatayAlpArDakatipayanemASca",
    text_dev       = "प्रथमचरमतयाल्पार्धकतिपयनेमाश्च",
    padaccheda_dev = "प्रथम-चरम-तय-अल्प-अर्ध-कतिपय-नेमाः च (सर्वनाम-संज्ञा)",
    why_dev        = "प्रथमादि-शब्दाः (सप्त) च सर्वनाम-संज्ञकाः — १.१.२७-अनुवृत्त्या।",
    anuvritti_from = ("1.1.27",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["PRATHAMADI_SLP1", "REGISTRY_KEY", "SUTRA"]
