"""
7.2.81  आतो ङितः  —  VIDHI

In karmani laṭ, the ātmanepada dual endings āta (3du) and āthāṃ (2du) carry
an initial long ā (ā-āgama). Before a ṅit suffix, this ā is replaced by iy:

  Ate  (āte,  from Atam/āta  after 3.4.79) → iy + t + e  = iyte
  ATe  (āthe, from ATAm/āthāṃ after 3.4.79) → iy + T + e  = iyTe (= iythe)

Then 6.1.66 drops the y before the following val consonant (t or th).

Arm flag: state.meta["7_2_81_Atam_arm"] must be True.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk


def _find_Ate(state: State):
    if not state.meta.get("7_2_81_Atam_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if t.meta.get("7_2_81_done"):
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "A":
            continue
        return ti
    return None


def cond(state: State) -> bool:
    return _find_Ate(state) is not None


def act(state: State) -> State:
    ti = _find_Ate(state)
    if ti is None:
        return state
    t = state.terms[ti]
    # Replace initial A (ā) with [i, y]
    t.varnas = [_mk("i"), _mk("y")] + list(t.varnas[1:])
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["7_2_81_done"] = True
    state.meta.pop("7_2_81_Atam_arm", None)
    state.samjna_registry["7.2.81_Ate_iy"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "Ato NitaH",
    text_dev              = "आतो ङितः",
    padaccheda_dev        = "आतः ङितः",
    why_dev               = (
        "आत्मनेपद-द्विवचन-प्रत्यये (आते/आथे) प्रारम्भिक-आकारस्य 'इय्'-आदेशः — "
        "आते → इय्ते, आथे → इय्थे।"
    ),
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
