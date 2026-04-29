"""
1.2.5  असंयोगाल्लिट् कित्  —  SAMJNA (narrow demo)

Demo slice (विभिदतुः):
  In liṭ, when the dhātu does not end in a consonant cluster (a-saṃyoga),
  treat the liṭ parasmaipada ending (here `atus`) as *kit* → behaves like
  kṅit for guṇa blocking (via **1.1.5 kṅiti** gate contract).

Engine:
  - tags the relevant pratyaya Term with ``kngiti``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _dhatu_ends_in_samyoga(state: State) -> bool:
    if not state.terms:
        return False
    dh = state.terms[0]
    if not dh.varnas:
        return False
    # Narrow: detect two final consonants.
    hal = {"k","K","g","G","N","c","C","j","J","Y","w","W","q","Q","R","t","T","d","D","n","p","P","b","B","m","y","r","l","v","S","z","s","h"}
    if len(dh.varnas) < 2:
        return False
    return dh.varnas[-1].slp1 in hal and dh.varnas[-2].slp1 in hal


def _find_pratyaya(state: State) -> int | None:
    if state.samjna_registry.get("1.2.5_asamyogal_lit_kit") is True:
        return None
    if not state.meta.get("lakara_liT"):
        return None
    if _dhatu_ends_in_samyoga(state):
        return None
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"atus", "Ralatus"} or t.meta.get("lit_atus") is True:
            if "kngiti" in t.tags:
                return None
            return i
    return None


def cond(state: State) -> bool:
    return _find_pratyaya(state) is not None


def act(state: State) -> State:
    i = _find_pratyaya(state)
    if i is None:
        return state
    state.terms[i].tags.add("kngiti")
    state.samjna_registry["1.2.5_asamyogal_lit_kit"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.5",
    sutra_type=SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1="asaMyogAlliT kit",
    text_dev="असंयोगाल्लिट् कित्",
    padaccheda_dev="असंयोगात् / लिट् / कित्",
    why_dev="लिटि असंयोगान्त-धातोः परे प्रत्ययः कित्-वत् (गुण-निषेध-प्रसङ्गः)।",
    anuvritti_from=("1.2.4",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

