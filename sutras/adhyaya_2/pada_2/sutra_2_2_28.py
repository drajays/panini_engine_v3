"""
2.2.28  तेन सह इति तुल्ययोगे  —  VIDHI

पदच्छेदः  तेन (तृतीया-एकवचनम्), सह (अव्ययम्), इति (अव्ययम्),
          तुल्ययोगे (सप्तमी-एकवचनम्)

अनुवृत्तिः  अनेकम् 2.2.24

अधिकारः (शास्त्रीय स्मरणार्थम्):
  • आकडारात् एका संज्ञा 1.4.1
  • प्राक्कडारात्समासः 2.1.3
  • सुप्सुपा 2.1.4
  • विभाषा 2.1.11

अनुवृत्तिसहितं सूत्रम्  तेन सह इति तुल्ययोगे

Meaning (Vasu / Kāśikā summary):
  *saha* ‘together’ compounds with a prior padam ending in the third-case
  (instrumental) affix; the compound is **bahuvrīhi**, when companion and
  principal are **tulyayoga** (equally affected).  Examples: *saha putreṇāgataḥ*
  → *saputraḥ*, *sacchātraḥ*, *sakarmakaraḥ*.  *Tulyayoga* is **prāyika**
  (Kāśikā); forms like *sakarmakaḥ* show *samāsa* elsewhere by *vidyamānatā*
  without the strict equality reading — the engine models that by **not**
  arming ``2_2_28_tulyayoga``.

Engine (narrow, mechanically blind):
  Requires **2.1.3** samāsa adhikāra on ``adhikara_stack``, recipe flags
  ``state.meta['2_2_28_arm']`` and ``state.meta['2_2_28_tulyayoga']`` (locative
  *tulyayoge* + *prāyikatva* folded into the recipe), a **prātipadika** companion
  Term tagged ``2_2_28_companion``, and an immediately following (optional
  *iti* nipāta) **saha** avyaya Term (``upadesha_slp1 == 'saha'``).

  Merges to one **bahuvrīhi** stem: *saha* is represented as **sa-** before the
  companion (``sa`` + stem).  An initial ``S`` (palatal ś) uses ``sac`` + rest
  as a narrow stand-in for *ś*–*c* class behaviour before dedicated sandhi
  sūtras (e.g. 6.3.82).

This does not implement 6.3.82 or full internal *sup*; it is an auditable slice.
"""
from __future__ import annotations

from typing import Optional, Tuple

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk
from phonology.varna import AC_DEV, HAL_DEV


def _varnas_from_slp1(slp1: str) -> list:
    varnas = []
    i = 0
    while i < len(slp1):
        ch = slp1[i]
        if ch in HAL_DEV or ch in AC_DEV:
            varnas.append(mk(ch))
        i += 1
    return varnas


def _in_samasa_adhikara(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _is_saha_avyaya(t: Term) -> bool:
    if t.meta.get("upadesha_slp1") != "saha":
        return False
    return "avyaya" in t.tags or t.kind == "nipata"


def _companion_stem_slp1(t: Term) -> str:
    u = t.meta.get("upadesha_slp1")
    if isinstance(u, str) and u.strip():
        return u.strip()
    return "".join(v.slp1 for v in t.varnas)


def _merged_stem_slp1(companion: str) -> str:
    if not companion:
        return "sa"
    if companion[0] == "S":
        return "sac" + companion[1:]
    return "sa" + companion


def _find_hit(state: State) -> Optional[Tuple[int, int, str]]:
    if not state.meta.get("2_2_28_arm"):
        return None
    if not state.meta.get("2_2_28_tulyayoga"):
        return None
    if not _in_samasa_adhikara(state):
        return None
    for i in range(len(state.terms)):
        t0 = state.terms[i]
        if t0.kind != "prakriti":
            continue
        if "prātipadika" not in t0.tags or "2_2_28_companion" not in t0.tags:
            continue
        j = i + 1
        if j >= len(state.terms):
            continue
        if (
            state.terms[j].meta.get("upadesha_slp1") == "iti"
            and "nipata" in state.terms[j].tags
        ):
            j += 1
        if j >= len(state.terms):
            continue
        if not _is_saha_avyaya(state.terms[j]):
            continue
        stem = _merged_stem_slp1(_companion_stem_slp1(t0))
        return i, j, stem
    return None


def cond(state: State) -> bool:
    return _find_hit(state) is not None


def act(state: State) -> State:
    hit = _find_hit(state)
    if hit is None:
        return state
    i, j, stem = hit
    merged = Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(stem),
        tags={"prātipadika", "anga", "sahasamasa", "bahuvrihi"},
        meta={
            "upadesha_slp1": stem,
            "contains_sarvadi": True,
        },
    )
    state.terms = state.terms[:i] + [merged] + state.terms[j + 1 :]
    state.meta["2_2_28_arm"] = False
    state.meta["2_2_28_tulyayoga"] = False
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.28",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tena saha iti tulyayoge",
    text_dev       = "तेन सह इति तुल्ययोगे",
    padaccheda_dev = (
        "तेन (तृतीया-एकवचनम्), सह (अव्ययम्), इति (अव्ययम्), "
        "तुल्ययोगे (सप्तमी-एकवचनम्)"
    ),
    why_dev        = (
        "तृतीयान्तेन सह समासो बहुव्रीहिः; तुल्ययोगे प्रायिकं — "
        "अनार्म्ड-तुल्ययोगे सकर्मकादयो नात्र।"
    ),
    anuvritti_from = ("2.2.24",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
