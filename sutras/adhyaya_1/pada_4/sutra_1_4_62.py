"""
1.4.62  अनुकरणं चानितिपरम्  (anukараṇaṃ cānitiрaram)  —  SAMJNA

An onomatopoeic word (anukаraṇa) that is not followed by the particle "iti"
also gets the gati-saṃjñā.

E.g., "ṭhakkura-kara", "paṭa-paṭa" type reduplicated sound-imitation
words compounding directly with a verb root (without intervening iti)
are treated as gati.

v3: registers the gate "1_4_62_anukаrana_gati" to mark that the rule has
    been applied; onomatopoeia detection is left to the recipe (which tags
    terms with "anukаrana").
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return state.samjna_registry.get("1_4_62_anukаrana_gati") is None


def act(state: State) -> State:
    state.samjna_registry["1_4_62_anukаrana_gati"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.62",
    sutra_type=SutraType.SAMJNA,
    text_slp1="anukAraRaM cAnitiрaram",
    text_dev="अनुकरणं चानितिपरम्",
    padaccheda_dev="अनुकरणम् / च / अनिति-परम्",
    why_dev="इतिशब्दपरं न भवति यत् अनुकरणं तत् गति-संज्ञकम् — गति-संज्ञाप्रयोजनार्थं द्वारं स्थाप्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
