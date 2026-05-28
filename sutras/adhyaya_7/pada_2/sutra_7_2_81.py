"""
7.2.81  आतो ङितः  —  VIDHI

*Padaccheda:* *ātaḥ* / *ṅitaḥ*.

*Śāstra:* in karmaṇi / bhāve, the initial *ā* of ātmanepada dual *tiṅ* (*āte*, *āthe* after
**3.4.79**) becomes *iy* when a *ṅit* *vikaraṇa* (*yaḳ*→*ya*) precedes.

*Engine:* ``bhava_karma_usage`` on *dhātu*; *tiṅ* *ādeśa* with initial ``A``; no ``_arm`` (Art. 13).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk


def _bhava_karma_dhatu(state: State) -> bool:
    return any("dhatu" in t.tags and "bhava_karma_usage" in t.tags for t in state.terms)


def _find_Ate(state: State):
    if not _bhava_karma_dhatu(state):
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
    t.varnas = [_mk("i"), _mk("y")] + list(t.varnas[1:])
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["7_2_81_done"] = True
    state.meta.pop("7_2_81_Atam_arm", None)
    state.samjna_registry["7.2.81_Ate_iy"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.81",
    sutra_type=SutraType.VIDHI,
    text_slp1="Ato NitaH",
    text_dev="आतो ङितः",
    padaccheda_dev="आतः ङितः",
    why_dev=(
        "कर्मणि/भावे ङित-विकरण-पूर्वम् आत्मनेपद-द्विवचनस्य आकारस्य 'इय्'-आदेशः — "
        "आते → इय्ते, आथे → इय्थे।"
    ),
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
