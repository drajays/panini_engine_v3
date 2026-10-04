"""
3.1.78  रुधादिभ्यः श्नम्  —  VIDHI (narrow demo)

Glass-box slice (भिनत्ति .md):
  For the dhātus `Bid` (bhid) and `Cid` (chid), insert the vikarana `Snam`.
  Since `Snam` is **mit** (final m is halantyam-it), it is positioned after the
  last vowel of the dhātu per 1.1.47 (infix insertion).

Engine:
  - recipe-armed by ``state.meta['3_1_78_snam_arm']``.
  - transforms a single dhātu Term into one dhātu Term with `n` inserted after
    its last vowel (post-it-lopa), and records `3_1_78_snam_done`.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31078 · रुधादिभ्यः श्नम्
              padaccheda: रुधादिभ्यः श्नम्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31022: धातोः | 31067: सार्वधातुके | 31068: कर्तरि | 11047: अचः अन्त्यात् परः
  Source #2 — Kāśikā 3.1.78 udāharaṇa:
                शपोऽपवादः
                मकारो देशविध्यर्थः
                शकारः  (६.४.२३) इति विशेषणार्थः
  Cross-check — surface pinned by: tests/constitutional/test_vipratisedha_resolver.py
  Reference record: sutra_ref_out/3_1_78.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_3.pada_1.vikarana_sap_3_1_68 import sarvadhatuka_lakara_context
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_dirgha, is_hrasva
from phonology.varna import mk_inherent_a


def _is_ac(ch: str) -> bool:
    return bool(is_hrasva(ch) or is_dirgha(ch) or ch in {"e", "E", "o", "O"})


def _matches(state: State) -> bool:
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if dh.meta.get("3_1_78_snam_done"):
        return False
    # रुधादिभ्यः श्नम् — any rudhādi (gaṇa-7) root (was four named roots)
    up = (dh.meta.get("upadesha_slp1") or "").strip()
    if dh.meta.get("gana") != 7 and up not in {"Bid", "Cid", "ruD", "viS"}:
        return False
    return any(_is_ac(v.slp1) for v in dh.varnas)


def cond(state: State) -> bool:
    return _matches(state) and sarvadhatuka_lakara_context(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    dh = state.terms[0]
    # Insert 'n' after the last vowel (1.1.47 gate respected by construction).
    j = None
    for i in range(len(dh.varnas) - 1, -1, -1):
        if _is_ac(dh.varnas[i].slp1):
            j = i
            break
    assert j is not None
    # śnam-remainder: classical teaching treats the resulting tape as ... n + a ...
    # before the final consonant (e.g. Binad + ti → Binatti via 8.4.55).
    n, a = mk("n"), mk_inherent_a()
    n.tags.add("snam"); a.tags.add("snam")      # 6.4.111 finds śnam's a by this
    dh.varnas.insert(j + 1, n)
    dh.varnas.insert(j + 2, a)
    dh.meta["3_1_78_snam_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.78",
    sutra_type=SutraType.VIDHI,
    text_slp1='ruDAdiByaH Snam',
    text_dev='रुधादिभ्यः श्नम्',
    padaccheda_dev="रुधादिभ्यः श्नम्",
    why_dev="रुधादि-गणेभ्यः धातुभ्यः श्नम्-विकरणः (मित्—१.१.४७ अनुसारम् अन्त्य-अच् परः)।",
    anuvritti_from=("3.1.1", "3.1.2", "3.1.3", "3.1.67", "3.1.91"),
    cond=cond,
    act=act,
    apavada_of=('3.1.68',),
)

register_sutra(SUTRA)

