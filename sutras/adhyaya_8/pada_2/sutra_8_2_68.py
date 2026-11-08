"""
8.2.68  अहन्  —  VIDHI

Padaccheda: अहन् (लुप्तषष्ठ्यन्तनिर्देशः)

अहन् (8.2.68)
Pāṭha: ashtadhyayi.com data.txt row i=82068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk, HAL


def _flat(varnas) -> str:
    return "".join(v.slp1 for v in varnas)


def _site(state: State):
    """(term index, varṇa index) of the n of the pada ahan, which becomes ru (ahobhiḥ, ahobhyām, ahaḥ; Kāśikā 8.2.68). Not 8.2.7's: that sūtra leaves ahan's n alone."""
    if not state.tripadi_zone and state.phase != "tripadi" and len(state.terms) < 2:
        return None
    for i, t in enumerate(state.terms):
        if "an_pratipadika" in t.tags and t.varnas and _flat(t.varnas) == "ahan":      # premerge: ahan + a hal-initial sup, or alone (su lupta)
            nxt = state.terms[i + 1] if i + 1 < len(state.terms) else None
            if nxt is None or not nxt.varnas or nxt.varnas[0].slp1 in HAL:
                return i, len(t.varnas) - 1
        if len(state.terms) == 1 and "pada" in t.tags:                                  # merged pada: the prātipadika's final n is tagged
            vs = t.varnas
            for k in range(len(vs) - 1):
                if "pratipadika_anta_v" in vs[k].tags and vs[k].slp1 == "n" and _flat(vs[:k + 1]) == "ahan" and vs[k + 1].slp1 in HAL:
                    return i, k
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    ti, vi = _site(state)
    ru = mk("r")
    ru.tags.add("ru_intermediate")
    state.terms[ti].varnas[vi] = ru
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ahan",
    text_dev              = "अहन्",
    samagra_slp1          = "padasya ahnaH ru~H",
    samagra_dev           = "पदस्य अह्नः रुँः",
    padaccheda_dev        = "अहन् (लुप्तषष्ठ्यन्तनिर्देशः)",
    why_dev               = "(सूत्रम् 8.2.68) अहन्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
