"""
1.2.17  (narrow demo: *stAdgor ic ca* spine for **gha** + luṅ **sic** → **इच्**)

After **gha** (**1.1.20**) in luṅ, **sic** (**सिच्**, modelled as ``s`` after **3.1.44** ITs) is
substituted by **इच्** — phonemic ``i`` + hal **c** (it). Re-tag **``upadesha``** so
**1.3.3**/**1.3.9** can drop ``c``, and mark **kṅiti** via ``kngiti`` for **6.4.64**.

Demo path for *da~da* + luṅ: ``sic`` Term still has ``upadesha_slp1='sic'`` for lookup;
recipe arms ``meta['1_2_17_ghu_sici_ic_arm']``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 12017 · स्था घ्वोरिच्च
              padaccheda: स्था-घ्वोः · इत् · च
              anuvṛtti:   12005: कित् | 12009: झल् | 12011: आत्मनेपदेषु | 12014: सिच्
  Source #2 — Kāśikā 1.2.17 udāharaṇa:
                उपास्थित
                घुसंज्ञकानाम् — अदित
                अधित
  Gloss (sa) — स्थाधातोः घुसंज्ञकेभ्यश्च सिचि आत्मनेपदे कित्प्रकरणे झल्त्वम्।
  Cross-check — surface pinned by: tests/unit/test_adita_luN_dAda_ghu.py
  Reference record: sutra_ref_out/1_2_17.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_20 import GHU_DHATU_UPADESHA_SLP1, ghu_samjna_is_registered


def _primary_dhatu_upadesha(state: State) -> str:
    for t in state.terms:
        if "dhatu" in t.tags:
            return (t.meta.get("upadesha_slp1") or "").strip()
    return ""


def _loop_site(state: State):
    """The loop's reading: ātmanepada luṅ, sic after sthā or a ghu root → ic (अधित, अदित, उपास्थित); no registry/arm flag."""
    if any("parasmaipada" in t.tags for t in state.terms):
        return None
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or "abhyasa" in dh.tags:
            continue
        up = (dh.meta.get("upadesha_slp1") or "").strip()
        if up not in ("zWA", "quDAY", "qudAY") and up not in GHU_DHATU_UPADESHA_SLP1:
            continue
        nxt = state.terms[i + 1]
        if nxt.kind == "pratyaya" and (nxt.meta.get("upadesha_slp1") or "").strip() == "sic" and not nxt.meta.get("1_2_17_ic_adesha_done") \
                and any("tin_adesha_3_4_78" in u.tags and (u.meta.get("source_lakara_upadesha") or "").strip() == "luG" for u in state.terms):
            return nxt
    return None


def _find_sic_term(state: State):
    if (hit := _loop_site(state)) is not None:
        return hit
    if not ghu_samjna_is_registered(state):
        return None
    up0 = _primary_dhatu_upadesha(state)
    if up0 not in GHU_DHATU_UPADESHA_SLP1:
        return None
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        if t.meta.get("1_2_17_ic_adesha_done"):
            continue
        return t
    return None


def cond(state: State) -> bool:
    return _find_sic_term(state) is not None


def act(state: State) -> State:
    t = _find_sic_term(state)
    if t is None:
        return state
    if _loop_site(state) is t:
        # ātmanepada luṅ: the ā of sthā/ghu becomes i (ic) and sic is kit: अधित (8.2.26 drops s before t), अधिषाताम्
        dh = state.terms[state.terms.index(t) - 1]
        if dh.varnas and dh.varnas[-1].slp1 == "A":
            old = dh.varnas[-1]
            dh.varnas[-1] = mk("i", *((old.tags - {"mula_dhatu_v"}) | {"dhatu_adesha_v"}))
        t.tags.add("kngiti")
        t.meta["1_2_17_ic_adesha_done"] = True
        return state
    t.varnas = parse_slp1_upadesha_sequence("ic")
    t.meta["upadesha_slp1"] = "ic"
    t.tags.add("upadesha")
    t.tags.add("kngiti")
    t.meta["1_2_17_ic_adesha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.17",
    sutra_type=SutraType.ATIDESHA,
    text_slp1='sTA Gvoricca',
    text_dev='स्था घ्वोरिच्च',
    padaccheda_dev="स्थाद्वोः / रिच्च",
    why_dev="गु-स्थानिके सिचोऽपेक्षया इच्संनिधानं (लुङ्-डेमो: सिच् आदेशश्च)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
