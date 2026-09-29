"""
6.4.87  हुश्नुवोः सार्वधातुके  —  VIDHI

Padaccheda: हु-श्नुवोः सार्वधातुके

हुश्नुवोः सार्वधातुके (6.4.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    """हुश्नुवोः सार्वधातुके (असंयोगपूर्वस्य, 6.4.82): the उ of श्नु (and of हु) not after a
    conjunct becomes व् before a vowel-initial sārvadhātuka — सुनु+अन्ति → सुन्वन्ति;
    after a conjunct 6.4.77 uvaṅ stays (आप्नुवन्ति)."""
    ts = state.terms
    for k in range(1, len(ts) - 1):
        nu, nxt = ts[k], ts[k + 1]
        if (nu.meta.get("upadesha_slp1") or "").strip() != "Snu" or [v.slp1 for v in nu.varnas] != ["n", "u"]:
            continue
        if not nxt.varnas or nxt.varnas[0].slp1 not in _AC:
            continue
        if not any(t.startswith("sarvadhatuka") for t in nxt.tags):
            continue
        prev = ts[k - 1].varnas
        if prev and prev[-1].slp1 in _AC:           # न् is the only consonant before उ
            return nu
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[-1] = mk("v")
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.87",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "huSnuvoH sArvaDAtuke",
    text_dev              = "हुश्नुवोः सार्वधातुके",
    padaccheda_dev        = "हु-श्नुवोः सार्वधातुके",
    why_dev               = "असंयोगपूर्वस्य श्नुप्रत्ययस्य उकारस्य यण् अजादौ सार्वधातुके (सुन्वन्ति, चिन्वन्ति)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
