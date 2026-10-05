"""
6.1.11  चङि  —  PARIBHASHA (narrow gate: *luṅ* reduplication frame)

Operational JSON **P037** cites *dvitva* under *luṅ*(*i*): this engine slice
records eligibility and arms the existing **6.1.1** *dvitva* hook (recipe must
still call **6.1.1** with ``dvitva_recipe`` afterwards).

COND: ``state.meta['lugi_recipe']`` after the luṅ spine has created
the structural aorist context.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61011 · चङि
              padaccheda: चङि
              anuvṛtti:   61008: धातोः अनभ्यासस्य | 61001: एकाचः द्वे प्रथमस्य | 61002: अजादेः द्वितीयस्य
  Source #2 — Kāśikā 6.1.11 udāharaṇa:
                अपीपचत्
                अपीपठत्
                आटिटत्
  Cross-check — surface pinned by: tests/unit/test_AwIwat_luN_aT_Nic_caN_tip.py, tests/unit/test_gita_gap_fixes.py, tests/unit/test_sthanivat_al_ashrita_exceptions.py
  Reference record: sutra_ref_out/6_1_11.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "P037_6_1_11_lugi_dvitva"


def _general(state: State):
    """चङि: the dhātu before caṅ is doubled (its first ekāc part; 7.4.60 trims the
    abhyāsa) — चुर् → चुचुर्. Hal-initial dhātus only here."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "caG" for t in state.terms):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags and "abhyasa" not in t.tags:
            if i and "abhyasa" in state.terms[i - 1].tags:
                return None
            j = next((k for k, v in enumerate(t.varnas) if "aT_agama_v" not in v.tags), None)    # the aṭ stands before the abhyāsa
            if j is None or t.varnas[j].slp1 in "aAiIuUfFxeEoO":
                return None
            return i
    return None

def cond(state: State) -> bool:
    if _general(state) is not None:
        return True
    if GATE_KEY in state.paribhasha_gates:
        return False
    return bool(state.meta.get("lugi_recipe"))


def act(state: State) -> State:
    gi = _general(state)
    if gi is not None:
        from copy import deepcopy
        from engine.state import Term
        dh = state.terms[gi]
        j = next(k for k, v in enumerate(dh.varnas) if "aT_agama_v" not in v.tags)
        pre, dh.varnas = dh.varnas[:j], dh.varnas[j:]      # aṭ + abhyāsa + dhātu (अचूचुरत्)
        ab = Term(kind=dh.kind, varnas=[deepcopy(v) for v in dh.varnas],
                  tags=(set(dh.tags) | {"abhyasa"}) - {"dhatu"}, meta={})
        state.terms.insert(gi, ab)
        if pre:         # the aṭ is its own Term before the abhyāsa — 7.4.60 must not read it
            state.terms.insert(gi, Term(kind="pratyaya", varnas=pre, tags={"pratyaya", "agama", "aT_agama"},
                                        meta={"upadesha_slp1": "aw"}))
        state.paribhasha_gates["6_1_11_cani_dvitva"] = True
        return state
    state.paribhasha_gates[GATE_KEY] = True
    state.meta.pop("lugi_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.11",
    sutra_type=SutraType.VIDHI,
    text_slp1='caNi',
    text_dev='चङि',
    padaccheda_dev="लुङि",
    why_dev="लुङ-प्रकरणे द्वित्व-प्रवृतौ ग्लास-बॉक्स् द्वारः (P037)।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
