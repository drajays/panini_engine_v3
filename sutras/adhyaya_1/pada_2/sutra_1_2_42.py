"""
1.2.42  तत्पुरुषः समानाधिकरणः कर्मधारयः  —  SAMJNA (narrow ``prakriya_37``)

**Pāṭha (cross-check: ``sutrANi.tsv``):** *tatpuruṣaḥ samānādhikaraṇaḥ karmadhārayaḥ* —
a ``tat-puruṣa`` compound whose members have ``samānādhikaraṇa`` reference receives the
technical name *karmadhāraya*.

Narrow v3 (**पाचकवृन्दारिका** commentary spine — ``…/separated_prakriyas/prakriya_37_*.json``):
  • ``prakriya_37_1_2_42_arm`` + ``meta['prakriya_37_tatpurusa_upapatti_note']`` + tagged witness
    Term ``prakriya_37_pAcikA_vndArikA_witness`` → ``samjna_registry['1.2.42_karmadhAraya_prakriya_37']``.

No ``varṇa`` mutation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_37_1_2_42_arm"):
        return False
    if not state.meta.get("prakriya_37_tatpurusa_upapatti_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_37_pAcikA_vndArikA_witness" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("1.2.42_karmadhAraya_prakriya_37"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["1.2.42_karmadhAraya_prakriya_37"] = True
    state.meta.pop("prakriya_37_1_2_42_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.42",
    sutra_type=SutraType.SAMJNA,
    text_slp1="tatpuruzaH samAnAdhikaraRaH karmadhArayaH",
    text_dev="तत्पुरुषः समानाधिकरणः कर्मधारयः",
    padaccheda_dev="तत्पुरुषः / समानाधिकरणः / कर्मधारयः",
    why_dev="समानाधिकरण-तत्पुरुषः कर्मधारयः (*prakriya_37*, **पाचिका**/**वृन्दारिका**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
