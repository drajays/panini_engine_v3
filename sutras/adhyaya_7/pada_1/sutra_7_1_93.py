"""
7.1.93  अनङ् सौ  —  VIDHI

Padaccheda: अनङ् सौ

In the 1sg (sau = su pratyaya context), the stem sakhi takes the ādeśa
"anang" (= aN = [a,n] after ṅ-IT lopa). ṅit→antya-ādeśa: replaces the
final 'i' of sakhi with [a,n].

Result: sakh+[i] → sakh+[a,n] = sakhan
Then 6.4.8 dīrgha: sakhān
Then 6.1.68 apṛkta s-lopa, then 8.2.7 n-lopa: sakhā

Engine: arm ``anaN_recipe`` + finds sakhi-type stem (prātipadika ending in 'i'
tagged sakhi_ikarant) and replaces final 'i' with [a,n] (anang after ṅ-lopa).
Pāṭha: ashtadhyayi.com data.txt row i=71093 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, is_stem
from phonology     import mk

def _site(state: State):
    """सखि + su (sau) that is not sambuddhi: the aṅga's last letter i becomes अनङ् (a n; ṅit, so it replaces only the final)."""
    hit = anga_and_sup(state, "7.1.93")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "saKi", tadanta=True) or "sambuddhi" in sup.tags or anga.meta.get("7_1_93_done"):
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() not in {"s~", "su", "su~"} or "vib_prathama" not in sup.tags:
        return None
    return anga if anga.varnas[-1].slp1 == "i" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1:] = [mk("a"), mk("n")]
    anga.meta["7_1_93_done"] = True
    anga.tags.add("an_pratipadika")        # the anaṅ-made न् is a prātipadika-final न्: 8.2.7 reads it (as after 7.1.94)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.93",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "anaN sO",
    text_dev              = "अनङ् सौ",
    samagra_slp1          = "asambudDO sO saKyuH anaN",
    samagra_dev           = "असम्बुद्धौ सौ सख्युः अनङ्",
    padaccheda_dev        = "अनङ् सौ",
    why_dev               = (
        "सखि-शब्दस्य सौ-प्रत्यये परे 'अनङ्'-आदेशः — "
        "अन्त्य-इकारस्य स्थाने [अ,न्] (ṅकार-लोपानन्तरम्): "
        "सखि → सखन् → सखान् → सखा।"
    ),
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ('7.1.92',),     # su: अनङ्, not the ṇidvat of the other sarvanāmasthānas
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
