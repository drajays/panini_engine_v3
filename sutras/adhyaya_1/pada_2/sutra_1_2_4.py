"""
1.2.4  सार्वधातुकमपित्  —  SAMJNA

  A *sārvadhātuka* pratyaya (tiṅ-ādeśa **or** vikaraṇa — 3.4.113 makes both
  sārvadhātuka) that is **a-pit** (its own upadeśa does *not* end in the
  इत् letter प्) behaves as *kṅit* for the purpose of blocking guṇa/vṛddhi
  under **1.1.5 kṅiti**. This is why शप् ("Sap", प्-इत्, पित्) never blocks
  guṇa (भवति) while श्यन् ("Syan", no प्-इत्, अपित्) always does (दीव्यति,
  not देव्यति) — the पित्/अपित् split is phonological (does the upadeśa end
  in प्/फ्, i.e. SLP1 ``p``/``P``), not a hardcoded name list.

Engine contract:
  - We model this by tagging the qualifying pratyaya Term with ``kngiti`` and
    recording ``samjna_registry['1.2.4_sarvadhatukam_apit'] = True``.
  - ``_find`` returns the *first* untagged qualifying term still on the tape;
    callers that introduce a new sārvadhātuka pratyaya later (e.g. a
    vikaraṇa inserted after the tiṅ-ādeśa is already on the tape) re-call
    **1.2.4** after popping the registry key (see e.g.
    ``pipelines/tinanta.py``'s upasarga+kṛ ātmanepada spine) so it can find
    and tag that new term too.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 12004 · सार्वधातुकमपित्
              padaccheda: सार्वधातुकम् · अपित्
              anuvṛtti:   12001: ङित्
  Source #2 — Kāśikā 1.2.4 udāharaṇa:
                कुरुतः
                चिनुतः
                सार्वधातुकमिति किम्? कर्ता
  Gloss (sa) — सार्वधातुकं प्रत्ययम् अपित् संज्ञकम् — पकारो न इत्।
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_nayaka.py, tests/forward/test_forward_krdanta_pacaka.py, tests/unit/test_Amalakam.py
  Reference record: sutra_ref_out/1_2_4.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import (
    is_sarvadhatuka_upadesha_slp1,
    sthanin_was_pit,
    tin_by_sthanin,
)

# पित् = the upadeśa's own trailing letter is प् (an इत्, dropped later by
# 1.3.3 हलन्त्यम्). तिप्/सिप्/मिप् are the three tiṅ ādeśa with this; शप्
# ("Sap") carries it too — by design, the very reason गण-1/6/10 roots take
# guṇa under शप् while श्यन् ("Syan", no प्) does not. Phonological, not a
# hardcoded name list: any sārvadhātuka upadeśa ending "p"/"P" is पित्.
def _is_pit_upadesha(up: str) -> bool:
    return up.endswith(("p", "P"))


def _find(state: State) -> int | None:
    # (no once-per-derivation registry gate: the tag on each Term is the idempotence — a vikaraṇa (śnu, śnā, śyan…)
    # arrives after the tiṅ and is just as much sārvadhātuka and apit)
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        if "ardhadhatuka" in t.tags:
            continue            # liṭ's eś (śit by upadeśa) is ārdhadhātuka (3.4.115 > 3.4.113): not "sārvadhātukam apit"
        up = (t.meta.get("upadesha_slp1") or "").strip()
        by_sthanin = tin_by_sthanin(t)
        # a tiṅ ādeśa of laṭ/loṭ/laṅ/liṅ is sārvadhātuka (3.4.113) even after 3.4.101 turned thas → tam, tas → tām …
        by_lak = ("tin_adesha_3_4_78" in t.tags and (t.meta.get("source_lakara_upadesha") or "").strip() in {"laT", "loT", "laG", "liG"}
                  and "ardhadhatuka" not in t.tags and "ashir_liG" not in t.tags)
        if not (is_sarvadhatuka_upadesha_slp1(up) or by_sthanin or by_lak):
            continue
        if _is_pit_upadesha(up) or ((by_sthanin or by_lak) and sthanin_was_pit(t)):   # 1.1.56: ṇal for tip is pit too
            continue
        # 3.4.92 आडुत्तमस्य पिच्च: the loṭ uttama endings are pit (सुनवाव, करवाम)
        if ((t.meta.get("source_lakara_upadesha") or "").strip() == "loT"
                and up in {"mip", "vas", "mas", "ni", "va", "ma", "iw", "vahi", "mahiG", "e", "vahe", "mahe", "E", "vahE", "mahE"}):
            continue
        if t.meta.get("is_apit") is False:
            continue
        if "kngiti" in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("kngiti")
    state.samjna_registry["1.2.4_sarvadhatukam_apit"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.4",
    sutra_type=SutraType.ATIDESHA,
    r1_form_identity_exempt=True,
    text_slp1='sArvaDAtukamapit',
    text_dev='सार्वधातुकमपित्',
    samagra_slp1="apit sArvaDAtukam Nit",
    samagra_dev="अपित् सार्वधातुकम् ङित्",
    padaccheda_dev="सार्वधातुकम् / अपित्",
    why_dev="अपित्-सार्वधातुकस्य कङित्-व्यवहारः — गुणादि निषेध-प्रसङ्गः (कुरुतः)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

