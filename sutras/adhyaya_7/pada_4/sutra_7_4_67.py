"""
7.4.67  द्युतिस्वाप्योः सम्प्रसारणम्  —  VIDHI

Padaccheda: द्युति-स्वाप्योः सम्प्रसारणम्

द्युतिस्वाप्योः सम्प्रसारणम् (7.4.67)
Pāṭha: ashtadhyayi.com data.txt row i=74067 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_STEMS = frozenset({"dyut", "svAp"})        # dyuti (dyut) and the ṇic of svap (svāpi)
_SAMPRASARANA = {"y": "i", "v": "u"}
_VOWELS = frozenset("aAiIuUfFxXeEoO")


def _stem(t) -> str:
    return "".join(v.slp1 for v in t.varnas if "aT_agama_v" not in v.tags)


def _site(state: State):
    """The abhyāsa right before dyut / svāp: its y or v + vowel (Kāśikā: vididyute, suṣvāpayiṣati)."""
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or t.meta.get("7_4_67_done"):
            continue
        r = state.terms[i + 1]
        base = (r.meta.get("it_lopa_done") or (None,))[-1] if r.meta.get("it_lopa_done") else None
        if "dhatu" not in r.tags or (_stem(r) not in _STEMS and (base or "").rstrip("~") not in _STEMS and (r.meta.get("upadesha_slp1") or "").rstrip("~") not in ("dyut", "dyutf", "dyuta")):
            continue
        for j in range(len(t.varnas) - 1):
            if t.varnas[j].slp1 in _SAMPRASARANA and t.varnas[j + 1].slp1 in _VOWELS:
                return t, j
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, j = _site(state)
    t.varnas[j] = mk(_SAMPRASARANA[t.varnas[j].slp1])
    del t.varnas[j + 1]          # 6.1.108 samprasāraṇāc ca: the vowel after it is absorbed
    t.meta["7_4_67_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.67",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "dyutisvApyoH samprasAraRam",
    text_dev              = "द्युतिस्वाप्योः सम्प्रसारणम्",
    samagra_slp1          = "aNgasya aByAsasya dyutisvApyoH samprasAraRam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य द्युतिस्वाप्योः सम्प्रसारणम्",
    padaccheda_dev        = "द्युति-स्वाप्योः सम्प्रसारणम्",
    why_dev               = "(सूत्रम् 7.4.67) द्युतिस्वाप्योः सम्प्रसारणम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
