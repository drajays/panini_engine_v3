"""
3.1.95  कृत्याः  —  VIDHI

Padaccheda: कृत्याः प्राङ् ण्वुलः

Krt suffix rule from dhatu: कृत्याः प्राङ् ण्वुलः (95)
Pāṭha: ashtadhyayi.com data.txt row i=31095 (Art. 14).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_CATALOG = Path(__file__).resolve().parents[3] / "data" / "inputs" / "krit_pratyaya.json"


@lru_cache(maxsize=1)
def _kftya() -> frozenset[str]:
    """The pratyayas the kṛt catalogue files between 3.1.96 and ṇvul-tṛcau (3.1.133): prāṅ ṇvulaḥ."""
    key = lambda s: tuple(map(int, s.split(".")))
    d = json.loads(_CATALOG.read_text(encoding="utf-8"))
    return frozenset(k for k, v in d.items() if isinstance(v, dict) and v.get("vidhana_sutra")
                     and key("3.1.96") <= key(v["vidhana_sutra"]) < key("3.1.133"))


def _targets(state: State):
    return [t for t in state.terms if "pratyaya" in t.tags and "kftya" not in t.tags
            and (t.meta.get("upadesha_slp1") or "").strip() in _kftya()]


def cond(state: State) -> bool:
    return bool(_targets(state))


def act(state: State) -> State:
    for t in _targets(state):
        t.tags.add("kftya")
    state.samjna_registry["3_1_95_kftyAH"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.95",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = 'kftyAH',
    text_dev              = 'कृत्याः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kftyAH kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कृत्याः कृत्",
    padaccheda_dev        = "कृत्याः प्राङ् ण्वुलः",
    why_dev               = "धातोः [कृत्याः प्राङ् ण्वुलः]-प्रत्ययः विहितः (३.१.95)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
