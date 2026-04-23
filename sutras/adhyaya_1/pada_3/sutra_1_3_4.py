"""
1.3.4  न विभक्तौ तुस्माः  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — registers that **halantyam** (1.3.3) does **not** apply to
  a **sup** upadeśa whose final **hal** falls in **tusma** (engine: ``TUSMA``).

• **Structural trigger (Art. 2):** ``sup`` + ``upadesha`` on the pratyaya
  Term — not ``(vibhakti, vacana)``. In the subanta pipeline every **sup**
  attachment is a **vibhakti** pratyaya, so this matches *na vibhaktau*.

• **Interaction:** ``sutra_1_3_3`` skips tusma-final **sup** strips by the same
  phoneme check; this sūtra records the pratishedha in ``samjna_registry``.

• **v2 reference:** ``~/Documents/panini_engine_v2/core/it_rules.py``
  ``cond_1_3_4`` /
  ``act_1_3_4``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import HAL, TUSMA


def _tusma_sup_indices(state: State) -> list[int]:
    out: list[int] = []
    for i, t in enumerate(state.terms):
        if "sup" not in t.tags or "upadesha" not in t.tags:
            continue
        if not t.varnas:
            continue
        last = t.varnas[-1]
        if last.slp1 not in HAL or last.slp1 not in TUSMA:
            continue
        out.append(i)
    return out


def cond(state: State) -> bool:
    for i in _tusma_sup_indices(state):
        if ("1_3_4_tusma_vibhakti", i) not in state.samjna_registry:
            return True
    return False


def act(state: State) -> State:
    for i in _tusma_sup_indices(state):
        if ("1_3_4_tusma_vibhakti", i) in state.samjna_registry:
            continue
        last = state.terms[i].varnas[-1]
        state.samjna_registry[("1_3_4_tusma_vibhakti", i)] = frozenset(
            {last.slp1}
        )
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.4",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "na vibhaktO tusmAH",
    text_dev       = "न विभक्तौ तुस्माः",
    padaccheda_dev = "न विभक्तौ तु-स्माः",
    why_dev        = "विभक्ति-प्रत्यये अन्त्यौ तु-स्म-वर्णौ हलन्त्य-इत् संज्ञां न लभेते; "
                     "विधिः १.३.३ एव न प्रवर्तते (तुस्मान्त-निषेधः)।",
    anuvritti_from = ("1.3.2", "1.3.3"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
