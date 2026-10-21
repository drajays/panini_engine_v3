"""
2.2.18  कुगतिप्रादयः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=22018 · padaccheda कु-गति-प्र-आदयः · anuvṛtti समासः, सुप् सुपा, तत्पुरुषः, नित्यम्
- Kāśikā: "कुगतिप्रादयः समर्थेन शब्दान्तरेण सह नित्यं समस्यन्ते, तत्पुरुषश्च समासो भवति। … गति — उररीकृतम्।"
- Kāśikā on 1.4.60 cites this sūtra for प्रकृत्य
- Mahābhāṣya vārttika (2.2.19): "गतिकारकोपपदानां कृद्भिः सह समासवचनं प्राक् सुबुत्पत्तेः"
- Cross-validation: tests/regression/test_ktva_loop.py (प्रकृत्य, आगत्य, प्रपठ्य); Kāśikā 7.1.37 प्रकृत्य, प्रहृत्य

Implemented for the gati: the gati terms (1.4.60) standing right before a dhātu that already carries its kṛt compound
with that kṛdanta, nitya, before any sup (the vārttika). They are tagged the pūrvapada of a tatpuruṣa; 7.1.37 reads
that. Ku and the other prādis (2.2.18 vārttikas 5–9) are not modelled yet.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_18_ku_gati_pra"


def _gati_before_krdanta(state: State) -> list[int]:
    """Indexes of the uncompounded gatis that directly precede a dhātu followed by a kṛt."""
    for d, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if not any("krt" in x.tags for x in state.terms[d + 1:]):
            return []
        out = []
        g = d - 1
        while g >= 0 and "gati" in state.terms[g].tags:
            if "samasa_purvapada" not in state.terms[g].tags:
                out.append(g)
            g -= 1
        return out
    return []


def cond(state: State) -> bool:
    if _gati_before_krdanta(state):
        return True
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    sites = _gati_before_krdanta(state)
    for g in sites:
        state.terms[g].tags |= {"samasa_member", "samasa_purvapada", "tatpurusha"}
    if not sites:
        state.paribhasha_gates[_GATE_KEY] = True
        state.samjna_registry[_GATE_KEY]  = True
        state.meta["tatpurusha_kind"]     = "2.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kugatiprAdayaH",
    text_dev              = "कुगतिप्रादयः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH ku-gati-pra-AdayaH nityaM",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः कु-गति-प्र-आदयः नित्यं",
    padaccheda_dev        = "कु-गति-प्र-आदयः",
    why_dev               = "गतिः कृदन्तेन सह नित्यं समस्यते प्राक् सुबुत्पत्तेः (तत्पुरुषः)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
