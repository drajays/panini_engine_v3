"""
6.1.69  एङ्ह्रस्वात् सम्बुद्धेः  —  VIDHI

"After an eṅ (= e or o) or a hrasva (short vowel) stem, the final
 consonant of a sambuddhi-ekavacana pratyaya is elided (lopa)."

Operational reading: the sup pratyaya 'su' (upadeśa 's~') is used for
both prathamā-ekavacana (cell 1-1, gives रामः) AND sambuddhi-ekavacana
(cell 8-1, gives हे राम).  At sambuddhi-ekavacana the 's' of सु is
dropped (its inherent 'a' comes back with the preceding-a sandhi
giving just 'rAma' at the surface).

The engine's sup-attacher at 4.1.2 installs the same upadeśa for
cell 8-1 ('s' + anunāsika 'u').  We detect sambuddhi by checking
state.meta['vibhakti_vacana'] == '8-1' — BUT cond() cannot read
vibhakti/vacana (CONSTITUTION Article 2).  Instead, we tag the
pratyaya at 4.1.2 time with 'sambuddhi' when vv='8-1', and cond()
reads the tag.

To avoid modifying 4.1.2 just for this, we do the tagging lazily
here: if vibhakti_vacana == '8-1' (read in act() only — not cond()),
we install the tag; but since cond() must fire first, we use a
two-phase approach: cond() returns True whenever the pratyaya is
'su' AND carries tag 'sambuddhi'.  The tag is set by act() of 4.1.2
for cell 8-1 — see the tagging patch in sutras/adhyaya_4/pada_1/
sutra_4_1_2.py (companion update).

REPRESENTATIVE SIMPLIFICATION:
  For v3.1, we approximate: 6.1.69 fires when
    (a) preceding aṅga ends in a hrasva vowel ('a' here),
    (b) final pratyaya Term has tag 'sambuddhi', AND
    (c) the pratyaya contains 's' followed by anunāsika 'u'.
  Action: drop the 's' and the 'u(anunasika)', leaving the pratyaya
  empty — which then dissolves into the stem's inherent a.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


_HRASVA = frozenset({"a", "i", "u", "f", "x"})
_ENG    = frozenset({"e", "o"})


def _is_sambuddhi_su(state: State):
    """Detect the sambuddhi-ekavacana su configuration."""
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    if "sup" not in pratyaya.tags:
        return False
    if "sambuddhi" not in pratyaya.tags:
        return False
    if not anga.varnas or not pratyaya.varnas:
        return False
    last = anga.varnas[-1]
    if last.slp1 not in (_HRASVA | _ENG):
        return False
    # Pratyaya must still contain 's' (hasn't already been lopa-ed).
    if not any(v.slp1 == "s" for v in pratyaya.varnas):
        return False
    return True


def cond(state: State) -> bool:
    return _is_sambuddhi_su(state)


def act(state: State) -> State:
    if not _is_sambuddhi_su(state):
        return state
    pratyaya = state.terms[-1]
    # Drop all varṇas of the sambuddhi-su pratyaya (both 's' and
    # anunāsika 'u' — the whole pratyaya becomes zero).  Tag so the
    # sūtra doesn't re-fire.
    pratyaya.varnas = []
    pratyaya.meta["sambuddhi_lopa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.69",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "eN hrasvAt sambuddheH (haloH)",
    text_dev       = "एङ्ह्रस्वात् सम्बुद्धेः",
    padaccheda_dev = "एङ्-ह्रस्वात् सम्बुद्धेः — हलोः",
    why_dev        = "एङ्-अन्त / ह्रस्व-अन्त अङ्गात् परस्य सम्बुद्धि-एकवचन-"
                     "सु-प्रत्ययस्य हल्-वर्णस्य लोपः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
