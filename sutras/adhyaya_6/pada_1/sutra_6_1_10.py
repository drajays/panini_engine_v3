"""
6.1.10  श्लौ  —  VIDHI (narrow: **P040** *dhātu* *dvi*tva after *śluḥ*)

**Pāṭha:** *ślau* — *anuvṛtti* *ekācaḥ* **6.1.1** *prathamasya* (baked in teaching text).

*Śāstra (laghu):* when *śap* is lost by *śluḥ* (**2.4.75**), **6.1.10** doubles the
*prakṛti* *dhātu* before the *tiṅ* *ādeśa* (*dā* + *ti* → *dā* + *dā* + *ti* → *dadāti*;
*hu* + *ti* → *hu* + *hu* + *ti* → *juhoti* after *abhyāsa* rules).

Engine:
  - ``state.meta['P040_6_1_10_slau_arm']``
  - tape is ``[dhātu hu][ti]`` (no ``Slu`` placeholder — removed after **1.1.61**).
  - inserts an *abhyāsa* copy **without** the ``dhatu`` tag (only ``abhyasa``, ``anga``,
    ``P040_juhoti_abhyasa``) so **7.3.84** still targets the true *dhātu* ``Term``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


def _site(state: State) -> int | None:
    if not state.meta.get("P040_6_1_10_slau_arm"):
        return None
    if state.samjna_registry.get("6.1.10_P040_slau_dvitva_done"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if "P040_juhotyadi" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "hu":
            continue
        if i + 1 >= len(state.terms):
            return None
        nxt = state.terms[i + 1]
        if nxt.kind != "pratyaya":
            return None
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up not in {"ti", "tip"}:
            return None
        return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    dh = state.terms[i]
    abhy_tags = (set(dh.tags) | {"abhyasa", "anga", "P040_juhoti_abhyasa"}) - {"dhatu"}
    abhy = Term(
        kind=dh.kind,
        varnas=list(dh.varnas),
        tags=abhy_tags,
        meta=dict(dh.meta),
    )
    state.terms.insert(i, abhy)
    state.samjna_registry["6.1.10_P040_slau_dvitva_done"] = True
    state.meta.pop("P040_6_1_10_slau_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.10",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Slau (narrow P040)",
    text_dev       = "श्लौ — P040 संक्षेपः",
    padaccheda_dev = "श्लौ",
    why_dev        = "श्लौ-प्रसङ्गे धातोः द्वित्वम् (जुहोति) — P040।",
    anuvritti_from = ("6.1.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
