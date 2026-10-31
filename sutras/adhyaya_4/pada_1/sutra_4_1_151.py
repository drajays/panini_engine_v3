"""
4.1.151  कुर्वादिभ्यो ण्यः  —  VIDHI

Padaccheda: कुरु-आदिभ्यः ण्यः

कुर्वादिभ्यो ण्यः (4.1.151)
Pāṭha: ashtadhyayi.com data.txt row i=41151 (Art. 14).

The Gaṇapāṭha kurvādi (kuru, gargara, maṅguṣa …) takes ṇya in the offspring sense, displacing the aṇ of 4.1.83 (Kāśikā: kauravyaḥ, vāvadūkyaḥ).
The kṣatriya-janapada reading of kuru (4.1.172 kurunādibhyo ṇyaḥ) is a separate sūtra.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine       import gana
from engine.taddhita_attach import taddhita_site, attach_taddhita

_GATE_KEY: str = "4_1_151_kurvAdiByo_151"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.151", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.151"
    return state


def _site(state: State):
    t = taddhita_site(state, "apatya", gana_name="kurvAdiH")
    if t is None:
        return None
    # SHORTCUT S110: a stem listed in both kurvādi and śubhrādi (śubhra: śaubhreyaḥ by 4.1.123, śaubhryaḥ by this sūtra) keeps its ḍhak reading only; the loop does not explore
    # the vikalpa between two competing sūtras (S45 / S52), and para 4.1.151 would otherwise displace the Kāśikā's udāharaṇa śaubhreyaḥ.
    return None if gana.in_gana_of_sutra("4.1.123", t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)) else t


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    if _site(state) is None:
        return _legacy_act(state)
    return attach_taddhita(state, "Rya")


SUTRA = SutraRecord(
    sutra_id              = "4.1.151",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kurvAdiByo RyaH",
    text_dev              = "कुर्वादिभ्यो ण्यः",
    samagra_slp1          = "tasya apatyam iti kurvAdiByaH RyaH",
    samagra_dev           = "'तस्य अपत्यम्' (इति) कुर्वादिभ्यः ण्यः",
    padaccheda_dev        = "कुरु-आदिभ्यः ण्यः",
    why_dev               = "(सूत्रम् 4.1.151) कुर्वादिभ्यो ण्यः।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
