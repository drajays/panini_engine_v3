"""
1.2.51  लुपि युक्तवद् व्यक्तिवचने  —  SAMJNA (narrow ``prakriya_45`` / ``prakriya_46``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=10251):** *lupi yuktavad vyaktivacane* — when an affix is
removed by *luk*, the derived expression keeps the *liṅga* and *vacana* behaviour “as if” the
affix were still present (*yuktavat*), keyed to the *vyakti* (here: gender/number alignment with
the *prakṛti*).

• **prakriya_45** (**पञ्चालाः** *janapada* ``…/separated_prakriyas/prakriya_45_*.json``):
  ``prakriya_45_1_2_51_arm`` + ``meta['prakriya_45_lupi_yuktavad_note']`` +
  ``meta['prakriya_45_janapade_luk_context_note']`` (recipe marks **4.2.81** *janapade lup* backdrop)
  + witness ``Term`` tagged ``prakriya_45_paYcAla_demo`` →
  ``samjna_registry['1.2.51_lupi_yuktavad_prakriya_45']``.

• **prakriya_46** (**गोदौ ग्रामः** ``…/separated_prakriyas/prakriya_46_*.json``): after **4.2.70**
*adūrabhava* + **4.2.82** *varaṇādibhyaś ca* (*luk* of *aṇ*, machine index — OCR often says “4.2.81”):
  ``prakriya_46_1_2_51_arm`` + ``meta['prakriya_46_lupi_yuktavad_note']`` +
  ``meta['prakriya_46_varaNAdi_luk_context_note']`` + witness ``prakriya_46_godau_demo`` →
  ``samjna_registry['1.2.51_lupi_yuktavad_prakriya_46']``.

No ``varṇa`` mutation (recipe gate only); **6.1.88** *vṛddhi* etc. are out of scope for these demos.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site_prakriya_45(state: State) -> bool:
    if not state.meta.get("prakriya_45_1_2_51_arm"):
        return False
    if not state.meta.get("prakriya_45_lupi_yuktavad_note"):
        return False
    if not state.meta.get("prakriya_45_janapade_luk_context_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_45_paYcAla_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("1.2.51_lupi_yuktavad_prakriya_45"):
        return False
    return True


def _site_prakriya_46(state: State) -> bool:
    if not state.meta.get("prakriya_46_1_2_51_arm"):
        return False
    if not state.meta.get("prakriya_46_lupi_yuktavad_note"):
        return False
    if not state.meta.get("prakriya_46_varaNAdi_luk_context_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_46_godau_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("1.2.51_lupi_yuktavad_prakriya_46"):
        return False
    return True


def cond(state: State) -> bool:
    return _site_prakriya_45(state) or _site_prakriya_46(state)


def act(state: State) -> State:
    if _site_prakriya_45(state):
        state.samjna_registry["1.2.51_lupi_yuktavad_prakriya_45"] = True
        state.meta.pop("prakriya_45_1_2_51_arm", None)
        return state
    if _site_prakriya_46(state):
        state.samjna_registry["1.2.51_lupi_yuktavad_prakriya_46"] = True
        state.meta.pop("prakriya_46_1_2_51_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.51",
    sutra_type=SutraType.SAMJNA,
    text_slp1="lupi yuktavad vyaktivacane",
    text_dev="लुपि युक्तवद् व्यक्तिवचने",
    padaccheda_dev="लुपि / युक्तवत् / व्यक्ति-वचने",
    why_dev="लुपि लिङ्ग-वचने प्रकृतिवत् (*prakriya_45* **पञ्चालाः**, *prakriya_46* **गोदौ**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
