"""
4.2.4  लुबविशेषे  —  VIDHI

Padaccheda: लुप् अविशेषे

लुबविशेषे (4.2.4)
Pāṭha: ashtadhyayi.com data.txt row i=42004 (Art. 14).

The aṇ that 4.2.3 gave (nakṣatreṇa yuktaḥ kālaḥ) is taken away (lup, engine.luk) when the speaker names the time without a division of it (aviśeṣa: adya puṣyaḥ,
not puṣyeṇa yuktā rātriḥ): the stem stays puṣya, 1.1.63 lets no aṅgakārya see the lumat aṇ, and 1.2.51 gives the word the prakṛti's liṅga and vacana.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.luk   import live_taddhita, take_away
from engine.state import State
from engine.vivaksha import vivaksita

_GATE_KEY: str = "4_2_4_lubaviSeze_4"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.4", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.4"
    return state


def _site(state: State):
    i = live_taddhita(state, only_from=("4.2.3",))          # "pūrvasūtra vihitasya": the pratyaya of 4.2.3
    return i if i is not None and i > 0 and vivaksita(state, "arthaViSeSa", "aviSeza") else None


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return _legacy_act(state)
    return take_away(state, i, "lup")


SUTRA = SutraRecord(
    sutra_id              = "4.2.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lubaviSeze",
    text_dev              = "लुबविशेषे",
    samagra_slp1          = "nakzatreRa yuktaH kAlaH iti aviSeze lup",
    samagra_dev           = "'नक्षत्रेण युक्तः कालः' (इति) अविशेषे लुप्",
    padaccheda_dev        = "लुप् अविशेषे",
    why_dev               = "(सूत्रम् 4.2.4) लुबविशेषे।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
