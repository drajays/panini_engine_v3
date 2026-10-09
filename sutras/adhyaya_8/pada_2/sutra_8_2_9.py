"""
8.2.9  मादुपधायाश्च मतोर्वोऽयवादिभ्यः  —  VIDHI

Padaccheda: मात् उपधायाः च मतोः वः अ-यव-आदिभ्यः

मादुपधायाश्च मतोर्वोऽयवादिभ्यः (8.2.9)
Pāṭha: ashtadhyayi.com data.txt row i=82009 (Art. 14).
Authority: Kāśikā 8.2.9 (makārānta, makāropadha, avarṇānta, avarṇopadha; ayavādibhyaḥ — yava dalmi ūrmi bhūmi kṛmi kruñcā vaśā drākṣā), SK "kiṃvān, jñānavān … yavamān, bhūmimān".
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import JHAL

_MATUP = "matu~p"


@lru_cache(maxsize=1)
def _yavadi() -> frozenset[str]:
    """The yavādi gaṇa (Gaṇapāṭha under 8.2.9; Kāśikā: yava, dalmi, ūrmi, bhūmi, kṛmi, kruñcā, vaśā, drākṣā …)."""
    path = Path(__file__).parents[3] / "data" / "inputs" / "ganapatha.json"
    return frozenset(json.loads(path.read_text(encoding="utf-8"))["yavAdi_8_2_9"]["words"])


def _matup_after_prakriti(state: State):
    """(index of the matup Term, the prakṛti Term before it) for a matup whose m is still m."""
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "") != _MATUP or not t.varnas or t.varnas[0].slp1 != "m":
            continue
        prev = next((u for u in reversed(state.terms[:i]) if u.varnas), None)
        if prev is not None:
            yield i, prev


def _site(state: State):
    if not state.tripadi_zone:
        return None
    for i, prev in _matup_after_prakriti(state):
        if (prev.meta.get("upadesha_slp1") or "") in _yavadi():          # ayavādibhyaḥ
            continue
        vs = [v.slp1 for v in prev.varnas]
        # mād upadhāyāś ca — Kāśikā: makārānta, makāropadha, avarṇānta, avarṇopadha
        if vs[-1] in "maA" or (len(vs) > 1 and vs[-2] in "maA"):
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is not None:
        state.terms[i].varnas[0] = mk("v")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = 'mAdupaDAyASca matorvoyavAdiByaH',
    text_dev              = 'मादुपधायाश्च मतोर्वोऽयवादिभ्यः',
    samagra_slp1          = "padasya pUrvatrAsidDam mAt upaDAyAH ca matoH vaH ayavAdiByaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् मात् उपधायाः च मतोः वः अयवादिभ्यः",
    padaccheda_dev        = "मात् उपधायाः च मतोः वः अ-यव-आदिभ्यः",
    why_dev               = "(सूत्रम् 8.2.9) मादुपधायाश्च मतोर्वोऽयवादिभ्यः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
