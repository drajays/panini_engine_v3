"""
2.4.85  लुटः प्रथमस्य डारौरसः  —  VIDHI (narrow: *tip* → *ḍā*)

When ``2_4_85_lut_prathama_arm`` is set and the *tiṅ* residue is the *prathama*
singular *parasmaipada* shape ``ti`` (after *halantyam* on *tip*), replace it
with *ḍā* (SLP1 ``q`` + ``A``) so *cuṭ*-``it`` can mark the ``q`` as *ḍit*.

This is a recipe-gated slice of the *luṭ* *prathama* replacement (*tip*/*tas*/*jhi*
→ *ḍā* / *rau* / *ras* …); only the *tip* cell is implemented here.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk


def _find_ti(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "ti":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in {"tip", "ti"}:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("2_4_85_lut_prathama_arm"):
        return False
    if state.meta.get("2_4_85_lut_prathama_done"):
        return False
    return _find_ti(state) is not None


def act(state: State) -> State:
    j = _find_ti(state)
    if j is None:
        return state
    t = state.terms[j]
    t.varnas = [mk("q"), mk("A")]
    t.meta["upadesha_slp1"] = "qA"
    t.tags.add("tin_adesha_2_4_85")
    state.meta["2_4_85_lut_prathama_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.85",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "luTaH prathamasya dArAurasaH",
    text_dev       = "लुटः प्रथमस्य डारौरसः",
    padaccheda_dev = "लुटः प्रथमस्य डा-रौ-रसः",
    why_dev        = "लुट्-लकारे प्रथम-पुरुष-परस्मैपदानां डा-रौ-रस्-आदेशः (तिप्→डा)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
