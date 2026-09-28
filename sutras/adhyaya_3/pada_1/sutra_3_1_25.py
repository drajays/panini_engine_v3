"""
3.1.25  सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच्  —  VIDHI

Padaccheda: सत्याप-पाश-रूप-वीणा-तूल-श्लोक-सेना-लोम-त्वच-वर्म-वर्ण-चूर्ण-चुरादिभ्यः णिच्

Krt suffix rule from dhatu: सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच् (25)
"""
from __future__ import annotations
from phonology.varna import parse_slp1_upadesha_sequence
from engine.state import Term

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_25_satyApapASar_25"


def _curadi_dhatu(state: State):
    """…चुरादिभ्यो णिच्: a curādi (gaṇa-10) dhātu not yet followed by ṇic."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if t.meta.get("gana") != 10 or t.meta.get("3_1_25_nic_done"):
            return None
        return i
    return None


def cond(state: State) -> bool:
    return _curadi_dhatu(state) is not None


def act(state: State) -> State:
    i = _curadi_dhatu(state)
    if i is None:
        return state
    nic = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("Ric")),
               tags={"pratyaya", "upadesha", "sanadi", "nic", "ardhadhatuka"},
               meta={"upadesha_slp1": "Ric"})
    state.terms.insert(i + 1, nic)
    state.terms[i].meta["3_1_25_nic_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "3.1.25",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "satyApapASarUpavIRAtUlaSlokasenAlomatvacavarmavarRacUrRacurAdiByo Ric",
    text_dev              = "सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच्",
    padaccheda_dev        = "सत्याप-पाश-रूप-वीणा-तूल-श्लोक-सेना-लोम-त्वच-वर्म-वर्ण-चूर्ण-चुरादिभ्यः णिच्",
    why_dev               = "धातोः [सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच्]-प्रत्ययः विहितः (३.१.25)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
