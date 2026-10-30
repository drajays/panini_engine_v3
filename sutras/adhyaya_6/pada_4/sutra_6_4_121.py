"""
6.4.121  थलि च सेटि  —  VIDHI

Padaccheda: थलि च सेटि

थलि च सेटि (6.4.121)
Pāṭha: ashtadhyayi.com data.txt row i=64121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_121_Tali_121"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.121", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.121"
    return state


from sutras.adhyaya_6.pada_4.sutra_6_4_120 import _find as _find_120, act as _act_120


def _thal_seT(state: State):
    """The 6.4.120 site when the ending is thal with iṭ (पेचिथ): the same ए-ādeśa and abhyāsa-lopa, here for थलि च सेटि.
    SHORTCUT S85: 6.4.120 still licenses the thal case itself (pipelines/tinanta.py applies only 6.4.120); this sūtra delegates to its site and act."""
    i = _find_120(state)
    if i is None:
        return None
    up = (state.terms[i + 1].meta.get("upadesha_slp1") or "").strip()
    return i if up in ("Tal", "Ta") else None


def cond(state: State) -> bool:
    return _thal_seT(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    if _thal_seT(state) is None:
        return _legacy_act(state)
    return _act_120(state)


SUTRA = SutraRecord(
    sutra_id              = "6.4.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Tali ca sewi",
    text_dev              = "थलि च सेटि",
    samagra_slp1          = "aNgasya asidDavadatrABAt Tali ca sewi et hO aByAsalopaH ekahalmaDye anAdeSAdeH liwi ataH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् थलि च सेटि एत् हौ अभ्यासलोपः एकहल्मध्ये अनादेशादेः लिटि अतः",
    padaccheda_dev        = "थलि च सेटि",
    why_dev               = "थलि सेटि च लिटि एकहल्मध्यस्य अनादेशादेः अतः एकारः अभ्यासलोपश्च — पेचिथ, शेकिथ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
