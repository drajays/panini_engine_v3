"""engine/luk.py — adarśana (1.1.60) of a taddhita pratyaya under the names luk / ślu / lup (1.1.61).

Shared by the sūtras that teach it (4.3.163, 166, 167, 168, 4.4.24, 79, 1.2.49, 1.2.51); not a sūtra file. The pratyaya Term stays on the tape as a zero-width
ghost (``engine.lopa_ghost``): its ``pratyaya``/``taddhita`` tags and ``it_markers`` remain, so the stem is still a taddhitānta (1.1.62 pratyayalakṣaṇa) while
no ghost is ever the *nimitta* of an aṅgakārya (1.1.63 na lumatāṅgasya: ``is_lumat``)."""
from __future__ import annotations

from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from engine.state import State, Term

KINDS = ("luk", "Slu", "lup")
KIND_TAG = "lopa_kind:"
LUMAT_IT = "lumat_it_markers"
LUMAT_UPADESHA = "lumat_upadesha"


def is_lumat(t: Term) -> bool:
    """A pratyaya that luk/ślu/lup took away: 1.1.63 — no aṅgakārya is done on its account."""
    return LUK_LOPA_GHOST_TAG in t.tags and t.kind == "pratyaya"


def lopa_kind(t: Term) -> str | None:
    return next((x[len(KIND_TAG):] for x in t.tags if x.startswith(KIND_TAG)), None)


def live_taddhita(state: State, *, not_from: tuple[str, ...] = (), only_from: tuple[str, ...] | None = None, upadesha: tuple[str, ...] | None = None) -> int | None:
    """Index of the taddhita pratyaya that ends the tape and has not yet been taken away; ``not_from``: sūtras whose pratyaya an apavāda keeps (its varṇas carry
    ``origin:<sūtra>``); ``only_from``: only a pratyaya one of these sūtras gave; ``upadesha``: only these pratyayas."""
    if not state.terms:
        return None
    i = len(state.terms) - 1
    t = state.terms[i]
    if t.kind != "pratyaya" or not {"taddhita", "pratyaya"} <= t.tags or LUK_LOPA_GHOST_TAG in t.tags:
        return None
    if any(f"origin:{s}" in v.tags for v in t.varnas for s in not_from):
        return None
    if only_from is not None and not any(f"origin:{s}" in v.tags for v in t.varnas for s in only_from):
        return None
    if upadesha is not None and t.meta.get("upadesha_slp1") not in upadesha:
        return None
    return i


def take_away(state: State, idx: int, kind: str) -> State:
    """The adarśana itself: the Term loses its varṇas and is named luk / ślu / lup."""
    assert kind in KINDS
    t = state.terms[idx]
    t.varnas.clear()
    t.tags |= {LUK_LOPA_GHOST_TAG, KIND_TAG + kind}
    t.meta[LUMAT_IT] = t.meta.pop("it_markers", set())      # 1.1.63: aṅgakārya rules read ``it_markers``, ādeśa rules the ``upadesha_slp1`` (ṭhasyekaḥ 7.3.50 …);
    t.meta[LUMAT_UPADESHA] = t.meta.pop("upadesha_slp1", "")      # a lumat pratyaya offers neither (nor does the stem's origin record: 1.1.63 — 4.1.15 gives no ṅīp after a lumat ṭhak, lavaṇā)
    return state
