"""
6.1.105  दीर्घाज्जसि च  —  PRATISHEDHA

Padaccheda: दीर्घात् जसि च

दीर्घाज्जसि च (6.1.105)
Pāṭha: ashtadhyayi.com data.txt row i=61105 (Art. 14).
Kāśikā 6.1.105: kumāryau, kumāryaḥ, brahmabandhvau, brahmabandhvaḥ; Laghukaumudī: viśvapau, viśvapāḥ.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import build_pratyahara

_IC = build_pratyahara("i", "c")
_DIRGHA = frozenset("AIUFX")
_GATE_KEY: str = "6_1_105_dIrGAj_jasi_ca"


def _dirgha_before_jas_or_ic(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga, pratyaya = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "sup" not in pratyaya.tags or not anga.varnas or not pratyaya.varnas:
        return False
    if anga.varnas[-1].slp1 not in _DIRGHA:
        return False
    up = (pratyaya.meta.get("upadesha_slp1") or "").strip()
    return up == "jas" or pratyaya.varnas[0].slp1 in _IC


def _new_cond(state: State) -> bool:
    return _dirgha_before_jas_or_ic(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.meta["__why_now_dev__"] = "दीर्घात् परे जसि इचि च ६.१.१०२ पूर्वसवर्ण-दीर्घस्य निषेधः (६.१.१०५)।"
    return state


def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.105",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGAjjasi ca",
    text_dev              = "दीर्घाज्जसि च",
    samagra_slp1          = "dIrGAt ici jasi ca praTamayoH pUrvasavarRaH na ",
    samagra_dev           = "दीर्घात् इचि जसि च प्रथमयोः पूर्वसवर्णः न ।",
    padaccheda_dev        = "दीर्घात् जसि च",
    why_dev               = "काशिका ६.१.१०५ — दीर्घात् जसि इचि च परे पूर्वसवर्ण-दीर्घः न भवति (कुमार्यौ, कुमार्यः); ६.१.१०२ इत्यस्य निषेधः।",
    anuvritti_from        = ('6.1.1',),
    blocks_sutra_ids=("6.1.102",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
