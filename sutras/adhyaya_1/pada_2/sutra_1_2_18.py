"""
1.2.18  न क्त्वा सेट्  —  NIYAMA

Sources consulted:
- ashtadhyayi.com data.txt row i=12018 · anuvṛtti कित् (1.2.5 ff.)
- Kāśikā: "क्त्वाप्रत्ययः सेट् न किद् भवति। देवित्वा। वर्तित्वा।"
  pratyudāharaṇa: "सेडिति किम्? कृत्वा। हृत्वा। क्त्वाग्रहणं किम्? निगृहीतिः।"
- Cross-validation: tests/regression/test_kngit_from_it_samjna.py (देवित्वा, वर्तित्वा take guṇa; कृत्वा stays kit)

A ktvā that has taken iṭ (7.2.35) is not kit: the kṅit locus the it-saṃjñā gave it (1.3.8 k → ``kngiti``, ``it:kit``)
is withdrawn, so 1.1.5 no longer stops guṇa (7.3.84, 7.3.86). The it-record itself stays in the term's history.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State) -> int | None:
    """A seṭ ktvā that is still kit."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or t.meta.get("1_2_18_akit"):
            continue
        if (t.meta.get("upadesha_slp1_original") or t.meta.get("upadesha_slp1") or "").strip() != "ktvA":
            continue
        set_ = t.meta.get("it_agama_7_2_35_done") or (t.varnas and "it_agama" in t.varnas[0].tags)
        if set_ and {"kngiti", "it:kit", "kit"} & t.tags:
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags -= {"kngiti", "it:kit", "kit"}
    state.terms[i].meta["1_2_18_akit"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.18",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = 'na ktvA sew',
    text_dev              = 'न क्त्वा सेट्',
    samagra_slp1          = "na ktvA sew kit",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न क्त्वा सेट् कित्",
    padaccheda_dev        = "न / क्त्वा / सेट्",
    why_dev               = "सेट् क्त्वाप्रत्ययः न कित् (देवित्वा, वर्तित्वा)।",
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
