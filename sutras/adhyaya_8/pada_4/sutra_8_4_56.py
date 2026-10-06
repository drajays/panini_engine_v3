"""
8.4.56  वाऽवसाने  —  VIBHASHA

At avasāna (word boundary / pause), jaś consonants optionally become car
(voiceless stops): both readings are valid (वाक् / वाग्), so every branch is an output (Art. 21 vikalpa).

Phonological predicate: merged pada (single term) ends in a jaś consonant
(d, g, b, j, etc., placed there by 8.2.39 jhal→jaś). Converts to car (voiceless).

Jaś→car map (subset relevant to laṅ/luṅ):  d→t, g→k, j→c, b→p, etc.
For laṅ 3sg, 8.2.39 converts final 't'→'d', then 8.4.56 converts 'd'→'t'.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84056 · वाऽवसाने
              padaccheda: वा अवसाने
              anuvṛtti:   82108: संहितायाम् | 84053: झलाम् | 84054: चर्
  Source #2 — Kāśikā 8.4.56 udāharaṇa:
                अवसाने वर्तमानानां झलां वा चरादेशो भवति
                वाक्
                त्वक्
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhavat_lang.py
  Reference record: sutra_ref_out/8_4_56.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

# jaś → car: voiced obstruents → their voiceless equivalents at avasāna
_JAS_TO_CAR: dict[str, str] = {
    "d": "t",  "D": "T",  "g": "k",  "G": "K",
    "b": "p",  "B": "P",  "j": "c",  "J": "C",
    "q": "w",  "Q": "W",
}


def _find_jas_final(state: State) -> int | None:
    """Find the index of a jaś final consonant in the merged pada."""
    if not state.terms:
        return None
    t = state.terms[0] if len(state.terms) == 1 else None
    if t is None:
        return None
    if not t.varnas:
        return None
    last = t.varnas[-1]
    if last.slp1 in _JAS_TO_CAR:
        return len(t.varnas) - 1
    return None


def cond(state: State) -> bool:
    # वाऽवसाने: inside the tripāḍī, a jaś at the end of the pada has work to do.
    return state.tripadi_zone and _find_jas_final(state) is not None


def act(state: State) -> State:
    i = _find_jas_final(state)
    if i is None:
        return state
    old_slp1 = state.terms[0].varnas[i].slp1
    car_slp1 = _JAS_TO_CAR[old_slp1]
    state.terms[0].varnas[i] = parse_slp1_upadesha_sequence(car_slp1)[0]
    state.samjna_registry["8.4.56_jas_to_car"] = f"{old_slp1}→{car_slp1}"
    state.meta["__why_now_dev__"] = (
        f"अवसाने (पदान्ते विरामे) झलः जशः ({old_slp1}) विकल्पेन चर्-आदेशः ({car_slp1}) — "
        "अन्यतरस्यां पक्षे जश् एव तिष्ठति (वाक् / वाग्)। (८.४.५६)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.56",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = True,       # the car reading is taken; vikalpa.choose({"8.4.56": False}) keeps the jaś
    text_slp1             = 'vAvasAne',
    text_dev              = 'वाऽवसाने',
    samagra_slp1          = "JalAM car avasAne vA",
    samagra_dev           = "झलां चर् अवसाने वा",
    padaccheda_dev        = "वा अवसाने",
    why_dev               = "(सूत्रम् 8.4.56) वाऽवसाने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
