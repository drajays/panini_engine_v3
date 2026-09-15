"""
8.3.60  शासिवसिघसीनां च  —  VIDHI (narrow demo)

Demo slice (उषित्वा / uzitvA):
  For dhātu `vas`, after samprasāraṇa has produced initial `u`, change `s` → `z`
  (ṣatva) before the following `tvA` block.

Engine:
  - recipe arms via ``state.meta['shasi_vasi_recipe']``.
  - narrow: applies only when the primary dhātu upadeśa is `vas` and the dhātu
    term currently contains `s` as its final varṇa.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 83060 · शासिवसिघसीनां च
              padaccheda: शासि-वसि-घसीनाम् च
              anuvṛtti:   82108: संहितायाम् | 83055: अपदान्तस्य मूर्धन्यः | 83056: सः | 83057: इण्कोः
  Source #2 — Kāśikā 8.3.60 udāharaṇa:
                अन्वशिषत्
                शिष्टः
                शिष्टवान्
  Cross-check — surface pinned by: tests/unit/test_uditvA_uzitvA_ktvA_samprasaraNa.py
  Reference record: sutra_ref_out/8_3_60.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find_lit_ghas_s(state: State):
    """*Liṭ* *ghas* pada: *s* of *ghas*/*ghs* before following *hal* → *ṣ* (*z*)."""
    if not state.meta.get("lakara_liT"):
        return None
    if len(state.terms) != 1 or "pada" not in state.terms[0].tags:
        return None
    t = state.terms[0]
    if t.meta.get("8_3_60_satva_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 != "s":
            continue
        if i > 0 and vs[i - 1].slp1 in {"G", "g", "h"}:
            return i
    return None


def cond(state: State) -> bool:
    if _find_lit_ghas_s(state) is not None:
        return True
    if not state.meta.get("shasi_vasi_recipe"):
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "vas":
        return False
    if dh.meta.get("8_3_60_satva_done"):
        return False
    if not dh.varnas:
        return False
    return dh.varnas[-1].slp1 == "s"


def act(state: State) -> State:
    i = _find_lit_ghas_s(state)
    if i is not None:
        state.terms[0].varnas[i] = mk("z")
        state.terms[0].meta["8_3_60_satva_done"] = True
        return state
    if not state.meta.get("shasi_vasi_recipe"):
        return state
    dh = state.terms[0]
    dh.varnas[-1] = mk("z")
    dh.meta["8_3_60_satva_done"] = True
    state.meta["shasi_vasi_recipe"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.60",
    sutra_type=SutraType.VIDHI,
    text_slp1="SAsi-vasi-Gasi-nAm ca (narrow)",
    text_dev="शासिवसिघसीनां च",
    padaccheda_dev="शासि-वसि-घसि-नाम् / च",
    why_dev="वसादौ (सम्प्रसारणोत्तरं) सस्य षत्वं (उषित्वा)।",
    anuvritti_from=("8.3.57",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

