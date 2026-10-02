"""
3.1.74  श्रुवः शृ च  —  VIDHI

In the domain of śap (3.1.68, kartari sārvadhātuka) the bhvādi root श्रु takes śnu instead, and श्रु itself becomes शृ:
शृणोति शृणुतः शृण्वन्ति · शृणु · अशृणोत् · शृणुयात्.  (An apavāda of śap, like 3.1.73 for the svādi roots; 3.1.74 lists the
root's ādeśa too.)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 3.1.74 (padaccheda: श्रुवः शृ च; anuvṛtti: श्नुः 3.1.73, कर्तरि शप् 3.1.68)
  Source #2 — ashtadhyayi.com dhātu table, श्रु (bhvādi): laṭ शृणोति शृणुतः शृण्वन्ति शृणोषि शृणुथः शृणुथ शृणोमि शृणुवः/शृण्वः शृणुमः/शृण्मः ;
              loṭ शृणोतु … शृणु ; Gītā 2.29, 11.1 शृणु.

Engine: ``cond`` reads the root's lexical identity (श्रु = upadeśa ``Sru``, the name the sūtra gives) and a śap vikaraṇa on the
tape. The śnu Term replaces śap (as 3.1.73 does) and carries ``kngiti`` (apit sārvadhātuka); the root is replaced as a whole
(sarvādeśa, 1.1.55) and keeps dhātutva / aṅgatva (1.1.56).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.sthanivat import ANGATVA, DHATUTVA, adesha_substitute_varnas
from phonology.varna import parse_slp1_upadesha_sequence

_ROOT = "Sru"


def _site(state: State):
    root = next((t for t in state.terms if "dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == _ROOT
                 and not t.meta.get("3_1_74_done")), None)
    if root is None:
        return None
    sap = next((i for i, t in enumerate(state.terms)
                if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "Sap"), None)
    return None if sap is None else (root, sap)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    site = _site(state)
    if site is None:
        return state
    root, sap = site
    state.terms[sap] = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("Snu")),
                            tags={"pratyaya", "vikarana", "upadesha", "kngiti"}, meta={"upadesha_slp1": "Snu"})
    adesha_substitute_varnas(root, "Sf", state, sutra_id="3.1.74", gunadharmas=frozenset({DHATUTVA, ANGATVA}))
    root.meta["3_1_74_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.74",
    sutra_type=SutraType.VIDHI,
    text_slp1="SruvaH Sf ca",
    text_dev="श्रुवः शृ च",
    padaccheda_dev="श्रुवः शृ च",
    why_dev="शप् के विषय में भ्वादि श्रु से श्नु प्रत्यय, और श्रु को शृ आदेश (शृणोति)।",
    anuvritti_from=("3.1.73", "3.1.68"),
    apavada_of=("3.1.68",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
