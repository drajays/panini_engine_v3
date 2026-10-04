"""
2.4.75  जुहोत्यादिभ्यः श्लुः  —  VIDHI (narrow: **P040** *juhoti*)

*Śāstra (laghu):* for *juhotyādi* (*hu* …), *śap* is replaced by *śluḥ* — the
*ślu*-named *pratyaya-lopa* of *śap*, which **6.1.10** *ślau* follows with *dhātu*
*dvi*tva (*dadāti*, *juhoti*, …).

Engine (recipe-armed only):
  - ``state.meta['P040_2_4_75_arm']``
  - witness *dhātu* ``Term`` tagged ``P040_juhotyadi`` with ``upadesha_slp1`` ``hu``,
    immediately followed by *tiṅ* ``ti`` (after **3.4.78** + *it*-*lopa*).
  - inserts a ``Slu`` *pratyaya* ``Term`` (``S`` + ``l`` + ``u`` in SLP1) tagged
    ``P040_slu_placeholder`` so the recipe can apply **1.1.60**/**1.1.61** and then
    remove the placeholder structurally (JSON ``hu+0+ti``).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 24075 · जुहोत्यादिभ्यः श्लुः
              padaccheda: जुहोत्यादिभ्यः श्लुः
              anuvṛtti:   24072: शपः
  Source #2 — Kāśikā 2.4.75 udāharaṇa:
                जुहोत्यादिभ्य उत्तरस्य शपः श्लुर्भवति
                लुकि प्रकृते श्लुविधानं द्विर्वचनार्थम्
                जुहोति
  Cross-check — surface pinned by: tests/unit/test_juhoti_hu_lat_tip_Slu.py
  Reference record: sutra_ref_out/2_4_75.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    # Gaṇa-scoped by call-site only (pipelines/tinanta.py's gaṇa==3 branch);
    # any dhātu immediately followed by the tiṅ-ādeśa (no vikaraṇa yet on the
    # tape) is a juhotyādi site — not just P040's hu.
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        # जुहोत्यादिः = gaṇa 3 (lexical). The P040 tag is the legacy hand-built witness
        # of pipelines/juhoti_hu_lat_tip_Slu.py, whose dhātu carries no gaṇa.
        if t.meta.get("gana") != 3 and "P040_juhotyadi" not in t.tags:
            continue
        nxt = state.terms[i + 1]
        if nxt.kind != "pratyaya":
            continue
        return i
    return None


def _already_has_slu(state: State) -> bool:
    return any("P040_slu_placeholder" in t.tags for t in state.terms)


def cond(state: State) -> bool:
    i = _site(state)
    return i is not None and not _already_has_slu(state) and not state.terms[i].meta.get("2_4_75_slu_done")


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    if "P040_juhotyadi" not in state.terms[i].tags:
        # ślu is a luk-like lopa of śap (1.1.61): nothing is left on the tape, only the witness 6.1.10 reads, and
        # 3.1.68 must not bring śap back
        for k in reversed(range(len(state.terms))):
            if state.terms[k].kind == "pratyaya" and (state.terms[k].meta.get("upadesha_slp1") or "").strip() == "Sap":
                del state.terms[k]
                if k <= i:
                    i -= 1
        state.terms[i].meta["slu_replaced_sap"] = True
        state.terms[i].meta["3_1_68_sap_given"] = True
        state.terms[i].meta["2_4_75_slu_done"] = True
        return state
    slu = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Slu")),
        tags={"pratyaya", "upadesha", "P040_slu_placeholder"},
        meta={"upadesha_slp1": "Slu"},
    )
    state.terms.insert(i + 1, slu)
    state.terms[i].meta["slu_replaced_sap"] = True      # the witness 6.1.10 (ślau) reads
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.75",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'juhotyAdiByaH SluH',
    text_dev       = 'जुहोत्यादिभ्यः श्लुः',
    padaccheda_dev = "जुहोत्यादिभ्यः / श्लुः",
    why_dev        = "जुहोत्यादि-गणात् शप्-स्थाने श्लुः (२.४.७५) — P040।",
    apavada_of     = ("3.1.68",),   # अपवाद of 3.1.68 — sutra_ref_out resolver.apavada_of
    anuvritti_from = ("2.4.58",),
    r1_form_identity_exempt = True,       # ślu is a lopa: śap goes without a trace on the tape
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
