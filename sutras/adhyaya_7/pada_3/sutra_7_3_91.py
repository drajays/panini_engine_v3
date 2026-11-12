"""
7.3.91  गुणोऽपृक्ते  —  VIDHI

Padaccheda: गुणः अपृक्ते

गुणोऽपृक्ते (7.3.91)
Pāṭha: ashtadhyayi.com data.txt row i=73091 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from phonology    import mk
from sutras.adhyaya_7.pada_3.sutra_7_3_89 import _find
from engine.state import State

def _find91(state: State):
    """ūrṇu (7.3.90's root) before an apṛkta (one-letter, 1.2.41) hal-initial pit sārvadhātuka — aurṇot (laṅ 3sg t, 2sg s): guṇa.
    7.3.89 names the same site; when 7.3.90 has already taken the vṛddhi reading (meta 7_3_89_done) there is nothing left."""
    i = _find(state, urnu=True)
    if i is None:
        return None
    tin = next(u for u in state.terms[i + 1:] if u.varnas)
    return i if len(tin.varnas) == 1 else None


def cond(state: State) -> bool:
    return _find91(state) is not None


def act(state: State) -> State:
    i = _find91(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = mk("o")
    t.meta["7_3_89_done"] = True
    t.meta["anga_guna_7_3_84"] = True        # the guṇa is made; 7.3.84 must not repeat it
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'guRopfkte',
    text_dev              = 'गुणोऽपृक्ते',
    samagra_slp1          = "aNgasya guRaH apfkte piti sArvaDAtuke hali UrRoteH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य गुणः अपृक्ते पिति सार्वधातुके हलि ऊर्णोतेः",
    padaccheda_dev        = "गुणः अपृक्ते",
    why_dev               = "(सूत्रम् 7.3.91) गुणोऽपृक्ते।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
