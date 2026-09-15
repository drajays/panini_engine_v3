"""
3.1.55  पुषादिद्युताद्यॢदितः परस्मैपदेषु  —  VIDHI (narrow *aṅ*-substitution)

Teaching **corrected_prakriyas_v2** **P018-A** (*vyadyutat*): in luṅ *parasmaipada*,
*vikaraṇa* ``cli`` is replaced by **अङ्** (machine tape ``a`` + ``G`` with ``G``
as *halantyam-it*, **1.3.9** → ``a``) for *dyutādi* **``dyut``** before *tin*
substitution resolves ``luG``.

Engine:
  • ``state.meta['corrected_v2_P018_A_3_1_55_arm']`` (cleared in ``act``).
  • detects ``cli`` ``Term`` and a **``dyut``** *dhātu* (flat **or** ``upadesha_slp1``).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31055 · पुषादिद्युताद्यॢदितः परस्मैपदेषु
              padaccheda: पुषादि-द्युतादि-ऌदितः परस्मैपदेषु
              anuvṛtti:   31022: धातोः | 31043: लुङि | 31044: च्लेः | 31048: कर्तरि | 31052: अङ्
  Source #2 — Kāśikā 3.1.55 udāharaṇa:
                पुष — अपुषत्
                द्युतादि — अद्युतत्
                अश्वितत्
  Cross-check — surface pinned by: tests/unit/test_tinanta_ad_lug_kartari.py
  Reference record: sutra_ref_out/3_1_55.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk

_META_ARM = "corrected_v2_P018_A_3_1_55_arm"


def _ghas_luG_aG_site(state: State) -> bool:
    """*luṅ* *ghas* (2.4.37) + *cli* → *aṅ* (अघसत् clip).
    2_4_37_ad_to_gas flag (set by 2.4.37 act) implies luṅ structurally."""
    if not state.meta.get("2_4_37_ad_to_gas"):
        return False
    has_cli = False
    has_gas = False
    for t in state.terms:
        if (t.meta.get("upadesha_slp1") or "").strip() == "cli":
            has_cli = True
        if "dhatu" not in t.tags:
            continue
        flat = "".join(v.slp1 for v in t.varnas)
        if flat in {"Gas", "ghas"}:
            has_gas = True
        up = (t.meta.get("upadesha_slp1") or "").strip().rstrip("~")
        if up in {"Gas", "Gasx", "Gasx~"}:
            has_gas = True
    return has_cli and has_gas


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
    return _dyut_site(state) or _ghas_luG_aG_site(state)


def act(state: State) -> State:
    if not (_dyut_site(state) or _ghas_luG_aG_site(state)):
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
