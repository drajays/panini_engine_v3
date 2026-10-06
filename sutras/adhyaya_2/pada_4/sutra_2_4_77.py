"""
2.4.77  गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु  —  VIDHI

Two operational paths:
  1. Arm ``2_4_77_arm``: legacy gate-setter.
  2. Arm ``2_4_77_luG_sic_lopa_arm``: luṅ — luk (total deletion) of the siC
     pratyaya term for bhū in parasmaipada.  After 3.1.44 cli→sic, this arm
     removes the sic term entirely so only dhātu + tiṅ remain.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 24077 · गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु
              padaccheda: गाति-स्था-घु-पा-भूभ्यः सिचः परस्मैपदेषु
              anuvṛtti:   24058: लुक्
  Source #2 — Kāśikā 2.4.77 udāharaṇa:
                अगात्
                अस्थात्
                अदात्
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhut_lung.py
  Reference record: sutra_ref_out/2_4_77.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_77_gati_stha_sica"


def _find_sic_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        return i
    return None


# गाति-स्था-घु-पा-भू (upadeśa identity): इण् (→ गा, 2.4.45), ष्ठा, the ghu roots
# (1.1.20 दाधा घ्वदाप् — dā/dhā-rūpa, not दाप्/दैप्), पा पाने, भू.
SIC_LUK_UPADESHA = frozenset({"iR", "gA", "zWA", "qudAY", "quDAY", "do", "dAR", "deN", "DeW", "pA", "BU", "BU~"})


def sic_luk_dhatu(state: State) -> bool:
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    return dh is not None and (dh.meta.get("upadesha_slp1") or "").strip() in SIC_LUK_UPADESHA


def _parasmaipada(state: State) -> bool:
    """परस्मैपदेषु — the tiṅ ādeśa is a parasmaipada one (1.4.99 tag)."""
    # The pada belongs to the sthānin (1.4.99): a tiṅ that 3.4.101 made spell like ta (Ta → ta) is still parasmaipada.
    return any("tin_adesha_3_4_78" in t.tags and "atmanepada" not in t.tags
               and ("parasmaipada" in t.tags or (t.meta.get("upadesha_slp1") or "").strip() not in _TAN)
               for t in state.terms)


_TAN = frozenset({"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG", "mahiN"})


def cond(state: State) -> bool:
    # sic-luk only after these roots, only in parasmaipada (अभूत्, अस्थात्,
    # अदात्, अपात्); every other root keeps sic (अनैषीत्, अपाक्षीत्).
    return _find_sic_index(state) is not None and sic_luk_dhatu(state) and _parasmaipada(state)


def act(state: State) -> State:
    j = _find_sic_index(state)
    if j is not None:
        state.terms.pop(j)
        state.samjna_registry["2.4.77_sic_luk"] = True
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"] = "2.4.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gAtisTAGupABUByaH sicaH parasmEpadezu",
    text_dev              = "गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु",
    samagra_slp1          = "gAti-sTA-Gu-pA-BUByaH sicaH parasmEpadezu luk",
    samagra_dev           = "गाति-स्था-घु-पा-भूभ्यः सिचः परस्मैपदेषु लुक्",
    padaccheda_dev        = "गाति-स्था-घु-पा-भूभ्यः सिचः परस्मैपदेषु",
    why_dev               = (
        "लुङि भू-आदिभ्यः परस्मैपदे सिच्-विकरणस्य लुक् — "
        "सिच् सम्पूर्णतः लुप्यते; पश्चात् ६.४.८८ वुक्-आगमः।"
    ),
    anuvritti_from        = ('2.4.72',),
    # NOT a true apavāda (different sthānī: sic vs jhi) — a stand-in for a jñāpaka. Classically: 3.4.109's jus is not
    # triggered by a luk'd sic (1.1.62 pratyayalakṣaṇa does not carry it; 3.4.110 आतः would be vyartha otherwise), so
    # अभूवन् (jhi→ant, 7.1.3), not *अभूवुः. 1.1.63 alone does not explain it (jus is pratyaya-kārya, not aṅga-kārya).
    # Needed because the engine's 3.4.108 also does 3.4.109's luṅ-sic jus and sees sic before 2.4.77 pops it.
    # TODO: replace by a CONFLICT_OVERRIDES entry (Art. 21 L10) once an amendment records the jñāpaka.
    apavada_of            = ("3.4.108",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
