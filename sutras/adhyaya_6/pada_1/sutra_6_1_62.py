"""
6.1.62  अचि शीर्षः  —  VIDHI (narrow *glass-box*: *ā* + *om* → *o* junction)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61062):** *aci śīrṣaḥ* — in the general
*śīrṣa* / *ṛ*-before-*ac* doctrine, v3 already covers many *ṛ*-sandhis elsewhere.

For ``prakriya_25`` the JSON commentary bundles **pararūpa** *ādeśa* of
*subrahmaṇyā* + *om* → *subrahmaṇyom* under this spine entry.  We implement
only that junction:

  ``subrahmaRyA`` (stem-final ``A``) + ``om`` → ``subrahmaRy`` + ``o`` + ``m``
  (= ``subrahmaRyom`` in SLP1).

``cond`` uses ``meta`` + ``upadesha_slp1`` identity only (no *vibhakti*).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _matches(state: State) -> bool:
    if not state.meta.get("prakriya_25_6_1_62_pararupa_arm"):
        return False
    if len(state.terms) != 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if "anga" not in t0.tags:
        return False
    if not t0.varnas or t0.varnas[-1].slp1 != "A":
        return False
    if t1.meta.get("upadesha_slp1") != "om":
        return False
    if not t1.varnas or len(t1.varnas) < 2:
        return False
    if t1.varnas[0].slp1 != "o" or t1.varnas[1].slp1 != "m":
        return False
    if t0.meta.get("prakriya_25_6_1_62_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    t0, t1 = state.terms[0], state.terms[1]
    del t0.varnas[-1]
    del t1.varnas[0]
    t0.varnas.append(mk("o"))
    t0.meta["prakriya_25_6_1_62_done"] = True
    state.meta.pop("prakriya_25_6_1_62_pararupa_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.62",
    sutra_type=SutraType.VIDHI,
    text_slp1="aci SIrSaH",
    text_dev="अचि शीर्षः",
    padaccheda_dev="अचि / शीर्षः",
    why_dev="आ-कारान्त + ओम् → पररूप *o* + *m* (*prakriya_25*, ग्लास-बॉक्स्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
