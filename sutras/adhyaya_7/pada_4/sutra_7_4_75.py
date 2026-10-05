"""
7.4.75  निजां त्रयाणां गुणः श्लौ  —  VIDHI

Padaccheda: निजाम् त्रयाणाम् गुणः श्लौ

Under गण-3 *ślu* (**6.1.10** *ślau*), the *abhyāsa* of निज्/विज्/विष् (the
"three of *nij*") always takes *guṇa* (इ → ए) — नेनेक्ति *and* नेनिक्तः
(both strong and weak cells; every other root's *abhyāsa* stays at its
base grade regardless of the *aṅga*'s own strong/weak alternation).

Engine: structural — the *abhyāsa* Term's own root sibling (non-*abhyāsa*
``dhatu``) has varṇas ``nij``/``vij``/``viz`` (after *it*-lopa); replace the
*abhyāsa*'s इ with ए, once (idempotent).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 74075 · निजां त्रयाणां गुणः श्लौ
              padaccheda: निजाम् त्रयाणाम् गुणः श्लौ
              anuvṛtti:   74058: अभ्यासस्य
  Source #2 — Kāśikā 7.4.75 udāharaṇa:
                नेनेक्ति
                वेवेक्ति
                वेवेष्टि
  Reference record: sutra_ref_out/7_4_75.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_TARGET_ROOTS = {"nij", "vij", "viz"}


def _root_varnas(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _find(state: State):
    dhatu = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dhatu is None:
        return None
    up = (dhatu.meta.get("upadesha_slp1") or "").replace("~", "")
    if not (_root_varnas(dhatu) in _TARGET_ROOTS or up.startswith(("Rij", "vij", "viz"))):   # Riji~r: ṇ is still ṇ here
        return None
    if not dhatu.meta.get("slu_replaced_sap"):
        return None            # ślau (7.4.75 anuvṛtti): juhotyādi only — not tudādi vijI~ in liṭ (vivije)
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags or t.meta.get("7_4_75_nijadi_guna_done"):
            continue
        for j, v in enumerate(t.varnas):
            if v.slp1 == "i":
                return ti, j
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j = hit
    state.terms[ti].varnas[j] = mk("e")
    state.terms[ti].meta["7_4_75_nijadi_guna_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.75",
    sutra_type            = SutraType.VIDHI,
    text_slp1              = "nijAM trayARAM guRaH SlO",
    text_dev               = "निजां त्रयाणां गुणः श्लौ",
    padaccheda_dev         = "निजाम् त्रयाणाम् गुणः श्लौ",
    why_dev                = "निज्-विज्-विषाम् अभ्यासस्य नित्यं गुणः श्लौ (नेनेक्ति, नेनिक्तः दोनों)।",
    anuvritti_from         = ("7.4.58",),
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
