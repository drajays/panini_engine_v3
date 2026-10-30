"""
6.1.138  समवाये च  —  VIDHI

Padaccheda: समवाये च

समवाये च (6.1.138)
Pāṭha: ashtadhyayi.com data.txt row i=61138 (Art. 14).
Kāśikā 6.1.138: tatra naḥ saṃskṛtam, parikṛtam (samavāye: samudite); Laghukaumudī: saṃskurvanti — saṅghībhavanti.
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

_UPA = frozenset(('sam', 'pari', 'upa'))
_DHATU = frozenset(('kf', 'qukfY'))


def _find(state: State):
    if not vivaksita(state, "arthaViSeSa", "samavAya"):
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
    state.meta["__why_now_dev__"] = "सम्-परि-उपेभ्यः करोतौ समवाये सुट् कात् पूर्वः (६.१.१३८)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samavAye ca",
    text_dev              = "समवाये च",
    samagra_slp1          = "saMhitAyAm suwkAtpUrvaH samavAye ca sam-pari-upeByaH karotO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् सुट्कात्पूर्वः समवाये च सम्-परि-उपेभ्यः करोतौ",
    padaccheda_dev        = "समवाये च",
    why_dev               = "काशिका ६.१.१३८ — सम्परि-उपेभ्यः करोतौ समवाये (समुदाये) अर्थे सुट् कात् पूर्वः (संस्कृतम्, परिष्कृतम्)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
