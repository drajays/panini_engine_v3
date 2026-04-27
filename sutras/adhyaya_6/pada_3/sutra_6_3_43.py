"""
6.3.43  घ्यप्कल्पचेलड्… ङ्योऽनेकाचो ह्रस्वः  —  VIDHI (narrow *ṅy*ant + *anekāca* + *gha*)

*Kāśikā* *prayoga* (``kumari.md``): *kumArI* + *tar*/*tam* (***gha***, **1.1.22**) → *ī* → *i*.

v3: ``state.meta['6_3_43_NGy_hrasva_arm']``; *aṅga* *strī*; final **I** (*ṅy* proxy); *taddhita*
*upadeśa* *tarap* / *tamap*; ``count_vowel_letters(anga_flat) > 1``; rightmost mappable dīrgha
in ``_D2H`` → hrasva.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import is_dirgha, mk
from phonology.pratyahara import count_vowel_letters

from sutras.adhyaya_1.pada_1.sutra_1_1_22 import taddhita_pratyaya_upadesha_slp1_is_gha

# Narrow *dīrgha* → hrasva (SLP1) for this *corpus* slice.
_D2H: dict[str, str] = {
    "A": "a",
    "I": "i",
    "U": "u",
    "F": "f",
    "X": "x",
}


def _rightmost_map_index(anga: Term) -> int | None:
    for i in range(len(anga.varnas) - 1, -1, -1):
        s = anga.varnas[i].slp1
        if is_dirgha(s) and s in _D2H:
            return i
    return None


def _site(state: State) -> int | None:
    if not state.meta.get("6_3_43_NGy_hrasva_arm"):
        return None
    if len(state.terms) < 2:
        return None
    an, td = state.terms[0], state.terms[1]
    if "strīliṅga" not in an.tags or "prātipadika" not in an.tags or "anga" not in an.tags:
        return None
    if "taddhita" not in td.tags or "pratyaya" not in td.tags:
        return None
    u = (td.meta.get("upadesha_slp1") or "").strip()
    if u not in {"tarap", "tamap"}:
        return None
    if not taddhita_pratyaya_upadesha_slp1_is_gha(state, u):
        return None
    if an.meta.get("6_3_43_hrasva_done"):
        return None
    if not an.varnas:
        return None
    # *ṅy* anta: glass-box *corpus* uses long final *ī* (SLP1 ``I``) on the *aṅga*.
    if an.varnas[-1].slp1 != "I":
        return None
    flat = "".join(v.slp1 for v in an.varnas)
    if count_vowel_letters(flat) < 2:
        return None
    if _rightmost_map_index(an) is None:
        return None
    return 0


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    an = state.terms[0]
    i = _rightmost_map_index(an)
    if i is None:
        return state
    s = an.varnas[i].slp1
    h = _D2H.get(s)
    if h is None:
        return state
    an.varnas[i] = mk(h)
    an.meta["6_3_43_hrasva_done"] = True
    state.meta.pop("6_3_43_NGy_hrasva_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.3.43",
    sutra_type=SutraType.VIDHI,
    text_slp1="Ghyapkalpacelaq bruvagotrImatahatezy Nyor anekAco hrasvaH",
    text_dev="घ…ङ्यो… अनेकाचो ह्रस्वः",
    padaccheda_dev="घ-प्रत्यय-औ / ङि-अनिक / ह्रस्वः",
    why_dev="घ-संज्ञक-तद्धिते *ङ्य*न्त-अनेकाच-अङ्गे अन्त्य-दीर्घस्य ह्रस्वः (अ।)",
    anuvritti_from=("6.3.1", "6.3.114"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
