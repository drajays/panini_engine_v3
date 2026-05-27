"""
pipelines/asmad_subanta.py — अस्मद् pronoun subanta derivation.
───────────────────────────────────────────────────────────────

Glass-box pipeline for first-person pronoun अस्मद् (asmad) — all 21 forms.

Pāṇinian sequence varies by cell; key sūtras used:
  7.1.27  yuṣmadaśmādbhyāṃ ṅasoś aś  (ṅas → aś)
  7.1.28  ṅe prathamayoram             (su/au/as/e → am)
  7.1.29  śasas n                      (śas ādi a → n)
  7.1.30  bhyasas bhyam                (bhyas → bhyam for caturthi bahu)
  7.1.31  pañcamyā at                  (bhyas → at for pañcami bahu)
  7.1.32  ekacasya at                  (ṅasi → at for pañcami eka)
  7.1.33  sāmām ākam                   (ām → ākam for ṣaṣṭhī bahu)
  7.2.86  yuṣmadaśmādor anādeśe       (d → ā general)
  7.2.87  dvitīyāyāṃ ca               (d → ā in dvitīyā)
  7.2.88  prathamāyāś ca dvivacane     (d → ā in prathamā dvivacana)
  7.2.89  yo'ci                        (d → y before vowel)
  7.2.90  śeṣe lopaḥ                  (delete final d)
  7.2.92  yuvāvau dvivacane            (asm → āva in dvivacana)
  7.2.93  yūyavayau jasi               (asm → vaya before jas)
  7.2.94  tvāhau sau                   (asm → aha before su)
  7.2.95  tubhyamahyau ṅayi            (asm → mahya before ṅe)
  7.2.96  tvamāv ekavacane             (asm → ma in ekavacana; asm → mama for ṅas)
  6.1.97  atah guṇe (extended)         (consecutive a+a → a pararūpa)
  6.1.101 akah savarṇe dīrghaḥ        (a+ā → ā within stem)
  6.1.107 ami pūrvaḥ                   (stem-final vowel + am-initial a)
  8.2.23  saṃyogāntasya lopaḥ         (drop final s of ns in dvitīyā bahu)
  8.2.39  jhalaṃ jaśo'nte             (t → d at pāda)
  8.2.66  sasajuṣo ruḥ                (s → ru)
  8.3.15  ru → visarga                (ru → ḥ)
"""
# ── CONSTITUTION-compliant · apply_rule only · Art.6 firewall · no gold shortcuts ──
from __future__ import annotations

import sutras  # noqa: F401  — side-effect: registers all sūtras

from engine            import apply_rule
from engine.state      import State
from pipelines.subanta import build_initial_state, _pada_merge

from core.canonical_pipelines import P01_subanta_bootstrap as run_subanta_preflight_through_1_4_7


def _build_base(vibhakti: int, vacana: int) -> State:
    """Build initial state and run standard preflight + sup attach + it-lopa."""
    s = build_initial_state("asmad", vibhakti, vacana, linga="pulliṅga")
    stem = s.terms[0]
    stem.tags.add("sarvanama")
    stem.tags.add("asmad_stem")
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    for sid in ("3.1.1", "3.1.2", "1.4.102", "1.1.43", "1.4.13", "1.4.14"):
        s = apply_rule(sid, s)
    # it-prakaraṇa
    for sid in ("1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8", "1.3.9"):
        s = apply_rule(sid, s)
    return s


def _arm(s: State, key: str) -> State:
    """Set an arm flag, apply_rule, then clear the flag."""
    return s  # flag set externally; helper just for clarity


def _merge_finish(s: State, *, need_tripadi: bool = False,
                  need_visarga: bool = False,
                  need_ns_drop: bool = False,
                  need_t_to_d: bool = False) -> State:
    """Merge terms and run tripāḍī as needed."""
    if len(s.terms) > 1:
        _pada_merge(s)
    if need_tripadi or need_visarga or need_ns_drop or need_t_to_d:
        s = apply_rule("8.2.1", s)
        if need_ns_drop:
            s.meta["8_2_23_asmad_ns_arm"] = True
            s = apply_rule("8.2.23", s)
            s.meta.pop("8_2_23_asmad_ns_arm", None)
        if need_t_to_d:
            s = apply_rule("8.2.39", s)
        if need_visarga:
            s = apply_rule("8.2.66", s)
            s = apply_rule("8.3.15", s)
    s = apply_rule("1.4.110", s)
    return s


# ─── Individual cell derivations ──────────────────────────────────────────────

