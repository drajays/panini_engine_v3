"""
2.1.6  अव्ययं विभक्तिसमीपसमृद्धिव्यृद्ध्यर्थाभावात्ययासम्प्रतिशब्दप्रादुर्भावपश्चाद्यथानुपूर्व्ययौगपद्यसादृश्यसम्पत्तिसाकल्यान्तवचनेषु  —  VIDHI (narrow v3 demo slice)

This engine uses 2.1.5 as the avyayībhāva adhikāra opener.  This file provides
a minimal, auditable *samāsa* assignment used by demos like **adhistri**:

  - When an avyaya (e.g. ``adhi``) combines with a prātipadika that still carries
    an internal sup (*avayava*), mark the state as avyayībhāva-ready.

We do not attempt full semantic parsing; the pipeline arms
``meta['avyayibhava_recipe']=True``.
Pāṭha: ashtadhyayi.com data.txt row i=21006 (Art. 14).
Kāśikā: विभक्त्यादिष्वर्थेषु यदव्ययं वर्तते, तत् समर्थन सुबन्तेन सह समस्यते, अव्ययीभावश्च समासो भवति।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

TAG_AVYAYIBHAVA: str = "avyayibhava"


def _old_cond(state: State) -> bool:
    return bool(state.meta.get("avyayibhava_recipe")) and not state.samjna_registry.get("2_1_6_avyayibhava")


def _old_act(state: State) -> State:
    # Structural mark for downstream samāsa steps (upasarjana/pūrvanipāta) + 1.1.41.
    for t in state.terms:
        if "samasa_member" in t.tags or "anga" in t.tags:
            t.tags.add(TAG_AVYAYIBHAVA)
    state.samjna_registry["2_1_6_avyayibhava"] = True
    state.meta["avyayibhava_kind"] = "2.1.6"
    return state


from engine.samasa_attach import pair, mark
from engine.vivaksha import vivaksita


def _site(state: State):
    """An avyaya pūrvapada (upa, adhi, prati) and a following subanta, in the sense of samīpa / vibhakti …: the speaker's vivakṣā."""
    return pair(state, "2.1.6", purva=lambda t: "avyaya" in t.tags) if vivaksita(state, "arthaViSeSa", "samIpa") else None


def cond(state: State) -> bool:
    return _site(state) is not None or _old_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _old_act(state)
    state = mark(state, list(s), TAG_AVYAYIBHAVA, "2.1.6")
    state.terms[s[0]].tags.add("upasarjana")
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.1.6",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1      = 'avyayaM viBaktisamIpasamfdDivyfdDyarTABAvAtyayAsampratiSabdaprAdurBAvapaScAdyaTAnupUrvyayOgapadyasAdfSyasampattisAkalyAntavacanezu',
    text_dev       = 'अव्ययं विभक्तिसमीपसमृद्धिव्यृद्ध्यर्थाभावात्ययासम्प्रतिशब्दप्रादुर्भावपश्चाद्यथानुपूर्व्ययौगपद्यसादृश्यसम्पत्तिसाकल्यान्तवचनेषु',
    samagra_slp1   = "avyayam viBakti-samIpa-samfdDi-vyfdDi-arTABAva-atyaya-asamprati-SabdaprAdurBAva-paScAt-yaTA-AnupUrvya-yOgapadya-sAdfSya-sampatti-sAkalyArTa-antavacanezu supA saha avyayIBAvaH samAsaH",
    samagra_dev    = "अव्ययम् विभक्ति-समीप-समृद्धि-व्यृद्धि-अर्थाभाव-अत्यय-असम्प्रति-शब्दप्रादुर्भाव-पश्चात्-यथा-आनुपूर्व्य-यौगपद्य-सादृश्य-सम्पत्ति-साकल्यार्थ-अन्तवचनेषु  सुपा सह अव्ययीभावः समासः",
    padaccheda_dev = "अव्ययम् / विभक्ति-समीप-समृद्धि…",
    why_dev        = "अव्यय-पूर्वकः समासः (अव्ययीभाव) — demo arm meta.",
    anuvritti_from = ("2.1.5",),
    apavada_of     = ("2.2.18",),      # a prādi in a sense of 2.1.6 (upa + kumbha, samīpa) is an avyayībhāva, not the nitya tatpuruṣa
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["TAG_AVYAYIBHAVA", "SUTRA"]

