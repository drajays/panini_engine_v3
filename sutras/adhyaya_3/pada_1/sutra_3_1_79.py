"""
3.1.79  तनादिकृञ्भ्य उः  —  VIDHI

For tanādi (gaṇa 8) and kṛñ roots, insert vikaraṇa ``u`` after the dhātu,
displacing śap (3.1.68 apavāda). The ``u`` is sārvadhatuka-tagged so 7.3.84
fires guṇa on the dhātu (kṛ → kar).

Structural trigger (CONSTITUTION Art. 13):
- dhātu ``gana == 8`` OR stem in ``_TANADI_STEMS``
- a ``tin_adesha_3_4_78``-tagged term is on tape (sārvadhatuka context)
- no ``u`` vikaraṇa already inserted

No arm flag required (Art. 13).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31079 · तनादिकृञ्भ्य उः
              padaccheda: तनादि-कृञ्भ्यः उः
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31022: धातोः | 31067: सार्वधातुके | 31068: कर्तरि
  Source #2 — Kāśikā 3.1.79 udāharaṇa:
                शपोऽपवादः
                तनोति
                सनोति
  Cross-check — surface pinned by: tests/constitutional/test_no_new_duplicates.py, tests/unit/test_akurvAtAm_laG_tanadi_kf.py, tests/unit/test_kurutaH_lat_tanadi_u.py
  Reference record: sutra_ref_out/3_1_79.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_3.pada_1.vikarana_sap_3_1_68 import sarvadhatuka_lakara_context
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

# Post-it-lopa stems of tanādi roots currently exercised in this repository.
_TANADI_STEMS: frozenset[str] = frozenset({"kf", "tan", "man", "san", "van", "kan", "kzaR"})


def _find_dhatu_for_u(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        gana = t.meta.get("gana")
        stem = "".join(v.slp1 for v in t.varnas)
        # तनादिकृञ्भ्यः: the tanādi gaṇa (8, kṛ included). A stem that merely *spells* like one
        # (van of vana~, san of ṣaṇa~, kan of kanī~ — gaṇa 1) is not tanādi; the spelling list is only a
        # fallback for hand-built dhātus that carry no gaṇa at all.
        if gana != 8 and not (gana is None and stem in _TANADI_STEMS):
            continue
        if t.meta.get("3_1_79_u_done"):
            continue
        # already inserted?
        if i + 1 < len(state.terms):
            nxt = state.terms[i + 1]
            if (nxt.meta.get("upadesha_slp1") or "").strip() == "u":
                continue
        # सार्वधातुके: the affix that stands right after the dhātu must not be ārdhadhātuka — in
        # lṛṭ/luṭ it is sya/tās (3.1.33), and the tiṅ behind it does not make the vikaraṇa u.
        head = next((u for u in state.terms[i + 1:] if u.kind == "pratyaya" and u.varnas), None)
        if head is None or "ardhadhatuka" in head.tags:
            continue
        if not any("tin_adesha_3_4_78" in t2.tags for t2 in state.terms):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_dhatu_for_u(state) is not None and sarvadhatuka_lakara_context(state)


def act(state: State) -> State:
    di = _find_dhatu_for_u(state)
    if di is None:
        return state
    u = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("u")),
        # "anga" too: 6.4.1 aṅgasya adhikāra covers the vikaraṇa-attached
        # stem, not just the bare dhātu — needed so a downstream aṅga-vs-ac
        # boundary rule (6.1.78, when guṇa turns this u into o and a vowel
        # follows) can see this term as the aṅga side of that boundary.
        tags={"anga", "pratyaya", "vikarana", "sarvadhatuka"},
        meta={"upadesha_slp1": "u"},
    )
    state.terms.insert(di + 1, u)
    state.terms[di].meta["3_1_79_u_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.79",
    sutra_type=SutraType.VIDHI,
    text_slp1='tanAdikfYBya uH',
    text_dev='तनादिकृञ्भ्य उः',
    samagra_slp1="karttari sArvaDAtuke tanAdikfYByaH DAtoH paraH u-pratyayaH",
    samagra_dev="कर्त्तरि सार्वधातुके तनादिकृञ्भ्यः धातोः परः उ-प्रत्ययः",
    padaccheda_dev="तनादि-कृञ्भ्यः / उः",
    why_dev="तनादि-गणे कृञ्-आदिभ्यः शप्-अपवादरूपेण उ-विकरणः (कुरुतः)।",
    anuvritti_from=("3.1.68",),
    cond=cond,
    act=act,
    apavada_of=('3.1.68',),
)

register_sutra(SUTRA)

