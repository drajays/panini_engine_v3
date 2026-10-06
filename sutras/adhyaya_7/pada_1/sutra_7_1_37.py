"""
7.1.37  समासेऽनञ्पूर्वे क्त्वो ल्यप्  —  VIDHI (narrow: ktvā → lyap)

Sources consulted:
- ashtadhyayi.com data.txt row i=71037
- Kāśikā: "प्रकृत्य, प्रहृत्य"
- Cross-validation: pipelines/prakftya_lyap_split_prakriyas.py,
  tests/unit/test_agaty_gam_lyap_acah_lesson.py

**1.1.56** extends *kṛt-pratyayatva*, *kit* it-saṃjñā (from *ktvā*), and *avyayatva* to *lyap*.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import AVYAYATVA, KRT_PRATYAYATVA, adesha_substitute_varnas


def _find_ktva(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        orig = (t.meta.get("upadesha_slp1_original") or "").strip()
        if orig == "ktvA":
            return i
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"ktvA", "itvA", "tvA"}:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("lyap_recipe"):
        return False
    i = _find_ktva(state)
    if i is None:
        return False
    return not state.terms[i].meta.get("7_1_37_ktvA_to_lyap_done")


def act(state: State) -> State:
    i = _find_ktva(state)
    if i is None:
        return state
    pr = state.terms[i]
    adesha_substitute_varnas(
        pr,
        "lyap",
        state,
        sutra_id="7.1.37",
        gunadharmas=frozenset({KRT_PRATYAYATVA, AVYAYATVA}),
    )
    pr.tags.add("upadesha")
    pr.meta["7_1_37_ktvA_to_lyap_done"] = True
    state.meta["lyap_recipe"] = False
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.37",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'samAsenaYpUrve ktvo lyap',
    text_dev       = 'समासेऽनञ्पूर्वे क्त्वो ल्यप्',
    samagra_slp1   = "aNgasya samAse anaYpUrve ktvaH lyap anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "अङ्गस्य समासे अनञ्पूर्वे क्त्वः ल्यप् अन्यतरस्याम्",
    padaccheda_dev = "समासे / अनञ्-पूर्वे / क्त्वः / ल्यप्",
    why_dev        = "उपसर्गादि-पूर्वे क्त्वा-प्रत्ययस्य ल्यप्-आदेशः (नरूप्य-डेमो)।",
    anuvritti_from = ("7.1.12",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

