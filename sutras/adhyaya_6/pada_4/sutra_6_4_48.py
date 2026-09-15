"""
6.4.48  अतो लोपः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=604048
- Kāśikā: अतः लोपः (परनिमित्तकः — उपधा-वृद्धि-निषेधः)
- Cross-validation: tests/unit/test_kathi_kath_nic.py,
  tests/unit/test_avadhIt_han_lun_ekavacana.py,
  tests/unit/test_yAyAvar_yang_varac_purvavidhau_lesson.py (*yaṅ* *a* before *varac*)

*Ato lopaḥ* on stem-final *a* before a following *ārdhadhātuka* / *ṇic* / *varac*
context. When **1.1.57** is on, the lupta *a* is *sthānivat* for a *para* rule, but
*upadhā* on the consonant before that *a* is destroyed — **7.2.116** / **7.2.7** do
not apply (P025 / कथ / हन्-लुङ् lessons). Under **1.1.58** (*vareya*), that *a* is
not *sthānivat* for **6.4.64** (*yāyāvar* lesson).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_META_YA_G_A_LOPA = "6_4_48_yaG_a_lopa_para_nimitta"
_META_KTIC_A_LOPA = "6_4_48_ktic_a_lopa_para_nimitta"

_VARAC_UPADESHA = frozenset({"varac", "vara"})
_KTIC_UPADESHA = frozenset({"ktic", "ti"})


def _nic_i_follows(terms: list, ang_i: int) -> bool:
    if ang_i + 1 >= len(terms):
        return False
    nic = terms[ang_i + 1]
    if nic.kind != "pratyaya":
        return False
    if "nic" not in nic.tags and not nic.meta.get("P025_Nic_pratyaya"):
        return False
    return bool(nic.varnas) and nic.varnas[0].slp1 == "i"


def _ardhadhatuka_follows(terms: list, ang_i: int) -> bool:
    for j in range(ang_i + 1, len(terms)):
        pr = terms[j]
        if pr.kind == "pratyaya" and "ardhadhatuka" in pr.tags:
            return True
    return False


def _varac_krt_follows(terms: list, ang_i: int) -> bool:
    if ang_i + 1 >= len(terms):
        return False
    nxt = terms[ang_i + 1]
    if nxt.kind != "pratyaya" or "krt" not in nxt.tags:
        return False
    up = (nxt.meta.get("upadesha_slp1") or "").strip()
    if up in _VARAC_UPADESHA:
        return True
    return bool(nxt.varnas) and nxt.varnas[0].slp1 == "v"


def _final_a_pop_index(ang) -> int | None:
    """Index of the *a* varṇa dropped by *ato lopaḥ* on this *aṅga* (string-final *a*)."""
    if not ang.varnas:
        return None
    if ang.varnas[-1].slp1 == "a":
        return len(ang.varnas) - 1
    return None


def _kath_site(state: State) -> int | None:
    """Curādi/ṇic: prātipadika ending in a before nic-i. Structural, no arm."""
    for i, ang in enumerate(state.terms):
        if "prātipadika" not in ang.tags:
            continue
        if _final_a_pop_index(ang) is None:
            continue
        if not _nic_i_follows(state.terms, i):
            continue
        if ang.meta.get("6_4_48_a_lopa_done"):
            continue
        return i
    return None


def _han_vadh_site(state: State) -> int | None:
    """han→vadha in luṅ: dhātu upadeśa in {vadh,vadha} + final a + ārdhadhātuka. Structural."""
    for i, ang in enumerate(state.terms):
        if "dhatu" not in ang.tags:
            continue
        up = (ang.meta.get("upadesha_slp1") or "").strip()
        if up not in ("vadh", "vadha"):
            continue
        if _final_a_pop_index(ang) is None:
            continue
        if not _ardhadhatuka_follows(state.terms, i):
            continue
        if ang.meta.get("6_4_48_a_lopa_done"):
            continue
        return i
    return None


def _ktic_krt_follows(terms: list, ang_i: int) -> bool:
    if ang_i + 1 >= len(terms):
        return False
    nxt = terms[ang_i + 1]
    if nxt.kind != "pratyaya":
        return False
    up = (nxt.meta.get("upadesha_slp1") or "").strip()
    if up in _KTIC_UPADESHA:
        return True
    return "krt" in nxt.tags and bool(nxt.varnas) and nxt.varnas[0].slp1 == "t"


def _ktic_site(state: State) -> int | None:
    """Structural: stem-final ``a`` before *ktic* / *ti* (*kaṇḍūti* lesson)."""
    for i, ang in enumerate(state.terms):
        if "dhatu" not in ang.tags and "anga" not in ang.tags:
            continue
        if _final_a_pop_index(ang) is None:
            continue
        if not _ktic_krt_follows(state.terms, i):
            continue
        if ang.meta.get("6_4_48_a_lopa_done"):
            continue
        return i
    return None


def _yang_varac_site(state: State) -> int | None:
    """Structural: *yaṅ* residue *a* before *varac* (*yāyāvar* lesson)."""
    for i, ang in enumerate(state.terms):
        if "dhatu" not in ang.tags and "anga" not in ang.tags:
            continue
        if _final_a_pop_index(ang) is None:
            continue
        if not _varac_krt_follows(state.terms, i):
            continue
        if ang.meta.get("6_4_48_a_lopa_done"):
            continue
        return i
    return None


def _site(state: State) -> int | None:
    if state.meta.get("trace_6_4_48_recipe"):
        return None
    site = _kath_site(state)
    if site is not None:
        return site
    site = _han_vadh_site(state)
    if site is not None:
        return site
    site = _yang_varac_site(state)
    if site is not None:
        return site
    return _ktic_site(state)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        if state.meta.get("trace_6_4_48_recipe"):
            state.meta["trace_6_4_48_recipe"] = False
        return state
    ang = state.terms[i]
    pop_i = _final_a_pop_index(ang)
    if pop_i is None:
        return state
    ang.varnas.pop(pop_i)
    ang.meta["6_4_48_a_lopa_done"] = True
    ang.meta["upadha_blocked_para_nimitta"] = True
    if _varac_krt_follows(state.terms, i):
        ang.meta[_META_YA_G_A_LOPA] = True
    elif _ktic_krt_follows(state.terms, i):
        ang.meta[_META_KTIC_A_LOPA] = True
    base = "".join(v.slp1 for v in ang.varnas)
    ang.meta["upadesha_slp1"] = base
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.48",
    sutra_type=SutraType.VIDHI,
    text_slp1="ato lopaH",
    text_dev="अतो लोपः",
    padaccheda_dev="अतः / लोपः",
    why_dev="अकारान्त-अङ्गस्य परे अकारादौ अ-लोपः; परनिमित्तकः उपधा-वृद्धिं निवारयति।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

META_YA_G_A_LOPA = _META_YA_G_A_LOPA
META_KTIC_A_LOPA = _META_KTIC_A_LOPA

__all__ = ["META_KTIC_A_LOPA", "META_YA_G_A_LOPA", "SUTRA"]
