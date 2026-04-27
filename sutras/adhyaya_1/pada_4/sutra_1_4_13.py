"""
1.4.13  यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्  —  SAMJNA

The *ādi* of what follows from a pratyaya-ādeśa whose cause is a given
element — that element is called *aṅga* with respect to that affix.

Operational: when a *dhātu* ``Term`` precedes a *pratyaya* ``Term``, the *dhātu*
is the *aṅga* (registry *…_anga*).  **Case B:** *taddhite* (``pipelines/taddhita_salIya``) —
*prakriti* is *aṅga* for the *taddhita* *pratyaya* when ``prakriya_sAlIya``; stem
is already *aṅga*-*tag*ged, **1.4.13** registers the *aṅga* relation in the
same *registry* *slot*.  **Case C:** ``prakriya_itika_phak`` (``pipelines/taddhita_itika_etikAyana``) —
same pattern as Case B.  **Case D:** ``prakriya_matup_asti`` — *go* + *matup* style
``[prātipadika, taddhita]`` after **2.4.71** *luk* (``pipelines/gomAn_prathamA_go_matup``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    if state.samjna_registry.get(("1.4.13_anga", 0)) is not None:
        return False
    for j in range(1, len(state.terms)):
        t1 = state.terms[j]
        if "pratyaya" not in t1.tags:
            continue
        t0 = state.terms[j - 1]
        if "dhatu" in t0.tags:
            return True
        # *śālīya* taddhita: *aṅga* = *prakriti* (not *dhātu*) *nimitta* of *taddhita*.
        if (
            state.meta.get("prakriya_sAlIya")
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "dhatu" not in t0.tags
            and "taddhita" in t1.tags
        ):
            return True
        if (
            state.meta.get("prakriya_itika_phak")
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "dhatu" not in t0.tags
            and "taddhita" in t1.tags
        ):
            return True
        if (
            state.meta.get("prakriya_matup_asti")
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "dhatu" not in t0.tags
            and "taddhita" in t1.tags
        ):
            return True
    return False


def act(state: State) -> State:
    state.samjna_registry[("1.4.13_anga", 0)] = frozenset({"active"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.13",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "yasmAt pratyayavidhis tadAdi pratyaye~Nga",
    text_dev       = "यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्",
    padaccheda_dev = "यस्मात् प्रत्यय-विधिः तदादि प्रत्यये अङ्गम्",
    why_dev        = "प्रत्यय-विधेर् यस्मात् तदादि प्रत्यये यत् तद् अङ्गम्।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
