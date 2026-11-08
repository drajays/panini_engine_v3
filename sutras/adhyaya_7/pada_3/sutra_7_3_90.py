"""
7.3.90  ऊर्णोतेर्विभाषा  —  VIBHASHA

Padaccheda: ऊर्णोतेः विभाषा

ऊर्णोतेर्विभाषा (7.3.90)
Pāṭha: ashtadhyayi.com data.txt row i=73090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from phonology    import mk
from sutras.adhyaya_7.pada_3.sutra_7_3_89 import _find
from engine.state import State

def cond(state: State) -> bool:
    return _find(state, urnu=True) is not None


def act(state: State) -> State:
    i = _find(state, urnu=True)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = mk("O")                  # the vṛddhi reading: ऊर्णौति; declined, 7.3.84's guṇa gives ऊर्णोति
    t.meta["7_3_89_done"] = True
    t.meta["anga_guna_7_3_84"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.90",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,     # the guṇa reading is the default; explore() gives the vṛddhi one
    vibhasha_scope        = lambda state: _find(state, urnu=True) is not None,
    text_slp1             = "UrRoterviBAzA",
    text_dev              = "ऊर्णोतेर्विभाषा",
    samagra_slp1          = "aNgasya UrRoteH viBAzA piti sArvaDAtuke vfdDiH hali",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऊर्णोतेः विभाषा पिति सार्वधातुके वृद्धिः हलि",
    padaccheda_dev        = "ऊर्णोतेः विभाषा",
    why_dev               = "(सूत्रम् 7.3.90) ऊर्णोतेर्विभाषा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
