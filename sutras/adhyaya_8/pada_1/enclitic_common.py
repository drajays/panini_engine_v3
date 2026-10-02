"""
sutras/adhyaya_8/pada_1/enclitic_common.py — shared predicates for **8.1.20–26** (yuṣmad / asmad ādeśas: वाम् नौ वस् नस् ते मे त्वा मा).

Mechanically blind (Art. 2): everything read here is a Term tag, a lexical identity named in the
sūtras (yuṣmad / asmad; ca vā ha aha eva), or the adhikāra stack. Never the (vibhakti, vacana)
coordinates: those arrive as the saṃjñā-names 4.1.2 stamped (``vib_*`` / ``vac_*``).

The sentence is on the tape: ``[… preceding padas …, <pronoun pada>, … following padas …]``, each a
``pada``-tagged Term. ``pAdAdi`` marks a pada that opens a verse-pāda.
"""
from __future__ import annotations

from typing import Optional

from engine.gates import adhikara_in_effect
from engine.state import State
from engine.sthanivat import PADATVA, adesha_substitute_varnas

PRONOUN_STEMS = frozenset({"asmad", "yuzmad"})
# ṣaṣṭhī-caturthī-dvitīyā-stha (8.1.20), carried by anuvṛtti into 8.1.21–23
STHA_VIBHAKTI = frozenset({"vib_shashthi", "vib_caturthi", "vib_dvitiya"})
PARTICLES_8_1_24 = frozenset({"ca", "vA", "ha", "aha", "eva"})
ADESHA_SUTRAS = ("8.1.20", "8.1.21", "8.1.22", "8.1.23")


def target(state: State, sutra_id: str, *, replaced_ok: bool = False) -> Optional[int]:
    """Index of the yuṣmad/asmad pada the ādeśa sūtras address: *padāt param* (8.1.17) and *apādādau* (8.1.18)."""
    if not (adhikara_in_effect(sutra_id, state, "8.1.17") and adhikara_in_effect(sutra_id, state, "8.1.18")):
        return None
    for i, t in enumerate(state.terms):
        if "pada" not in t.tags or t.meta.get("stem_upadesha_slp1") not in PRONOUN_STEMS:
            continue
        if "enclitic" in t.tags and not replaced_ok:
            continue
        if i == 0 or "pada" not in state.terms[i - 1].tags:  # padāt: a pada must precede
            continue
        if "pAdAdi" in t.tags:                               # apādādau: not the first pada of a pāda
            continue
        if "enclitic_nivrtta_8_1_26" in t.tags:              # vibhāṣā exercised: no ādeśa
            continue
        return i
    return None


def replace(state: State, i: int, sutra_id: str, table: dict[str, str]) -> State:
    """Sarvādeśa (1.1.55: the ādeśa is anekāl) of the whole pada; padatva is inherited (1.1.56)."""
    t = state.terms[i]
    adesha_substitute_varnas(t, table[t.meta["stem_upadesha_slp1"]], state,
                             sutra_id=sutra_id, gunadharmas=frozenset({PADATVA}))
    t.tags.add("enclitic")
    t.meta["anudAtta_adesha_from"] = sutra_id  # display note (accent is not modelled): the ādeśa is anudātta
    if adhikara_in_effect(sutra_id, state, "8.1.18"):
        t.meta["sarva_anudAtta_8_1_18"] = True  # 8.1.18 anudāttaṃ sarvam: the whole ādeśa pada
    t.meta[f"{sutra_id.replace('.', '_')}_adesha_done"] = True
    return state
