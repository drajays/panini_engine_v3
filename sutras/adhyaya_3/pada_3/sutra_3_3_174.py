"""
3.3.174  क्तिच्क्तौ च संज्ञायाम्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=303174
- Kāśikā: क्तिच्क्तौ च संज्ञायाम् (क्तिच्-प्रत्ययः — कण्डूति इत्यादि)
- Cross-validation: tests/unit/test_kaNDUti_ktic_vareya_yalopa_lesson.py;
  tests/unit/test_vAyavaH.py (*uṇ* path, ``uR_recipe``)

Engine:
  • ``state.meta['uR_recipe']`` + ``vA`` dhātu → append ``uR`` (*prakriya_24*).
  • ``state.meta['ktic_3_3_174_recipe']`` + single ``dhātu`` → append ``ktic``
    (*kṅiti*, *cit*) for *kaṇḍūti* / **6.4.48** / **6.1.66** lessons.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site_uR(state: State) -> bool:
    if not state.meta.get("uR_recipe"):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    return (t0.meta.get("upadesha_slp1") or "").strip() == "vA"


def _site_ktic(state: State) -> bool:
    if not state.meta.get("ktic_3_3_174_recipe"):
        return False
    if any((t.meta.get("upadesha_slp1") or "").strip() == "ktic" for t in state.terms):
        return False
    if len(state.terms) != 1:
        return False
    return "dhatu" in state.terms[0].tags


def cond(state: State) -> bool:
    return _site_uR(state) or _site_ktic(state)


def act(state: State) -> State:
    if _site_uR(state):
        uR = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("uR")),
            tags={"pratyaya", "upadesha", "krt"},
            meta={"upadesha_slp1": "uR", "prakriya_24_uR_source": True},
        )
        state.terms.append(uR)
        state.meta.pop("uR_recipe", None)
        return state
    if _site_ktic(state):
        ktic = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("ktic")),
            tags={"pratyaya", "upadesha", "krt", "kngiti"},
            meta={"upadesha_slp1": "ktic", "it_markers": {"k", "c"}},
        )
        state.terms.append(ktic)
        state.meta.pop("ktic_3_3_174_recipe", None)
        state.samjna_registry["3.3.174_ktic_samjna"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.174",
    sutra_type=SutraType.VIDHI,
    text_slp1="kticktO ca saMjYAyAm",
    text_dev="क्तिच्क्तौ च संज्ञायाम्",
    padaccheda_dev="क्तिच्-क्तौ / च / संज्ञायाम्",
    why_dev="संज्ञायां क्तिच्-प्रत्ययः (कण्डूति); वा-धातोः उण् (प०२४)।",
    anuvritti_from=("3.1.91",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
