"""
4.2.70  अदूरभवश्च  —  SAMJNA (narrow ``prakriya_46``)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=42070):** *adūrabhavaś ca* — *aṇ* after the sixth-case base in the sense “whose region bears that name and exists **not far from** (*adūrabhava*) here.”

**Engine:** glass-box one-shot *prayoga* note — ``samjna_registry['4.2.70_adUrabhava_prakriya_46']`` when **4.1.76** *taddhita* *adhikāra* is open, recipe arms **4.2.70**, ``meta['prakriya_46_adUrabhava_aR_note']``, and witness ``goda`` carries ``prakriya_46_godau_demo``. No ``varṇa`` change.

Cross-check full *śāstra* chain (*śeṣe* **4.2.92**, **4.1.82**, etc.) offline — narrow demo only.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _taddhita_adhikara_open(state: State) -> bool:
    return any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_46_4_2_70_arm"):
        return False
    if not _taddhita_adhikara_open(state):
        return False
    if not state.meta.get("prakriya_46_adUrabhava_aR_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_46_godau_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("4.2.70_adUrabhava_prakriya_46"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["4.2.70_adUrabhava_prakriya_46"] = True
    state.meta.pop("prakriya_46_4_2_70_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="4.2.70",
    sutra_type=SutraType.SAMJNA,
    text_slp1="adUrabhavaSca",
    text_dev="अदूरभवश्च",
    padaccheda_dev="अदूरभवः / च",
    why_dev=(
        "अदूरभवार्थे अण् (*prakriya_46*, **गोदौ ग्रामः** विग्रहादेशः) — संज्ञा-चिह्नम्।"
    ),
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
