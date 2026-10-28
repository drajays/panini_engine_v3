"""
7.3.20  अनुशतिकादीनां च  —  VIDHI

Padaccheda: अनुशतिक-आदीनाम् च

अनुशतिकादीनां च (7.3.20)
Pāṭha: ashtadhyayi.com data.txt row i=73020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_20_anuSatikAd_20"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.20", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.20"
    return state


from engine import gana
from engine.lopa_ghost import term_is_sup_luk_ghost
from phonology import mk

# SHORTCUT S30: the pūrvapada of each anuśatikādi stem (the gaṇa lists the compounds whole, the stem is one Term) — until a samāsa is a pair of Terms.
_PURVA = {"anuSatika": "anu", "anuhoqa": "anu", "anusaMvaraRa": "anu", "anusaMcaraRa": "anu", "anusaMvatsara": "anu", "aNgAraveRu": "aNgAra", "asihatya": "asi",
          "puzkarasad": "puzkara", "anuharat": "anu", "kurukata": "kuru", "kurupaYcAla": "kuru", "udakaSudDa": "udaka", "ihaloka": "iha", "paraloka": "para",
          "sarvaloka": "sarva", "sarvapuruza": "sarva", "sarvaBUmi": "sarva", "prayoga": "pra", "parastrI": "para", "sUtranaqa": "sUtra", "aBigama": "aBi",
          "aDiBUta": "aDi", "aDideva": "aDi", "caturvidyA": "catur"}
_AC = "aAiIuUfFxXeEoO"
_VRDDHI = {"a": "A", "A": "A", "i": "E", "I": "E", "u": "O", "U": "O", "e": "E", "E": "E", "o": "O", "O": "O", "f": "Ar", "F": "Ar", "x": "Al", "X": "Al"}


def _find(state: State):
    """(term index, varna index) of the first vowel of the uttarapada of an anuśatikādi stem before a ñit / ṇit taddhita."""
    for pj in range(1, len(state.terms)):
        pr = state.terms[pj]
        if term_is_sup_luk_ghost(pr) or "taddhita" not in pr.tags or not ({"Y", "R", "N"} & set(pr.meta.get("it_markers", ()))):
            continue
        k = pj - 1
        t = state.terms[k]
        flat = "".join(v.slp1 for v in t.varnas)
        key = next((m for m in _PURVA if gana.in_gana("anuSatikAdiH", m) and _same(m, flat)), None)
        if key is None or t.meta.get("7_3_20_done"):
            continue
        n = sum(c in _AC for c in _PURVA[key])           # acs of the pūrvapada; the next ac begins the uttarapada
        seen = 0
        for j, v in enumerate(t.varnas):
            if v.slp1 in _AC:
                if seen == n:
                    return (k, j) if v.slp1 in _VRDDHI and _VRDDHI[v.slp1] != v.slp1 else None
                seen += 1
    return None


def _same(stem: str, flat: str) -> bool:
    """``flat`` is ``stem`` itself or the stem after the vṛddhi of its first vowel (7.2.117)."""
    i = next(i for i, c in enumerate(stem) if c in _AC)
    return flat == stem or (len(flat) == len(stem) and flat[:i] == stem[:i] and flat[i + 1:] == stem[i + 1:] and _VRDDHI.get(stem[i]) == flat[i])


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
    t.varnas[j:j + 1] = [mk(c) for c in _VRDDHI[t.varnas[j].slp1]]
    t.meta["7_3_20_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anuSatikAdInAM ca",
    text_dev              = "अनुशतिकादीनां च",
    samagra_slp1          = "aNgasya uttarapadasya anuSatikAdInAm ca vfdDiH acaH YRiti tadDitezu AdeH pUrvapadasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उत्तरपदस्य अनुशतिकादीनाम् च वृद्धिः अचः ञ्णिति तद्धितेषु आदेः पूर्वपदस्य",
    padaccheda_dev        = "अनुशतिक-आदीनाम् च",
    why_dev               = "(सूत्रम् 7.3.20) अनुशतिकादीनां च।",
    anuvritti_from        = ('7.1.1',),
    also_vidhi            = True,          # the loop applies it (ubhayapada-vṛddhi) to the stems of the gaṇa
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
