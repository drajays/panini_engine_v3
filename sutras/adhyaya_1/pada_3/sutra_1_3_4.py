"""
1.3.4  न विभक्तौ तुस्माः  —  SAMJNA (pratiṣedha of 1.3.3)

Sources consulted:
- ashtadhyayi.com data.txt row i=13004
- Kāśikā: "तवर्ग — वृक्षात्, प्लक्षात्। सकार — जस् — ब्राह्मणाः। तस्, थस् — पचतः, पचथः"
- Cross-validation: regression tests tests/unit/test_it_prakarana.py (जस् keeps स्,
  अम् keeps म्, तस् keeps स्; तुमुन् loses न्)

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA (niṣedha) — the final **tu-varga / s / m** of a *vibhakti*
  upadeśa does **not** get *halantyam* (1.3.3).  Recorded per Varṇa as
  ``it_pratishedha_1_3_4`` so the trace shows *why* the sound survives.

• **Vibhakti (1.4.104 सुप्तिङौ; 5.3.1 प्राग्दिशो विभक्तिः):** ``is_vibhakti_upadesha``
  — a *sup* Term (not a luk ghost), a *tiṅ* ādeśa of *la*, or a Term carrying the
  1.4.104 / 5.3.1 *vibhakti* saṃjñā tag.  Read structurally (Art. 2) — never
  ``(vibhakti, vacana)`` coordinates.  **1.3.3** consults the same predicate.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_samjna import it_lopa_already_done
from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from engine.state  import State
from phonology     import HAL, TUSMA

from sutras.adhyaya_1.pada_4.vibhakti_samjna_1_4_104 import (
    TAG_1_4_104_VIBHAKTI,
    is_tin_vibhakti_pratyaya,
)

TAG_5_3_1_VIBHAKTI = "samjna_5_3_1_vibhakti"
PRATISHEDHA_TAG = "it_pratishedha_1_3_4"


def is_vibhakti_upadesha(t) -> bool:
    if LUK_LOPA_GHOST_TAG in t.tags:
        return False
    if t.tags & {"sup", "tin_adesha_3_4_78", TAG_1_4_104_VIBHAKTI, TAG_5_3_1_VIBHAKTI}:
        return True
    return is_tin_vibhakti_pratyaya(t)


def tusma_final_vibhakti(t) -> bool:
    """The upadeśa is a vibhakti ending in tu-varga / s / m (1.3.3 blocked)."""
    if not t.varnas or not is_vibhakti_upadesha(t):
        return False
    last = t.varnas[-1].slp1
    return last in HAL and last in TUSMA


def _pending(state: State) -> list[int]:
    out: list[int] = []
    for i, t in enumerate(state.terms):
        if "upadesha" not in t.tags or it_lopa_already_done(t):
            continue
        if not tusma_final_vibhakti(t):
            continue
        if PRATISHEDHA_TAG in t.varnas[-1].tags:
            continue
        out.append(i)
    return out


def cond(state: State) -> bool:
    return bool(_pending(state))


def act(state: State) -> State:
    for i in _pending(state):
        last = state.terms[i].varnas[-1]
        last.tags.add(PRATISHEDHA_TAG)
        state.samjna_registry[("1_3_4_tusma_vibhakti", i)] = frozenset({last.slp1})
    state.meta["__why_now_dev__"] = (
        "विभक्ति-प्रत्यये अन्त्यौ तु-स्म-वर्णौ हलन्त्य-इत् (१.३.३) संज्ञां न लभेते; "
        "अयं प्रतिषेधः, अतः अन्त्य-हल् न लुप्यते (यथा जस्, तस्, अम्)। (१.३.४)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.4",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'na viBaktO tusmAH',
    text_dev       = 'न विभक्तौ तुस्माः',
    padaccheda_dev = "न विभक्तौ तु-स्माः",
    why_dev        = "विभक्ति-प्रत्यये अन्त्यौ तु-स्म-वर्णौ हलन्त्य-इत् संज्ञां न लभेते; "
                     "विधिः १.३.३ एव न प्रवर्तते (तुस्मान्त-निषेधः)।",
    apavada_of     = ("1.3.3",),
    anuvritti_from = ("1.3.2", "1.3.3"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
