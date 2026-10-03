"""
3.4.85  लोटो लङ्वत्  —  ATIDESHA (लकारप्रत्ययातिदेशः)

Padaccheda: लोटः लङ्-वत्   Anuvṛtti: लस्य 3.4.77 · adhikāra: प्रत्ययः · परश्च · आद्युदात्तश्च · धातोः

लोट्-लकारस्य प्रत्ययाः लङ्-लकारवत् — the *pratyaya*-kārya of laṅ holds for loṭ: 3.4.101 (तस्→ताम्, थस्→तम्,
थ→त) and 3.4.99 (वस्/मस् lose s). The *aṅga*-kārya of laṅ — 6.4.71 अट् — does not: the Kāśikā reads वा in
from 3.4.83 as a व्यवस्थितविभाषा (प्रत्ययकार्यं भवति, अङ्गकार्यं न). Where loṭ has its own ādeśa that
stands (3.4.89 मेर्निः for मिप्; 3.4.86 एरुः against 3.4.100 इतश्च) it wins as apavāda.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34085 · लोटो लङ्वत्   anuvṛtti: 34077: लस्य
  Source #2 — Kāśikā 3.4.85: "विदो लटो वा (३.४.८३) इत्यतो वाग्रहणमनुवर्तते" (व्यवस्थितविभाषा);
              user-supplied commentary text of 2026-10-03 (examples: पठतम्, पठाव; मेर्नि / एरुः as apavādas)
  Cross-check — tests/unit/test_lot_laNvat.py
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _loT_tin_terms(state: State):
    """tiṅ ādeśas whose source lakāra is loṭ and that have not yet been given laṅ's pratyaya-kārya."""
    for t in state.terms:
        if t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags:
            continue
        if (t.meta.get("source_lakara_upadesha") or "").strip() != "loT":
            continue
        if "laNvat" in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_loT_tin_terms(state), None) is not None


def act(state: State) -> State:
    # अतिदेश: loṭ's pratyaya-kārya is laṅ's. What laṅ has that is *aṅga*-kārya (6.4.71 aṭ) is not
    # carried over — the Kāśikā reads 'vā' in from 3.4.83 as a vyavasthita vibhāṣā — so the property
    # is a tag on the tiṅ ādeśa, and the sūtras that read it (3.4.99 · 3.4.100 · 3.4.101) are all
    # pratyaya-kārya.
    for t in _loT_tin_terms(state):
        t.tags.add("laNvat")
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.85",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = "lowo laNvat",
    text_dev              = "लोटो लङ्वत्",
    padaccheda_dev        = "लोटः लङ्-वत्",
    why_dev               = "लोट्-लकारस्य प्रत्ययकार्यं लङ्-वत् (नित्यं ङितः, इतश्च, तस्थस्थमिपां…); अङ्गकार्यं (अडागमः) न।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
