"""
1.4.22  द्व्येकयोर्द्विवचनैकवचने  —  PARIBHASHA

*Padaccheda:* *dvi-ekayoḥ* (saptamī *dvivacanam* of *dvi* and *eka* in compound), *dvivacana-ekavacane* (nominative dual).

*Śāstra* *niyama (laghu):* when *dva* is to be denoted, *divivacana* *pratyaya*; when *eka*, *ekavacana* — for *tiṅ* (**1.4.102**) and *sup* (**1.4.103**).  *Vivakṣā* is by recipe: ``1_4_22_affix_class`` ∈ {``"dvi"``, ``"eka"``} on the primary *dhātu*.

*Anuvṛtti:* **1.4.1** *ekasañjñā*.

*Engine:* ``paribhasha_gates``; **R3**-safe ``cond``; no *vākya* semantics.
Pāṭha: ashtadhyayi.com data.txt row i=14022 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import find_primary_dhatu


# --- helpers of this sūtra (formerly dvi_eka_1_4_22.py; one sūtra, one file) ---
from typing import Final, Literal

from engine.state import State, Term

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import find_primary_dhatu

GATE_KEY: Final[str] = "prayoga_1_4_22_dvi_eka_affix_niyama"

# ``"dvi"`` ⇒ *divivacana*; ``"eka"`` ⇒ *ekavacana* — not *meta['vacana']* (CONSTITUTION Art. 2).
NIMITTA_VALUES: Final[tuple[str, ...]] = ("dvi", "eka")
DVI_EKA_NIMITTA_KEY: Final[str] = "1_4_22_affix_class"

def dvi_eka_22_licences(state: State) -> bool:
    g = state.paribhasha_gates.get(GATE_KEY, {})
    if g.get("active") is not True:
        return False
    return g.get("nimitta") in NIMITTA_VALUES


def _read_nimitta(d: Term) -> Literal["dvi", "eka"] | None:
    v = d.meta.get(DVI_EKA_NIMITTA_KEY)
    if v == "dvi" or v == "eka":
        return v
    return None


def dvi_eka_22_gate_needs_update(state: State) -> bool:
    d = find_primary_dhatu(state)
    if d is None:
        return False
    n = _read_nimitta(d)
    if n is None:
        return False
    cur = state.paribhasha_gates.get(GATE_KEY, {})
    if cur.get("nimitta") == n and cur.get("active") is True:
        return False
    return True



def cond(state: State) -> bool:
    return dvi_eka_22_gate_needs_update(state)


def act(state: State) -> State:
    d = find_primary_dhatu(state)
    assert d is not None
    n = d.meta.get(DVI_EKA_NIMITTA_KEY)
    assert n in ("dvi", "eka")
    state.paribhasha_gates[GATE_KEY] = {
        "active"  : True,
        "nimitta" : n,
        "pATha"   : "1.4.22",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.22",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'dvyekayordvivacanEkavacane',
    text_dev       = 'द्व्येकयोर्द्विवचनैकवचने',
    samagra_slp1   = "dvi-ekayoH dvivacana-ekavacane",
    samagra_dev    = "द्वि-एकयोः द्विवचन-एकवचने",
    padaccheda_dev = "द्वि-एकयोः (सप्तमी-द्वि) / द्विवचन-एकवचने (प्रथमा-द्वि)",
    why_dev        = (
        "द्वित्व-विवक्षायां द्वि-वचनिय-प्रत्ययः, एकत्व-विवक्षायाम् एक-वचनियः; "
        "विवक्षा अभिकल्प्य धातु-मेटा 1_4_22_affix_class इति।"
    ),
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
