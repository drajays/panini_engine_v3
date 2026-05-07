"""
pipelines/SamBu_subanta.py — **शम्भु** (u-stem masculine, घि-संज्ञक) subanta:
one prakriyā for all 24 *sup* cells.

प्राथमिक संज्ञाएँ
  • 1.2.45  अर्थवदधातुरप्रत्ययः प्रातिपदिकम् — 'शम्भु' की प्रातिपदिक-संज्ञा।
  • 1.4.7   शेषो घ्यसखि — ह्रस्व उकारान्त होने से 'शम्भु' की घि-संज्ञा।
  • 4.1.2   स्वौजसमौट्… — 21 *sup* प्रत्यय।

विभक्ति → मुख्य सूत्र-श्रृंखला
  1-1  सुँ      : ससजुषो रुः (8.2.66) + खरवसानयोर्विसर्जनीयः (8.3.15) → शम्भुः
  1-2  औ       : प्रथमयोः पूर्वसवर्णः (6.1.102) → शम्भू
  1-3  जस्     : जसि च (7.3.109) गुण, एचोऽयवायावः (6.1.78) → शम्भवः
  2-1  अम्     : अमि पूर्वः (6.1.107) → शम्भुम्
  2-2  औट्     : प्रथमयोः पूर्वसवर्णः (6.1.102) → शम्भू
  2-3  शस्     : पूर्वसवर्ण दीर्घ + तस्माच्छसो नः पुंसि (6.1.103) → शम्भून्
  3-1  टा      : आङो नाऽस्त्रियाम् (7.3.120) → शम्भुना
  3-2  भ्याम्  : वर्ण-संयोग → शम्भुभ्याम्
  3-3  भिस्    : रुत्व-विसर्ग → शम्भुभिः
  4-1  ङे      : घेर्ङिति (7.3.111) गुण + एचोऽयवायावः (6.1.78) → शम्भवे
  4-2  भ्याम्  : वर्ण-संयोग → शम्भुभ्याम्
  4-3  भ्यस्   : रुत्व-विसर्ग → शम्भुभ्यः
  5-1  ङसिँ    : घेर्ङिति (7.3.111) + ङसिङसोश्च (6.1.110) → शम्भोः
  5-2  भ्याम्  : वर्ण-संयोग → शम्भुभ्याम्
  5-3  भ्यस्   : रुत्व-विसर्ग → शम्भुभ्यः
  6-1  ङस्     : घेर्ङिति (7.3.111) + ङसिङसोश्च (6.1.110) → शम्भोः
  6-2  ओस्     : इको यणचि (6.1.77) → शम्भ्वोः
  6-3  आम्     : ह्रस्वनद्यापो नुट् (7.1.54) + नामी (6.4.3) → शम्भूनाम्
  7-1  ङि      : अच्च घेः (7.3.119) + वृद्धिरेचि (6.1.88) → शम्भौ
  7-2  ओस्     : इको यणचि (6.1.77) → शम्भ्वोः
  7-3  सुप्    : आदेशप्रत्यययोः (8.3.59) षत्व → शम्भुषु
  8-1  सु      : ह्रस्वस्य गुणः (7.3.108) + एङ्ह्रस्वात् सम्बुद्धेः (6.1.69) → शम्भो
  8-2  औ       : प्रथमयोः पूर्वसवर्णः (6.1.102) → शम्भू
  8-3  जस्     : जसि च (7.3.109) + एचोऽयवायावः (6.1.78) → शम्भवः

Engine notes:
  All 24 cells are derived by ``derive("SamBu", v, vac, linga="pulliṅga")`` — the
  single canonical subanta prakriyā (CONSTITUTION Art. 1: apply_rule only).
  No patchwork, no gold shortcuts (CONSTITUTION Art. 6).

  Key sūtra fix (u-kārānta accusative plural):
    • 6.4.146 guard: bhasya guṇa (u→o) does NOT fire before *śas* (sup context);
      pūrva-savarṇa dīrgha via 6.1.102–6.1.103 applies instead.
    • 6.1.103 u-stem arm: u + śas → ū + n (śambhu → śambhūn).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

from engine.state import State
from pipelines.subanta import derive, derive_ikarant_pullinga

SAMBHU_STEM_SLP1: str = "SamBu"
SAMBHU_LIṄGA: str = "pulliṅga"

SAMBHU_PUM_24_CELLS: tuple[tuple[int, int], ...] = tuple(
    (v, vac) for v in range(1, 9) for vac in range(1, 4)
)


def derive_SamBu_pulliṅga(vibhakti: int, vacana: int) -> State:
    """
    Subanta for *शम्भु* (puṃ, u-anta, ghī-saṃjñaka) at ``(vibhakti, vacana)``.

    Delegates to ``derive("SamBu", …, "pulliṅga")`` — same prakriyā spine as
    any other u-kārānta masculine (भानु, विष्णु, वायु, गुरु, शिशु …).
    """
    return derive(
        SAMBHU_STEM_SLP1,
        vibhakti,
        vacana,
        linga=SAMBHU_LIṄGA,
    )


def sambhu_cell_key(vibhakti: int, vacana: int) -> str:
    return f"{vibhakti}-{vacana}"


def iter_SamBu_paradigm() -> tuple[tuple[str, State], ...]:
    """All 24 cells, each as ``(cell_key, final_state)``."""
    out: list[tuple[str, State]] = []
    for v, vac in SAMBHU_PUM_24_CELLS:
        s = derive_SamBu_pulliṅga(v, vac)
        out.append((sambhu_cell_key(v, vac), s))
    return tuple(out)


def stem_slp1_looks_ukarant_pullinga(stem_slp1: str) -> bool:
    """
    True if ``stem_slp1`` ends in hrasa ``u`` — the SLP1 shape for
    उकारान्त पुंलिङ्ग prātipadikas like ``SamBu``, ``BAnu``, ``vAyu``, ``guru``.
    """
    s = stem_slp1.strip()
    return bool(s) and s[-1] == "u"


def derive_ukarant_pullinga(
    stem_slp1: str,
    vibhakti: int,
    vacana: int,
    *,
    strict_stem: bool = True,
) -> State:
    """
    Run the subanta recipe for **उकारान्त पुंलिङ्ग** (u-stem masculine).

    Same as ``derive(stem_slp1, vibhakti, vacana, linga="pulliṅga")`` but
    optionally validates that the stem ends in hrasa ``u`` (``strict_stem=True``).

    Works for any u-kārānta ghī-saṃjñaka stem: शम्भु, भानु, विष्णु, वायु, गुरु, शिशु …
    """
    if strict_stem and not stem_slp1_looks_ukarant_pullinga(stem_slp1):
        raise ValueError(
            "उकारान्त पुंलिङ्ग हेतु प्रातिपदिक अन्त में ह्रस्व 'u' (SLP1) चाहिए — "
            f"उदाहरण: SamBu, BAnu, guru। प्राप्त: {stem_slp1!r}"
        )
    return derive(stem_slp1, vibhakti, vacana, linga="pulliṅga")


__all__ = [
    "SAMBHU_LIṄGA",
    "SAMBHU_PUM_24_CELLS",
    "SAMBHU_STEM_SLP1",
    "derive_SamBu_pulliṅga",
    "derive_ukarant_pullinga",
    "iter_SamBu_paradigm",
    "sambhu_cell_key",
    "stem_slp1_looks_ukarant_pullinga",
]
