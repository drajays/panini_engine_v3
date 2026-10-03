"""
7.1.94  ऋदुशनस्पुरुदंसोऽनेहसां च  —  VIDHI

For any ṛ-final (vocalic **f**) prātipadika before **su** — not just tṛc
agent nouns (kartā, hartā) but the inherited ṛ-stem kinship/agent nouns too
(mātṛ→mātā, pitṛ→pitā, bhrātṛ→bhrātā, svasṛ→svasā, ...) — substitute **an**
for that **f**. The rule's own text has no kṛt-vs-non-kṛt restriction; the
earlier ``krt_tfc``-only ``cond()`` was too narrow and silently left every
non-kṛt ṛ-stem noun undeclined through the general subanta pipeline (see
Prakriyotsava sweep bug #7).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 71094 · ऋदुशनस्पुरुदंसोऽनेहसां च
              padaccheda: ऋत्-उशनस्-पुरुदंस्-अनेहसाम् च
              anuvṛtti:   64001: अङ्गस्य | 71092: असम्बुद्धौ | 71093: अनङ् सौ
  Source #2 — Kāśikā 7.1.94 udāharaṇa:
                कर्ता
                हर्ता
                माता
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_trc.py, tests/unit/test_vaktA_split_prakriyas.py
  Reference record: sutra_ref_out/7_1_94.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    ang = state.terms[0]
    sup = state.terms[-1]
    if "prātipadika" not in ang.tags or "sup" not in sup.tags:
        return False
    if ang.meta.get("anaN_7_1_94_done"):
        return False
    if not ang.varnas or ang.varnas[-1].slp1 != "f":
        return False
    if (sup.meta.get("upadesha_slp1") or "").strip() != "s~" or "sambuddhi" in sup.tags:
        return False        # sau = the nominative singular su (not the loc. pl. sup), and asambuddhau (7.1.92): हे पितः
    if not sup.varnas or sup.varnas[0].slp1 != "s":
        return False
    return True


def act(state: State) -> State:
    ang = state.terms[0]
    ang.varnas[-1] = mk("a")
    ang.varnas.append(mk("n"))
    ang.meta["anaN_7_1_94_done"] = True
    # The अन्-आदेश just made this a genuine न्-final अङ्ग (part of the
    # प्रातिपदिक itself, not a न्-आगम) — 8.2.7 needs this tag to see it
    # (mirrors what pipelines/subanta.py does at tape-init for stems that
    # already end in "n", e.g. राजन्).
    ang.tags.add("an_pratipadika")
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.94",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'fduSanaspurudaMsonehasAM ca',
    text_dev       = 'ऋदुशनस्पुरुदंसोऽनेहसां च',
    padaccheda_dev = "ऋत्-उशनस्-पुरुदंसोः अनेहसां च",
    why_dev        = "ऋकारान्ते अनङ्-आदेशः (तृच् + सु)।",
    anuvritti_from = ("7.1.93",),
    # अनङ् takes the ṛ of pitṛ/bhrātṛ… before su and the other sarvanāmasthāna; 7.3.110 (ṛto ṅi सर्वनामस्थानयोर्गुणः)
    # would give guṇa to the same ṛ (पितर्). Declared — the gold forms पिता/भ्राता need it (Art. 15; scholar to confirm).
    apavada_of     = ("7.3.110",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
