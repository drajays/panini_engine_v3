"""
7.1.18  औङ आपः  —  VIDHI

Padaccheda: औङः आपः

औङ आपः (7.1.18)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 71018 · औङः आपः
              anuvṛtti: 64001: अङ्गस्य | 71017: शी
  Source #2 — Kāśikā 7.1.18 udāharaṇa:
                खट्वे तिष्ठतः
                खट्वे पश्य
                बहुराजे
                कारीषगन्ध्ये
  Cross-check — tests/unit/test_sutra_7_1_18_ONa_ApaH.py; the vendored rādhā paradigm pins राधे.
  Reference record: sutra_ref_out/7_1_18.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

# औङ् = the dual of prathamā (au) and of dvitīyā (auṭ).
_AUNG = frozenset({"O", "Ow"})


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags and "prātipadika" not in anga.tags:
        return False
    # ponytail: āp-anta is read as "ā-final strīliṅga" — the engine does not yet carry
    # which of ṭāp/ḍāp/cāp made the stem; upgrade when 4.1.4–4.1.15 are real rules.
    if "strīliṅga" not in anga.tags or not anga.varnas or anga.varnas[-1].slp1 != "A":
        return False
    return "sup" in pr.tags and pr.meta.get("upadesha_slp1") in _AUNG


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    pr = state.terms[-1]
    pr.varnas = [mk("S"), mk("I")]
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1")
    pr.meta["upadesha_slp1"] = "SI"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.18",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "ONa ApaH",
    text_dev              = "औङ आपः",
    samagra_slp1          = "ApaH aNgAt ONaH SI",
    samagra_dev           = "आपः अङ्गात् औङः शी",
    padaccheda_dev        = "औङः आपः",
    why_dev               = "आबन्तात् अङ्गात् परस्य औङः (औ / औट्) स्थाने शी (राधा + औ → राधा + शी → राधे)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
