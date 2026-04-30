"""
8.3.41  इदुदुपधस्य चाप्रत्ययस्य  —  VIDHI (narrow ``prakriya_40``)

**Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com ``data.txt`` i=80341):**
*idudupadhasya cāpratyayasya* — extends murdhanya / ṣatva contexts (Tripāḍī).

Narrow v3 (**निष्कोशाम्बिः** ``…/separated_prakriyas/prakriya_40_*.json`` ``panini_engine_pipeline``):
  After **8.3.15** has turned ``ru`` into visarga (*ḥ*), the sequence ``निः`` + ``क…``
  becomes ``निष्`` + ``क…`` — visarga is replaced by retroflex ``ṣ`` before a ``ka``-varga
  onset (glass-box: ``H`` + ``k`` within one ``Term``).

Engine slice:
  • ``state.meta['prakriya_40_8_3_41_arm'] == True``
  • witness ``Term`` tagged ``prakriya_40_nihka_witness``
  • scan varṇa tape for ``H`` immediately followed by ``k`` (narrow ``ka``-varga anchor only).

Tripāḍī: ``state.tripadi_zone`` must be True (**8.2.1**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    if not state.tripadi_zone:
        return None
    if not state.meta.get("prakriya_40_8_3_41_arm"):
        return None
    if state.meta.get("prakriya_40_8_3_41_done"):
        return None
    for t in state.terms:
        if "prakriya_40_nihka_witness" not in t.tags:
            continue
        vns = t.varnas
        for i in range(len(vns) - 1):
            if vns[i].slp1 != "H":
                continue
            if vns[i + 1].slp1 != "k":
                continue
            return t, i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    t, i = hit
    t.varnas[i] = mk("z")
    state.meta["prakriya_40_8_3_41_arm"] = False
    state.meta["prakriya_40_8_3_41_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.41",
    sutra_type=SutraType.VIDHI,
    text_slp1="idudupadasya cApratyayasya",
    text_dev="इदुदुपधस्य चाप्रत्ययस्य",
    padaccheda_dev="इदुदुपधस्य / च / अप्रत्ययस्य",
    why_dev="निः-क-प्रसङ्गे विसर्गस्य मूर्धन्य ष् (*prakriya_40*, **निष्कोशाम्बिः** डेमो)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
