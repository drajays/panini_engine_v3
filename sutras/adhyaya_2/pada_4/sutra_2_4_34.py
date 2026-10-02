"""
2.4.34  द्वितीयाटौस्स्वेनः  —  VIDHI

Padaccheda: द्वितीया-टा-ओस्सु एनः

In anvādeśa (a second mention of what a clause already named, now with a new predicate: 2.4.32) इदम् and एतद्
are replaced, as a whole, by एन before the dvitīyā sups and ṭā / os: एनम्, एनौ, एनान्, एनेन, एनयोः (strī एनाम्, एनया).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 2.4.34 (padaccheda: द्वितीया-टा-ओस्सु एनः)
  Source #2 — ashtadhyayi.com śabda-prakriyā for इदम् : एन+अम् [2.4.34] | एनम् [6.1.107] ;
              एन+आ [2.4.34] | एन+इन [7.1.12] | एनेन [6.1.87] ; एन+ओस् [2.4.34] | एनयोस् [6.1.78]

Engine: ``anvadesha`` is a Term tag on the stem — an input like the liṅga tag, because anvādeśa is a fact about the
sentence, not about the word (Art. 17: analysis proposes, generation verifies). The rule reads the tag, the stem's
lexical identity (idam / etad) and the sup's identity (am, auṭ, śas, ṭā, os — ṭā also as its ādeśa ina). The ādeśa is
the whole stem (sarvādeśa, 1.1.55); aṅgatva and the sarvanāma saṃjñā pass to it by 1.1.56.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import ANGATVA, adesha_substitute_varnas

_STEMS = frozenset({"idam", "etad"})
_SUPS = frozenset({"am", "Ow", "Sas", "wA", "os"})   # dvitīyā (am, auṭ, śas), ṭā, os


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "anvadesha" not in t.tags or (t.meta.get("upadesha_slp1") or "").strip() not in _STEMS:
            continue
        if t.meta.get("2_4_34_done"):
            continue
        nxt = state.terms[i + 1]
        ident = (nxt.meta.get("upadesha_slp1_original") or nxt.meta.get("upadesha_slp1") or "").strip()
        if "sup" in nxt.tags and ident in _SUPS:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        adesha_substitute_varnas(t, "ena", state, sutra_id="2.4.34", gunadharmas=frozenset({ANGATVA}))
        t.meta["2_4_34_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.34",
    sutra_type=SutraType.VIDHI,
    text_slp1="dvitIyAwOssvenaH",
    text_dev="द्वितीयाटौस्स्वेनः",
    padaccheda_dev="द्वितीया-टा-ओस्सु एनः",
    why_dev="अन्वादेश में इदम् / एतद् को एन आदेश, द्वितीया-टा-ओस् परे (एनम्, एनेन, एनयोः)।",
    anuvritti_from=("2.4.32",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
