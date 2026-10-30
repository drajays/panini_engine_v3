"""
6.1.141  हिंसायां प्रतेश्च  —  VIDHI

Padaccheda: हिंसायाम् प्रतेः च

हिंसायां प्रतेश्च (6.1.141)
Pāṭha: ashtadhyayi.com data.txt row i=61141 (Art. 14).
Kāśikā 6.1.141: upaskīrṇaṃ haṃ te vṛṣala bhūyāt, pratiskīrṇam (hiṃsāyām); pratikīrṇam is outside.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

from engine.state import Term
from engine.vivaksha import vivaksita
from phonology.varna import parse_slp1_upadesha_sequence

_UPA = frozenset(('upa', 'prati'))
_DHATU = frozenset(('kF',))


def _find(state: State):
    if not vivaksita(state, "arthaViSeSa", "hiMsA"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "upasarga" not in t.tags or (t.meta.get("upadesha_slp1") or "").strip().replace("~", "") not in _UPA:
            continue
        nxt = state.terms[i + 1]
        if "dhatu" not in nxt.tags or (nxt.meta.get("upadesha_slp1") or "").strip() not in _DHATU:
            continue
        return i
    return None


def _new_cond(state: State) -> bool:
    i = _find(state)
    if i is None:
        return False
    ins = i + 1
    return (state.terms[ins].meta.get("upadesha_slp1") or "").strip() not in {"suw", "suT"}


def act(state: State) -> State:
    i = _find(state)
    if i is None or not _new_cond(state):
        return state
    su = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("suT")), tags={"pratyaya", "upadesha"}, meta={"upadesha_slp1": "suT"})
    state.terms.insert(i + 1, su)                      # kāt pūrvaḥ (6.1.135): between the upasarga and the dhātu
    state.meta["__why_now_dev__"] = "उपात् प्रतेश्च किरतौ हिंसायां सुट् कात् पूर्वः (६.१.१४१)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.141",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hiMsAyAM prateSca",
    text_dev              = "हिंसायां प्रतेश्च",
    samagra_slp1          = "saMhitAyAm suwkAtpUrvaH hiMsAyAm prateH ca upAt kiratO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् सुट्कात्पूर्वः हिंसायाम् प्रतेः च उपात् किरतौ",
    padaccheda_dev        = "हिंसायाम् प्रतेः च",
    why_dev               = "काशिका ६.१.१४१ — उपात् प्रतेश्च उत्तरस्मिन् किरतौ हिंसायां सुट् कात् पूर्वः (उपस्किरति, प्रतिस्किरति)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
