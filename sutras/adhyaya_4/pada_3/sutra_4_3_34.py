"""
4.3.34  श्रवणाद्द्विवचनाच्च  —  VIDHI (narrow: **luk** of **aṇ** after *viśākhā*) — P039

The full *gaṇa* (“*śravaṇā* … *viśākhā* …”) is not modelled; this slice only
removes the **aṇ** *pratyaya* Term inserted for **P039**, matching the JSON
``output_slp1``: ``viSAKA+0`` (*luk*).

Actual *pratyaya-lopa* is structural removal here; **1.1.60**/**1.1.61** in the
recipe then supply the *lopa* / *luk*-saṃjñā spine cited in the JSON.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 43034 · श्रविष्ठाफल्गुन्यनुराधास्वातितिष्यपुनर्वसुहस्तविशाखाऽषाढाबहुलाल्लुक्
              padaccheda: श्रविष्ठा-फल्गुनी-अनुराधा-स्वाति-तिष्य-पुनर्वसु-हस्त-विशाखा-अषाढा-बहुलात् लुक्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः | 42092: शेषे | 43025: तत्र जातः
  Source #2 — Kāśikā 4.3.34 udāharaṇa:
                तस्मिन् स्त्रीप्रत्ययस्यापि   इति लुग् भवति
                श्रविष्ठासु जातः श्रविष्ठः
                फल्गुनः
  Cross-check — surface pinned by: tests/unit/test_viSAKaH_taddhita_luk_aR_paribhasha.py
  Reference record: sutra_ref_out/4_3_34.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_aR_idx(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "aR":
            continue
        if i > 0 and "P039_viSAKA_demo" in state.terms[i - 1].tags:
            return i
    return None


def cond(state: State) -> bool:
    return _find_aR_idx(state) is not None


def act(state: State) -> State:
    j = _find_aR_idx(state)
    if j is None:
        return state
    state.terms.pop(j)
    state.samjna_registry["P039_4_3_34_aR_luk_structural"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.3.34",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "zravaRAd dvivacanAcca (luk aR) (narrow P039)",
    text_dev       = "श्रवणाद्द्विवचनाच्च (लुक्-अण्) — P039 संक्षेपः",
    padaccheda_dev = "श्रवणात् / द्विवचनात् / च",
    why_dev        = "विशाखायाः अण्-प्रत्ययस्य लुक् (४.३.३४) — P039 संक्षेप-छेदः।",
    anuvritti_from = ("4.3.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
