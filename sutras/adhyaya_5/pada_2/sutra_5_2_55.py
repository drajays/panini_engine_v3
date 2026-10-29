"""
5.2.55  त्रेः सम्प्रसारणं च  —  VIDHI

Padaccheda: त्रेः सम्प्रसारणम् च

त्रेः सम्प्रसारणम् च (5.2.55)
Pāṭha: ashtadhyayi.com data.txt row i=52055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_55_treH_55"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.55", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.55"
    return state


# SHORTCUT S43: saṃkhyā / saṃkhyādi are lex: tags from the caller (S33)
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, None, ok=vivaksita(state, "taddhitArtha", "tasyapUraRa"), stems=frozenset({"tri"}))


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    del t.varnas[-2:]                    # SHORTCUT S40: samprasāraṇa of tri done here (r -> ṛ, the i taken by 6.1.108), not through 1.1.45 / 6.1.108 (dhātu-bound)
    from phonology.varna import parse_slp1_upadesha_sequence
    t.varnas.extend(parse_slp1_upadesha_sequence("f"))
    return attach_taddhita(state, "tIya")


SUTRA = SutraRecord(
    sutra_id              = "5.2.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'treH samprasAraRaM ca',
    text_dev              = 'त्रेः सम्प्रसारणं च',
    samagra_slp1          = "tasya pUraRe iti treH tIyaH samprasAraRam ca",
    samagra_dev           = "'तस्य पूरणे' (इति) त्रेः तीयः, सम्प्रसारणम् च",
    padaccheda_dev        = "त्रेः सम्प्रसारणम् च",
    why_dev               = "(सूत्रम् 5.2.55) त्रेः सम्प्रसारणम् च।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.48',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
