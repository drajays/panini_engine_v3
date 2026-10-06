"""
8.4.45  यरोऽनुनासिकेऽनुनासिको वा  —  VIBHASHA  (Tripāḍī)

पदान्त a यर् (any hal except ह्) followed by an anunāsika (ङ ञ ण न म, or a varṇa
carrying the ``anunasika`` tag) optionally becomes the anunāsika of its own varga
(sthāna-ānantarya); य् व् ल् become the nasal semivowels (``anunasika`` tag):

    वाग् + मुखम् → वाङ्मुखम् | वाग्मुखम्        मरुज् + ञ → मरुञ्ञ…
    षड् + मुख → षण्मुख | षड्मुख                 सुहृद् + मम → सुहृन्मम | सुहृद्मम
    त्रिष्टुब् + नमति → त्रिष्टुम्नमति            चल् + नमति → चल्ँनमति | चल्नमति

Optional (vibhāṣā): the default reading leaves the rule unapplied;
``engine.vikalpa.choose({"8.4.45": True})`` / ``explore`` yields the nasal pakṣa.
*Padānta* = the left varṇa is the last of a Term tagged ``pada``; ``bha``-tagged
Terms (मरुत्मत्, 1.4.19) are not padas.  Scans the flattened varṇa stream across
Terms.  Not modelled: the vārttika that makes it nitya before a nasal *pratyaya*
(तन्मात्र, चिन्मय, षण्णाम्).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84045 · यरोऽनुनासिकेऽनुनासिको वा
              padaccheda: यरः · अनुनासिके · अनुनासिकः · वा
              anuvṛtti:   84042: पदान्तस्य | 82108: संहितायाम्
  Source #2 — Kāśikā 8.4.45 udāharaṇa:
                वाङ्मुखम् / वाग्मुखम्
                षण्मुखः / षड्मुखः
                तन्मात्रम् (vārttika, nitya)
  Cross-check — surface pinned by: tests/unit/test_8_4_45.py
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_NASAL_OF = {c: n for n, cs in (("N", "kKgG"), ("Y", "cCjJ"), ("R", "wWqQ"),
                                ("n", "tTdD"), ("m", "pPbB")) for c in cs}
_SEMI = frozenset("yvl")
_NASALS = frozenset("NYRnm")


def _find(state: State):
    """First (Term, index) of a padānta yar before an anunāsika, or None."""
    if not state.tripadi_zone:
        return None
    live = [t for t in state.terms if t.varnas]
    for a, b in zip(live, live[1:]):
        x, y = a.varnas[-1], b.varnas[0]
        if "pada" not in a.tags or "bha" in a.tags:
            continue
        if x.slp1 not in _NASAL_OF and not (x.slp1 in _SEMI and "anunasika" not in x.tags):
            continue
        if y.slp1 in _NASALS or "anunasika" in y.tags:
            return a, len(a.varnas) - 1
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    t, i = hit
    old = t.varnas[i].slp1
    if old in _SEMI:
        t.varnas[i].tags.add("anunasika")
        new = old + "~"
    else:
        new = _NASAL_OF[old]
        t.varnas[i] = mk(new)
    state.meta["__why_now_dev__"] = (
        f"पदान्त-यरः ({old}) अनुनासिके परे विकल्पेन अनुनासिकः ({new}); "
        "यथा वाग्+मुखम् → वाङ्मुखम्, पक्षे वाग्मुखम्। (८.४.४५)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.45",
    sutra_type=SutraType.VIBHASHA,
    text_slp1="yaronunAsikenunAsiko vA",
    text_dev="यरोऽनुनासिकेऽनुनासिको वा",
    samagra_slp1="padasya yaraH anunAsike anunAsikaH vA",
    samagra_dev="पदस्य यरः अनुनासिके अनुनासिकः वा",
    padaccheda_dev="यरः अनुनासिके अनुनासिकः वा",
    why_dev="पदान्तस्य यरः अनुनासिके परे विकल्पेन स्ववर्गीयः अनुनासिकः (य्-व्-ल् अनुनासिकाः)।",
    anuvritti_from=("8.4.42", "8.2.108"),
    vibhasha_default=False,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
