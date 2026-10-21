"""
7.1.37  समासेऽनञ्पूर्वे क्त्वो ल्यप्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=71037 (its `an` lists अन्यतरस्याम् from 71035 — over-carried; owner ruling
  docs/SOURCE_CONFLICTS.md SC-004: nitya in bhāṣā, by the jñāpaka 7.1.38 क्त्वाऽपि छन्दसि, Kāśikā and SK)
- Kāśikā: "समासेऽनञ्पूर्वे क्त्वा इत्येतस्य ल्यबित्ययमादेशो भवति। प्रकृत्य। प्रहृत्य।"
  pratyudāharaṇa: "समास इति किम्? कृत्वा। हृत्वा। अनञ्पूर्व इति किम्? अकृत्वा। अहृत्वा।"
- Padamañjarī: "प्रकृत्येति। समानकर्तृकयोः पूर्वकाले इति क्त्वा, कुगतिप्रादयः इति समासः, ल्यपि सति ह्रस्वस्य तुक्।"
- Cross-validation: tests/regression/test_ktva_loop.py (प्रकृत्य, आगत्य, प्रपठ्य, निशम्य through the loop);
  tests/unit/test_prakftya_lyap_split_prakriyas.py, tests/unit/test_agaty_gam_lyap_acah_lesson.py

समासे: the ktvā belongs to a compound — a pūrvapada (2.2.18 tags the gati) stands before its dhātu. अनञ्पूर्वे: no
pūrvapada of that compound is nañ. **1.1.56** extends kṛt-pratyayatva, kit it-saṃjñā (from ktvā) and avyayatva to lyap.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import AVYAYATVA, KRT_PRATYAYATVA, adesha_substitute_varnas

_NAN = frozenset({"naY", "a", "an"})


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


def _in_anan_samasa(state: State, k: int) -> bool:
    purva = [t for t in state.terms[:k] if "samasa_purvapada" in t.tags]
    return bool(purva) and not any((t.meta.get("upadesha_slp1") or "").strip() in _NAN for t in purva)


def cond(state: State) -> bool:
    i = _find_ktva(state)
    if i is None or state.terms[i].meta.get("7_1_37_ktvA_to_lyap_done"):
        return False
    return _in_anan_samasa(state, i)


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
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.37",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'samAsenaYpUrve ktvo lyap',
    text_dev       = 'समासेऽनञ्पूर्वे क्त्वो ल्यप्',
    samagra_slp1   = "aNgasya samAse anaYpUrve ktvaH lyap",  # brain correction X-001 (ruling R-004): अन्यतरस्याम् does not reach 7.1.37
    samagra_dev    = "अङ्गस्य समासे अनञ्पूर्वे क्त्वः ल्यप्",
    padaccheda_dev = "समासे / अनञ्-पूर्वे / क्त्वः / ल्यप्",
    why_dev        = "अनञ्पूर्वे समासे क्त्वः ल्यबादेशः (प्रकृत्य)।",
    anuvritti_from = ("7.1.12",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
