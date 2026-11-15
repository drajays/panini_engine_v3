"""
4.1.88  द्विगोर्लुगनपत्ये  —  SAMJNA (narrow ``prakriya_42``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41088):** *dvigor lug anapatye* — *luk* of a *taddhita*
suffix after a *dvigu* when the sense is not *apatya* / when conditions match (scholia link **अनपत्ये**).

Narrow v3 (**पञ्चेन्द्र** `panini_engine_pipeline` — *aṇ* *luk* after *dvigu* *paYcendra*):
  • **4.1.76** *taddhita* *adhikāra* on ``adhikara_stack``.
  • ``prakriya_42_4_1_88_arm`` + ``meta['prakriya_42_dvigu_anapatye_note']`` +
    witness ``Term`` tagged ``prakriya_42_paYcendra_demo`` →
    ``samjna_registry['4.1.88_dvigor_lug_anapatye_prakriya_42']``.

No ``varṇa`` mutation (recipe gate only).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.luk import live_taddhita, take_away
from engine.state import State
from engine.taddhita_attach import frame_open


def _in_agni_zone(t) -> bool:
    """Did a sūtra between 4.1.83 and 4.3.168 give this pratyaya? (its varṇas carry ``origin:<sūtra>``)"""
    for v in t.varnas:
        for tag in v.tags:
            if tag.startswith("origin:") and tag[7:].count(".") == 2:
                k = tuple(int(x) for x in tag[7:].split("."))
                if (4, 1, 83) <= k <= (4, 3, 168):
                    return True
    return False


def _site(state: State):
    """Kāśikā 4.1.88: dvigoḥ parasya taddhitasya luk bhavati anapatye (pañcakapālaḥ, paṅcakapālaḥ; dvaidevadattiḥ keeps its pratyaya: apatya).
    The dvigu saṃjñā is the stem's (`dvigu`, the samāsa tag, or the lexical fact `lex:dvigu`, S14); anapatye = the apatya frame (4.1.92) is not open."""
    i = live_taddhita(state)
    if i is None or i < 1 or frame_open(state, "apatya"):
        return None
    if not _in_agni_zone(state.terms[i]):
        return None             # the anuvṛtti is prāg dīvyato 'ṇ (4.1.83 – 4.3.168): a pratyaya a sūtra of 5.1.x or the samāsānta of 5.4.x gave is outside it (ṣāṇmāsyam, dvyañjalam keep theirs)
    return i if {"dvigu", "lex:dvigu"} & state.terms[i - 1].tags else None


def _legacy_site(state: State) -> bool:
    # SHORTCUT S24: the old `prakriya_42` demo recipe (pipelines/paYcendra.py) still pins this registry key; removed with the demo
    if not any(e.get("id") == "4.1.76" for e in state.adhikara_stack):
        return False
    if not state.meta.get("prakriya_42_dvigu_anapatye_note") or not state.terms:
        return False
    if not any("prakriya_42_paYcendra_demo" in t.tags for t in state.terms):
        return False
    return not state.samjna_registry.get("4.1.88_dvigor_lug_anapatye_prakriya_42")


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_site(state)


def act(state: State) -> State:
    i = _site(state)
    if i is not None:
        return take_away(state, i, "luk")
    if _legacy_site(state):
        state.samjna_registry["4.1.88_dvigor_lug_anapatye_prakriya_42"] = True
    return state

SUTRA = SutraRecord(
    sutra_id="4.1.88",
    sutra_type=SutraType.VIDHI,
    text_slp1="dvigorluganapatye",
    text_dev="द्विगोर्लुगनपत्ये",
    samagra_slp1="anapatye dvigoH aci tadDitaH luk",
    samagra_dev="अनपत्ये द्विगोः अचि तद्धितः लुक्",
    padaccheda_dev="द्विगोः / लुक् / अनपत्ये",
    why_dev="द्विगोः परस्य तद्धितस्य लुक् (*devatā*, न अपत्ये) (*prakriya_42*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
