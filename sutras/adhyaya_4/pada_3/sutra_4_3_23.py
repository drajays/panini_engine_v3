"""
4.3.23  तत्र भवः  —  VIDHI (narrow: attach tyup to kāla-vācī stems) — P019

The JSON ``split_prakriyas_11/P019.json`` attaches **tyup** to the time-word
*adya* to derive **adyatana**.

Engine (narrow, recipe-armed):
  - recipe sets ``state.meta['prakriya_P019_4_3_23_tyup_arm'] = True``
  - expects an ``anga``+``prātipadika`` witness tagged ``prakriya_P019_adyatanam_demo``.
  - inserts a taddhita pratyaya ``tyup`` (final p = it by **1.3.3**; lopa by **1.3.9**).

No semantic selection beyond arming.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 43023 · सायंचिरम्प्राह्णेप्रगेऽव्ययेभ्यष्ट्युट्युलौ तुट् च
              padaccheda: सायं-चिरम्-प्राह्णे-प्रगे-अव्ययेभ्यः ट्यु-ट्युलौ तुट् च
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः | 42092: शेषे | 43011: कालात्
  Source #2 — Kāśikā 4.3.23 udāharaṇa:
                सायंतनम्
                चिरंतनम्
                प्राह्णेतनम्
  Cross-check — surface pinned by: tests/unit/test_adyatanam_taddhita_split_prakriyas.py
  Reference record: sutra_ref_out/4_3_23.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("prakriya_P019_4_3_23_tyup_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if "prakriya_P019_adyatanam_demo" not in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    i = _site(state)
    if i is None:
        return False
    return not any((t.meta.get("upadesha_slp1") or "").strip() == "tyup" for t in state.terms)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("tyup")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "tyup"},
    )
    state.terms.insert(i + 1, pr)
    state.meta["prakriya_P019_4_3_23_tyup_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.3.23",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tatra BavaH (tyup) (narrow)",
    text_dev       = "तत्र भवः (त्युप्) — संक्षेपः",
    padaccheda_dev = "तत्र / भवः",
    why_dev        = "कालवाचक-शब्देभ्यः त्युप् (अद्य→अद्यतन) — P019 narrow demo.",
    anuvritti_from = ("4.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

