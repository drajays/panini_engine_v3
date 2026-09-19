"""
7.3.93  ब्रुव ईट्  —  VIDHI

Padaccheda: ब्रुवः ईट्

ब्रू, before a हल्-आदि पित् सार्वधातुक affix (तिप्/सिप्/मिप्), takes the
आगम **ईट्** (दीर्घ ई). Combined with 7.3.84's ordinary guṇa (ऊ→ओ) and
6.1.78's एचोऽयवायावः (ओ+ई → अव्+ई), this gives ब्रवीति/ब्रवीषि/ब्रवीमि —
not the 6.4.77 उवङ्-आदेश path (ब्रुवन्ति), which applies only before a
vowel-initial affix (झि/अन्ति etc.), never a हल्-आदि one.

Source: PDF p.809–810 (Mīmāṃsaka Aṣṭādhyāyī-Bhāṣya परिशिष्टम्) — direct
transcription: "ब्रुव ईट् (7.3.93) से हल्आदि पित् सार्वधातुक 'तिप्' को
ईट् आगम होकर 'ब्रू ईट् ति' रहा। गुण एव अवादेश होकर 'ब्रवीति' बन गया।"
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_PIT_TIN_UPADESHA: frozenset = frozenset({"tip", "sip", "mip"})
_DONE = "7_3_93_iw_agama_done"


def _target(state: State):
    if len(state.terms) < 2:
        return None
    dhatu, affix = state.terms[-2], state.terms[-1]
    if "dhatu" not in dhatu.tags:
        return None
    if "".join(v.slp1 for v in dhatu.varnas) != "brU":
        return None
    if "pratyaya" not in affix.tags or not affix.varnas:
        return None
    if affix.meta.get(_DONE):
        return None
    if (affix.meta.get("upadesha_slp1") or "").strip() not in _PIT_TIN_UPADESHA:
        return None
    return affix


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    affix = _target(state)
    if affix is None:
        return state
    affix.varnas.insert(0, parse_slp1_upadesha_sequence("I")[0])
    affix.meta[_DONE] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bruva Iw",
    text_dev              = "ब्रुव ईट्",
    padaccheda_dev        = "ब्रुवः ईट्",
    why_dev               = "(सूत्रम् 7.3.93) ब्रुव ईट्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
