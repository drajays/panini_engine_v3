"""
1.3.12  अनुदात्तङित आत्मनेपदम्  —  PARIBHASHA

*Padaccheda:* *anudātta-ṅit* / *ātmanepadam*.

*Śāstra:* *anudāttet* (ekāc) *dhātu* takes *ātmanepada* in *kartari* (**1.3.12**–**77** block;
**1.3.78** *śeṣa* applies only when this block does not license *parasmaipada*).

*Engine:* ``cond`` reads ``ekac_dhatu`` on the primary *dhātu* *Term* (from dhātupāṭha /
``_build_dhatu_term``), not *puruṣa* / *vacana* (Art. 2).  Sets ``kartari_atmanepada_licensed``
so **1.3.78** does not force *parasmaipada*.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 13012 · अनुदात्तङित आत्मनेपदम्
              padaccheda: अनुदात्तङितः · आत्मनेपदम्
  Source #2 — Kāśikā 1.3.12 udāharaṇa:
                अनुदात्तेद्भ्यः — आस् — आस्ते
                वस् — वस्ते
                ङिद्भ्यः खल्वपि — षूङ् — सूते
  Gloss (sa) — अनुदात्त-ङितः आत्मनेपदम्।
  Cross-check — surface pinned by: tests/unit/test_prakriya_integrity.py, tests/unit/test_tinanta_pathati_lat.py
  Reference record: sutra_ref_out/1_3_12.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import ATMANE_LICENSE_META_KEY


def _primary_dhatu(state: State) -> Term | None:
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    """अनुदात्तङित आत्मनेपदम्: the dhātu's own it-svara/ṅit makes it ātmanepadī. The lexical fact (the dhātupāṭha's
    pada, which *is* that anubandha) is carried on the dhātu Term as ``kartari_atmanepada_licensed is True``; this rule
    is where it takes effect (``pada``, the gate) — once. An ubhayapadī root (``"ubhaya"``) is 1.3.72/1.3.78's."""
    d = _primary_dhatu(state)
    if d is None or d.meta.get("1_3_12_done"):
        return False
    return d.meta.get(ATMANE_LICENSE_META_KEY) is True


def act(state: State) -> State:
    d = _primary_dhatu(state)
    if d is None:
        return state
    d.meta["1_3_12_done"] = True
    state.meta["pada"] = "Atmanepada"
    state.paribhasha_gates["1.3.12_anudatta_nit_atmanepada"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.12",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='anudAttaNita Atmanepadam',
    text_dev='अनुदात्तङित आत्मनेपदम्',
    samagra_slp1="anudAttaNitaH Atmanepadam",
    samagra_dev="अनुदात्तङितः आत्मनेपदम्",
    padaccheda_dev="अनुदात्त-ङित् / आत्मनेपदम्",
    why_dev="अनुदात्तेत्-धातोः कर्तरि आत्मनेपदम्; १.३.७८-शेष-परस्मैपदं न भवति।",
    anuvritti_from=("1.3.14",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
