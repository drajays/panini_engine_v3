"""
7.1.92  सख्युरसम्बुद्धौ  —  VIDHI

Padaccheda: सख्युः अ-सम्बुद्धौ

In sarvananāmasthāna contexts OTHER than sambodhana, the pratyaya after
sakhi is treated as ṇit (ṇidvat). This causes vṛddhi on the final 'i' of
sakhi (via 7.2.115 acoñṇiti): i → ai (vṛddhi). Then 6.1.78 eco'yavāyāvaḥ:
ai → āy. Result: sakhi → sakhāy + pratyaya.

Engine: arm ``sakhyu_recipe`` + finds the pratyaya term tagged "sarvanamasthana"
(and not sambodhana/sambuddhi). Applies vṛddhi to the stem's final 'i'.
Pāṭha: ashtadhyayi.com data.txt row i=71092 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, is_stem

def _site(state: State):
    """सखि-aṅga (the word, 1.4.7's asakhi; with tadantavidhi) + a sarvanāmasthāna sup that is not sambuddhi."""
    hit = anga_and_sup(state, "7.1.92")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "saKi", tadanta=True) or "sarvanamasthana" not in sup.tags or "sambuddhi" in sup.tags:
        return None
    return None if "Nidvat" in sup.tags else sup


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    sup = _site(state)
    sup.tags.add("Nidvat")      # 7.2.115 (अचो ञ्णिति) reads it: सखि → सखै → (6.1.78) सखाय्
    state.atidesha_map[("sup_after_saKi", "Nit")] = "Nidvat"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.92",
    sutra_type            = SutraType.ATIDESHA,
    text_slp1             = "saKyurasambudDO",
    text_dev              = "सख्युरसम्बुद्धौ",
    samagra_slp1          = "asambudDO sarvanAmasTAne saKyuH Rit",
    samagra_dev           = "असम्बुद्धौ सर्वनामस्थाने सख्युः णित्",
    padaccheda_dev        = "सख्युः अ-सम्बुद्धौ",
    why_dev               = (
        "सखि-शब्दात् सर्वनामस्थान-प्रत्यये (सम्बोधनेतर) ṇिद्वद्भावः → "
        "अचो ञ्णिति (७.२.११५) वृद्धिः: अन्त्य-इकारस्य ऐकारः → "
        "एचोऽयवायावः (६.१.७८): ऐ → आय् → सखाय् + प्रत्ययः।"
    ),
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
