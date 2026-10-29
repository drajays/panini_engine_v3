"""
7.2.103  किमः कः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=72103
- Kāśikā: किम् + औ → क + औ (कौ)
- Cross-validation: pipelines/kO_staH_vakya.py; sthanivat_anal_ashrita_lesson.py

*Kim* is replaced by *ka* before a *sup* beginning with *au*; **1.1.56** extends *aṅgatva*
so **7.3.102** *sūpi ca* can lengthen the *ādeśa* *aṅga*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import ANGATVA, adesha_substitute_varnas
from sutras.adhyaya_1.pada_3.sutra_1_3_4 import TAG_5_3_1_VIBHAKTI


def _sup_luk_follows(a, b) -> bool:
    """Neuter su / am is deleted by luk (7.1.23): no *vibhakti* is left for the ādeśa (किम्, not *कम्*)."""
    return "napuṃsaka" in a.tags and (b.meta.get("upadesha_slp1") or "").strip() in ("s~", "am")


def kim_site(state: State, first=None, upadesha=None) -> int | None:
    """The kim stem that a vibhakti follows (7.2.103 – 105 share it): a sup, or a taddhita pratyaya of 5.3.1's scope (kutaḥ, kadā, kathaṃ).
    ``first``: the letters the vibhakti may begin with (7.2.104 t / h); ``upadesha``: the pratyaya's own name (7.2.105 at)."""
    if len(state.terms) < 2:
        return None
    a, b = state.terms[0], state.terms[1]
    if "prātipadika" not in a.tags:
        return None
    if (a.meta.get("upadesha_slp1") or "").strip() != "kim":
        return None
    if b.kind != "pratyaya" or not ("sup" in b.tags or TAG_5_3_1_VIBHAKTI in b.tags):
        return None
    if not b.varnas:
        return None
    if first is not None and b.varnas[0].slp1 not in first:
        return None
    if upadesha is not None and (b.meta.get("upadesha_slp1") or "").strip() != upadesha:
        return None
    if _sup_luk_follows(a, b):
        return None
    if a.meta.get("7_2_103_kim_kah_done"):
        return None
    return 0


def kim_adesha(state: State, i: int, new_slp1: str, sutra_id: str) -> State:
    """kim → ka / ku / kva as the aṅga (1.1.56 lets 7.3.102 sūpi ca read it)."""
    a = state.terms[i]
    if "anga" not in a.tags:
        a.tags.add("anga")
    adesha_substitute_varnas(a, new_slp1, state, sutra_id=sutra_id, gunadharmas=frozenset({ANGATVA}))
    a.meta["7_2_103_kim_kah_done"] = True
    a.meta["tyadadi_a_adesha_done"] = True      # the ādeśa replaced the whole stem: 7.2.102 (apavāda of it) has nothing left to act on
    return state


def _site(state: State) -> int | None:
    return kim_site(state)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    return state if i is None else kim_adesha(state, i, "ka", "7.2.103")


SUTRA = SutraRecord(
    sutra_id="7.2.103",
    sutra_type=SutraType.VIDHI,
    text_slp1="kimaH kaH",
    text_dev="किमः कः",
    samagra_slp1="kimaH kaH viBaktO",
    samagra_dev="किमः कः विभक्तौ",
    padaccheda_dev="किमः / कः",
    why_dev="किम्-शब्दस्य क-आदेशः; स्थानिवद्भावेन अङ्गत्वम् (७.३.१०२ सुपि च)।",
    anuvritti_from=("7.2.102",),
    apavada_of=("7.2.102",),  # kim → ka (whole stem) displaces tyadādi final-hal → a
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
