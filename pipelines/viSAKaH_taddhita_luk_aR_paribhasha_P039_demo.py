"""
pipelines/viSAKaH_taddhita_luk_aR_paribhasha_P039_demo.py — P039 (विशाखः)

Target (SLP1): ``viSAKaH`` — *viśākhā* + *aṇ* (*tatra-bhava*) with **luk** by
**4.3.34** (narrow slice), then *subanta* tail and visarga.

JSON spine (``split_prakriyas_11/P039.json``):
  **1.1.68** → **4.1.76** → **4.3.25** (*aṇ*) → **4.3.34** (*luk*) →
  **1.1.60**, **1.1.61** (*luk*-saṃjñā) → **4.1.1**, **4.1.3**, **4.1.4** (no-op
  on long-ā stem) → **4.1.2** (*su*) → **1.3.2**, **1.3.9**, **1.2.41** →
  **6.1.68** (apṛkta *s* lopa; P039-armed ṭāp-anta branch) →
  structural pulliṅga + pada-final *s* for **8.2.66**/**8.3.15** (JSON step 8
  compresses commentary: *ā*-stem *subanta* lopa then masc. *viśākha-* + *s* →
  visarga) → **8.2.1** → **8.2.66** → **8.3.15** → **1.1.68**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _p039_masc_pada_for_visarga(state: State) -> None:
    """
    After **6.1.68** the tape is ``viSAKA`` (long ``A``); the JSON's **8.2.66**
    step bundles pulliṅga stem ``viSAKa`` + prathamā *s* that feeds visarga.
    """
    if not state.terms:
        return
    t = state.terms[0]
    if not t.varnas or t.varnas[-1].slp1 != "A":
        return
    t.varnas[-1] = mk("a")
    t.tags.discard("strīliṅga")
    t.tags.add("pulliṅga")
    t.tags.add("anga")
    t.varnas.append(mk("s"))
    t.kind = "pada"
    t.tags.add("pada")
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "P039-पुं-प्रथम-पद",
            "form_before": state.flat_slp1(),
            "form_after": state.flat_slp1(),
            "why_dev": (
                "टाप्-अन्त-स्त्रीमूलात् पुंलिङ्ग-प्रथमायाः विशाख-आकारान्तं "
                "तथा पदान्त-सकारं संरचनात्मकं (JSON क्रमे ८.२.६६ सङ्क्षेपः)।"
            ),
            "status": "APPLIED",
        }
    )


def derive_viSAKaH_taddhita_luk_aR_P039() -> State:
    viSAKA = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("viSAKA")),
        tags={"anga", "prātipadika", "strīliṅga", "TAp_anta", "P039_viSAKA_demo"},
        meta={"upadesha_slp1": "viSAKA", "vyutpanna": True},
    )
    s = State(terms=[viSAKA], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)
    s = apply_rule("4.1.76", s)

    s.meta["P039_4_3_25_arm"] = True
    s = apply_rule("4.3.25", s)
    s.meta["P039_4_3_34_arm"] = True
    s = apply_rule("4.3.34", s)

    s = apply_rule("1.1.60", s)
    s = apply_rule("1.1.61", s)

    s = apply_rule("4.1.1", s)
    s = apply_rule("4.1.3", s)
    s = apply_rule("4.1.4", s)

    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.2.41", s)

    s.meta["P039_6_1_68_tApanta_arm"] = True
    s = apply_rule("6.1.68", s)

    _p039_masc_pada_for_visarga(s)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    s = apply_rule("1.1.68", s)
    return s


__all__ = ["derive_viSAKaH_taddhita_luk_aR_P039"]
