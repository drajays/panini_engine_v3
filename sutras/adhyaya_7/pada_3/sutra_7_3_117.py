"""
7.3.117  इदुद्भ्याम्  —  VIDHI

Kāśikā: इकारोकाराभ्यां नदीसंज्ञकाभ्यामुत्तरस्य ङेरामादेशो भवति। कृत्याम्। धेन्वाम्॥
(a hrasva i / u that 1.4.6 made nadī: kṛti + ṅi → kṛty + Ām; the long ī/ū nadī and the āp-stems are 7.3.116's.)
Pāṭha: ashtadhyayi.com data.txt row i=73117 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_DONE = "7_3_117_Am_adesha_done"


def _target(state: State):
    if len(state.terms) < 2:
        return None
    anga, affix = state.terms[-2], state.terms[-1]
    if "nadi" not in anga.tags or "sup" not in affix.tags or not anga.varnas or anga.varnas[-1].slp1 not in ("i", "u"):
        return None
    if affix.meta.get(_DONE) or not affix.varnas or (affix.meta.get("upadesha_slp1") or "") != "Ni":
        return None
    if affix.varnas[0].slp1 == "N":          # after 1.3.8 → 1.3.9 took the ṅ
        return None
    return anga, affix


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    _anga, affix = _target(state)
    affix.varnas[:] = [mk("A"), mk("m")]
    affix.meta[_DONE] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "idudByAm",
    text_dev              = "इदुद्भ्याम्",
    samagra_slp1          = "idudByAm nadyAH aNgAt NeH Am",
    samagra_dev           = "इदुद्भ्याम् नद्याः अङ्गात् ङेः आम्",
    padaccheda_dev        = "इत्-उद्‍भ्याम्",
    why_dev               = "हृस्व इ/उ-अन्त नदीसंज्ञक से परे ङि के स्थान पर आम् (कृत्याम्, धेन्वाम्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
