"""
1.3.29  समो गम्यृच्छिभ्याम् …  —  SAMJNA (narrow demo)

Narrow demo (संगसीष्ट / ``saGgasIzwa``):
  When ``sam``‑pūrvā *gam* participates in kartāri *ātmanepada* licences in this repo,
  mark the neighbouring *dhātu* ``gam`` Term with ``ātmanepada_licensed_1_3_29``.

Engine:
  - recipe arms via ``state.meta['1_3_29_samo_gamyricchiblAm_arm']``.
  - requires contiguous ``[ Term tagged upasarga with surface ``sam`` ][ dhātu with
    ``upadesha_slp1=='gam'`` ]``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("1_3_29_samo_gamyricchiblAm_arm"):
        return False
    for i in range(len(state.terms) - 1):
        u, dh = state.terms[i], state.terms[i + 1]
        if "upasarga" not in u.tags:
            continue
        if "".join(v.slp1 for v in u.varnas) != "sam":
            continue
        if "dhatu" not in dh.tags:
            continue
        if (dh.meta.get("upadesha_slp1") or "").strip() != "gam":
            continue
        if dh.meta.get("1_3_29_done"):
            return False
        return True
    return False


def act(state: State) -> State:
    if not cond(state):
        return state
    for i in range(len(state.terms) - 1):
        u, dh = state.terms[i], state.terms[i + 1]
        if (
            "upasarga" in u.tags
            and "".join(v.slp1 for v in u.varnas) == "sam"
            and (dh.meta.get("upadesha_slp1") or "").strip() == "gam"
        ):
            dh.tags.add("ātmanepada_licensed_1_3_29")
            dh.meta["1_3_29_done"] = True
            state.samjna_registry["1.3.29_samo_gam_tag"] = True
            state.meta["1_3_29_samo_gamyricchiblAm_arm"] = False
            break
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.29",
    sutra_type=SutraType.SAMJNA,
    text_slp1="samH gamyfCIBhyAm (...)",
    text_dev="समो गम्यृच्छिभ्याम् (संकीर्ण)",
    padaccheda_dev="समः / गमेः …",
    why_dev=(
        "\"सम्\"पूर्वात् धातुर् \"\"गम्\" आत्मनेपद-पथे जातुः (आशिषि; डेमो-संज्ञा सूत्रस्थ।"
    ),
    anuvritti_from=("1.3.27",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
