"""
7.4.94  दीर्घो लघोः  —  VIDHI (narrow: P037 *abhyāsa-laghu*)

Teaching **P037** step 14: lengthen the *hrasva* onset of the *abhyāsa* after
**7.4.93** so ``i`` → ``ī`` (*ik* represented as ``I`` in SLP1).

Narrow: ``state.meta['P037_7_4_94_dirgha_arm']`` + first ``abhyasa`` with
leading ``i`` before ``w`` → ``I`` + ``w``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 74094 · दीर्घो लघोः
              padaccheda: दीर्घः लघोः
              anuvṛtti:   64001: अङ्गस्य | 74058: अभ्यासस्य | 74093: लघुनि चङ्परेऽनग्लोपे
  Source #2 — Kāśikā 7.4.94 udāharaṇa:
                अचीकरत्
                अजीहरत्
                अलीलवत्
  Cross-check — surface pinned by: tests/unit/test_AwIwat_luN_aT_Nic_caN_tip.py
  Reference record: sutra_ref_out/7_4_94.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _abhyasa_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "abhyasa" in t.tags:
            return i
    return None


def _site(state: State) -> bool:
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P037_7_4_94_done"):
        return False
    if len(t.varnas) != 2:
        return False
    return t.varnas[0].slp1 == "i" and t.varnas[1].slp1 == "w"


_AC = frozenset("aAiIuUfFxXeEoO")
_LONG = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}


def _general(state: State):
    """दीर्घो लघोः: a laghu abhyāsa vowel (sanvat) is lengthened — चुचुर् → चूचुर्;
    not before a conjunct (अचिक्षलत्)."""
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or not t.meta.get("sanvat") or t.meta.get("7_4_94_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 not in _LONG:
            return None
        dh = state.terms[i + 1].varnas
        if len(dh) >= 2 and dh[0].slp1 not in _AC and dh[1].slp1 not in _AC:
            return None
        return t
    return None

def cond(state: State) -> bool:
    if _general(state) is not None:
        return True
    return _site(state)


def act(state: State) -> State:
    g = _general(state)
    if g is not None:
        g.varnas[-1] = mk(_LONG[g.varnas[-1].slp1])
        g.meta["7_4_94_done"] = True
        return state
    if not _site(state):
        return state
    i = _abhyasa_index(state)
    assert i is not None
    t = state.terms[i]
    t.varnas[0] = mk("I")
    t.meta["P037_7_4_94_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.94",
    sutra_type=SutraType.VIDHI,
    text_slp1='dIrGo laGoH',
    text_dev='दीर्घो लघोः',
    padaccheda_dev="दीर्घः / लघोः",
    why_dev="अभ्यास-laghu-वर्णस्य दीर्घः (प०३७: ``iw``→``Iw``)।",
    anuvritti_from=("7.4.93",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
