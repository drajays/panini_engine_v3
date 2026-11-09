"""
7.4.80  ओः पुयण्ज्यपरे  —  VIDHI

Padaccheda: ओः पु-यण्-जि अ-परे
Pāṭha: ashtadhyayi.com data.txt row i=74080 (Art. 14).
Sanvat/san abhyāsa u/ū → i when the root begins with a pu (p ph b bh m), a yaṇ (y v r l) or j, followed by an a-varṇa.
Examples and counter-examples: पिपविषते, पिपावयिषति, बिभावयिषति, यियविषति, जिजावयिषति; ओः इति किम्? पापच्यतेः सन् पापचिषते;
पुयण्जि इति किम्? अवतुतावयिषति, जुहावयिषति; अपरे इति किम्? बुभूषति.
The caṅ case (abībhavat) is reached through 7.4.93 sanvadbhāva.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_ONSET = frozenset("pPbBmyvrlj")
_A = frozenset("aA")


def _site(state: State):
    san = any("sanadi" in t.tags for t in state.terms)
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or t.meta.get("7_4_80_done") or not (san or t.meta.get("sanvat")):
            continue
        if not t.varnas or t.varnas[-1].slp1 not in ("u", "U"):
            continue
        dh = [v.slp1 for v in state.terms[i + 1].varnas if "aT_agama_v" not in v.tags]
        if len(dh) >= 2 and dh[0] in _ONSET and dh[1] in _A:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    t.varnas[-1] = mk("i")
    t.meta["7_4_80_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.80",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "oH puyaRjyapare",
    text_dev              = "ओः पुयण्ज्यपरे",
    samagra_slp1          = "aNgasya aByAsasya oH puyaRji apare it sani",
    samagra_dev           = "अङ्गस्य अभ्यासस्य ओः पुयण्जि अपरे इत् सनि",
    padaccheda_dev        = "ओः पु-यण्-जि अ-परे",
    why_dev               = "(सूत्रम् 7.4.80) ओः पुयण्ज्यपरे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
