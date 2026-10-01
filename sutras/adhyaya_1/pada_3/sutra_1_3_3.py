"""
1.3.3  हलन्त्यम्  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — final **hal** of an upadeśa gets the name *it* (via
  candidate tag); deletion is **1.3.9**, not here.

• **1.3.4 (न विभक्तौ तुस्माः):** A **sup** pratyaya whose final **hal** is in
  **tusma** does **not** get halantyam (structural ``sup`` + ``TUSMA``; see
  ``sutra_1_3_4``). The ``has_halant_it`` tag (from ``sup_upadesha.json``
  ``_meta``) still gates which affixes participate in halantyam at all.
  The same *tusma*-final exclusion applies to **tiṅ** *ādeśa* *vibhakti* *Terms*
  (e.g. *tas*, *mas*) — one predicate, ``sutra_1_3_4.tusma_final_vibhakti``.

• **Upadeśa only:** a Term already through **1.3.9** (``it_lopa_already_done``)
  keeps its residue: the स् of सिच्, the म् of गमॢँ are not *halantyam* again.

• **Anuvṛtti (Art. 4):** ``upadeśe`` and ``it`` are baked into ``text_*``;
  ``anuvritti_from`` points at **1.3.2** for the *upadeśe* anchor.

• **Blindness:** No paradigm coordinates in ``cond`` (Art. 2).

• **Upasargas:** the prādi are taught with their final hal as real sound
  (सम्'s म् — सममंस्त), except आङ्, whose ङ् Pāṇini uses as an anubandha
  (1.1.14 निपात एकाजनाङ्, 6.1.74 आङ्माङोश्च): आङ्+यम् → आयच्छते.

Sources consulted:
- ashtadhyayi.com data.txt row i=13003
- Kāśikā: "अइउण् — णकारः। ऋऌक् — ककारः। एओङ् — ङकारः।"
- Cross-validation: regression tests tests/unit/test_tinanta_yam_lat_p010.py
  (आयच्छते), tests/unit/test_bhattikavya_1_2.py (सममंस्त)
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_samjna import TAG_HALANTYAM, it_lopa_already_done, register_candidate_tag
from engine.state  import State, Term
from phonology     import HAL, TUSMA
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_3.sutra_1_3_4 import tusma_final_vibhakti

META_P011_B_suT_IC = "corrected_v2_P011_B_suT_ic_arm"

_ANUBANDHA_UPASARGA = frozenset({"A~N", "AN"})


def _p011_b_suT_mid_u_it(state: State) -> None:
    """**P011-B:** *suṭ* residue ``suT`` → ``s`` — medial ``u`` is *it* (bundle); **1.3.9** elides."""
    for i, t in enumerate(state.terms):
        if "upadesha" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "suT":
            continue
        vs = t.varnas
        if len(vs) != 3:
            continue
        if vs[0].slp1 != "s" or vs[1].slp1 != "u" or vs[2].slp1 != "T":
            continue
        if "it" in vs[1].tags:
            continue
        vs[1].tags.add("it")
        state.samjna_registry[("it_P011_B_suT_u", i)] = frozenset({"u"})
    state.meta.pop(META_P011_B_suT_IC, None)


def _eligible(t: Term, state: State) -> bool:
    if "upadesha" not in t.tags or it_lopa_already_done(t):
        return False
    if "upasarga" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() not in _ANUBANDHA_UPASARGA:
        return False
    if "sup" in t.tags and "has_halant_it" not in t.tags:
        return False
    if not t.varnas:
        return False
    last = t.varnas[-1]
    if last.slp1 not in HAL:
        return False
    if "sup" in t.tags and last.slp1 in TUSMA:
        return False
    if tusma_final_vibhakti(t):
        return False
    up_tin = (t.meta.get("upadesha_slp1") or "").strip()
    # **tām** (narrow **3.4.101** output): final nasal *m* is not *halantyam-it*.
    if up_tin == "tAm" and last.slp1 == "m":
        return False
    # **ktrim** (*ktri* + Vt. **4.4.20** *mam*): final **m** is the augment, not
    # *halantyam-it* (corrected-v2 **P003**).
    if up_tin == "ktrim" and last.slp1 == "m":
        return False
    # **P010** *āyacchate*: keep *yam*’s final *m* until **7.3.78** (*yacch*).
    if state.meta.get("corrected_v2_P010_preserve_yam_m") and "dhatu" in t.tags:
        if up_tin == "yam" and last.slp1 == "m":
            return False
    # **P019** *avartsyat*: keep **vft**’s final **t** until **7.3.86** (not *halantyam-it* here).
    if state.meta.get("corrected_v2_P019_demo") and "dhatu" in t.tags:
        if up_tin == "vft" and last.slp1 == "t":
            return False
    if last.tags & {"it", "it_candidate_halantyam", "it_candidate_irit"}:
        return False                     # इर् is one it (vārttika), not र् by halantyam
    if "dhatu" in t.tags and _upadesha_final(up_tin) not in (None, last.slp1):
        return False                     # गमॢँ after it-lopa: म् is not the upadeśa-final
    return True


def term_candidates(state: State, ti: int) -> list[int]:
    """Varṇa index of the final hal of ``terms[ti]`` if it still has to be named *it*."""
    t = state.terms[ti]
    return [len(t.varnas) - 1] if _eligible(t, state) else []


def _eligible_terms(state: State):
    """Yield (index, term) with an unmarked final hal in upadeśa (when allowed)."""
    for i, t in enumerate(state.terms):
        if _eligible(t, state):
            yield i, t


def _upadesha_final(upadesha_slp1: str) -> str | None:
    vs = parse_slp1_upadesha_sequence(upadesha_slp1) if upadesha_slp1 else []
    return vs[-1].slp1 if vs else None


def cond(state: State) -> bool:
    for t in state.terms:
        if "upadesha" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "suT":
            continue
        vs = t.varnas
        if (
            len(vs) == 3
            and vs[0].slp1 == "s"
            and vs[1].slp1 == "u"
            and vs[2].slp1 == "T"
        ):
            return True
    return next(_eligible_terms(state), None) is not None


def act(state: State) -> State:
    for i, t in _eligible_terms(state):
        t.varnas[-1].tags.add("it_candidate_halantyam")
        # Back-compat: keep the historical index-only key expected by some tests.
        # Also keep a stable key that survives later structural insertions.
        state.samjna_registry[("it_halantyam", i)] = frozenset({t.varnas[-1].slp1})

        up = (t.meta.get("upadesha_slp1") or "").strip()
        key = ("it_halantyam", i, up)
        state.samjna_registry[key] = frozenset({t.varnas[-1].slp1})
    _p011_b_suT_mid_u_it(state)
    state.meta.pop(META_P011_B_suT_IC, None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.3",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'halantyam',
    text_dev       = 'हलन्त्यम्',
    padaccheda_dev = "उपदेशे अन्त्यं हलन्त्यम्",
    why_dev        = "उपदेशे अन्त्यः हल् वर्णः ‘इत्’ संज्ञां लभते; "
                     "तुस्मान्त-विभक्तौ निषेधः १.३.४। लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
register_candidate_tag(TAG_HALANTYAM, SUTRA.sutra_id)