def _cell_1_1(s: State) -> State:
    """अहम् — prathamā ekavacana."""
    s = apply_rule("7.1.28", s)       # su → am
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.4", s)
    s = apply_rule("7.2.94", s)       # asm → aha
    s = apply_rule("6.1.97", s)       # a+a → a
    s = apply_rule("7.2.90", s)       # del d
    s = apply_rule("6.1.107", s)      # ami pūrvaḥ
    return _merge_finish(s)


def _cell_1_2(s: State) -> State:
    """आवाम् — prathamā dvivacana."""
    s.meta["7_1_28_au_arm"] = True
    s = apply_rule("7.1.28", s)       # au → am
    s.meta.pop("7_1_28_au_arm", None)
    s.meta["7_2_92_arm"] = True
    s = apply_rule("7.2.92", s)       # asm → āva
    s.meta.pop("7_2_92_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s.meta["7_2_88_arm"] = True
    s = apply_rule("7.2.88", s)       # d → ā (prathamā dvivacana)
    s.meta.pop("7_2_88_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā within stem
    s = apply_rule("6.1.107", s)      # ami pūrvaḥ (del suffix-a)
    return _merge_finish(s)


def _cell_1_3(s: State) -> State:
    """वयम् — prathamā bahuvacana."""
    s.meta["7_1_28_as_arm"] = True
    s = apply_rule("7.1.28", s)       # jas/as → am
    s.meta.pop("7_1_28_as_arm", None)
    s.meta["7_2_93_arm"] = True
    s = apply_rule("7.2.93", s)       # asm → vaya
    s.meta.pop("7_2_93_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s = apply_rule("7.2.90", s)       # del d
    s = apply_rule("6.1.107", s)      # ami pūrvaḥ
    return _merge_finish(s)


def _cell_2_1(s: State) -> State:
    """माम् — dvitīyā ekavacana."""
    # pratyaya 'am' already (no 7.1.28 needed)
    s.meta["7_2_96_ma_arm"] = True
    s = apply_rule("7.2.96", s)       # asm → ma
    s.meta.pop("7_2_96_ma_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s.meta["7_2_87_arm"] = True
    s = apply_rule("7.2.87", s)       # d → ā (dvitīyā)
    s.meta.pop("7_2_87_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā within stem
    s = apply_rule("6.1.107", s)      # ami pūrvaḥ
    return _merge_finish(s)


def _cell_2_2(s: State) -> State:
    """आवाम् — dvitīyā dvivacana."""
    s.meta["7_1_28_au_arm"] = True
    s = apply_rule("7.1.28", s)       # auT → am (after T-it lopa)
    s.meta.pop("7_1_28_au_arm", None)
    s.meta["7_2_92_arm"] = True
    s = apply_rule("7.2.92", s)       # asm → āva
    s.meta.pop("7_2_92_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s.meta["7_2_87_arm"] = True
    s = apply_rule("7.2.87", s)       # d → ā (dvitīyā)
    s.meta.pop("7_2_87_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā within stem
    s = apply_rule("6.1.107", s)      # ami pūrvaḥ
    return _merge_finish(s)


def _cell_2_3(s: State) -> State:
    """अस्मान् — dvitīyā bahuvacana."""
    s.meta["7_1_29_arm"] = True
    s = apply_rule("7.1.29", s)       # śas ādi a → n (→ [n,s])
    s.meta.pop("7_1_29_arm", None)
    s.meta["7_2_87_arm"] = True
    s = apply_rule("7.2.87", s)       # d → ā (dvitīyā)
    s.meta.pop("7_2_87_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā within stem
    return _merge_finish(s, need_tripadi=True, need_ns_drop=True)


def _cell_3_1(s: State) -> State:
    """मया — tṛtīyā ekavacana."""
    s.meta["7_2_96_ma_arm"] = True
    s = apply_rule("7.2.96", s)       # asm → ma
    s.meta.pop("7_2_96_ma_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s.meta["7_2_89_arm"] = True
    s = apply_rule("7.2.89", s)       # d → y (before vowel ā of ṭā)
    s.meta.pop("7_2_89_arm", None)
    return _merge_finish(s)


def _cell_3_2(s: State) -> State:
    """आवाभ्याम् — tṛtīyā dvivacana."""
    s.meta["7_2_92_arm"] = True
    s = apply_rule("7.2.92", s)       # asm → āva
    s.meta.pop("7_2_92_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s.meta["7_2_86_arm"] = True
    s = apply_rule("7.2.86", s)       # d → ā (general)
    s.meta.pop("7_2_86_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā within stem
    return _merge_finish(s)


def _cell_3_3(s: State) -> State:
    """अस्माभिः — tṛtīyā bahuvacana."""
    s.meta["7_2_86_arm"] = True
    s = apply_rule("7.2.86", s)       # d → ā (general)
    s.meta.pop("7_2_86_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā within stem
    return _merge_finish(s, need_tripadi=True, need_visarga=True)


def _cell_4_1(s: State) -> State:
    """मह्यम् — caturthi ekavacana."""
    s.meta["7_1_28_e_arm"] = True
    s = apply_rule("7.1.28", s)       # ṅe/e → am
    s.meta.pop("7_1_28_e_arm", None)
    s.meta["7_2_95_arm"] = True
    s = apply_rule("7.2.95", s)       # asm → mahya
    s.meta.pop("7_2_95_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s = apply_rule("7.2.90", s)       # del d
    s = apply_rule("6.1.107", s)      # ami pūrvaḥ
    return _merge_finish(s)


def _cell_4_2(s: State) -> State:
    """आवाभ्याम् — caturthi dvivacana (same as 3-2)."""
    return _cell_3_2(s)


def _cell_4_3(s: State) -> State:
    """अस्मभ्यम् — caturthi bahuvacana."""
    s.meta["7_1_30_arm"] = True
    s = apply_rule("7.1.30", s)       # bhyas → bhyam
    s.meta.pop("7_1_30_arm", None)
    s.meta["7_2_90_direct_arm"] = True
    s = apply_rule("7.2.90", s)       # del d (direct arm)
    s.meta.pop("7_2_90_direct_arm", None)
    return _merge_finish(s)


def _cell_5_1(s: State) -> State:
    """मद् — pañcami ekavacana."""
    s.meta["7_1_32_arm"] = True
    s = apply_rule("7.1.32", s)       # ṅasi → at
    s.meta.pop("7_1_32_arm", None)
    s.meta["7_2_96_ma_arm"] = True
    s = apply_rule("7.2.96", s)       # asm → ma
    s.meta.pop("7_2_96_ma_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a (intra-stem)
    s = apply_rule("7.2.90", s)       # del d (Mode A)
    s = apply_rule("6.1.97", s)       # a+a cross-term (ma + at boundary)
    return _merge_finish(s, need_tripadi=True, need_t_to_d=True)


def _cell_5_2(s: State) -> State:
    """आवाभ्याम् — pañcami dvivacana (same as 3-2)."""
    return _cell_3_2(s)


def _cell_5_3(s: State) -> State:
    """अस्मद् — pañcami bahuvacana."""
    s.meta["7_1_31_arm"] = True
    s = apply_rule("7.1.31", s)       # bhyas → at
    s.meta.pop("7_1_31_arm", None)
    s.meta["7_2_90_direct_arm"] = True
    s = apply_rule("7.2.90", s)       # del d (direct arm)
    s.meta.pop("7_2_90_direct_arm", None)
    s = apply_rule("6.1.97", s)       # a+a cross-term (asma + at boundary)
    return _merge_finish(s, need_tripadi=True, need_t_to_d=True)


def _cell_6_1(s: State) -> State:
    """मम — ṣaṣṭhī ekavacana."""
    # 7.1.27: ṅas → aś
    s.meta["7_1_27_arm"] = True
    s = apply_rule("7.1.27", s)
    s.meta.pop("7_1_27_arm", None)
    # 1.3.3+1.3.9: ś → it → lopa → leaving [a]
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    # 7.2.96 mama: asm → mama
    s.meta["7_2_96_mama_arm"] = True
    s = apply_rule("7.2.96", s)
    s.meta.pop("7_2_96_mama_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a (intra-stem: mamaad → mamad)
    s = apply_rule("7.2.90", s)       # del d (Mode A)
    s = apply_rule("6.1.97", s)       # cross-term a+a → a (stem-final + pratyaya)
    return _merge_finish(s)


def _cell_6_2(s: State) -> State:
    """आवयोः — ṣaṣṭhī dvivacana."""
    s.meta["7_2_92_arm"] = True
    s = apply_rule("7.2.92", s)       # asm → āva
    s.meta.pop("7_2_92_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s.meta["7_2_89_arm"] = True
    s = apply_rule("7.2.89", s)       # d → y (before o of os)
    s.meta.pop("7_2_89_arm", None)
    return _merge_finish(s, need_tripadi=True, need_visarga=True)


def _cell_6_3(s: State) -> State:
    """अस्माकम् — ṣaṣṭhī bahuvacana."""
    s.meta["7_1_33_arm"] = True
    s = apply_rule("7.1.33", s)       # ām → ākam
    s.meta.pop("7_1_33_arm", None)
    s.meta["7_2_90_direct_arm"] = True
    s = apply_rule("7.2.90", s)       # del d (direct arm)
    s.meta.pop("7_2_90_direct_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā (stem-final a + ākam-initial ā)
    return _merge_finish(s)


def _cell_7_1(s: State) -> State:
    """मयि — saptami ekavacana."""
    s.meta["7_2_96_ma_arm"] = True
    s = apply_rule("7.2.96", s)       # asm → ma
    s.meta.pop("7_2_96_ma_arm", None)
    s = apply_rule("6.1.97", s)       # a+a → a
    s.meta["7_2_89_arm"] = True
    s = apply_rule("7.2.89", s)       # d → y (before i of ṅi)
    s.meta.pop("7_2_89_arm", None)
    return _merge_finish(s)


def _cell_7_2(s: State) -> State:
    """आवयोः — saptami dvivacana (same as 6-2)."""
    return _cell_6_2(s)


def _cell_7_3(s: State) -> State:
    """अस्मासु — saptami bahuvacana."""
    s.meta["7_2_86_arm"] = True
    s = apply_rule("7.2.86", s)       # d → ā (general; before su)
    s.meta.pop("7_2_86_arm", None)
    s = apply_rule("6.1.101", s)      # a+ā → ā within stem
    return _merge_finish(s)


# ─── Router ────────────────────────────────────────────────────────────────────

_CELL_MAP = {
    (1, 1): _cell_1_1,
    (1, 2): _cell_1_2,
    (1, 3): _cell_1_3,
    (2, 1): _cell_2_1,
    (2, 2): _cell_2_2,
    (2, 3): _cell_2_3,
    (3, 1): _cell_3_1,
    (3, 2): _cell_3_2,
    (3, 3): _cell_3_3,
    (4, 1): _cell_4_1,
    (4, 2): _cell_4_2,
    (4, 3): _cell_4_3,
    (5, 1): _cell_5_1,
    (5, 2): _cell_5_2,
    (5, 3): _cell_5_3,
    (6, 1): _cell_6_1,
    (6, 2): _cell_6_2,
    (6, 3): _cell_6_3,
    (7, 1): _cell_7_1,
    (7, 2): _cell_7_2,
    (7, 3): _cell_7_3,
}


def derive_asmad(vibhakti: int, vacana: int) -> State:
    """
    Derive अस्मद् subanta form.

    Implements all 21 primary cells (vibhakti 1–7, vacana 1–3).

    Args:
        vibhakti: 1..7  (1=prathamā … 7=saptami; no sambodhana for pronouns)
        vacana:   1..3  (1=eka, 2=dvi, 3=bahu)

    Returns:
        State with full derivation trace; state.flat_dev() gives the Devanāgarī form.

    Forms:
        1-1 अहम्      1-2 आवाम्    1-3 वयम्
        2-1 माम्      2-2 आवाम्    2-3 अस्मान्
        3-1 मया       3-2 आवाभ्याम् 3-3 अस्माभिः
        4-1 मह्यम्    4-2 आवाभ्याम् 4-3 अस्मभ्यम्
        5-1 मद्       5-2 आवाभ्याम् 5-3 अस्मद्
        6-1 मम        6-2 आवयोः    6-3 अस्माकम्
        7-1 मयि       7-2 आवयोः    7-3 अस्मासु
    """
    cell = (vibhakti, vacana)
    if cell not in _CELL_MAP:
        raise ValueError(
            f"अस्मद् हेतु vibhakti={vibhakti}, vacana={vacana} अमान्य। "
            f"1≤vibhakti≤7, 1≤vacana≤3।"
        )
    s = _build_base(vibhakti, vacana)
    return _CELL_MAP[cell](s)


__all__ = ["derive_asmad"]


if __name__ == "__main__":
    expected = {
        (1, 1): "अहम्",    (1, 2): "आवाम्",    (1, 3): "वयम्",
        (2, 1): "माम्",    (2, 2): "आवाम्",    (2, 3): "अस्मान्",
        (3, 1): "मया",     (3, 2): "आवाभ्याम्", (3, 3): "अस्माभिः",
        (4, 1): "मह्यम्",  (4, 2): "आवाभ्याम्", (4, 3): "अस्मभ्यम्",
        (5, 1): "मद्",     (5, 2): "आवाभ्याम्", (5, 3): "अस्मद्",
        (6, 1): "मम",      (6, 2): "आवयोः",    (6, 3): "अस्माकम्",
        (7, 1): "मयि",     (7, 2): "आवयोः",    (7, 3): "अस्मासु",
    }
    all_pass = True
    for (v, vac), exp in sorted(expected.items()):
        got = derive_asmad(v, vac).flat_dev()
        ok = got == exp
        if not ok:
            all_pass = False
        mark = "✓" if ok else "✗"
        mismatch = f" ≠ {exp}" if not ok else ""
        print(f"{mark} {v}-{vac}: {got}{mismatch}")
    if all_pass:
        print("\nसर्वे रूपाः सम्यक् सिद्धाः। ✓")
    else:
        print("\nकेचन रूपाः असम्यक्। ✗")
