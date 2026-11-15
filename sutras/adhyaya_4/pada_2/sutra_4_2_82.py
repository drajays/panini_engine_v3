"""
4.2.82  वरणादिभ्यश्च  —  SAMJNA (narrow ``prakriya_46``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=42082):** *varaṇādibhyaś ca* — *luk* of *taddhita* **after** bases of the *varaṇādi-gaṇa* (includes **गोद**). Machine **anuvṛtti** links ``लुप्`` to **4.2.81** (*janapade lup*, i=42081).

**Edition note:** Some commentaries/OCR label this rule “**4.2.81**”; on ashtadhyayi-com **4.2.81** is *janapade lup* (42081). The **varaṇādi** *luk* rule is **4.2.82** here.

**Engine:** glass-box note ``samjna_registry['4.2.82_varaNAdi_luk_prakriya_46']`` — recipe gate only; no ``varṇa`` mutation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra, gana
from engine.luk import live_taddhita, take_away
from engine.state import State
from engine.taddhita_attach import frame_open


def _site(state: State):
    """Kāśikā 4.2.82: after a varaṇādi stem the taddhita of the nivāsa / adūrabhava senses is taken away by lup (varaṇānām adūrabhavaṃ nagaraṃ varaṇāḥ)."""
    i = live_taddhita(state)
    if i is None or i < 1:
        return None
    stem = state.terms[i - 1]
    name = stem.meta.get("upadesha_slp1") or "".join(v.slp1 for v in stem.varnas)
    if not gana.in_gana("varaRAdiH", name):
        return None
    return i if frame_open(state, "cAturarTika") else None   # Kāśikā: cāturarthikasya pratyayasya — the frame 4.2.67 / 4.2.69 / 4.2.70 opened; the sūtra names no sense itself (AMENDMENT 25)


def _legacy_site(state: State) -> bool:
    # SHORTCUT S24: the old `prakriya_46` demo recipe (pipelines/godau.py) still pins this registry key; removed with the demo
    if not any(e.get("id") == "4.1.76" for e in state.adhikara_stack):
        return False
    if not state.meta.get("prakriya_46_varaNAdi_luk_note") or not state.terms:
        return False
    if not any("prakriya_46_godau_demo" in t.tags for t in state.terms):
        return False
    return not state.samjna_registry.get("4.2.82_varaNAdi_luk_prakriya_46")


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_site(state)


def act(state: State) -> State:
    i = _site(state)
    if i is not None:
        return take_away(state, i, "lup")
    if _legacy_site(state):
        state.samjna_registry["4.2.82_varaNAdi_luk_prakriya_46"] = True
    return state

SUTRA = SutraRecord(
    sutra_id="4.2.82",
    sutra_type=SutraType.VIDHI,
    text_slp1='varaRAdiByaSca',
    text_dev='वरणादिभ्यश्च',
    samagra_slp1="pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA varaRa-AdiByaH ca lup",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा वरण-आदिभ्यः च लुप्",
    padaccheda_dev="वरणादिभ्यः / च",
    why_dev=(
        "वरणाद्यन्ताद् अण्-लुपि चिह्नम् (*prakriya_46*); **4.2.81** इत्यत्र *जनपदे लुप्* पृथक्।"
    ),
    anuvritti_from=("4.2.81",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
