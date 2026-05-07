"""
3.1.55  पुषादिद्युताद्यॢदितः परस्मैपदेषु  —  VIDHI (narrow *aṅ*-substitution)

Teaching **corrected_prakriyas_v2** **P018-A** (*vyadyutat*): in luṅ *parasmaipada*,
*vikaraṇa* ``cli`` is replaced by **अङ्** (machine tape ``a`` + ``G`` with ``G``
as *halantyam-it*, **1.3.9** → ``a``) for *dyutādi* **``dyut``** before *tin*
substitution resolves ``luG``.

Engine:
  • ``state.meta['corrected_v2_P018_A_3_1_55_arm']`` (cleared in ``act``).
  • detects ``cli`` ``Term`` and a **``dyut``** *dhātu* (flat **or** ``upadesha_slp1``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk

_META_ARM = "corrected_v2_P018_A_3_1_55_arm"


def _dyut_site(state: State) -> bool:
    flat_ok = False
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) == "dyut":
            flat_ok = True
            break
        up = (t.meta.get("upadesha_slp1") or "").strip().rstrip("~")
        if up == "dyut":
            flat_ok = True
            break
    if not flat_ok:
        return False
    for t in state.terms:
        if (t.meta.get("upadesha_slp1") or "").strip() != "cli":
            continue
        return True
    return False


def cond(state: State) -> bool:
    if not state.meta.get(_META_ARM):
        return False
    return _dyut_site(state)


def act(state: State) -> State:
    if not _dyut_site(state):
        return state
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() != "cli":
            continue
        t.varnas = [mk("a"), mk("G")]
        t.meta["upadesha_slp1"] = "aG"
        t.tags.add("upadesha")
        t.kind = "pratyaya"
        # *aṅ* is **ङित्** — **1.1.5** *kṅiti ca* blocks **7.3.86** (P018-A note).
        t.tags.add("kngiti")
        break
    state.meta.pop(_META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.55",
    sutra_type=SutraType.VIDHI,
    text_slp1="puzAdidyutAdyaRqfitaH parasmaipadaizu",
    text_dev="पुषादिद्युताद्यॢदितः परस्मैपदेषु",
    padaccheda_dev="पुषादि-द्युतादि-ॢदितः / परस्मैपदेषु",
    why_dev=(
        "द्युत्-आदेर् धातोः परस्मैपद-लुङि च्लि-स्थाने अङादेशः (अङ् इति; P018-A)।"
    ),
    anuvritti_from=("3.1.43",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
