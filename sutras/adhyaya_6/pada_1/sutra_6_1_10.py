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

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61010 · श्लौ
              padaccheda: श्लौ
              anuvṛtti:   61008: धातोः अनभ्यासस्य | 61001: एकाचः द्वे प्रथमस्य | 61002: अजादेः द्वितीयस्य
  Source #2 — Kāśikā 6.1.10 udāharaṇa:
                जुहोति
                बिभेति
                जिह्रेति
  Cross-check — surface pinned by: tests/regression/test_anya_pullinga_gold.py, tests/regression/test_rADA_strilinga_gold.py, tests/unit/test_6_1_104_nadici_ramau.py
  Reference record: sutra_ref_out/6_1_10.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


def _site(state: State) -> int | None:
    # Gaṇa-scoped by call-site only (pipelines/tinanta.py's gaṇa==3 branch,
    # after 2.4.75 śluḥ has removed śap): any dhātu directly followed by the
    # tiṅ-ādeśa, not just P040's hu.
    if state.samjna_registry.get("6.1.10_P040_slau_dvitva_done"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if not t.meta.get("slu_replaced_sap"):      # श्लौ: only where śap went to ślu (2.4.75)
            return None
        if i + 1 >= len(state.terms):
            return None
        nxt = state.terms[i + 1]
        if nxt.kind != "pratyaya":
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
    vs = list(dh.varnas)
    aT = []
    if vs and "aT_agama_v" in vs[0].tags:      # the aṭ precedes the whole aṅga (abhyāsa included): a-bi-bhet, not *a-bhI-a-bhet
        aT, vs = [vs[0]], vs[1:]
        dh.varnas = list(vs)
    abhy = Term(
        kind=dh.kind,
        varnas=list(vs),
        tags=abhy_tags,
        meta=dict(dh.meta),
    )
    state.terms.insert(i, abhy)
    if aT:      # the aṭ as its own Term before the abhyāsa: it is no part of the abhyāsa (7.4.60 must not read it)
        state.terms.insert(i, Term(kind="pratyaya", varnas=aT, tags={"pratyaya", "agama", "aT_agama"},
                                   meta={"upadesha_slp1": "aw"}))
    state.samjna_registry["6.1.10_P040_slau_dvitva_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.10",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'SlO',
    text_dev       = 'श्लौ',
    samagra_slp1   = "DAtoH anaByAsasya SlO dve ",
    samagra_dev    = "धातोः अनभ्यासस्य श्लौ द्वे ।",
    padaccheda_dev = "श्लौ",
    why_dev        = "श्लौ-प्रसङ्गे धातोः द्वित्वम् (जुहोति) — P040।",
    anuvritti_from = ("6.1.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
