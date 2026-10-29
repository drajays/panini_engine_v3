"""
7.3.16  वर्षस्याभविष्यति  —  VIDHI

Padaccheda: वर्षस्य अभविष्यति

वर्षस्याभविष्यति (7.3.16)
Pāṭha: ashtadhyayi.com data.txt row i=73016 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_16_varzasyABa_16"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.16", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.16"
    return state


from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.vivaksha import vivaksita
from phonology import mk


def _find(state: State):
    """The first vowel of the uttarapada varṣa after a saṃkhyā (a dvigu), before a ñit / ṇit taddhita, when the speaker means a sense that is not the future (abhaviṣyati)."""
    if not vivaksita(state, "bhavizyat", "aBavizyat"):
        return None
    for pj in range(1, len(state.terms)):
        pr = state.terms[pj]
        if term_is_sup_luk_ghost(pr) or "taddhita" not in pr.tags or not ({"Y", "R", "N"} & set(pr.meta.get("it_markers", ()))):
            continue
        t = state.terms[pj - 1]
        flat = "".join(v.slp1 for v in t.varnas)
        if "lex:dvigu" not in t.tags or not flat.endswith("varza") or t.meta.get("7_3_16_done"):
            continue
        return (pj - 1, len(t.varnas) - 4)      # the a of va in …varza (the uttarapada's first vowel)
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    k, j = hit
    t = state.terms[k]
    t.varnas[j:j + 1] = [mk("A")]
    t.meta["7_3_16_done"] = True
    t.meta["7_2_117_adi_vrddhi_done"] = True      # the vṛddhi is the uttarapada's alone (dvivārṣika, not dvaivārṣika)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varzasyABavizyati",
    text_dev              = "वर्षस्याभविष्यति",
    samagra_slp1          = "aNgasya uttarapadasya varzasya aBavizyati vfdDiH YRiti acaH tadDitezu AdeH SvAdeH saMKyAyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उत्तरपदस्य वर्षस्य अभविष्यति वृद्धिः ञ्णिति अचः तद्धितेषु आदेः श्वादेः संख्यायाः",
    padaccheda_dev        = "वर्षस्य अभविष्यति",
    why_dev               = "(सूत्रम् 7.3.16) वर्षस्याभविष्यति।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ('7.2.117',),   # the uttarapada's vṛddhi takes the place of the ādi-vṛddhi of the aṅga
    also_vidhi            = True,          # the loop applies it to a dvigu ending in varṣa
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
