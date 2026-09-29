"""
3.1.73  स्वादिभ्यः श्नुः  —  VIDHI (narrow: replace *Sap* with *śnu*)

Glass-box: when a pipeline arms ``state.meta["snu_recipe"]`` and a *Sap*
*vikaraṇa* *Term* is present (from **3.1.68**), replace it with *śnu* *upadeśa*
``Snu`` — *ś* is *it* (**1.3.8**); after **1.3.9** only ``nu`` remains.

The inserted *Term* carries ``kngiti`` so **1.1.5** / **7.3.84** treat *apit*
*śit*–*vikaraṇa* behaviour (e.g. *ci* + *nu* + *tas*: no *guṇa* on *i* before *nu*).

*Cross-check:* ``sutrANi.tsv`` row 3.1.73; machine index i=31073.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_sap(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "Sap":
            return i
    return None


def _svadi_dhatu(state: State) -> int | None:
    """स्वादिभ्यः श्नुः: a svādi (gaṇa-5) dhātu before a sārvadhātuka tiṅ, no
    vikaraṇa yet — returns the insertion index (right after the dhātu)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("gana") != 5:
            continue
        if any("vikarana" in u.tags for u in state.terms[i + 1:]):
            return None
        if any("tin_adesha_3_4_78" in u.tags for u in state.terms[i + 1:]):
            return i + 1
    return None


def cond(state: State) -> bool:
    if state.meta.get("snu_recipe"):
        return _find_sap(state) is not None
    return _svadi_dhatu(state) is not None


def act(state: State) -> State:
    j = _svadi_dhatu(state)
    if j is not None and not state.meta.get("snu_recipe"):
        state.terms.insert(j, Term(kind="pratyaya", varnas=parse_slp1_upadesha_sequence("Snu"),
                                   tags={"pratyaya", "vikarana", "upadesha"},
                                   meta={"upadesha_slp1": "Snu"}))
        return state
    i = _find_sap(state)
    if i is None:
        return state
    snu = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Snu"),
        tags={"pratyaya", "vikarana", "upadesha", "kngiti"},
        meta={"upadesha_slp1": "Snu"},
    )
    state.terms[i] = snu
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.73",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'svAdiByaH SnuH',
    text_dev       = 'स्वादिभ्यः श्नुः',
    padaccheda_dev = "स्वादिभ्यः / श्नुः",
    why_dev        = (
        "स्वादिगणीय-धातोः कर्तरि सार्वधातुके शप्-अपवादः — श्नु-विकरणः; "
        "श् इत् (१.३.८), लोपे नु शेषः।"
    ),
    anuvritti_from = ("3.1.67", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

# SOI: svAdi (gana 5) śnu — apavāda to śap; score 10 when gana matches, else 0.
from engine.specificity_registry import register_specificity as _rs
_rs("3.1.73", lambda state, _g=5: (
    10 if next((t.meta.get("gana") for t in state.terms if "dhatu" in t.tags), None) == _g else 0
))
del _rs
