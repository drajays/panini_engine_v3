"""
8.1.26  सपूर्वायाः प्रथमाया विभाषा  —  VIBHASHA

When the pada immediately before the pronoun is prathamānta *and itself has a pada before it*
(sapūrva), the ādeśas of 8.1.20–23 are optional: ग्रामे कम्बलस्ते स्वम् / ग्रामे कम्बलस्तव स्वम्,
ग्रामे कम्बलो मे स्वम् / ग्रामे कम्बलो मम स्वम्. Without a pada before the prathamānta (ग्रामस्ते स्वम्)
the ādeśa is nitya.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com 8.1.26 
  Source #2 — Kāśikā 8.1.26 examples (as above)

Engine: scheduled before 8.1.20–23. Default (``vibhasha_default=False``) leaves the ādeśa standing
(the first form the Kāśikā lists); choosing True records ``enclitic_nivrtta_8_1_26`` on the pronoun so
8.1.20–23 decline. ``engine.vikalpa.explore`` returns both readings.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_8.pada_1.enclitic_common import target
from engine.state import State


def _site(state: State):
    i = target(state, "8.1.26")
    if i is None or i < 2:
        return None
    prev, before = state.terms[i - 1], state.terms[i - 2]
    return i if "vib_prathama" in prev.tags and "pada" in before.tags else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is not None:
        state.terms[i].tags.add("enclitic_nivrtta_8_1_26")
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.26",
    sutra_type=SutraType.VIBHASHA,
    text_slp1="sapUrvAyAH praTamAyA viBAzA",
    text_dev="सपूर्वायाः प्रथमाया विभाषा",
    padaccheda_dev="सपूर्वायाः प्रथमायाः विभाषा",
    why_dev="सपूर्व प्रथमान्त पद के पश्चात् युष्मद्-अस्मद् आदेश (८.१.२०–२३) विकल्प से।",
    anuvritti_from=("8.1.17", "8.1.18", "8.1.20", "8.1.24"),
    vibhasha_default=False,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
