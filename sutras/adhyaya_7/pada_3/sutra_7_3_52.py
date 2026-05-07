"""
7.3.52  चजोः कु घिण्ण्यतोः  —  VIDHI (narrow: **P007** *BaYj* + *Gurc* → *bhaNg*)

**Śāstra:** palatal **ca** / **ja** of the *aṅga* become **ku**-series before a
*ghiti* / *ṇi* / *Ṇy* *pratyaya* (here **Gurc** bears ``ghiti``).

Engine: two-term frame — *dhātu* tape ``BaYj`` + *kṛt* residue ``ur`` from **Gurc**
after **1.3** *it*-*lopa*, with the affix Term tagged ``ghiti``.  Rewrites **Y**
→ **N** (ङ्), **j** → **g** (ग्).
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
    if (pr.meta.get("upadesha_slp1") or "").strip() != "Gurc":
        return False
    if _stem(anga) != "BaYj":
        return False
    if _stem(pr) != "ur":
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
    new_vs = []
    for v in anga.varnas:
        if v.slp1 == "Y":
            new_vs.append(mk("N"))
        elif v.slp1 == "j":
            new_vs.append(mk("g"))
        else:
            new_vs.append(v.clone())
    anga.varnas = new_vs
    state.samjna_registry["7.3.52_cajoH_ku_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.52",
    sutra_type=SutraType.VIDHI,
    text_slp1="cajoH ku GiRRNyatoH",
    text_dev="चजोः कु घिण्ण्यतोः",
    padaccheda_dev="चजोः / कु / घि-णि-ण्यतः",
    why_dev="घिति-परकात् पूर्वपदाच् चवर्ग-जवर्गयोः कवर्गादेशः — प००७।",
    anuvritti_from=("7.3.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
