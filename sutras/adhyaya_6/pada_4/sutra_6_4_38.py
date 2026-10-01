"""
6.4.38  वा ल्यपि  —  VIBHASHA

Sources consulted:
- ashtadhyayi.com data.txt row i=64038 · वा ल्यपि
  (anuvṛtti: अनुदात्तोपदेश-वनति-तनोति-आदीनाम् अनुनासिक लोपः 6.4.37)
- Kāśikā: "ल्यपि परतोऽनुदात्तोपदेशवनतितनोत्यादीनामनुनासिकलोपो वा भवति।
  व्यवस्थितविभाषा (परि०९९) चेयम्। तेन मकारान्तानां विकल्पो भवति, अन्यत्र नित्यमेव
  लोपः। प्रयत्य, प्रयम्य। प्ररत्य, प्ररम्य। प्रणत्य, प्रणम्य। आगत्य, आगम्य। आहत्य।
  प्रमत्य। प्रवत्य। प्रक्षत्य॥"
- Cross-validation: tests/unit/test_agaty_gam_lyap_acah_lesson.py,
  tests/constitutional/test_vikalpa_branches.py (आगत्य / आगम्य) and
  tests/unit/test_lyap_6_4_38_nitya.py (आहत्य, no आहन्य branch)

Before ल्यप्, the final anunāsika of an anudāttopadeśa dhātu (गमॢँ, यमँ, रमुँ,
णमँ, हनँ), of वनँ, or of a tanādi root is dropped. As a vyavasthita-vibhāṣā the
option holds only for म्-final roots (``vibhasha_scope``); for न्/ण्-final roots
(हन् → आहत्य, क्षण् → प्रक्षत्य) the lopa is nitya. The dropped nasal is a hal,
so 1.1.57 gives it no sthānivadbhāva and 6.1.71 adds तुक् after the now-hrasva
aṅga.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_ANUNASIKA_HAL = frozenset({"m", "n", "R", "Y", "N"})
_VANATI = "vana~"
_TANADI_GANA = 8


def _in_6_4_37_class(d) -> bool:
    """अनुदात्तोपदेश / वनति / तनोत्यादि — the dhātus 6.4.37 names."""
    if not d.meta.get("udatta_dhatu", True):
        return True
    if (d.meta.get("upadesha_slp1") or "").strip() == _VANATI:
        return True
    return d.meta.get("gana") == _TANADI_GANA


def _find_dhatu(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or (t.meta.get("upadesha_slp1") or "").strip() != "lyap":
            continue
        dh = next((j for j in range(i - 1, -1, -1) if state.terms[j].varnas), None)
        if dh is None:
            return None
        d = state.terms[dh]
        if "dhatu" not in d.tags or d.meta.get("6_4_38_m_lopa_done"):
            return None
        if not _in_6_4_37_class(d):
            return None
        return dh if d.varnas[-1].slp1 in _ANUNASIKA_HAL else None
    return None


def cond(state: State) -> bool:
    return _find_dhatu(state) is not None


def option_live(state: State) -> bool:
    """मकारान्तानां विकल्पः — elsewhere the lopa is nitya."""
    i = _find_dhatu(state)
    return i is None or state.terms[i].varnas[-1].slp1 == "m"


def act(state: State) -> State:
    i = _find_dhatu(state)
    if i is None:
        return state
    d = state.terms[i]
    d.varnas.pop()
    d.meta["6_4_38_m_lopa_done"] = True
    d.meta["hal_lupta_not_ac_sthanivat"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.38",
    sutra_type=SutraType.VIBHASHA,
    text_slp1="vA lyapi",
    text_dev="वा ल्यपि",
    padaccheda_dev="वा / ल्यपि",
    why_dev="ल्यपि परे अनुदात्तोपदेशादेः धातोः अनुनासिक-लोपः — मकारान्ते विकल्पः (आगत्य / आगम्य), अन्यत्र नित्यम् (आहत्य)।",
    anuvritti_from=("6.4.37",),
    vibhasha_scope=option_live,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
