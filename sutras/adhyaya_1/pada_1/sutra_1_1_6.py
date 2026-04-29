"""
1.1.6  दीधीवेवीटाम्  —  PARIBHASHA  (representative)

इडागमस्य गुणनिषेधः (v3 representative)

शास्त्रीय आशयः (आप्त-विवरणानुसारः):
यत्र विकरणप्रत्ययस्य **इडागमः** भवति, तत्र सः इडागमः परतः प्रत्ययार्थम्
अङ्गावयवरूपेण स्वीक्रियते। एतादृशे प्रसङ्गे इडागमस्य इकारे गुणादेशः
प्राप्तेऽपि, **अयम् गुणः निषिध्यते**।

Engine policy:
This is implemented as a PARIBHASHA that sets a gate in
``state.paribhasha_gates``. Vidhis that would otherwise guṇa a vowel
must consult this gate and skip when the target vowel carries the
``it_agama`` tag (inserted by 7.2.35 iṭ-āgama).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


# In practice, the classical paribhāṣā is invoked by name for a small
# fixed dhātu set (दीधी / वेवी / ईट्).  We expose a helper so vidhis can
# block guṇa/vṛddhi by **dhātu identity** rather than pipeline-injected meta.
_DIDHI_VEVI_IT_BASES: frozenset[str] = frozenset({"dIDhI", "vevI", "iw"})


def _normalize_upadesha_base(up: str | None) -> str:
    """
    Best-effort normalizer for dhātu identity checks.
    Examples:
      'dIDhI~N' → 'dIDhI'
      'iw'      → 'iw'
    """
    if not up:
        return ""
    s = up.strip().replace("~", "")
    # Drop trailing it letters if present (common in upadeśa strings).
    while s and s[-1] in {"N", "Y", "R"}:
        s = s[:-1]
    return s


def dhatu_blocked_by_1_1_6(upadesha_slp1: str | None) -> bool:
    """True iff the dhātu is in the 1.1.6 दीधी-वेवी-ईट् set (operational helper)."""
    return _normalize_upadesha_base(upadesha_slp1) in _DIDHI_VEVI_IT_BASES


def cond(state: State) -> bool:
    return "id_agama_guna_nishedha" not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates["id_agama_guna_nishedha"] = True
    return state


SUTRA = SutraRecord(
    sutra_id         = "1.1.6",
    sutra_type       = SutraType.PARIBHASHA,
    text_slp1        = "dIDIvevIwAm",
    text_dev         = "दीधीवेवीटाम्",
    padaccheda_dev   = "दीधी-वेवी-इटाम्",
    why_dev          = "इडागम-इकारस्य गुणनिषेधः (परिभाषा-गेट)।",
    anuvritti_from   = (),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
