"""
1.4.79  जीविकोपनिषदावौपम्ये  (jīvikopaniṣadāv aupamye)  —  SAMJNA

The words "jīvikā" (livelihood) and "upaniṣad" (secret teaching) get the
gati-saṃjñā when used in the sense of aupamya (comparison / simile).

E.g., "upaniṣad-kṛ" = to make something into an upaniṣad (by way of
comparison); "jīvikā-kṛ" = to make one's livelihood of something.

v3: registers samjna_registry["gati_jivika_upanisad"] = frozenset({"jIvikA","upanizad"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_JIVIKA_UPANISAD: frozenset[str] = frozenset({"jIvikA", "upanizad"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_jivika_upanisad") is None


def act(state: State) -> State:
    state.samjna_registry["gati_jivika_upanisad"] = _JIVIKA_UPANISAD
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _JIVIKA_UPANISAD
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.79",
    sutra_type=SutraType.SAMJNA,
    text_slp1="jIvikopanizadAvOpamye",
    text_dev="जीविकोपनिषदावौपम्ये",
    padaccheda_dev="जीविका-उपनिषदौ / औपम्ये",
    why_dev="औपम्ये 'जीविका' 'उपनिषद्' गति-संज्ञके — गति-सेटे योज्येते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
