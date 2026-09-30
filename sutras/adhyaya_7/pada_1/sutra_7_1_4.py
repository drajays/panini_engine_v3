"""
7.1.4  अदभ्यस्तात्  —  VIDHI (apavāda of 7.1.3)

Padaccheda: अत् अभ्यस्तात्

After an *abhyasta* aṅga (6.1.5 उभे अभ्यस्तम् — the reduplicated *gaṇa* 3
*juhotyādi* stem, or any other *abhyasta* formation), the *jhi* tiṅ-ādeśa's
*jh* is replaced by *at* (not **7.1.3**'s general *ant*): *jhi* → *ati*
(जुहु + अति → जुह्वति, not *जुहवन्ति), *jh* → *at*.

Engine: structural — same ``jhi``/``jh`` term detection as **7.1.3**, but
fires first when any ``Term`` on the tape carries the ``abhyasa`` tag (the
signal **6.1.5**'s own docstring names). Once this replaces the term's
``upadesha_slp1``, **7.1.3**'s own site-check no longer matches ``jhi``, so
calling **7.1.4** before **7.1.3** in a pipeline is a correct apavāda order
without needing an explicit gate on **7.1.3** itself.

Scope: the *abhyasta* half of the sūtra only (gaṇa 3 śluvikaraṇa, gaṇa 2's
lexically-reduplicated roots like जक्ष्). The *ad* (अत्ति) half is not yet
wired — अद्-root laṭ 3pl (अदन्ति) still resolves through the general 7.1.3
path, since अद् does not carry an ``abhyasa`` Term.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 71004 · अदभ्यस्तात्
              padaccheda: अत् अभ्यस्तात्
              anuvṛtti:   71003: झः | 71002: प्रत्ययस्यादेः | 64001: अङ्गस्य
  Source #2 — Kāśikā 7.1.4 udāharaṇa:
                जुह्वति
                बिभ्रति
                ददति
  Reference record: sutra_ref_out/7_1_4.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _has_abhyasa(state: State) -> bool:
    return any("abhyasa" in t.tags for t in state.terms)


def _find_jh_term(state: State):
    """Return (index, kind) where kind in {'jhi', 'jh'} — parasmai jhi only;
    the abhyasta apavāda does not touch the ātmanepada Ja/Je path."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        vs = t.varnas
        if up != "jhi":
            continue
        if len(vs) == 3 and vs[0].slp1 in {"j", "J"} and vs[1].slp1 == "h" and vs[2].slp1 == "i":
            return (i, "jhi")
        if len(vs) == 2 and vs[0].slp1 in {"j", "J"} and vs[1].slp1 == "h":
            return (i, "jh")
    return None


def cond(state: State) -> bool:
    return _has_abhyasa(state) and _find_jh_term(state) is not None


def act(state: State) -> State:
    if not _has_abhyasa(state):
        return state
    result = _find_jh_term(state)
    if result is None:
        return state
    idx, kind = result
    old = state.terms[idx]
    new_slp1 = "ati" if kind == "jhi" else "at"
    new_term = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(new_slp1),
        tags=set(old.tags),
        meta=dict(old.meta),
    )
    new_term.meta["upadesha_slp1"] = new_slp1
    new_term.tags.discard("upadesha")
    state.terms[idx] = new_term
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1              = "adaByastAt",
    text_dev               = "अदभ्यस्तात्",
    padaccheda_dev         = "अत् अभ्यस्तात्",
    why_dev                = "अभ्यस्तात् परस्य झेः अत्-आदेशः (जुह्वति) — सप्तम्याः ७.१.३ अपवादः।",
    anuvritti_from         = ("7.1.1", "7.1.3"),
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
