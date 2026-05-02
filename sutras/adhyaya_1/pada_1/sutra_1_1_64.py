"""
1.1.64  अचोऽन्त्यादि टि  —  SAMJNA (narrow)

Demo use (भीषयते .md):
  Mark the final vowel of an ātmanepada tiṅ affix (e.g. `ta`) as `Ti` so that
  3.4.79 can rewrite it (a → e).

**P043** (``split_prakriyas_11/P043.json``): paribhāṣā illustration queue
``state.meta['P043_1_1_64_queue']`` — each step registers a distinct
``samjna_registry`` key (R2).  For illustration stems, ``ṭi``-segment SLP1
(from the last ``ac`` onward) is stored on the ``Term`` as
``meta['1_1_64_ti_segment_slp1']`` and the last ``ac`` Varṇa receives tag ``Ti``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.pratyahara import is_dirgha, is_hrasva

P043_QUEUE_KEY = "P043_1_1_64_queue"
P043_WORD_META = "prakriya_P043_word"


def _is_ac(ch: str) -> bool:
    return bool(is_hrasva(ch) or is_dirgha(ch) or ch in {"e", "E", "o", "O"})


def _p043_queue_peek(state: State) -> str | None:
    q = state.meta.get(P043_QUEUE_KEY)
    if not isinstance(q, list) or not q:
        return None
    h = q[0]
    return h if isinstance(h, str) else None


def _find_p043_word_term(state: State, head: str):
    for ti, t in enumerate(state.terms):
        if t.meta.get(P043_WORD_META) == head:
            return ti, t
    return None


def _last_ac_index(t: Term) -> int | None:
    for vi in range(len(t.varnas) - 1, -1, -1):
        v = t.varnas[vi]
        if _is_ac(v.slp1):
            return vi
    return None


def _eligible(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "pratyaya" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in {"ta", "iw"}:
            continue
        for vi in range(len(t.varnas) - 1, -1, -1):
            v = t.varnas[vi]
            if _is_ac(v.slp1) and "Ti" not in v.tags:
                yield ti, vi
                break


def _p043_cond(state: State) -> bool:
    head = _p043_queue_peek(state)
    if head is None:
        return False
    if head in ("definition", "siddhi"):
        return True
    if head in ("paceyAtAm", "agnicit", "somasut"):
        hit = _find_p043_word_term(state, head)
        if hit is None:
            return False
        _ti, t = hit
        return _last_ac_index(t) is not None
    return False


def cond(state: State) -> bool:
    if _p043_cond(state):
        return True
    return next(_eligible(state), None) is not None


def _p043_act(state: State) -> State:
    head = _p043_queue_peek(state)
    if head is None:
        return state
    q = state.meta[P043_QUEUE_KEY]
    state.meta[P043_QUEUE_KEY] = q[1:]
    if head == "definition":
        state.samjna_registry["1.1.64_P043_acontyAdi_Ti_paribhasha"] = True
        return state
    if head == "siddhi":
        state.samjna_registry["1.1.64_P043_Ti_samjna_siddhi"] = True
        return state
    found = _find_p043_word_term(state, head)
    if found is None:
        return state
    ti, t = found
    li = _last_ac_index(t)
    if li is None:
        return state
    seg = "".join(v.slp1 for v in t.varnas[li:])
    t.meta["1_1_64_ti_segment_slp1"] = seg
    state.samjna_registry[f"1.1.64_P043_Ti_bhaga::{head}"] = seg
    state.terms[ti].varnas[li].tags.add("Ti")
    state.samjna_registry[("1.1.64_Ti", ti, li)] = True
    return state


def act(state: State) -> State:
    if _p043_queue_peek(state) is not None:
        return _p043_act(state)
    hit = next(_eligible(state), None)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi].tags.add("Ti")
    state.samjna_registry[("1.1.64_Ti", ti, vi)] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.64",
    sutra_type=SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1="aco antyAdi Ti",
    text_dev="अचोऽन्त्यादि टि",
    padaccheda_dev="अचः अन्त्य-आदि टि",
    why_dev="प्रत्ययस्य अन्त्य-अच्-आदि-भागः ‘टि’ संज्ञकः (डेमो-स्लाइस)।",
    anuvritti_from=("1.1.63",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

