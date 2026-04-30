"""
8.1.19  आमन्त्रितस्य च  —  ANUVADA (narrow ``prakriya_30`` / ``prakriya_32``)

**Pāṭha (Kāśikā on *Aṣṭ*. 8.1.19, *anuvṛtti* from **8.1.18**):** *āmantriṭasya ca* —
the *āmantrita* *pada* (when not *pāda*-initial; *apādādau*) becomes *sarvānudātta*
(all syllables *anudātta* / “unaccented high” in the *śikṣā* sense).

Narrow v3:
  • ``prakriya_30`` — ``maGavan``: ``prakriya_30_8_1_19_arm``, stamps
    ``meta['prakriya_30_sarvAnudAtta_note']`` on ``terms[0]``.
  • ``prakriya_32`` — ``jaWilaka`` / ``aDyApaka`` after ``EdaviDa``: separate arms
    ``prakriya_32_8_1_19_jWilaka_arm`` / ``prakriya_32_8_1_19_aDyApaka_arm``;
    requires **8.1.73** *samānādhikaraṇa* registry flag; stamps per-term notes.
  • ``prakriya_34`` — ``aDyApaka`` before ``kv``: ``prakriya_34_8_1_19_arm`` stamps
    ``meta['prakriya_34_aDyApaka_sarvAnudAtta_note']`` on ``terms[0]``.

**Note:** **6.1.198** (*ṝk-prātishākhya* neighbourhood) is a different anchor from this **8.1.19**
accent sandhi row — both may read *āmantriṭasya ca* in machine metadata.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _adhikara_8_1_18_open(state: State) -> bool:
    return any(e.get("id") == "8.1.18" for e in state.adhikara_stack)


def _site_prakriya_30(state: State) -> bool:
    if not state.meta.get("prakriya_30_8_1_19_arm"):
        return False
    if not _adhikara_8_1_18_open(state):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "sAmantrita" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "maGavan":
        return False
    if t0.meta.get("prakriya_30_sarvAnudAtta_note"):
        return False
    return True


def _site_prakriya_32_jWilaka(state: State) -> bool:
    if not state.meta.get("prakriya_32_8_1_19_jWilaka_arm"):
        return False
    if not _adhikara_8_1_18_open(state):
        return False
    if len(state.terms) < 2:
        return False
    if not state.samjna_registry.get("prakriya_32_samAnAdhikaraRa"):
        return False
    t1 = state.terms[1]
    if "sAmantrita" not in t1.tags:
        return False
    if t1.meta.get("upadesha_slp1") != "jaWilaka":
        return False
    if t1.meta.get("prakriya_32_jWilaka_sarvAnudAtta_note"):
        return False
    return True


def _site_prakriya_32_aDyApaka(state: State) -> bool:
    if not state.meta.get("prakriya_32_8_1_19_aDyApaka_arm"):
        return False
    if not _adhikara_8_1_18_open(state):
        return False
    if len(state.terms) < 3:
        return False
    if not state.samjna_registry.get("prakriya_32_samAnAdhikaraRa"):
        return False
    t2 = state.terms[2]
    if "sAmantrita" not in t2.tags:
        return False
    if t2.meta.get("upadesha_slp1") != "aDyApaka":
        return False
    if t2.meta.get("prakriya_32_aDyApaka_sarvAnudAtta_note"):
        return False
    return True


def _site_prakriya_34_aDyApaka_kv(state: State) -> bool:
    if not state.meta.get("prakriya_34_8_1_19_arm"):
        return False
    if not _adhikara_8_1_18_open(state):
        return False
    if len(state.terms) < 2:
        return False
    t0 = state.terms[0]
    if "sAmantrita" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "aDyApaka":
        return False
    if "prakriya_34_aDyApaka_kv_demo" not in t0.tags:
        return False
    if t0.meta.get("prakriya_34_aDyApaka_sarvAnudAtta_note"):
        return False
    return True


def cond(state: State) -> bool:
    return (
        _site_prakriya_32_jWilaka(state)
        or _site_prakriya_32_aDyApaka(state)
        or _site_prakriya_34_aDyApaka_kv(state)
        or _site_prakriya_30(state)
    )


def act(state: State) -> State:
    if _site_prakriya_32_jWilaka(state):
        state.terms[1].meta["prakriya_32_jWilaka_sarvAnudAtta_note"] = True
        state.meta.pop("prakriya_32_8_1_19_jWilaka_arm", None)
        return state
    if _site_prakriya_32_aDyApaka(state):
        state.terms[2].meta["prakriya_32_aDyApaka_sarvAnudAtta_note"] = True
        state.meta.pop("prakriya_32_8_1_19_aDyApaka_arm", None)
        return state
    if _site_prakriya_34_aDyApaka_kv(state):
        state.terms[0].meta["prakriya_34_aDyApaka_sarvAnudAtta_note"] = True
        state.meta.pop("prakriya_34_8_1_19_arm", None)
        return state
    if _site_prakriya_30(state):
        state.terms[0].meta["prakriya_30_sarvAnudAtta_note"] = True
        state.meta.pop("prakriya_30_8_1_19_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.19",
    sutra_type=SutraType.ANUVADA,
    text_slp1="aamantritasya ca",
    text_dev="आमन्त्रितस्य च",
    padaccheda_dev="आमन्त्रितस्य च",
    why_dev="आमन्त्रित-पदं सर्वानुदात्तम् (*prakriya_30* / *32* / *34*, **८.१.१८**-अधिकारे)।",
    anuvritti_from=("8.1.18",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
