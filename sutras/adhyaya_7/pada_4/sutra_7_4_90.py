"""
7.4.90  रीगृदुपधस्य च  —  VIDHI (narrow: *rīk* augment after abhyāsa)

Glass-box slice for *yaṅ*-luganta *mṛj* (``mFj`` after *it*-*lopa*): when the
non-abhyāsa dhātu has vocalic ṛ in *upadhā* (penultimate vowel position in a
tri-skeleton ``hal–ṛ–hal`` row), append the augment ``r`` + ``I`` (दीर्घ-ई)
to the abhyāsa *Term* after **7.4.60** has run.

The kit ``k`` of traditional ``rIk`` is not modeled as a separate *upadeśa*
row here.  After **7.4.60** the abhyāsa may be a lone *hal* (``m``); an
inherent-``a`` row is inserted before ``r`` + ``I`` so ``flat_slp1`` yields
``marI`` (मरी), not ``mrI``.

Arm with ``state.meta["7_4_90_rIk_arm"]`` in the recipe.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.varna import mk_inherent_a


def _upadhA_f_in_non_abhyasa_dhatu(state: State) -> bool:
    for t in state.terms:
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        vs = t.varnas
        if len(vs) < 3:
            continue
        for k in range(1, len(vs) - 1):
            if vs[k].slp1 in {"f", "F"}:
                return True
    return False


def _find_abhyasa(state: State):
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if not t.meta.get("7_4_60_haladi_done"):
            continue
        if t.meta.get("7_4_90_rIk_done"):
            continue
        return ti
    return None


def cond(state: State) -> bool:
    if not state.meta.get("7_4_90_rIk_arm"):
        return False
    if not _upadhA_f_in_non_abhyasa_dhatu(state):
        return False
    return _find_abhyasa(state) is not None


def act(state: State) -> State:
    ti = _find_abhyasa(state)
    if ti is None:
        return state
    t = state.terms[ti]
    t.varnas.extend((mk_inherent_a(), mk("r"), mk("I")))
    t.meta["7_4_90_rIk_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.4.90",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "rIgf-dupadhasya ca",
    text_dev       = "रीगृदुपधस्य च",
    padaccheda_dev = "रीक् / गृदुपधस्य / च",
    why_dev        = "यङ्लुगन्ते गृदुपध-ऋकारे अभ्यासस्य री-आगमः (ग्लास-बॉक्स्)।",
    anuvritti_from = ("7.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
