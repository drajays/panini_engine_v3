"""
6.4.38  वा ल्यपि  —  VIBHASHA

Sources consulted:
- ashtadhyayi.com data.txt row i=604038
- Kāśikā: वा ल्यपि (ल्यप्-प्रत्ययस्य मकारस्य वैकल्पिको लोपः)
- Cross-validation: tests/unit/test_agaty_gam_lyap_acah_lesson.py

Optional *m*-lopa on *lyap* (``l + ṃ + y + …``). The lupta **hal** ``m`` is **not**
*sthānivat* under **1.1.57** (*acaḥ* only) — **6.1.71** *tuk* must still apply
(दलकृत्यम् / आगत्य lesson).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_lyap_m(state: State) -> tuple[int, int] | None:
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "lyap":
            continue
        if t.meta.get("6_4_38_m_lopa_done"):
            continue
        for vi, v in enumerate(t.varnas):
            if v.slp1 == "m":
                return (ti, vi)
    return None


def cond(state: State) -> bool:
    return _find_lyap_m(state) is not None


def act(state: State) -> State:
    hit = _find_lyap_m(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    t.varnas.pop(vi)
    t.meta["6_4_38_m_lopa_done"] = True
    t.meta["hal_lupta_not_ac_sthanivat"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.38",
    sutra_type=SutraType.VIBHASHA,
    text_slp1="vA lyapi",
    text_dev="वा ल्यपि",
    padaccheda_dev="वा / ल्यपि",
    why_dev="ल्यप्-प्रत्यये मकारस्य वैकल्पिको लोपः; लुप्त-हल् स्थानिवत् न (१.१.५७)।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
