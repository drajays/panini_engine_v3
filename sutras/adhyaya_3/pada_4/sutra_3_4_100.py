"""
3.4.100  इतश्च  —  VIDHI (laṅ/luṅ/lṛṅ: drop final 'i' of tiṅ ādeśa)

Drops the final 'i' of a tiṅ ādeśa in laṅ / luṅ / lṛṅ contexts:
  tip→ti → t,  sip→si → s,  jhi → jh  (then 7.1.3 converts jh→ant for 3pl).

Note: mip→mi is handled by 3.4.101 (apavāda); 3.4.100 naturally skips 'mi'
when 3.4.101 has already converted it to 'am' (varnas end in 'm' not 'i').

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34100 · इतश्च
              padaccheda: इतः च
              anuvṛtti:   34077: लस्य | 34097: लोपः | 34099: नित्यम् ङितः
  Source #2 — Kāśikā 3.4.100 udāharaṇa:
                ङिल्लकारसंबन्धिन इकारस्य नित्यं लोपो भवति
                अपचत्
                अपाक्षीत्
  Cross-check — surface pinned by: tests/unit/test_avadhIt_han_lun_ekavacana.py, tests/unit/test_tinanta_abhavat_lang.py, tests/unit/test_tinanta_bhavatu_lot.py
  Reference record: sutra_ref_out/3_4_100.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.nimitta_predicates import acts_as_ngit_lakara
from phonology import mk


# 1.4.100 तङानावात्मनेपदम् — the nine taṅ ādeśas (upadeśa identity).
_TAN = frozenset({"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG", "mahiN"})   # engine spells ṅ-it G (laG, mahiG)


def _find_i_final_tin(state: State):
    """Find a tiṅ ādeśa term ending in 'i' in laṅ/luṅ/lṛṅ context."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if not acts_as_ngit_lakara(t):      # ṅit lakāra — or loṭ by 3.4.85 (3.4.86 then wins as apavāda)
            continue
        # The "i" is the one of the ādeśa 3.4.78 gave; hi (3.4.87) and ni (3.4.89) are ādeśas of their own.
        if (t.meta.get("upadesha_slp1") or "").strip() in {"hi", "ni"}:
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_100_itasca_done"):
            continue
        # परस्मैपदेषु (from 3.4.97): ātmanepada iṭ / vahi / mahi keep their i
        # (ऐधे, ऐधावहि — not ऐध, ऐधाव).
        if "atmanepada" in t.tags or (t.meta.get("upadesha_slp1") or "").strip() in _TAN:
            continue
        vs = t.varnas
        if not vs or vs[-1].slp1 != "i":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_i_final_tin(state) is not None


def act(state: State) -> State:
    i = _find_i_final_tin(state)
    if i is None:
        return state
    t = state.terms[i]
    # Drop the final 'i' varna.
    if t.varnas and t.varnas[-1].slp1 == "i":
        del t.varnas[-1]
    t.meta["3_4_100_itasca_done"] = True
    # The residue (jh of jhi, s of sip, t of tip) is an ādeśa's body, not an upadeśa: 1.3.3 must not read
    # its final consonant as a halantyam it (as 3.4.101 already ensures for its own output).
    t.tags.discard("upadesha")
    # Lṛṅ ṛ-dhātu (P019 / vftu~): ``sy`` + ``t`` needs intervening ``a`` (*avartsyat*).
    if i > 0 and (state.meta.get("lakara") or "").strip() == "lRG":
        prev = state.terms[i - 1]
        if (prev.meta.get("upadesha_slp1") or "").strip() == "sy":
            if not state.meta.get("lrng_ṛ_tin_a_done"):
                ins = Term(
                    kind="pratyaya",
                    varnas=[mk("a")],
                    tags={"pratyaya"},
                    meta={"upadesha_slp1": "a"},
                )
                state.terms.insert(i, ins)
                state.meta["lrng_ṛ_tin_a_done"] = True
    # Legacy demo flag (until P019 pipeline deleted).
    if state.meta.get("corrected_v2_P019_demo") and i > 0:
        prev = state.terms[i - 1]
        if (prev.meta.get("upadesha_slp1") or "").strip() == "sy":
            if not state.meta.get("lrng_ṛ_tin_a_done"):
                ins = Term(
                    kind="pratyaya",
                    varnas=[mk("a")],
                    tags={"pratyaya"},
                    meta={"upadesha_slp1": "a"},
                )
                state.terms.insert(i, ins)
                state.meta["lrng_ṛ_tin_a_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.100",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'itaSca',
    text_dev       = 'इतश्च',
    samagra_slp1   = "NitaH parasmEpadezu itaH lopaH",
    samagra_dev    = "ङितः परस्मैपदेषु इतः लोपः",
    padaccheda_dev = "इतः / च",
    why_dev        = (
        "लङ्/लुङ्/लृङ्-प्रक्रियायां तिङ्-अन्तस्थ इकारस्य लोपः "
        "(ति→त्, सि→स्, झि→झ्); लङि: ७.१.३-पूर्वं झि→झ् → अन्त्।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

