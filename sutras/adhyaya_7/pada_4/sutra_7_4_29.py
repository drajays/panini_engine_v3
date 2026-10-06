"""
7.4.29  गुणोऽर्तिसंयोगाद्योः  —  VIDHI

Padaccheda: गुणः अर्ति-संयोग-आद्योः

गुणोऽर्तिसंयोगाद्योः (7.4.29)
Pāṭha: ashtadhyayi.com data.txt row i=74029 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_VOWELS = frozenset("aAiIuUfFxXeEoO")


def _yak_or_ashir_ling(t) -> bool:
    """The two loci carried from 7.4.28 that 7.4.29 overrides for these roots."""
    return ("3_1_67_yak" in t.tags or "yasut_agama" in t.tags
            or (t.meta.get("source_lakara_upadesha") == "liG" and "ardhadhatuka" in t.tags))


def _find(state: State) -> int | None:
    """ṛ-final dhātu that is ṛ itself (अर्ति) or begins with a saṃyoga, before yak/āśīrliṅ."""
    for i, t in enumerate(state.terms[:-1]):
        vs = [v.slp1 for v in t.varnas]
        if "dhatu" not in t.tags or not vs or vs[-1] != "f":
            continue
        if not (vs == ["f"] or (len(vs) >= 3 and vs[0] not in _VOWELS and vs[1] not in _VOWELS)):
            continue
        if _yak_or_ashir_ling(state.terms[i + 1]):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is not None:
        t = state.terms[i]
        t.varnas[-1:] = [mk("a"), mk("r")]      # guṇa + 1.1.51 rapara: स्मृ → स्मर् (स्मर्यते)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.29",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'guRortisaMyogAdyoH',
    text_dev              = 'गुणोऽर्तिसंयोगाद्योः',
    samagra_slp1          = "aNgasya guRaH artisaMyogAdyoH yi akftsArvaDAtukayoH ftaH SayagliNkzu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य गुणः अर्तिसंयोगाद्योः यि अकृत्सार्वधातुकयोः ऋतः शयग्लिङ्क्षु",
    padaccheda_dev        = "गुणः अर्ति-संयोग-आद्योः",
    why_dev               = "ऋ-धातोः संयोगादेः ऋदन्तस्य च यकि आशीर्लिङि च गुणः (स्मर्यते, अर्यते) — रिङोऽपवादः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
