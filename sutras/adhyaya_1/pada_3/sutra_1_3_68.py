"""
1.3.68  भीस्म्योर्हेतुभये  —  VIDHI (narrow demo)

Glass-box note (भीषयते .md):
  In the causative-fear sense for `bhI`, the prayoga is forced to ātmanepada.

Engine:
  - recipe-armed: ``state.meta['1_3_68_arm']``.
  - records `state.meta['pada'] = 'Atmanepada'` for downstream scheduling.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("1_3_68_arm"):
        return False
    if state.meta.get("pada") == "Atmanepada":
        return False
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return False
    return (state.terms[0].meta.get("upadesha_slp1") or "").strip() in {"BI"}


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.68",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="BIsmyor hetuBaye (Atmanepadam)",
    text_dev="भीस्म्योर्हेतुभये",
    padaccheda_dev="भीस्म्योः / हेतु-भये",
    why_dev="भि/स्मि-धात्वोः हेतु-भय-अर्थे आत्मनेपद-नियमः (डेमो-स्लाइस)।",
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

