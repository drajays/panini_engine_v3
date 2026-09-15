"""
7.2.103  किमः कः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=702103
- Kāśikā: किम् + औ → क + औ (कौ)
- Cross-validation: pipelines/kO_staH_vakya.py; sthanivat_anal_ashrita_lesson.py

*Kim* is replaced by *ka* before a *sup* beginning with *au*; **1.1.56** extends *aṅgatva*
so **7.3.102** *sūpi ca* can lengthen the *ādeśa* *aṅga*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import ANGATVA, adesha_substitute_varnas


def _site(state: State) -> int | None:
    if len(state.terms) < 2:
        return None
    a, b = state.terms[0], state.terms[1]
    if "prātipadika" not in a.tags:
        return None
    if (a.meta.get("upadesha_slp1") or "").strip() != "kim":
        return None
    if b.kind != "pratyaya" or "sup" not in b.tags:
        return None
    if not b.varnas:
        return None
    first = b.varnas[0].slp1
    up = (b.meta.get("upadesha_slp1") or "").strip()
    # Nom. du. ``O`` (कौ) or inst. du. ``ByAm`` (काभ्याम्) per lesson / P028.
    if first not in {"O", "B"} and up not in {"O", "ByAm"}:
        return None
    if a.meta.get("7_2_103_kim_kah_done"):
        return None
    return 0


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    a = state.terms[i]
    if "anga" not in a.tags:
        a.tags.add("anga")
    adesha_substitute_varnas(
        a,
        "ka",
        state,
        sutra_id="7.2.103",
        gunadharmas=frozenset({ANGATVA}),
    )
    a.meta["7_2_103_kim_kah_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.103",
    sutra_type=SutraType.VIDHI,
    text_slp1="kimaH kaH",
    text_dev="किमः कः",
    padaccheda_dev="किमः / कः",
    why_dev="किम्-शब्दस्य क-आदेशः; स्थानिवद्भावेन अङ्गत्वम् (७.३.१०२ सुपि च)।",
    anuvritti_from=("7.2.102",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
