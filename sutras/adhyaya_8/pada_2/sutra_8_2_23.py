"""
8.2.23  संयोगान्तस्य लोपः  —  VIDHI

Narrow v3: in Tripāḍī, when ``state.meta["8_2_23_arm"]`` and the *pada* ends in
``nt`` (``…n`` + ``t``), delete the final ``t`` (*saṃyogānta* *lopa* of the
cluster-final consonant).

v3 extension (narrow, P022 द्यौः):
  When recipe arms ``state.meta["P022_8_2_23_final_v_lopa_arm"]`` and the first
  term ends in ``…Ov`` (``O`` + ``v``), delete that final ``v`` before a
  following ``su`` sup.  This models the JSON's *dyOv + su → dyO + su* slice.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _hit(state: State):
    if not state.meta.get("8_2_23_arm"):
        return None
    if not state.tripadi_zone:
        return None
    if len(state.terms) != 1:
        return None
    vs = state.terms[0].varnas
    if len(vs) < 2:
        return None
    if vs[-1].slp1 != "t" or vs[-2].slp1 != "n":
        return None
    return len(vs) - 1


def _hit_P022_final_v(state: State):
    if not state.meta.get("P022_8_2_23_final_v_lopa_arm"):
        return None
    if not state.tripadi_zone:
        return None
    if len(state.terms) < 2:
        return None
    left = state.terms[0]
    right = state.terms[1]
    if not left.varnas:
        return None
    if left.varnas[-1].slp1 != "v":
        return None
    if len(left.varnas) < 2 or left.varnas[-2].slp1 != "O":
        return None
    if right.kind != "pratyaya" or "sup" not in right.tags:
        return None
    # Engine inventory uses prathamā-ekavacana as ``s~`` (anunāsika marker).
    if (right.meta.get("upadesha_slp1") or "").strip() not in {"s~", "sU", "su"}:
        return None
    return 0, len(left.varnas) - 1


def cond(state: State) -> bool:
    return _hit(state) is not None or _hit_P022_final_v(state) is not None


def act(state: State) -> State:
    hit = _hit_P022_final_v(state)
    if hit is not None:
        ti, vi = hit
        del state.terms[ti].varnas[vi]
        state.meta["P022_8_2_23_final_v_lopa_arm"] = False
        state.samjna_registry["8.2.23_samyoganta_lopa"] = True
        return state

    ji = _hit(state)
    if ji is None:
        return state
    del state.terms[0].varnas[ji]
    state.samjna_registry["8.2.23_samyoganta_lopa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.23",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "saMyogAntasya lopaH",
    text_dev       = "संयोगान्तस्य लोपः",
    padaccheda_dev = "संयोग-अन्तस्य / लोपः",
    why_dev        = "संयोगान्त-पदस्य अन्त्य-हल्-लोपः (चितवान्)।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
