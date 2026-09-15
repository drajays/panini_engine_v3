"""
8.4.47 अनचि च — VIDHI (यर्-विकल्प-द्वित्व, saṃhitā)

Sources consulted:
- ashtadhyayi.com data.txt row i=84047
- Kāśikā: "कृष्णः → कृष्ष्णः", "मत्यत्र → मत्त्यत्र", "रामात् → रामात्त्"
- Kāśikā vārttikas on **8.4.47** (द्वित्व):
  - यणो मयो द्वे वाच्ये — यणात् परो मय् / मयात् परो यण् (वाल्मीकि, दध्य्यत्र)
  - शरः खयो द्वे वाच्ये — शरात् परो खय् / खयात् परः शर् (स्थाता, अप्सरा)
  - अवसाने च — covered by *anaci* when a pada ends in *ac* + *hal*
- Cross-validation: pipelines/yar_anaci_dvitva_tripadi.py;
  tests/unit/test_madhvari_madhu_ari_dvitva_lesson.py (**6.1.77** *v* is not doubled;
  **a**+**d** in *madhu* still geminates → *maddhvari* per **1.1.58** *dvirvacana*)

Anuvṛtti of **8.4.46** *द्वे* + **8.2.108** *saṃhitā*: optional gemination (*vikalpa*) when the
target consonant is not immediately followed by *ac*.  Kāśikā vārttikas extend this to
यण्‖मय् and शर्‖खय् adjacencies (no *ac* on the left).  The general *anaci* path doubles
*yar* (*hal* − *h*) after *ac*; **8.4.46** doubles the *following* *yar* when *r* / *h*
intervene after *ac*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import HAL, YAN
from phonology.varna import AC_DEV

from sutras.adhyaya_6.pada_1.sutra_6_1_77 import IKO_YANACI_ADESHA_TAG

# यर् = हकारं विहाय सर्वाणि व्यञ्जनानि (lesson); engine: HAL − {h}.
_AC = frozenset(AC_DEV.keys())
_YAR_HAL = HAL - frozenset({"h"})
_RAH = frozenset({"r", "h"})
# मय् = ञकारं विहाय सर्वाणि वर्गीयव्यञ्जनानि (Kāśikā vārttika).
_MAY = frozenset(
    {"k", "K", "g", "G", "N", "c", "C", "j", "J", "w", "W", "q", "Q", "R",
     "t", "T", "d", "D", "n", "p", "P", "b", "B", "m"}
)
# शर् = श् ष् स् ; खय् = वर्गप्रथमौ द्वितीयौ च.
_SHAR = frozenset({"S", "z", "s"})
_KHAY = frozenset({"k", "K", "c", "C", "w", "W", "t", "T", "p", "P"})
_DVITVA_TAG = "yar_dvitva_8_4_47"


def _flat_varnas(state: State) -> list[tuple[int, int, str]]:
    out: list[tuple[int, int, str]] = []
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            out.append((ti, vi, v.slp1))
    return out


def _right_not_followed_by_ac(flat: list[tuple[int, int, str]], left_i: int) -> bool:
    """True when the consonant at ``left_i + 1`` is not immediately followed by *ac*."""
    return left_i + 2 >= len(flat) or flat[left_i + 2][2] not in _AC


def _already_doubled(state: State, ti: int, vi: int) -> bool:
    return _DVITVA_TAG in state.terms[ti].varnas[vi].tags


def _find_vartika_dvitva(state: State) -> tuple[int, int] | None:
    """Kāśikā vārttikas यणो मयो द्वे / शरः खयो द्वे (phase 1 — before *anaci*)."""
    flat = _flat_varnas(state)
    n = len(flat)
    for i in range(n - 1):
        left, right = flat[i][2], flat[i + 1][2]
        ti_r, vi_r = flat[i + 1][0], flat[i + 1][1]
        if _already_doubled(state, ti_r, vi_r):
            continue
        # यणो मयो (पञ्चमी-षष्ठी): यणात् परो मय्
        if left in YAN and right in _MAY:
            return (ti_r, vi_r)
        # मयो यणो (षष्ठी-पञ्चमी): मयात् परो यण् — not when मय् immediately follows *ac*
        if left in _MAY and right in YAN and (i == 0 or flat[i - 1][2] not in _AC):
            return (ti_r, vi_r)
        # शरः खयो: शरात् परो खय्
        if left in _SHAR and right in _KHAY:
            return (ti_r, vi_r)
        # खयो शरः: खयात् परः शर्
        if left in _KHAY and right in _SHAR:
            return (ti_r, vi_r)
    return None


def _find_anaci_yar_dvitva(state: State) -> tuple[int, int] | None:
    flat = _flat_varnas(state)
    n = len(flat)
    for i in range(n - 1):
        if flat[i][2] not in _AC:
            continue
        ti_y, vi_y, yar_slp = flat[i + 1]
        if yar_slp not in _YAR_HAL or yar_slp in _RAH:
            continue
        if _already_doubled(state, ti_y, vi_y):
            continue
        # **1.1.58** (*dvirvacana*): **6.1.77** *yaṇ* ādeśa is *para-nimitta* — do not
        # geminate the ādeśa itself (``u``→``v``); other sites (``a``+``d`` in *madhu*) stand.
        if IKO_YANACI_ADESHA_TAG in state.terms[ti_y].varnas[vi_y].tags:
            continue
        if not _right_not_followed_by_ac(flat, i):
            continue
        # Defer to vārttika when the consonant after *ac* heads a शर्‖खय् pair.
        if i + 2 < n:
            c1, c2 = yar_slp, flat[i + 2][2]
            if (c1 in _KHAY and c2 in _SHAR) or (c1 in _SHAR and c2 in _KHAY):
                continue
        # Defer when *ac* + यण् and यणात् परो मय् (वाल्मीकि).
        if i + 2 < n and yar_slp in YAN and flat[i + 2][2] in _MAY:
            continue
        return (ti_y, vi_y)
    return None


def _find_dvitva_site(state: State) -> tuple[int, int] | None:
    return _find_vartika_dvitva(state) or _find_anaci_yar_dvitva(state)


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find_dvitva_site(state) is not None


def act(state: State) -> State:
    hit = _find_dvitva_site(state)
    if hit is None:
        return state
    ti, vi = hit
    v = state.terms[ti].varnas[vi]
    dup = mk(v.slp1)
    dup.tags.update(v.tags)
    dup.tags.add(_DVITVA_TAG)
    v.tags.add(_DVITVA_TAG)
    state.terms[ti].varnas.insert(vi + 1, dup)
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.47",
    sutra_type=SutraType.VIDHI,
    text_slp1="anaci ca",
    text_dev="अनचि च",
    padaccheda_dev="अनचि च",
    why_dev=(
        "अचः परो यर् (ह-वर्जितः) अनचि परे विकल्पेन द्वित्वम्; "
        "काशिकावार्त्तिके यणो मयो द्वे, शरः खयो द्वे; "
        "८.४.४६ अपवादेन र-ह-वर्णौ न द्विर्येते।"
    ),
    anuvritti_from=("8.4.46", "8.2.108"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
