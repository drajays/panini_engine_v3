"""
6.1.64  धात्वादेः षः सः  —  VIDHI (narrow **corrected-v2 P001-C**)

Glass-box row for *ñiṣvidā̃* → *ṣvid* → *svid* before *kta* *niṣṭhā* (**8.2.42**).

General *dhātvādeḥ ṣaḥ saḥ* scope is **not** attempted here (CONSTITUTION Art. 7).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61064 · धात्वादेः षः सः
              padaccheda: धातु-आदेः षः सः
              anuvṛtti:   61045: उपदेशे
  Source #2 — Kāśikā 6.1.64 udāharaṇa:
                षह — सहते
                षिच — सिञ्चति
                धातुग्रहणं किम् ? षोडश
  Cross-check — surface pinned by: tests/unit/test_corrected_prakriyas_v2_bundle.py, tests/unit/test_svinnaH_kta_YizvidA.py
  Reference record: sutra_ref_out/6_1_64.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

META_ARM = "corrected_v2_P001_C_6_1_64_arm"


def cond(state: State) -> bool:
    if len(state.terms) < 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if not t0.varnas:
        return False
    if t0.varnas[0].slp1 != "z":
        return False
    if t0.meta.get("corrected_v2_P001_C_6_1_64_done"):
        return False
    # vārttika सुब्धातुष्ठिवुष्वष्कतीनां प्रतिषेधः: ष्ठिव्, ष्वष्क् keep ṣ.
    if (t0.meta.get("upadesha_slp1") or "").strip() in _PRATISHEDHA:
        return False
    return True


_PRATISHEDHA = {"zWivu~", "zvazka~"}
# The ṭ-varga after ṣ was ṣ's doing (8.4.41 ष्टुना ष्टुः); with ṣ gone it reverts
# (निमित्तापाये नैमित्तिकस्याप्यपायः): ष्टुच् → स्तुच्, ष्णा → स्ना.
_TU_TO_TU = {"w": "t", "W": "T", "q": "d", "Q": "D", "R": "n"}


def act(state: State) -> State:
    t0 = state.terms[0]
    t0.varnas[0] = mk("s")
    if len(t0.varnas) > 1 and t0.varnas[1].slp1 in _TU_TO_TU:
        t0.varnas[1] = mk(_TU_TO_TU[t0.varnas[1].slp1])
    t0.meta["corrected_v2_P001_C_6_1_64_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.64",
    sutra_type=SutraType.VIDHI,
    text_slp1="dhAtvAdeH zaH saH",
    text_dev="धात्वादेः षः सः",
    padaccheda_dev="धात्वादेः / षः / सः",
    why_dev="धात्वादौ षकारस्य सकारः (P001-C ञिष्विदाँ → स्विद्, आर्म्-सीमितम्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
