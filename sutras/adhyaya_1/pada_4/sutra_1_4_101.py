"""
1.4.101  तिङस्त्रीणि त्रीणि प्रथममध्यमोत्तमाः  —  SAMJNA

*Padaccheda:* *tiṅaḥ* (ṣaṣṭhī), *trīṇi trīṇi* (dva prathamā *bahuvacanam*), *prathama-madhyam-ottamāḥ* (pl.).

*Anuvṛtti* **1.4.1** *ā kaḍārād ekā sañjñā*.

*Śāstra:* the eighteen *tiṅ* *ādeśa* (**3.4.78**) in order form six successive triples; each *triplet* is
named ( *prathama* / *madhyama* *uttama* in the *parasmaipada* and again in the *ātmanepada* *navaka* ).

*Engine (CONSTITUTION Art. 2):* ``cond`` only delegates to ``terms_needing_tin_101_tripartite`` — *no* read of
*paradigm* *meta* keys.  *Tripartite* classes are three distinguishable *tags* (A/B/C in code) mapped to
*prathama* / *madhyama* / *uttama* in the module docstring.  *Registry* R2: ``1.4.101_tiN_tripartite_abc`` holds the
*triplet* of tag *names* in *śāstrīya* order.
Pāṭha: ashtadhyayi.com data.txt row i=14101 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


# --- helpers of this sūtra (formerly tin_tripartite_1_4_101.py; one sūtra, one file) ---
from typing import Final, Tuple

from engine.state import State, Term

from sutras.adhyaya_3.pada_4.sutra_3_4_78 import TIN_ADESHA_18, TIN_ADESHA_SET

# Distinct *Term* tags (avoid ``'puruṣa'`` as a *meta* key; CONSTITUTION Art. 2 *cond* scan).
TIN_101_TAG_TRIPARTITE_A: Final[str] = "tin_101_tripartite_A"  # प्रथम (first triple in each *pari*)
TIN_101_TAG_TRIPARTITE_B: Final[str] = "tin_101_tripartite_B"  # मध्यम
TIN_101_TAG_TRIPARTITE_C: Final[str] = "tin_101_tripartite_C"  # उत्तम

# Human-readable (trace / UIs): *prathama* = A, *madhyama* = B, *uttama* = C in each block of nine.
TIN_101_TRIPARTITE: Final[Tuple[str, str, str]] = (
    TIN_101_TAG_TRIPARTITE_A,
    TIN_101_TAG_TRIPARTITE_B,
    TIN_101_TAG_TRIPARTITE_C,
)
TIN_101_ALL_TRIPARTITE_TAGS: Final[frozenset[str]] = frozenset(TIN_101_TRIPARTITE)


def _normalise_tin_adesha_form(s: str) -> str:
    t = s.strip()
    if t in TIN_ADESHA_SET:
        return t
    if t.endswith("~") and t[:-1] in TIN_ADESHA_SET:
        return t[:-1]
    return t


def tripartite_101_tag_for_tin_adesha(s: str) -> str | None:
    """Return the *tiṅ* *tripartite* *tag* for a normalised *ādeśa* *upadeśa* string, or *None*."""
    key = _normalise_tin_adesha_form(s)
    if key not in TIN_ADESHA_SET:
        return None
    i = TIN_ADESHA_18.index(key)
    return TIN_101_TRIPARTITE[i // 3 % 3]


def tin_tripartite_101_is_registered(t: Term) -> bool:
    return bool(t.tags & TIN_101_ALL_TRIPARTITE_TAGS)


def terms_needing_tin_101_tripartite(state: State) -> list[Term]:
    out: list[Term] = []
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if tripartite_101_tag_for_tin_adesha(up) is None:
            continue
        if tin_tripartite_101_is_registered(t):
            continue
        out.append(t)
    return out




def cond(state: State) -> bool:
    return bool(terms_needing_tin_101_tripartite(state))


def _apply_tripartite_101(t: Term) -> None:
    t.tags -= TIN_101_ALL_TRIPARTITE_TAGS
    up = (t.meta.get("upadesha_slp1") or "").strip()
    new_tag = tripartite_101_tag_for_tin_adesha(up)
    assert new_tag is not None
    t.tags.add(new_tag)


def act(state: State) -> State:
    pending = terms_needing_tin_101_tripartite(state)
    state.samjna_registry["1.4.101_tiN_tripartite_abc"] = TIN_101_TRIPARTITE
    for t in pending:
        _apply_tripartite_101(t)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.101",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'tiNastrIRi trIRi praTamamaDyamottamAH',
    text_dev       = 'तिङस्त्रीणि त्रीणि प्रथममध्यमोत्तमाः',
    samagra_slp1   = "tiNaH trIRi trIRi praTama-maDyama-uttamAH",
    samagra_dev    = "तिङः त्रीणि त्रीणि प्रथम-मध्यम-उत्तमाः",
    padaccheda_dev = "तिङ् / त्रीணि-त्रीणि (द्वि-वारम) / प्रथम-मध्यम-उत्तमाः (प्रथमा-बहु)",
    why_dev        = (
        "तिङादेश-अष्टादशानां क्रमेण षड्-त्र्यायाः, प्रथम-मध्यम-उत्तम-संज्ञा (पर-आत्म-नव-नव)।"
    ),
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
