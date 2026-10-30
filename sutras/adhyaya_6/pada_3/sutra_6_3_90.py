"""
6.3.90  इदङ्किमोरीश्की  —  VIDHI

Padaccheda: इदम्-किमोः ईश्-की (लुप्तप्रथमान्तनिर्देशः)

इदङ्किमोरीश्की (6.3.90)
Pāṭha: ashtadhyayi.com data.txt row i=63090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_90_idaNkimorI_90"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.90", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.90"
    return state



# the vatu pratyayas (5.2.39 vatup; 5.2.40 – 41 vatup with va → gha, S36 folds the gha into the name)
_VATU = ("vatu~p", "Gatu~p")


def _site(state: State, stems=None):
    """Index of a sarvanāma stem Term standing before a vatu pratyaya (dṛk / dṛśa upapadas are the kṛdanta loop's)."""
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if t.meta.get("6_3_90_done") or pr.kind != "pratyaya" or "taddhita" not in pr.tags or pr.meta.get("upadesha_slp1") not in _VATU:
            continue
        name = t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)
        if "sarvanama" in t.tags and (stems is None or name in stems):
            return i
    return None


_ESH = {"idam": "I", "kim": "kI"}      # īś, kī (śit: the whole stem is replaced, 1.1.55)


def _new_cond(state: State) -> bool:
    return _site(state, frozenset(_ESH)) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    i = _site(state, frozenset(_ESH))
    if i is None:
        return _legacy_act(state)
    t = state.terms[i]
    t.varnas[:] = [mk(c) for c in _ESH[t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)]]
    t.meta["6_3_90_done"] = True
    t.tags -= {"tyadadi", "sarvanama"}           # īś / kī are not tyadādi words: 7.2.102 must not act on the remnant
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "idaNkimorISkI",
    text_dev              = "इदङ्किमोरीश्की",
    samagra_slp1          = "uttarapade idam-kimoH IS-kI dfk-dfSa-vatuzu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे इदम्-किमोः ईश्-की दृक्-दृश-वतुषु",
    padaccheda_dev        = "इदम्-किमोः ईश्-की (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "दृग्-दृश-वतुषु इदम्-किम्-योः यथासंख्यम् ईश्-की (शित्: सर्वादेशः): इयान्, कियान्; ७.२.१०२ बाधित्वा।",
    anuvritti_from        = ('6.1.1',),
    apavada_of     = ('6.3.91', '7.2.102', '7.2.103'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
