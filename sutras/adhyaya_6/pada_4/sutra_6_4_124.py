"""
6.4.124  वा जॄभ्रमुत्रसाम्  —  VIDHI

Padaccheda: वा जॄ-भ्रमु-त्रसाम्

वा जॄभ्रमुत्रसाम् (6.4.124)
Pāṭha: ashtadhyayi.com data.txt row i=64124 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_124_vA_124"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.124", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.124"
    return state


from engine.state import State
from phonology import mk

from sutras.adhyaya_6.pada_4.sutra_6_4_120 import _ending_licenses

_ROOTS = frozenset({"jar", "Bram", "tras"})      # जॄ (ṛ → ar), भ्रमु, त्रसी


def _find(state: State):
    if not any((u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in state.terms):
        return None
    for i in range(1, len(state.terms) - 1):
        ab, t, nxt = state.terms[i - 1], state.terms[i], state.terms[i + 1]
        if ("abhyasa" in ab.tags and "dhatu" in t.tags and "abhyasa" not in t.tags and not t.meta.get("6_4_124_done")
                and "".join(v.slp1 for v in t.varnas) in _ROOTS and _ending_licenses(nxt)):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    j = next(j for j, v in enumerate(t.varnas) if v.slp1 == "a")
    t.varnas[j] = mk("e")                   # जर् → जेर्, भ्रम् → भ्रेम्, त्रस् → त्रेस् (the vā: जजरतुः …)
    t.meta["6_4_124_done"] = True
    del state.terms[hit - 1]                # अभ्यासलोपः
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.124",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "vA jFBramutrasAm",
    text_dev              = "वा जॄभ्रमुत्रसाम्",
    samagra_slp1          = "aNgasya asidDavadatrABAt vA jF-Bramu-trasAm kNiti aByAsalopaH ataH Tali sewi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् वा जॄ-भ्रमु-त्रसाम् क्ङिति अभ्यासलोपः अतः थलि सेटि",
    padaccheda_dev        = "वा जॄ-भ्रमु-त्रसाम्",
    why_dev               = "जॄ-भ्रमु-त्रसाम् अतः लिटि क्ङिति थलि सेटि च वा एकारः अभ्यासलोपश्च — जेरतुः / जजरतुः।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
