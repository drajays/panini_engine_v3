"""
6.4.38  वा ल्यपि  —  VIBHASHA

Sources consulted:
- ashtadhyayi.com data.txt row i=64038 · वा ल्यपि
  (anuvṛtti: अनुदात्तोपदेश-वनति-तनोति-आदीनाम् अनुनासिक लोपः 6.4.37)
- Kāśikā: "व्यवस्थितविभाषा चेयम्। तेन मकारान्तानां विकल्पो भवति, अन्यत्र नित्यमेव
  लोपः। प्रयत्य, प्रयम्य। प्ररत्य, प्ररम्य। प्रणत्य, प्रणम्य। आगत्य, आगम्य। आहत्य।"
  (the नित्य न्-लोप of आहत्य is not modelled here)
- Cross-validation: tests/unit/test_agaty_gam_lyap_acah_lesson.py and
  tests/constitutional/test_vikalpa_branches.py (आगत्य / आगम्य, प्रगत्य / प्रगम्य)

Before ल्यप्, the final anunāsika of an anudāttopadeśa dhātu (गमॢँ, यमँ,
रमुँ, णमँ) is optionally dropped. As a vyavasthita-vibhāṣā the option holds
for म्-final roots; the dropped म् is a hal, so 1.1.57 gives it no
sthānivadbhāva and 6.1.71 adds तुक् after the now-hrasva aṅga (आगत्य).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_dhatu_m(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or (t.meta.get("upadesha_slp1") or "").strip() != "lyap":
            continue
        dh = next((j for j in range(i - 1, -1, -1) if state.terms[j].varnas), None)
        if dh is None:
            return None
        d = state.terms[dh]
        if "dhatu" not in d.tags or d.meta.get("6_4_38_m_lopa_done"):
            return None
        if d.meta.get("udatta_dhatu", True):    # anudāttopadeśa only
            return None
        return dh if d.varnas[-1].slp1 == "m" else None
    return None


def cond(state: State) -> bool:
    return _find_dhatu_m(state) is not None


def act(state: State) -> State:
    i = _find_dhatu_m(state)
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
    why_dev="ल्यपि परे अनुदात्तोपदेशस्य धातोः अन्त्य-मकारस्य वैकल्पिको लोपः (आगत्य / आगम्य)।",
    anuvritti_from=("6.4.37",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
