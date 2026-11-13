"""
8.2.29  स्कोः संयोगाद्योरन्ते च  —  VIDHI

Two operational paths:
  1. Arm ``8_2_29_arm``: legacy gate-setter.
  2. Arm ``ashir_8_2_29_recipe``: āśīr-liṅ saṃyoga s-lopa.

āśīr-liṅ path (fires on terms, before _pada_merge):

Step A — yāsuṭ 's' before suṭ 's' (saṃyoga 'ss'):
  Find yāsuṭ term ending in 's' immediately followed by suṭ term (single 's').
  Drop the yāsuṭ-s.  This fires for all forms that have both yāsuṭ + suṭ
  (i.e. t-initial tiṅ: 3sg, 3du, 2du, 2pl).

Step B — suṭ 's' before final pure-consonant tiṅ (saṃyoga at pada-end):
  After Step A: find suṭ term (single 's') followed by a LAST term whose
  varṇas are all consonants (no vowels).  Drop the suṭ term.
  This fires only for 3sg (tiṅ = [t], pure consonant) — giving bhūyāt.
  Does NOT fire for 3du/2du/2pl (tiṅ = tāṃ/tam/ta, all contain vowels).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 82029 · स्कोः संयोगाद्योरन्ते च
              padaccheda: स्-कोः संयोग-आद्योः अन्ते च
              anuvṛtti:   81016: पदस्य | 82023: लोपः | 82026: झलि
  Source #2 — Kāśikā 8.2.29 udāharaṇa:
                लस्जेः — लग्नः
                लग्नवान्
                साधुलक्
  Cross-check — surface pinned by: tests/unit/test_tinanta_ad_ashir_lig_kartari.py, tests/unit/test_tinanta_bhuyat_ashirling.py
  Reference record: sutra_ref_out/8_2_29.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible
from phonology    import HAL

_GATE_KEY: str = "8_2_29_skoH_29"


def _find_lig_ad_suw(state: State) -> int | None:
    """*Ad* vidhi-liṅ*: drop *suṭ* after **7.2.79** (``yās``→``yā``) before *tiṅ*."""
    if not state.meta.get("liG_ad_8_2_29_suw_recipe"):
        return None
    for i, t in enumerate(state.terms):
        if "suw_agama" not in t.tags:
            continue
        if t.meta.get("8_2_29_suw_done"):
            continue
        if i == 0:
            continue
        prev = state.terms[i - 1]
        if "yasut_agama" not in prev.tags:
            continue
        if prev.varnas and prev.varnas[-1].slp1 == "A":
            return i
    return None


def _find_yasut_suw_pair(state: State):
    """Return index of yāsuṭ term that precedes a suṭ term."""
    for i, t in enumerate(state.terms):
        if "yasut_agama" not in t.tags:
            continue
        if t.meta.get("8_2_29_yasut_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "s":
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if "suw_agama" not in nxt.tags:
            continue
        return i
    return None


def _all_hal(t) -> bool:
    return bool(t.varnas) and all(v.slp1 in HAL for v in t.varnas)


_SKOH = frozenset({"s", "k", "K", "g", "G", "N"})          # सकारः and the kavarga
_JHAL = frozenset("kKgGcCjJwWqQtTdDpPbBzsSh")


def _inner_cluster(vs) -> int | None:
    """झलि परतो यः संयोगः (Kāśikā 8.2.29: lagnaḥ, magnaḥ, taṣṭaḥ; maṅktā = mas-n-j-t-ā): a cluster that starts with s or k
    and has, at or after its third place, a jhal that follows a sub-saṃyoga of two or more letters (s-j|t: lasj-ta; s-n|j-t: masnj-ta).
    A lone s-jhal (asti) is no saṃyoga, so it stays; the end-of-pada case is below."""
    i = 0
    while i < len(vs):
        if vs[i].slp1 not in HAL or (i and vs[i - 1].slp1 in HAL):
            i += 1
            continue
        m = i
        while m < len(vs) and vs[m].slp1 in HAL:
            m += 1
        if vs[i].slp1 in ("s", "k") and m < len(vs) and any(v.slp1 in _JHAL for v in vs[i + 2:m]):
            return i
        i = m
    return None


def _find_final_cluster(state: State) -> int | None:
    """स्कोः संयोगाद्योरन्ते च: in the pada (a single merged term, inside the tripāḍī) whose end is a
    consonant cluster, a saṃyoga-initial sakāra or kavarga letter before a jhal drops — भूयास्स्त् → भूयात्,
    by two applications (the loop offers it again for the cluster that is left)."""
    if not state.tripadi_zone or len(state.terms) != 1:
        return None
    vs = state.terms[0].varnas
    inner = _inner_cluster(vs)
    if inner is not None:
        return inner
    k = len(vs)
    while k > 0 and vs[k - 1].slp1 in HAL:
        k -= 1
    if len(vs) - k < 2 or k == 0:
        return None
    if vs[k].slp1 in _SKOH and vs[k + 1].slp1 in _JHAL:
        return k
    return None


def cond(state: State) -> bool:
    if _find_final_cluster(state) is not None:
        return True
    if state.tripadi_zone and len(state.terms) == 1:      # a merged pada with no such cluster: nothing to do (the gate-setter below is pre-merge only)
        return False
    # Recipe paths fire pre-merge (before tripadi zone opens).
    if state.meta.get("ashir_8_2_29_recipe") or state.meta.get("liG_ad_8_2_29_suw_recipe"):
        return bool(state.terms)
    return tripadi_gate_eligible(state, "8.2.29", gate_key=_GATE_KEY)


def act(state: State) -> State:
    k = _find_final_cluster(state)
    if k is not None:
        dropped = state.terms[0].varnas[k].slp1
        del state.terms[0].varnas[k]
        state.meta["__why_now_dev__"] = (
            f"पदान्ते संयोगस्य आदौ वर्तमानस्य सकार-कवर्गयोः ({dropped}) झलि परे लोपः — "
            "भूयास्स्त् → भूयास्त् → भूयात्। (८.२.२९)"
        )
        return state
    j = _find_lig_ad_suw(state)
    if j is not None:
        state.terms.pop(j)
        state.meta.pop("liG_ad_8_2_29_suw_recipe", None)
        state.samjna_registry["8.2.29_lig_ad_suw_lopa"] = True
        return state

    if state.meta.get("ashir_8_2_29_recipe"):
        j = _find_yasut_suw_pair(state)
        if j is None:
            return state

        yāsuṭ = state.terms[j]
        suṭ   = state.terms[j + 1]

        # Step A: drop yāsuṭ-s (last varṇa of yāsuṭ term)
        del yāsuṭ.varnas[-1]
        yāsuṭ.meta["8_2_29_yasut_done"] = True
        state.samjna_registry["8.2.29_yasut_s_lopa"] = True

        # Step B: drop suṭ when followed by final all-consonant tiṅ
        suw_idx = j + 1
        if suw_idx + 1 < len(state.terms):
            tin = state.terms[suw_idx + 1]
            if suw_idx + 1 == len(state.terms) - 1 and _all_hal(tin):
                state.terms.pop(suw_idx)
                state.samjna_registry["8.2.29_suw_s_lopa"] = True

        return state

    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"] = "8.2.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "skoH saMyogAdyorante ca",
    text_dev              = "स्कोः संयोगाद्योरन्ते च",
    samagra_slp1          = "saMyogAdyoH skoH padasya ante Jali ca lopaH",
    samagra_dev           = "संयोगाद्योः स्कोः पदस्य अन्ते झलि च लोपः",
    padaccheda_dev        = "स्-कोः संयोग-आद्योः अन्ते च",
    why_dev               = (
        "आशीर्-लिङि: यासुट्-सकारस्य लोपः (सुट्-पूर्वं संयोग-आदि) — "
        "तदनन्तरं सुट्-सकारस्यापि लोपः यदि पद-अन्ते केवल-व्यञ्जन-तिङ् (३एकवचन)।"
    ),
    anuvritti_from        = ('8.1.1',),
    apavada_of            = ("8.2.23",),   # संयोगान्तस्य लोपः is the general rule; this one names the cluster-initial s / kavarga
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
