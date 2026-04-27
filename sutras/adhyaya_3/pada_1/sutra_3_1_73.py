"""
3.1.73  स्वादिभ्यः श्नुः  —  VIDHI (narrow: replace *Sap* with *śnu*)

Glass-box: when a pipeline arms ``state.meta["3_1_73_snu_arm"]`` and a *Sap*
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


def cond(state: State) -> bool:
    if not state.meta.get("3_1_73_snu_arm"):
        return False
    return _find_sap(state) is not None


def act(state: State) -> State:
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
    text_slp1      = "svAdibhyaH SnuH",
    text_dev       = "स्वादिभ्यः श्नुः",
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
