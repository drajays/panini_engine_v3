"""
3.4.78  लस्य तिप्-तस्-…-महिङ् —  VIDHI

**Padaccheda (teaching):** *tip* (1.1) … *mahiṅ* (1.1) — the eighteen *tiṅ* *ādeśa* items.

**Anuvṛtti (baked, Art. 4):** *pratyayaḥ* **3.1.1**, *paraś ca* **3.1.2**, *ādyudāttaś ca* **3.1.3**,
*dhātoḥ* **3.1.91**, *lasaḥ* **3.4.77** — the *lakāra* (abstract *lac*) in *tiṅānta* is replaced
by one of the eighteen *ādeśa* *pratyaya* strings, *para* to the *dhātu*.

**Engine (CONSTITUTION Art. 2):** ``cond`` does **not** read *puruṣa* / *vacana* / *lakāra-name*
as paradigm coordinates.  The *recipe* commits the target *ādeśa* in
``state.meta['tin_adesha_slp1']`` (a string from :data:`TIN_ADESHA_18`) and sets
``state.meta['tin_adesha_pending'] is True`` when substitution should fire.

The *lakāra* *pratyaya* ``Term`` is recognised by ``meta['upadesha_slp1']`` ∈
``LAKAARA_UPADESHA_SLP1`` (e.g. ``'laT'`` for *laṭ*).

**Cross-refs:** 1.4.99, 1.4.100 (pada), 1.4.101 / 1.4.102 (*puruṣa* / *vacana*), 1.4.104
(*vibhakti* of *tiẖ*) — separate sūtras; 1.3.3/1.3.4 (*it* on *p*, *m* in *tip* etc., *tu-smāḥ*).
"""
from __future__ import annotations

from engine         import SutraType, SutraRecord, register_sutra
from engine.gates   import adhikara_in_effect
from engine.state   import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import (
    LAKAARA_UPADESHA_SLP1,
    TIN_ADESHA_18,
    is_tin_adesha,
)


def _lakara_pratyaya_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in LAKAARA_UPADESHA_SLP1:
            return i
    return None


def cond(state: State) -> bool:
    if not adhikara_in_effect("3.4.78", state, "3.4.77"):
        return False
    if not state.meta.get("tin_adesha_pending"):
        return False
    adesha = (state.meta.get("tin_adesha_slp1") or "").strip()
    if not is_tin_adesha(adesha):
        return False
    return _lakara_pratyaya_index(state) is not None


def act(state: State) -> State:
    idx = _lakara_pratyaya_index(state)
    assert idx is not None
    adesha = (state.meta.get("tin_adesha_slp1") or "").strip()
    t = state.terms[idx]
    t.varnas = parse_slp1_upadesha_sequence(adesha)
    t.meta["upadesha_slp1"] = adesha
    t.tags.add("tin_adesha_3_4_78")
    t.tags.discard("lakAra_pratyaya_placeholder")
    state.meta["tin_adesha_pending"] = False
    state.meta.pop("tin_adesha_slp1", None)
    return state


_WHY = (
    "लकार-प्रत्ययस्य स्थाने तिङ्-आदेश (तिप्-तस्-झि-…-महिङ्) — संज्ञाः १.४.९९ इत्यादि-सूत्रैः पृथक्; "
    "सूत्रे अभिकल्पित-तिङ्-लक्ष्यम्, न पुरुष-वचन-परिगणनम् (CONSTITUTION २)।"
)

# Baked sūtra-pāṭha (3.1.1–3.1.3, 3.1.91, 3.4.77 anuvṛtti); list = ``TIN_ADESHA_18`` order.
_TIN_LIST_SLP1 = "-".join(TIN_ADESHA_18)

SUTRA = SutraRecord(
    sutra_id       = "3.4.78",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = (
        "pratyayaH, paraScA, AdyudAttaz ca, DAtA, lasaH — "
        f"lasaH {_TIN_LIST_SLP1} pratyayaH DAtoH paraH"
    ),
    text_dev       = "लस्य तिप्-तस्-झि-…-महिङ् प्रत्ययः धातोः परः",
    padaccheda_dev = "लः / तिप्-तस्-झि-… (परस्मैपदादि) / प्रत्ययः / धातोः / परः",
    why_dev        = _WHY,
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.91", "3.4.77"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
