"""
8.2.23  संयोगान्तस्य लोपः  —  VIDHI

Three operational paths — all phonologically discriminated:

  1. Tripāḍī zone, pada ends in ``nt`` → drop final ``t``.
  2. ``8_2_23_dyauH_v_lopa_arm`` (dyauḥ-specific): first term ends in ``…Ov``,
     followed by a ``su`` sup → drop final ``v``.
  3. ``8_2_23_asmad_ns_arm`` (asmad dvitīyā bahu): pada ends in ``ns`` → drop final ``s``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82023 · संयोगान्तस्य लोपः
              padaccheda: संयोग-अन्तस्य ६/१ लोपः १/१
              anuvṛtti:   81016: पदस्य
  Source #2 — Kāśikā 8.2.23 udāharaṇa:
                गोमान्
                यवमान्
                कृतवान्
  Gloss (sa) — पदान्ते संयोगान्तस्य वर्णस्य लोपः।
  Cross-check — surface pinned by: tests/unit/test_dyOH_div_subanta.py, tests/unit/test_gomAn_pipeline.py
  Reference record: sutra_ref_out/8_2_23.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _hit(state: State):
    """Tripāḍī nt-lopa: fires on phonological environment alone."""
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


def _hit_asmad_ns(state: State):
    """Asmad dvitīyā bahu: pada ends in 'ns' → drop final 's'."""
    if len(state.terms) != 1:
        return None
    vs = state.terms[0].varnas
    if len(vs) < 2:
        return None
    if vs[-1].slp1 != "s" or vs[-2].slp1 != "n":
        return None
    return len(vs) - 1


def _hit_P022_final_v(state: State):
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
    return (
        _hit(state) is not None
        or _hit_P022_final_v(state) is not None
        or _hit_asmad_ns(state) is not None
    )


def act(state: State) -> State:
    hit = _hit_P022_final_v(state)
    if hit is not None:
        ti, vi = hit
        del state.terms[ti].varnas[vi]
        state.samjna_registry["8.2.23_samyoganta_lopa"] = True
        return state

    # Asmad dvitīyā bahu: drop final 's' from '...ns'
    ji_ns = _hit_asmad_ns(state)
    if ji_ns is not None:
        del state.terms[0].varnas[ji_ns]
        state.samjna_registry["8.2.23_samyoganta_lopa_asmad"] = True
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
