"""
3.2.78  सुप्यजातौ णिनिस्ताच्छील्ये  —  VIDHI

Padaccheda: सुपि अ-जातौ णिनिः ताच्छील्ये

krt-suffix rule: सुप्यजातौ णिनिस्ताच्छिल्ये (78)
Pāṭha: ashtadhyayi.com data.txt row i=32078 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, upapada_site, no_upasarga
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita

_JATI = frozenset()      # SHORTCUT S11: ajāti — the Lexicon does not yet say which upapada stems name a jāti (brāhmaṇa …); none is excluded


def _jati(state: State) -> bool:
    return (state.terms[-2].meta.get("upadesha_slp1") or "") in _JATI


def _site(state: State):
    return upapada_site(state, None) if no_upasarga(state) and vivaksita(state, "tAcCIlya", "tAcCIlya") and not _jati(state) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "Rin")      # SHORTCUT S12: ṇini is taken as ṇin (the final i of the sūtra's word as uccāraṇa)


SUTRA = SutraRecord(
    sutra_id              = "3.2.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'supyajAtO RinistAcCIlye',
    text_dev              = 'सुप्यजातौ णिनिस्ताच्छील्ये',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH supi ajAtO RiniH tAcCIlye kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः सुपि अजातौ णिनिः ताच्छील्ये कृत्",
    padaccheda_dev        = "सुपि अ-जातौ णिनिः ताच्छील्ये",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुप्यजातौ णिनिस्ताच्छिल्ये] विहितः (३.२.78)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
