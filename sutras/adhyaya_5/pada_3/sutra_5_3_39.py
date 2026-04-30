"""
5.3.39  पूर्वाधरावराणामसि पुरधवां चैषाम्  —  VIDHI (narrow)

**Pāṭha:** *pūrvādhara-varāṇām asi puradhavāṃ caiṣām* — with **asi**, the stems
*pūrva*, *adhara*, *vara* (and cognates) take **pur-**, **adhar-**, **var-**
substitutes.

Narrow v3 (``prakriya_19`` *puras* leg):
  • ``state.meta['prakriya_19_puras_5_3_39_arm']`` and exactly three ``Term``s:
    *aṅga* ``pUrva`` + internal ``Ni`` *sup* + ``asi`` *taddhita* with
    ``asarva_vibhakti_taddhita`` (``1.1.38`` meta).
  • ``act`` — rewrite the first ``Term``’s *upadeśa* surface to ``pur``;
    clear the arm.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA


def _eligible(state: State) -> bool:
    if not state.meta.get("prakriya_19_puras_5_3_39_arm"):
        return False
    if len(state.terms) != 3:
        return False
    t0, t1, t2 = state.terms
    if "anga" not in t0.tags or "prātipadika" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != "pUrva":
        return False
    if "sup" not in t1.tags or "pratyaya" not in t1.tags:
        return False
    if (t1.meta.get("upadesha_slp1") or "").strip() != "Ni":
        return False
    if "taddhita" not in t2.tags or "pratyaya" not in t2.tags:
        return False
    if (t2.meta.get("upadesha_slp1") or "").strip() != "asi":
        return False
    if t2.meta.get(META_ASARVA_VIBHAKTI_TADDHITA) is not True:
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    t0 = state.terms[0]
    t0.varnas = list(parse_slp1_upadesha_sequence("pur"))
    t0.meta["upadesha_slp1"] = "pur"
    state.meta.pop("prakriya_19_puras_5_3_39_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.3.39",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "pUrvA-dharA-varARAm asi pura-dhavAM cEzAm",
    text_dev       = "पूर्वाधरावराणामसि पुरधवां चैषाम्",
    padaccheda_dev = "पूर्व-अधर-अवराणाम् / असि / पुर-धवां / च / एषाम्",
    why_dev        = "असि-प्रत्यये पूर्वादीनां पुरादेशः (प्रक्रिया-१९)।",
    anuvritti_from = ("5.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
