"""
7.2.3  वदव्रजहलन्तस्याचः  —  VIDHI

Padaccheda: वद-व्रज-हल्-अन्तस्य अचः

वदव्रजहलन्तस्याचः (7.2.3)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 72003 · वदव्रजहलन्तस्याचः
              padaccheda: वद-व्रज-हल्-अन्तस्य अचः
              anuvṛtti:   64001: अङ्गस्य | 72001: सिचि वृद्धिः परस्मैपदेषु
  Source #2 — Kāśikā 7.2.3 udāharaṇa:
                अवादीत्
                अव्राजीत्
                विकल्पबाधनार्थं वदिव्रजिग्रहणम्
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_trc.py, tests/unit/test_Bavitavyam_split_prakriyas.py, tests/unit/test_Bavitum_split_prakriyas.py
  Reference record: sutra_ref_out/7_2_3.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_GATE_KEY: str = "7_2_3_vadavrajah_3"


_VRDDHI = {"a": "A", "i": "E", "I": "E", "u": "O", "U": "O", "e": "E", "o": "O"}
_AC = set("aAiIuUfFxXeEoO")


def _find(state: State):
    """वदव्रजहलन्तस्याचः (सिचि वृद्धिः परस्मैपदेषु, 7.2.1): the vowel of a
    hal-final aṅga before sic, in parasmaipada. 7.2.4 नेटि (not before iṭ) is the
    caller's condition: the luṅ spine asks only after 7.2.10 blocked iṭ."""
    if state.meta.get("_3_1_45_ksa_recipe"):
        return None            # 3.1.45 अपवाद: no वृद्धि for शल्-इगुपध-अनिट् roots
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or t.meta.get("7_2_3_done") or not t.varnas:
            continue
        if t.meta.get("6_4_48_a_lopa_done"):
            return None                       # 1.1.57 sthānivat: अवधीत्
        if t.varnas[-1].slp1 in _AC:
            return None                       # ac-final: 7.2.1's case
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or (nxt.meta.get("upadesha_slp1") or "").strip() != "sic":
            return None
        if "neti_7_2_4" in nxt.tags:
            return None            # 7.2.4 नेटि: sic has its iṭ, no vṛddhi
        tin = state.terms[-1]
        if "atmanepada" in tin.tags:
            return None
        for j in range(len(t.varnas) - 1, -1, -1):
            if t.varnas[j].slp1 in _VRDDHI:
                return (i, j)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    i, j = hit
    t = state.terms[i]
    t.varnas[j] = mk(_VRDDHI[t.varnas[j].slp1])      # पच् → पाच् (अपाक्षीत्)
    t.meta["7_2_3_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vadavrajahalantasyAcaH",
    text_dev              = "वदव्रजहलन्तस्याचः",
    padaccheda_dev        = "वद-व्रज-हल्-अन्तस्य अचः",
    why_dev               = "(सूत्रम् 7.2.3) वदव्रजहलन्तस्याचः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
