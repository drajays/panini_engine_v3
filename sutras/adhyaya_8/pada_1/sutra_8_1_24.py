"""
8.1.24  न चवाहाहैवयुक्ते  —  PRATISHEDHA

The ādeśas of 8.1.20–23 do not apply when the yuṣmad/asmad pada is *yukta* (directly joined) with
ca, vā, ha, aha or eva: तव च, मम वा, मे च is wrong — the full form stays.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com 8.1.24 
  Source #2 — Kāśikā 8.1.24: "युक्तग्रहणं साक्षाद्योगप्रतिपत्त्यर्थम्। युक्तयुक्ते प्रतिषेधो न भवति।
              ग्रामश्च ते स्वम्" — ca joined to *grāma*, not to te, so te is NOT blocked.
              (the blocked cases are ग्रामस्तव च स्वम्, … वा, … ह, … अह, … एव)

Engine: *yukta* = the very next pada on the tape is one of the five named particles (lexical identity
of the Term, as 7.2.94 reads "asmad"). A particle that precedes the pronoun belongs to the previous word.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_8.pada_1.enclitic_common import ADESHA_SUTRAS, PARTICLES_8_1_24, target
from engine.state import State


def _site(state: State):
    i = target(state, "8.1.24")
    if i is None or i + 1 >= len(state.terms):
        return None
    nxt = state.terms[i + 1]
    return i if "pada" in nxt.tags and (nxt.meta.get("upadesha_slp1") or "") in PARTICLES_8_1_24 else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.24",
    sutra_type=SutraType.PRATISHEDHA,
    text_slp1="na cavAhAhEvayukte",
    text_dev="न चवाहाहैवयुक्ते",
    padaccheda_dev="न च-वा-ह-अह-एव-युक्ते",
    why_dev="च / वा / ह / अह / एव से साक्षात् युक्त युष्मद्-अस्मद् पद पर ८.१.२०–२३ के आदेश नहीं होते।",
    anuvritti_from=("8.1.17", "8.1.18", "8.1.20"),
    blocks_sutra_ids=ADESHA_SUTRAS,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
