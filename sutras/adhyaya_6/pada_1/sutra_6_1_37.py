"""
6.1.37  न सम्प्रसारणे सम्प्रसारणम्  —  VIDHI

Padaccheda: न सम्प्रसारणे सम्प्रसारणम्

न सम्प्रसारणे सम्प्रसारणम् (6.1.37)
Pāṭha: ashtadhyayi.com data.txt row i=61037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import is_stem
from engine.state import State

_YAN = frozenset("yvrl")


def _site(state: State):
    """न सम्प्रसारणे सम्प्रसारणम् — when a samprasāraṇa has just been made (yuvan → yUn by 6.4.133), the yaṇ before it (the y of yuvan) does not itself take
    samprasāraṇa: यूनः, यूना (not *इऊनः)."""
    for t in state.terms:
        if "anga" in t.tags and t.meta.get("6_4_133_done") and not t.meta.get("6_1_37_done") and is_stem(t, "yuvan", tadanta=True):
            vs = [v.slp1 for v in t.varnas]
            if len(vs) >= 3 and vs[-3] in _YAN and vs[-2] in "UuoO":
                return t
    return None


# SHORTCUT S134: see docs/SHORTCUT_LEDGER.md
def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).meta["6_1_37_done"] = True            # the y stays: no later samprasāraṇa rule may take it
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.37",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na samprasAraRe samprasAraRam",
    text_dev              = "न सम्प्रसारणे सम्प्रसारणम्",
    samagra_slp1          = "na samprasAraRe samprasAraRam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न सम्प्रसारणे सम्प्रसारणम्",
    padaccheda_dev        = "न सम्प्रसारणे सम्प्रसारणम्",
    why_dev               = "न सम्प्रसारणे सम्प्रसारणम् — सम्प्रसारणे कृते पूर्वस्य यणः (यकारस्य) सम्प्रसारणं न (यूनः)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
