"""
2.1.2  सुबामन्त्रिते पराङ्गवत् स्वरे  —  SAMJNA (narrow *glass-box* for ``prakriya_28``)

**Pāṭha (Kāśikā):** *subāmantite parāṅgavat svare* — a *subanta* (nominal) that is
also *āmantrita* (vocative) is treated *parāṅgavat* to the *aṅga* of the *para*
(following) *pada* for accent purposes (*samhitā* · *ākārṣṭ* interpretation).

Narrow v3 (``prakriya_28``, Vedic **मेघातिथे मन्महे**):
  • Two ``Term``s: vocative ``meGAtithe`` + finite ``manmahe`` (recipe arms +
    tags — no *vibhakti* reads in ``cond``).
  • Registers ``samjna_registry['2.1.2_subAmantrite_parA~ggavat_28']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_28_2_1_2_arm"):
        return False
    if len(state.terms) < 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if "prakriya_28_subanta_vocative" not in t0.tags:
        return False
    if "prakriya_28_following_tin" not in t1.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "meGAtithe":
        return False
    if t1.meta.get("upadesha_slp1") != "manmahe":
        return False
    if "2.1.2_subAmantrite_parA~ggavat_28" in state.samjna_registry:
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["2.1.2_subAmantrite_parA~ggavat_28"] = frozenset({"meGAtithe", "manmahe"})
    state.meta.pop("prakriya_28_2_1_2_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.1.2",
    sutra_type=SutraType.SAMJNA,
    text_slp1="subAmantrite parA~ggavat svare",
    text_dev="सुबामन्त्रिते पराङ्गवत् स्वरे",
    padaccheda_dev="सुबान्तम् आमन्त्रिते / पराङ्गवत् / स्वरे",
    why_dev="आमन्त्रित-सुबन्तस्य पराङ्गवत् स्वर-संज्ञा (*prakriya_28*, मेघातिथे-मन्महे)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
