"""
8.2.30  चोः कुः  —  VIDHI

Operational role (v3.6, demo slice for `1145.md`):
  If a dhātu ends in 'c' (cu-varṇa) and the following sound begins with a
  jhal (e.g. 't'), replace that final 'c' with 'k' (ku-varṇa).

Example:
  u c + t  → u k + t

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82030 · चोः कुः
              padaccheda: चोः कुः
              anuvṛtti:   81016: पदस्य | 82026: झलि | 82029: अन्ते च
  Source #2 — Kāśikā 8.2.30 udāharaṇa:
                पक्ता
                पक्तुम्
                पक्तव्यम्
  Cross-check — surface pinned by: tests/unit/test_agnicit_agni_ci_kvip.py, tests/unit/test_corrected_prakriyas_v2_bundle.py, tests/unit/test_gArgyAH_garga_yaY_luk.py
  Reference record: sutra_ref_out/8_2_30.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import JHAL

META_PRE_TRIPADI_P003_A = "corrected_v2_P003_A_8_2_30_arm"


# चोः कुः — the whole cu-varga (by sthāna/prayatna, 1.1.50)
_CU = {"c": "k", "C": "K", "j": "g", "J": "G"}


def _find(state: State):
    # 1) Intra-term: ... c + JHAL ...
    for ti, t in enumerate(state.terms):
        if t.meta.get("8_2_30_cutuku_done"):
            continue
        vs = t.varnas
        for vi in range(len(vs) - 1):
            if vs[vi].slp1 in _CU and vs[vi + 1].slp1 in JHAL:
                # a cu-varga letter before another (cC, cc, jj, jJ) is a stem-internal cluster (accha, icchā, lāmajjaka), not a
                # pada-final c meeting a jhal (vāc+bhiḥ, pac+ta) — coḥ kuḥ leaves it alone
                if vs[vi + 1].slp1 in _CU:
                    continue
                return (ti, vi)
    # 2) Cross-term boundary: X ends with c, next begins with JHAL.
    for i in range(len(state.terms) - 1):
        left = state.terms[i]
        right = state.terms[i + 1]
        if left.meta.get("8_2_30_cutuku_done"):
            continue
        if not left.varnas or left.varnas[-1].slp1 not in _CU:
            continue
        if not right.varnas or right.varnas[0].slp1 not in JHAL:
            continue
        return (i, len(left.varnas) - 1)
    # 3) पदान्ते (anuvṛtti अन्ते च, 8.2.29): merged pada ends in c with nothing
    #    following (avasāna) — वाच् -> वाक्.
    if len(state.terms) == 1:
        t = state.terms[0]
        if (
            "pada" in t.tags
            and not t.meta.get("8_2_30_cutuku_done")
            and t.varnas
            and t.varnas[-1].slp1 in _CU
        ):
            return (0, len(t.varnas) - 1)
    return None


def _has_ktrim_krt(state: State) -> bool:
    """Structural: a kṛt Term with ``ktrim`` upadeśa is present — pre-tripāḍī *coḥ kuḥ* allowed."""
    return any(
        "krt" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "ktrim"
        for t in state.terms
    )


def cond(state: State) -> bool:
    if _find(state) is None:
        return False
    if _has_ktrim_krt(state):
        return True
    return bool(state.tripadi_zone)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    t.varnas[vi] = mk(_CU[t.varnas[vi].slp1])     # c→k, ch→kh, j→g, jh→gh
    t.meta["8_2_30_cutuku_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.30",
    sutra_type=SutraType.VIDHI,
    text_slp1="coH kuH",
    text_dev="चोः कुः",
    samagra_slp1="coH kuH Jali padasya ante",
    samagra_dev="चोः कुः झलि पदस्य अन्ते",
    padaccheda_dev="चोः कुः",
    why_dev="झलि/पदान्ते परे च-वर्णस्य क-वर्णादेशः (उक्त-उपपत्ति)। "
             "प००३-ए: त्रिपादी-प्रवेशात् पूर्वम् अनुमतम्।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

