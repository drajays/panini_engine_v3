"""
1.3.8  उपदेशे लशक्वतद्धिते  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — initial **ḷ**-**ś**-**ku** (ल्·श्·कवर्ग) of a **non-taddhita**
  pratyaya in upadeśa gets *it* (then **1.3.9** deletes).

• **v3 encoding:** **Non-taddhita**, **non-dhātu** ``Term`` with ``upadesha`` whose **first**
  Varṇa is **ल्·श्·कु** (SLP1 ``l``, ``S``, or ``KU_VARGA``) gets ``it_candidate_lasaku`` —
  covers *śap* ``Sap``, **sup** *Ne*, etc.  Terms tagged ``lakAra_pratyaya_placeholder`` are
  skipped so abstract ``laT`` keeps **1.3.3**-only *it* on ``T`` (gold *tin*anta spine).

• **v2 reference:** ``~/Documents/panini_engine_v2/core/sutra_1_3_8.py`` +
  ``it_rules.py``
  ``_terms_sup_or_primary_upadesh`` family — different Term model; same idea:
  first-hal it for eligible affixes.

• **Blindness:** ``cond`` reads tags / first Varṇa only — not paradigm coords.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology      import KU_VARGA

# ल्·श्·कवर्ग (SLP1) — *upadeśa* first letter for **1.3.8** *ataddhite*.
_LASAKU_INITIAL_SLP1 = frozenset({"l", "S"}) | KU_VARGA


def _eligible_terms(state: State):
    for i, t in enumerate(state.terms):
        if not t.varnas:
            continue
        first = t.varnas[0]
        if "it" in first.tags or "it_candidate_lasaku" in first.tags:
            continue
        # Abstract *lakāra* spine (``laT`` …) — initial ``l`` is not *laśakavataddhite* *it* here;
        # **1.3.3** *halantyam* on the final ``T`` / *lac* collapse handles the *lakāra* row.
        if "lakAra_pratyaya_placeholder" in t.tags:
            continue
        # Classical *laśakavataddhite* on *pratyaya* / affix *upadeśa* (not *dhātu*).
        # Covers **sup** *Ne*-type rows (*ṅ* ∈ *ku*) and *śap* ``Sap`` (*ś* = ``S``), etc.
        if (
            "upadesha" in t.tags
            and "dhatu" not in t.tags
            and "taddhita" not in t.tags
            and first.slp1 in _LASAKU_INITIAL_SLP1
        ):
            yield i


def cond(state: State) -> bool:
    return next(_eligible_terms(state), None) is not None


def act(state: State) -> State:
    for i in _eligible_terms(state):
        state.terms[i].varnas[0].tags.add("it_candidate_lasaku")
        key = ("it_lasaku", i)
        state.samjna_registry[key] = frozenset({state.terms[i].varnas[0].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.8",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "upadeSe laSakv ataddhite it",
    text_dev       = "उपदेशे लशक्वतद्धिते इत्",
    padaccheda_dev = "उपदेशे लशकु-अतद्धिते इत्",
    why_dev        = (
        "अतद्धिते प्रत्ययादौ ल्-श्-कु-वर्णानाम् इत्-संज्ञा; लोपः १.३.९। "
        "सुप्-पङ्क्तिषु ङ्-आदिर् अपि (*N* ∈ *ku*)।"
    ),
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
