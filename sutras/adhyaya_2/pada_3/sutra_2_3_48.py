"""
2.3.48  सामन्त्रितम्  —  SAMJNA (narrow *glass-box*)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=23048):** *sāmantritam* — technical name
for the *sambuddhi* *prayoga* (vocative) shape under discussion.

Engine:
  • ``prakriya_26`` — ``indra`` vocative (``prakriya_26_2_3_48_arm``).
  • ``prakriya_29`` — ``gaurAvaskandin`` vocative accent demo (``prakriya_29_2_3_48_arm``).
  • ``prakriya_30`` — ``maGavan`` vocative (**8.1.19** spine; ``prakriya_30_2_3_48_arm``).
  • ``prakriya_32`` — ``EdaviDa`` + ``jaWilaka`` + ``aDyApaka`` tri-vocative phrase
    (``prakriya_32_2_3_48_arm``).
  • ``prakriya_34`` — ``aDyApaka`` + ``kv`` (``prakriya_34_2_3_48_arm``).

``cond`` does not read *vibhakti* coordinates.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site_26(state: State) -> bool:
    if not state.meta.get("prakriya_26_2_3_48_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "sambuddhi_prayoga" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "indra":
        return False
    if "sAmantrita" in t0.tags:
        return False
    return True


def _site_29(state: State) -> bool:
    if not state.meta.get("prakriya_29_2_3_48_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "sambuddhi_prayoga" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "gaurAvaskandin":
        return False
    if "sAmantrita" in t0.tags:
        return False
    return True


def _site_30(state: State) -> bool:
    if not state.meta.get("prakriya_30_2_3_48_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "sambuddhi_prayoga" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "maGavan":
        return False
    if "sAmantrita" in t0.tags:
        return False
    return True


def _site_32(state: State) -> bool:
    if not state.meta.get("prakriya_32_2_3_48_arm"):
        return False
    if len(state.terms) != 3:
        return False
    ups = [state.terms[i].meta.get("upadesha_slp1") for i in range(3)]
    if ups != ["EdaviDa", "jaWilaka", "aDyApaka"]:
        return False
    for t in state.terms:
        if "sambuddhi_prayoga" not in t.tags:
            return False
        if "prakriya_32_tri_vocative_demo" not in t.tags:
            return False
        if "sAmantrita" in t.tags:
            return False
    return True


def _site_34(state: State) -> bool:
    if not state.meta.get("prakriya_34_2_3_48_arm"):
        return False
    if len(state.terms) != 2:
        return False
    t0, t1 = state.terms[0], state.terms[1]
    if "sambuddhi_prayoga" not in t0.tags:
        return False
    if "prakriya_34_aDyApaka_kv_demo" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "aDyApaka":
        return False
    if "prakriya_34_kv_interrogative_demo" not in t1.tags:
        return False
    if t1.meta.get("upadesha_slp1") != "kv":
        return False
    if "sAmantrita" in t0.tags:
        return False
    return True


def cond(state: State) -> bool:
    return (
        _site_26(state)
        or _site_29(state)
        or _site_30(state)
        or _site_32(state)
        or _site_34(state)
    )


def act(state: State) -> State:
    if _site_32(state):
        for t in state.terms:
            t.tags.add("sAmantrita")
        state.samjna_registry["2.3.48_sAmantrita_triplet_prakriya_32"] = True
        state.meta.pop("prakriya_32_2_3_48_arm", None)
        return state
    if _site_34(state):
        state.terms[0].tags.add("sAmantrita")
        state.samjna_registry["2.3.48_sAmantrita_aDyApaka_prakriya_34"] = True
        state.meta.pop("prakriya_34_2_3_48_arm", None)
        return state
    if _site_30(state):
        state.terms[0].tags.add("sAmantrita")
        state.samjna_registry["2.3.48_sAmantrita_maGavan"] = True
        state.meta.pop("prakriya_30_2_3_48_arm", None)
        return state
    if _site_29(state):
        state.terms[0].tags.add("sAmantrita")
        state.samjna_registry["2.3.48_sAmantrita_gaurAvaskandin"] = True
        state.meta.pop("prakriya_29_2_3_48_arm", None)
        return state
    if _site_26(state):
        state.terms[0].tags.add("sAmantrita")
        state.samjna_registry["2.3.48_sAmantrita_indra"] = True
        state.meta.pop("prakriya_26_2_3_48_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="2.3.48",
    sutra_type=SutraType.SAMJNA,
    text_slp1="saamantritam",
    text_dev="सामन्त्रितम्",
    padaccheda_dev="सामन्त्रितम्",
    why_dev="सम्बोधन-प्रयोगस्य सामन्त्रित-संज्ञा (*prakriya_26* / *29* / *30* / *32* / *34*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
