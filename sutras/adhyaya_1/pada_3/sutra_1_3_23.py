"""
1.3.23  प्रकाशनस्थेयाख्ययोश्च  —  VIDHI

*Padaccheda:* *prakāśana-stheyā-ākhyāyoḥ* (षष्ठी-द्विवचन) / *ca*.

*Anuvṛtti:* ātmanepada from 1.3.12; sthā from 1.3.22.

*Content:* For the root sthā (to stand/dwell) also in the senses of prakāśana
(illumination / manifestation) and stheyā (stability / dwelling), ātmanepada
endings are prescribed — independently of any prefix requirement.

*Engine:* cond checks (a) pada not already "Atmanepada", (b) a dhātu Term whose
upadesha_slp1 is "zwA", (c) that dhātu carries the tag "prakASana_usage" OR
"sTeyA_usage", and (d) idempotency guard "Atmanepada_1_3_23" absent from meta.
No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_STHA_ROOTS: frozenset[str] = frozenset({"zwA"})
_REGISTRY_KEY = "1_3_23_prakASana_sTeyA"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_23"):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _STHA_ROOTS
        and ("prakASana_usage" in t.tags or "sTeyA_usage" in t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_23"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.23",
    sutra_type=SutraType.VIDHI,
    text_slp1="prakASanasTeYAKyAyoSca",
    text_dev="प्रकाशनस्थेयाख्ययोश्च",
    padaccheda_dev="प्रकाशन-स्थेया-आख्यायोः (षष्ठी-द्विवचन) / च",
    why_dev=(
        "प्रकाशन-अर्थे स्थेया-अर्थे च स्था-धातोः आत्मनेपदं भवति; "
        "१.३.२२ इत्यतः स्था-ग्रहणम्, १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.22",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
