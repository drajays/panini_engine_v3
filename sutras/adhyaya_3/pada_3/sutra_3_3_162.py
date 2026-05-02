"""
3.3.162  लोट् च  —  ADHIKARA (narrow: P031 *loṭ* spine)

Teaching JSON **P031**: *loṭ* is taught as a *vidhi* *lakāra* alongside *laṭ*.

Glass-box: open the *loṭ* *adhikāra* marker (recipe-only) so **3.4.77**/**3.4.78**
can resolve *lac* → *tiṅ* *ādeśa* on a structural ``loT`` placeholder ``Term``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("P031_3_3_162_loT_adhikara_arm"):
        return False
    return not any(e.get("id") == "3.3.162" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id": "3.3.162",
        "scope_end": "3.3.1",
        "text_dev": "लोट् च",
    })
    state.meta.pop("P031_3_3_162_loT_adhikara_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.162",
    sutra_type=SutraType.ADHIKARA,
    text_slp1="loT ca",
    text_dev="लोट् च",
    padaccheda_dev="लोट् / च",
    why_dev="लोट्-प्रकरणाधिकारः — प०३१।",
    anuvritti_from=(),
    cond=cond,
    act=act,
    adhikara_scope=("3.3.162", "3.3.1"),
)

register_sutra(SUTRA)
