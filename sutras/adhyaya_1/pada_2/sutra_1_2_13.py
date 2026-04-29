"""
1.2.13  वा गमहनविदविशām  …  —  VIDHI (narrow demo fragment)

Operational narrow demo (संगसीष्ट / ``saGgasIzwa`` fragment):
  For *√gam*, optionally treat the ``sīyuṭ``‑block (**3.4.102** ``ling_sIyuw``) as
  *kitvat* (**kṅiti** / ``kngiti``).

Engine:
  - recipe arms via ``state.meta['1_2_13_va_gam_kit_arm']``.
  - requires preceding *dhātu* ``upadesha_slp1=='gam'``.
  - requires a ``ling_sIyuw`` pratyaya and a *taṅ* *tiṅ* termination (ātmanepada).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


_ATMANEPADA_TIN = frozenset({"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG"})


def _find(state: State) -> int | None:
    if not state.meta.get("1_2_13_va_gam_kit_arm"):
        return None
    if not state.meta.get("ashir_liG"):
        return None
    if len(state.terms) < 2:
        return None
    last = state.terms[-1]
    if "pratyaya" not in last.tags:
        return None
    if (last.meta.get("upadesha_slp1") or "").strip() not in _ATMANEPADA_TIN:
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "gam":
            continue
        for i, pr in enumerate(state.terms):
            if "ling_sIyuw" not in pr.tags:
                continue
            if "kngiti" in pr.tags:
                return None
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("kngiti")
    state.samjna_registry["1.2.13_va_gam_kit"] = True
    state.meta["1_2_13_va_gam_kit_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.13",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="vA gamahana (...)",
    text_dev="वा गमहन… (आशीर्लिङ्गे डेमो-खण्डम्)",
    padaccheda_dev="वा /* गम्-आश्रितः सीयुट् / च",
    why_dev=(
        "\\\"√गम्\\\"-परे आशिषि \\\"वा\\\" इति सीयुट्‌ आगमे किद्वन्-आचरणम् (संज्ञा-मात्रम्)।"
    ),
    anuvritti_from=("1.2.11",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
