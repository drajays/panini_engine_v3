"""
7.3.52  चजोः कु घिण्ण्यतोः  —  VIDHI (narrow: भन्ज् + घुरच् → भङ्गुर)

**Śāstra:** palatal **ca** / **ja** of the *aṅga* become **ku**-series before a
*ghit* / *ṇyat* *pratyaya* (here घुरच् bears ``ghiti``).

Sources consulted:
- ashtadhyayi.com data.txt row i=73052 · चजोः कु घित्-ण्यतोः
- Kāśikā: "घिति — पाकः, त्यागः, रागः; ण्यति — पाक्यम्"
- Cross-validation: regression test tests/unit/test_bhaNguram_Ghurac.py (भङ्गुरम्)

Engine: two-term frame — *dhātu* भन्ज् + *kṛt* residue ``ura`` from घुरच् after
**1.3** *it*-*lopa*, with the affix Term tagged ``ghiti``. Rewrites the final
**j** → **g**; the न् before it becomes ङ् in the tripāḍī (8.3.24, 8.4.58).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _stem(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _matches(state: State) -> bool:
    if len(state.terms) != 2:
        return False
    anga, pr = state.terms[0], state.terms[1]
    if "dhatu" not in anga.tags:
        return False
    if "pratyaya" not in pr.tags or "krt" not in pr.tags:
        return False
    if "ghiti" not in pr.tags:
        return False
    if (pr.meta.get("upadesha_slp1") or "").strip() != "Gurac":
        return False
    if not anga.varnas or anga.varnas[-1].slp1 not in ("c", "j"):
        return False
    if _stem(pr) != "ura":
        return False
    if state.samjna_registry.get("7.3.52_cajoH_ku_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[0]
    anga.varnas[-1] = mk({"c": "k", "j": "g"}[anga.varnas[-1].slp1])
    state.samjna_registry["7.3.52_cajoH_ku_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.52",
    sutra_type=SutraType.VIDHI,
    text_slp1='cajoH ku GiRRyatoH',
    text_dev='चजोः कु घिण्ण्यतोः',
    padaccheda_dev="चजोः / कु / घि-णि-ण्यतः",
    why_dev="घिति ण्यति च परे अङ्गान्त्यस्य च-ज-योः कवर्गादेशः (भञ्ज् → भङ्ग्)।",
    anuvritti_from=("7.3.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
