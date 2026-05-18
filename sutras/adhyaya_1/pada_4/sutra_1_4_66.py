"""
1.4.66  कणेमनसी श्रद्धाप्रतीघाते  (kaṇe-manasī śraddhā-pratīghāte)  —  SAMJNA

The words "kaṇe" (in the ear/whisper sense) and "manasi" (in the mind sense)
get the gati-saṃjñā when used with the meaning of śraddhā (faith/trust) or
pratīghāta (hostility/resistance).

E.g., "kaṇe-kṛ" = to whisper in the ear; "manasi-kṛ" = to fix in the mind.

v3: registers samjna_registry["gati_kane_manasi"] = frozenset({"kaRe","manasi"}).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_KANE_MANASI: frozenset[str] = frozenset({"kaRe", "manasi"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_kane_manasi") is None


def act(state: State) -> State:
    state.samjna_registry["gati_kane_manasi"] = _KANE_MANASI
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _KANE_MANASI
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.66",
    sutra_type=SutraType.SAMJNA,
    text_slp1="kaRemanasI SradDApratIGAte",
    text_dev="कणेमनसी श्रद्धाप्रतीघाते",
    padaccheda_dev="कणे-मनसी / श्रद्धा-प्रतीघाते",
    why_dev="श्रद्धाप्रतीघाते 'कणे' 'मनसि' शब्दौ गति-संज्ञकौ — द्वौ शब्दौ गति-सेटे योज्येते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
