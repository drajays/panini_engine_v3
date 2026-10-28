"""
8.1.20  युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ  —  VIDHI

द्विवचने ṣaṣṭhī / caturthī / dvitīyā में युष्मद्→वाम्, अस्मद्→नौ (पदात् परस्य, अपादादौ)।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 8.1.20 
  Source #2 — Kāśikā 8.1.20: ग्रामो वां स्वम् / ग्रामो वः स्वम् / ग्रामस्ते स्वम् / ग्रामस्त्वा पश्यति (as the sūtra)
  Reference — ashtadhyayi.com sūtra-prayoga list (Kirātārjunīya, Bhaṭṭikāvya … attestations)

Engine: ``cond`` reads Term tags only — the pada's saṃjñā-names ``vib_*`` / ``vac_*`` (4.1.2), the
pronoun's lexical identity, and the adhikāras 8.1.17 / 8.1.18 (*padāt* … *apādādau*). The ādeśa
replaces the whole pada (sarvādeśa, 1.1.55) and is anudātta (accent is not modelled).
Pāṭha: ashtadhyayi.com data.txt row i=81020 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


# --- shared by 8.1.20 – 26 (the head sūtra of the group holds it; formerly enclitic_common.py) ---
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


_ADESHA = {'yuzmad': 'vAm', 'asmad': 'nO'}


def _site(state: State):
    i = target(state, "8.1.20")
    if i is None:
        return None
    t = state.terms[i]
    return i if (t.tags & STHA_VIBHAKTI and "vac_dvi" in t.tags) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    return state if i is None else replace(state, i, "8.1.20", _ADESHA)


SUTRA = SutraRecord(
    sutra_id="8.1.20",
    sutra_type=SutraType.VIDHI,
    text_slp1='yuzmadasmadoH zazWIcaturWIdvitIyAsWayorvAnnAvO',
    text_dev='युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ',
    samagra_slp1="padasya padAt anudAttaM sarvamApAdAdO yuzmadasmadoH zazWIcaturTIdvitIyAsTayoH vAnnAvO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="पदस्य पदात् अनुदात्तं सर्वमापादादौ युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोः वान्नावौ",
    padaccheda_dev='युष्मद्-अस्मदोः षष्ठी-चतुर्थी-द्वितीया-स्थयोः वाम्-नौ',
    why_dev='द्विवचनान्त षष्ठी/चतुर्थी/द्वितीया युष्मद्-अस्मद् पद → वाम्/नौ (अपादादौ, पदात् परम्)।',
    anuvritti_from=("8.1.17", "8.1.18"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
