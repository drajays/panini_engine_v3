"""
6.4.134  अल्लोपोऽनः  —  VIDHI

Under *bhasya*, before an affix such as *śas* (→ *as* after *it*-lopa), the
penultimate *a* of an *n*-final stem (*upadhā*) is deleted — e.g. *rājan* + *as*
→ *rājn* + *as* … *rājñaḥ*.

Engine slice: *bha* *aṅga* whose last two phonemes are ``a`` + ``n`` (hrasva
``a`` as upadhā to final ``n``); delete that ``a``.

Narrow extension (split_prakriyas_11 P006 only):
  Some feminine derivations in the JSON corpus model *yuvan* → *yuva* before
  vowel-initial strī-pratyaya **ti** using this sūtra id. To stay rule-based
  while avoiding global behavior changes, we provide an **armed** alternate
  branch that deletes the **final n** of an ``an``-stem when
  ``state.meta['6_4_134_an_final_n_lopa_arm']`` is True.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State


def _find_upadhā_a(state: State):
    if len(state.terms) < 2:
        return None
    for ti in range(len(state.terms) - 1):
        anga = state.terms[ti]
        if "anga" not in anga.tags or "bha" not in anga.tags:
            continue
        if not adhikara_in_effect("6.4.134", state, "6.4.1"):
            continue
        if not adhikara_in_effect("6.4.134", state, "6.4.129"):
            continue
        vs = anga.varnas
        if len(vs) < 2:
            continue
        if vs[-1].slp1 != "n":
            continue
        if vs[-2].slp1 != "a":
            continue
        return (ti, len(vs) - 2)
    return None


def _find_final_n_arm(state: State):
    if not state.meta.get("6_4_134_an_final_n_lopa_arm"):
        return None
    if len(state.terms) < 2:
        return None
    for ti in range(len(state.terms) - 1):
        anga = state.terms[ti]
        if "anga" not in anga.tags:
            continue
        vs = anga.varnas
        if not vs or vs[-1].slp1 != "n":
            continue
        # n-final with preceding a (an-stem) — this is the narrow P006 witness.
        if len(vs) < 2 or vs[-2].slp1 != "a":
            continue
        # Require a following affix; P006 uses **ti**.
        nxt = state.terms[ti + 1]
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if nxt.kind != "pratyaya" or up not in {"ti", "tip"}:
            continue
        return (ti, len(vs) - 1)
    return None


def cond(state: State) -> bool:
    return _find_upadhā_a(state) is not None or _find_final_n_arm(state) is not None


def act(state: State) -> State:
    hit = _find_upadhā_a(state)
    if hit is None:
        hit = _find_final_n_arm(state)
    if hit is None:
        return state
    ti, vi = hit
    del state.terms[ti].varnas[vi]
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.134",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "allopo'naH",
    text_dev       = "अल्लोपोऽनः",
    padaccheda_dev = "अत्-लोपः अनः",
    why_dev        = "भसंज्ञके नान्ते उपधायाः अकारस्य लोपः (उदा. राजन् + शस्)।",
    anuvritti_from = ("6.4.1", "6.4.129"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
