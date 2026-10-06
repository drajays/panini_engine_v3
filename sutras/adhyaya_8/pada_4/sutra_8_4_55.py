"""
8.4.55  खरि च  —  VIDHI

झलाम् (8.4.53) चर् (8.4.54) संहितायाम् (8.2.108): a jhal followed by a khar becomes
its antaratama car (voiceless unaspirated of its own varga).  Tripāḍī only.

    bhaj + ta → bhak-ta (g→k)    dath + ta → dat-ta (th→t)    jaGzatus → jakzatus
    labh + sya → laps-ya (bh→p)

Scans the flattened varṇa stream, so it fires inside a Term and across a Term
boundary alike (empty Terms are invisible, 1.1.60).  Not reached by this rule
(taken earlier in Tripāḍī order): c-varga 8.2.30 (coḥ kuḥ), h 8.2.31 (ho ḍhaḥ);
śṣs are already car.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84055 · खरि च
              padaccheda: खरि । च
              anuvṛtti:   82108: संहितायाम् | 84053: झलाम् | 84054: चर्
  Source #2 — Kāśikā 8.4.55 udāharaṇa:
                भेद् + ता → भेत्ता
                भेद् + तुम् → भेत्तुम्
                भेद् + तव्यम् → भेत्तव्यम्
  Cross-check — surface pinned by: tests/unit/test_BitzIzwa_ashir_ling.py, tests/unit/test_jakzatuH_lit_ad_gas.py
  Reference record: sutra_ref_out/8_4_55.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import KHAR

# jhal → car (antaratama).  c-varga and h are 8.2.30 / 8.2.31's; ś ṣ s are already car.
_JHAL_CAR: dict[str, str] = {
    "G": "k", "g": "k", "K": "k",
    "Q": "w", "q": "w", "W": "w",
    "D": "t", "d": "t", "T": "t",
    "B": "p", "b": "p", "P": "p",
}


def _hits(state: State) -> list[tuple[int, int]]:
    flat = [(ti, vi) for ti, t in enumerate(state.terms) for vi in range(len(t.varnas))]
    out = []
    for (ti, vi), (tj, vj) in zip(flat, flat[1:]):
        if state.terms[ti].varnas[vi].slp1 in _JHAL_CAR and state.terms[tj].varnas[vj].slp1 in KHAR:
            out.append((ti, vi))
    return out


def cond(state: State) -> bool:
    return bool(state.tripadi_zone) and bool(_hits(state))


def act(state: State) -> State:
    if not state.tripadi_zone:
        return state
    changes = []
    for ti, vi in _hits(state):
        old = state.terms[ti].varnas[vi].slp1
        new = _JHAL_CAR[old]
        state.terms[ti].varnas[vi] = mk(new)
        changes.append(f"{old}→{new}")
    if changes:
        state.meta["__why_now_dev__"] = (
            f"खर्-वर्णे परे झल् → अन्तरतमः चर् ({', '.join(changes)}); "
            "यथा भज्+त → भक्त, दथ्+त → दत्त। (८.४.५५)"
        )
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.55",
    sutra_type=SutraType.VIDHI,
    text_slp1="Kari ca",
    text_dev="खरि च",
    samagra_slp1="JalAm Kari car saMhitAyAm",
    samagra_dev="झलाम् खरि चर् संहितायाम्",
    padaccheda_dev="खरि च",
    why_dev="खरि परे झलः स्थाने अन्तरतमः चर् (चर्त्वम्)।",
    anuvritti_from=("8.4.53",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
