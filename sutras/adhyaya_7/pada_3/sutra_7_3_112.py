"""
7.3.112  आण्नद्याः  —  VIDHI

Padaccheda: आट् · नद्याः

After a stem with the **नदी** saṃjñā (1.4.3), a ṅit sup takes the आट् āgama.
The augment is all this rule does; the rest is ordinary sandhi, and doing it
any other way would hide two rules that are already implemented:

    नदी + ए     (ङे, after 1.3.8/1.3.9 drop the ṅ)
    नदी + आ ए   आट् — this sūtra
    नदी + ऐ     6.1.88 वृद्धिरेचि
    नद्यै        6.1.77 इको यणचि

The same augment gives नद्याः for ङसि and ङस् (आ + अस् → आस् by 6.1.101).
सप्तमी एकवचन is not here: ङि is replaced by आम् under 7.3.116.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 73112 · आण्नद्याः
              padaccheda: आट् नद्याः
              anuvṛtti:   64001: अङ्गस्य | 73111: ङिति
  Source #2 — Kāśikā 7.3.112 udāharaṇa:
                कुमार्यै
                ब्रह्मबन्ध्वै
                कुमार्याः
  Cross-check — surface pinned by: tests/regression/test_shabda_paradigms.py
  Reference record: sutra_ref_out/7_3_112.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

# ङे · ङसि · ङस् — the ṅit sups this augment attaches to. ङि goes to 7.3.116.
NGIT_SUPS: frozenset = frozenset({"Ne", "Nasi", "Nas"})
_DONE = "7_3_112_At_agama_done"


def _target(state: State):
    """(aṅga, affix) when नदी + ṅit-sup is on the tape and āṭ is still owed."""
    if len(state.terms) < 2:
        return None
    anga, affix = state.terms[-2], state.terms[-1]
    if "nadi" not in anga.tags or "sup" not in affix.tags:
        return None
    if affix.meta.get(_DONE) or not affix.varnas:
        return None
    if (affix.meta.get("upadesha_slp1") or "") not in NGIT_SUPS:
        return None
    # Only once the ṅ of ङे / ङसि / ङस् has gone (1.3.8 → 1.3.9): the āgama
    # attaches to the affix, not in front of an it-marker that is about to be
    # dropped. The ordering is the condition's business, not the schedule's.
    if affix.varnas[0].slp1 == "N":
        return None
    return anga, affix


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    found = _target(state)
    if found is None:
        return state
    _anga, affix = found
    affix.varnas.insert(0, mk("A"))
    # ङसि carries an उच्चारणार्थ इ that is no part of the affix's phonetic
    # content; 6.1.110 already trims it the same way where it consumes ङसि.
    if affix.meta.get("upadesha_slp1") == "Nasi" and affix.varnas[-1].slp1 == "i":
        del affix.varnas[-1]
    affix.meta[_DONE] = True
    state.meta["__why_now_dev__"] = (
        "नदी-संज्ञकात् परे ङित्-सुपि आट्-आगमः; ततः ६.१.८८ (आ+ए → ऐ) अथवा "
        "६.१.१०१ (आ+अ → आ) इति एकादेशः।"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.112",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ARnadyAH",
    text_dev       = "आण्नद्याः",
    padaccheda_dev = "आट् · नद्याः",
    why_dev        = "नदी-संज्ञकात् परे ङित्-सुप्-प्रत्ययस्य आट्-आगमः (नद्यै · नद्याः)।",
    anuvritti_from = ("7.3.111",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
