"""
7.4.76  भृञामित्  —  VIDHI (apavāda of 7.4.66 उरत्, in श्लौ)

Padaccheda: भृञाम् इत्

Under **7.4.75**'s ``śrau`` (गण 3 *ślu*-vikaraṇa) context, *bhṛñ*'s (भृ)
*abhyāsa* ऋ becomes *it* (इ) — बिभर्ति, not *बर्भर्ति (the general **7.4.66**
उरत् ऋ→अ would give). Scoped to भृ specifically (root varṇas ``Bf`` after
*it*-lopa); other गण-3 ऋ-roots (घृ, हृ, सृ, …) still take **7.4.66**.

Engine: structural — finds the ``abhyasa``-tagged Term whose sibling
non-``abhyasa`` ``dhatu`` Term has varṇas ``Bf``, replaces its ``f``/``F``
with ``i``. Must run before **7.4.66** (mutual exclusion by consuming the
ऋ/ॠ varṇa **7.4.66** would otherwise find).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 74076 · भृञामित्
              padaccheda: भृञाम् इत्
              anuvṛtti:   74075: त्रयाणाम् गुणः श्लौ (श्लौ carried; गुणः/त्रयाणाम् not) |
                          74058: अभ्यासस्य
  Source #2 — Kāśikā 7.4.76 udāharaṇa:
                बिभर्ति
                बिभृतः
                बिभ्रति
  Reference record: sutra_ref_out/7_4_76.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_TARGET_ROOTS = {"Bf", "mA", "hA"}      # भृञ्, माङ्, ओहाङ् (juhotyādi: abhyāsa → i: बिभर्ति, मिमीते, जिहीते)


def _root_varnas(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _find(state: State):
    dhatu = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dhatu is None or _root_varnas(dhatu) not in _TARGET_ROOTS:
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_76_done"):
            continue
        for j, v in enumerate(t.varnas):
            if v.slp1 in {"f", "F"} or (v.slp1 in {"a", "A"} and _root_varnas(dhatu) in {"mA", "hA"}
                                         and dhatu.meta.get("slu_replaced_sap")):
                return ti, j
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j = hit
    state.terms[ti].varnas[j] = mk("i")
    state.terms[ti].meta["7_4_76_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.76",
    sutra_type            = SutraType.VIDHI,
    text_slp1              = "BfYAmit",
    text_dev               = "भृञामित्",
    padaccheda_dev         = "भृञाम् इत्",
    why_dev                = "भृञः अभ्यासस्य ऋकारस्य इत्-आदेशः श्लौ (बिभर्ति) — ७.४.६६ उरत्-अपवादः।",
    anuvritti_from         = ("7.4.75", "7.4.58"),
    apavada_of            = ("7.4.66",),   # the ṛ of the abhyāsa goes to i, not (u)ra-t
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
