"""
1.4.101  तिङः त्रीणि त्रीणि प्रथम-मध्यम-उत्तमाः  —  SAMJNA

*Padaccheda:* *tiṅaḥ* (ṣaṣṭhī), *trīṇi trīṇi* (dva prathamā *bahuvacanam*), *prathama-madhyam-ottamāḥ* (pl.).

*Anuvṛtti* **1.4.1** *ā kaḍārād ekā sañjñā*.

*Śāstra:* the eighteen *tiṅ* *ādeśa* (**3.4.78**) in order form six successive triples; each *triplet* is
named ( *prathama* / *madhyama* *uttama* in the *parasmaipada* and again in the *ātmanepada* *navaka* ).

*Engine (CONSTITUTION Art. 2):* ``cond`` only delegates to ``terms_needing_tin_101_tripartite`` — *no* read of
*paradigm* *meta* keys.  *Tripartite* classes are three distinguishable *tags* (A/B/C in code) mapped to
*prathama* / *madhyama* / *uttama* in the module docstring.  *Registry* R2: ``1.4.101_tiN_tripartite_abc`` holds the
*triplet* of tag *names* in *śāstrīya* order.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_4.tin_tripartite_1_4_101 import (
    TIN_101_ALL_TRIPARTITE_TAGS,
    TIN_101_TRIPARTITE,
    terms_needing_tin_101_tripartite,
    tripartite_101_tag_for_tin_adesha,
)


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
    text_slp1      = "tiNgaH trIRi trIRi prathama-madhyama-uttamAH",
    text_dev       = "तिङः त्रीणि त्रीणि प्रथम-मध्यम-उत्तमाः (एकसंज्ञाधिकारे)",
    padaccheda_dev = "तिङ् / त्रीணि-त्रीणि (द्वि-वारम) / प्रथम-मध्यम-उत्तमाः (प्रथमा-बहु)",
    why_dev        = (
        "तिङादेश-अष्टादशानां क्रमेण षड्-त्र्यायाः, प्रथम-मध्यम-उत्तम-संज्ञा (पर-आत्म-नव-नव)।"
    ),
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
