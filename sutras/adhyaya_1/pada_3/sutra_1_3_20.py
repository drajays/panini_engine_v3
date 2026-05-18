"""
1.3.20  आङो दोऽनास्यविहरणे  —  VIDHI

*Padaccheda:* *āṅaḥ* (षष्ठी) / *daḥ* (षष्ठी) / *anāsya-viharaṇe* (सप्तमी).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* For the root dā (to give) preceded by the prefix āṅ (ā-), ātmanepada
endings are prescribed — except when the meaning is āsya-viharaṇa (moving the
mouth / speech).

*Engine:* cond checks (a) pada not already "Atmanepada", (b) a dhātu Term whose
upadesha_slp1 is in {"qf", "dA"}, (c) that dhātu carries the tag "A_prefix",
(d) it does NOT carry "Asya_viharaRa_usage", and (e) idempotency guard
"Atmanepada_1_3_20" is absent from meta.  No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_DA_ROOTS: frozenset[str] = frozenset({"qf", "dA"})
_REGISTRY_KEY = "1_3_20_A_do"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get("Atmanepada_1_3_20"):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _DA_ROOTS
        and "A_prefix" in t.tags
        and "Asya_viharaRa_usage" not in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"] = "Atmanepada"
    state.meta["Atmanepada_1_3_20"] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.20",
    sutra_type=SutraType.VIDHI,
    text_slp1="ANo do'nAsyaviharaRe",
    text_dev="आङो दोऽनास्यविहरणे",
    padaccheda_dev="आङः (षष्ठी) / दः (षष्ठी) / अनास्य-विहरणे (सप्तमी)",
    why_dev=(
        "आङ्-पूर्वकस्य दा-धातोः आत्मनेपदं भवति — आस्य-विहरण-अर्थे तु न; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
