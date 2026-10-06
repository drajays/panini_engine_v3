"""
7.3.78  पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदां पिबजिघ्रधमतिष्ठमनयच्छपश्यर्च्छधौशीयसीदाः  —  VIDHI

Before a śit, eleven roots are replaced wholesale (यथासंख्यम्): पिबति, जिघ्रति,
धमति, तिष्ठति, मनति, यच्छति, पश्यति, ऋच्छति, शीयते, सीदति. सर्ति→धौ (शीघ्रगतौ) is
optional and not generated.
Pāṭha: ashtadhyayi.com data.txt row i=73078 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import dhatu_before_sit
from engine.state import State
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _stem(t) -> str:
    return "".join(v.slp1 for v in t.varnas)

# the dhātu as it stands after it-lopa and 6.1.64 (षः सः) → its ādeśa
_ADESHA = {   # छ-final ones get tuk from 6.1.73 (ऋछ → ऋच्छ), as in the sūtra-pāṭha
"pA": "piba", "GrA": "jiGra", "DmA": "Dama", "sTA": "tizWa", "zWA": "tizWa",
           "mnA": "mana", "dA": "yaCa", "dfS": "paSya", "f": "fCa",
           "Sad": "SIya", "sad": "sIda"}


def _hit(state: State):
    i = dhatu_before_sit(state)
    if i is None or _stem(state.terms[i]) not in _ADESHA:
        return None
    return i


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    t = state.terms[_hit(state)]
    t.varnas = list(parse_slp1_upadesha_sequence(_ADESHA[_stem(t)]))
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.78",
    sutra_type=SutraType.VIDHI,
    text_slp1='pAGrADmAsTAmnAdARdfSyarttisarttiSadasadAM pibajiGraDamatizWamanayacCapaSyarcCaDOSIyasIdAH',
    text_dev='पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदां पिबजिघ्रधमतिष्ठमनयच्छपश्यर्च्छधौशीयसीदाः',
    samagra_slp1="aNgasya pAGrADmAsTAmnAdARdfSyarttisarttiSadasadAm pibajiGraDamatizWamanayacCapaSyarcCaDOSIyasIdAH Siti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="अङ्गस्य पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदाम् पिबजिघ्रधमतिष्ठमनयच्छपश्यर्च्छधौशीयसीदाः शिति",
    padaccheda_dev="पा-घ्रा-ध्मा-स्था-म्ना-दाण्-दृशि-अर्ति-सर्ति-शद-सदाम् / पिब-जिघ्र-धम-तिष्ठ-मन-यच्छ-पश्य-ऋच्छ-धौ-शीय-सीदाः",
    why_dev="शिति परे पा→पिब, घ्रा→जिघ्र, ध्मा→धम, स्था→तिष्ठ, म्ना→मन, दाण्→यच्छ, दृश्→पश्य, ऋ→ऋच्छ, शद्→शीय, सद्→सीद।",
    anuvritti_from=("7.3.73",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
