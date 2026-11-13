"""
1.3.74  णिचश्च  —  VIDHI

*Padaccheda:* *ṇicaḥ* (pañcamī, ṇic-grahaṇa = ṇijantāt by pratyayagrahaṇa-paribhāṣā) / *ca*.
Anuvṛtti: *ātmanepadam* (1.3.12), *kartrabhiprāye kriyāphale* (1.3.72).
(The old file read this as an "apa-vad parasmaipada" rule — nothing in the text says that; the sūtra says: after
ṇic, ātmanepada, when the fruit goes to the agent.)

Kāśikā 1.3.74: "कर्त्रभिप्राये क्रियाफले इति वर्तते। णिजन्तादात्मनेपदं भवति कर्त्रभिप्राये क्रियाफले। कटं
कारयते। ओदनं पाचयते। कर्त्रभिप्राय इत्येव — कटं कारयति परस्य।"

Engine: ``cond`` needs a *ṇic* Term on the tape (tag ``nic``, put there by 3.1.26/3.1.25) after the dhātu AND
the kartrabhiprāya vivakṣā (``engine.vivaksha``). ``act`` sets ``state.meta['pada'] = 'Atmanepada'`` — the pada
the tiṅ-ādeśa step reads (``pipelines.tinanta._derive_laT_nic_atmane``). No ṇic: no fire; no vivakṣā: no fire
(kaṭaṃ kārayati parasya stays parasmaipada). Pāṭha: ashtadhyayi.com data.txt row i=13074 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita


def _nic_after_dhatu(state: State) -> bool:
    seen = False
    for t in state.terms:
        if "dhatu" in t.tags:
            seen = True
        elif seen and "nic" in t.tags:
            return True
    return False


def cond(state: State) -> bool:
    return (state.meta.get("pada") != "Atmanepada" and _nic_after_dhatu(state)
            and vivaksita(state, "kartrabhiprAya", "kartraBiprAya"))


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.samjna_registry["1_3_74_Nic_Atmanepada"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.74",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="RicaSca",
    text_dev="णिचश्च",
    samagra_slp1="RicaH ca Atmanepadam kartraBiprAye kriyAPale",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="णिचः च आत्मनेपदम् कर्त्रभिप्राये क्रियाफले",
    padaccheda_dev="णिचः (पञ्चमी-एकवचन) / च",
    why_dev=(
        "णिजन्ताद् धातोः कर्त्रभिप्राये क्रियाफले आत्मनेपदम् — "
        "कटं कारयते, ओदनं पाचयते; "
        "१.३.१२ इत्यतः आत्मनेपदम्, १.३.७२ इतः कर्त्रभिप्राये क्रियाफले अनुवर्तेते।"
    ),
    anuvritti_from=("1.3.12", "1.3.72"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
