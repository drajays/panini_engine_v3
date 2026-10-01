"""
1.3.29  समो गम्यृच्छिप्रच्छिस्वरत्यर्तिश्रुविदिभ्यः  —  SAMJNA (narrow demo)

Narrow demo (संगसीष्ट / ``saGgasIzwa``):
  When ``sam``‑pūrvā *gam* participates in kartāri *ātmanepada* licences in this repo,
  mark the neighbouring *dhātu* ``gam`` Term with ``ātmanepada_licensed_1_3_29``.

Engine:
  - recipe arms via ``state.meta['samo_recipe']``.
  - requires contiguous ``[ Term tagged upasarga with surface ``sam`` ][ dhātu
    गमॢँ (``upadesha_slp1=='gamx~'``) ]``.

Sources consulted:
- ashtadhyayi.com data.txt row i=13029 · समः गमि-ऋच्छि-प्रच्छि-स्वरति-अर्ति-श्रु-विदिभ्यः
  (anuvṛtti: आत्मनेपदम् 1.3.12, अकर्मकात् 1.3.26)
- Kāśikā: "संगच्छते, समृच्छते, संपृच्छते, संस्वरते"
- Cross-validation: regression test tests/unit/test_saGgasIzwa_sam_gam_ashir_ling.py
  (सङ्गसीष्ट)
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GAM_UPADESHA = frozenset({"gamx~"})   # गमॢँ गतौ (01.1137)


def cond(state: State) -> bool:
    if not state.meta.get("samo_recipe"):
        return False
    for i in range(len(state.terms) - 1):
        u, dh = state.terms[i], state.terms[i + 1]
        if "upasarga" not in u.tags:
            continue
        if "".join(v.slp1 for v in u.varnas) != "sam":
            continue
        if "dhatu" not in dh.tags:
            continue
        if (dh.meta.get("upadesha_slp1") or "").strip() not in _GAM_UPADESHA:
            continue
        if dh.meta.get("1_3_29_done"):
            return False
        return True
    return False


def act(state: State) -> State:
    if not cond(state):
        return state
    for i in range(len(state.terms) - 1):
        u, dh = state.terms[i], state.terms[i + 1]
        if (
            "upasarga" in u.tags
            and "".join(v.slp1 for v in u.varnas) == "sam"
            and (dh.meta.get("upadesha_slp1") or "").strip() in _GAM_UPADESHA
        ):
            dh.tags.add("ātmanepada_licensed_1_3_29")
            dh.meta["1_3_29_done"] = True
            state.samjna_registry["1.3.29_samo_gam_tag"] = True
            state.meta["samo_recipe"] = False
            break
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.29",
    sutra_type=SutraType.VIDHI,
    text_slp1='samo gamyfcCipracCisvaratyartiSruvidiByaH',
    text_dev='समो गम्यृच्छिप्रच्छिस्वरत्यर्तिश्रुविदिभ्यः',
    padaccheda_dev="समः / गमेः …",
    why_dev=(
        "\"सम्\"पूर्वात् धातुर् \"\"गम्\" आत्मनेपद-पथे जातुः (आशिषि; डेमो-संज्ञा सूत्रस्थ।"
    ),
    anuvritti_from=("1.3.27",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
