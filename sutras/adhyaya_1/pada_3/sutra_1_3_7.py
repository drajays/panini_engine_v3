"""
1.3.7  चुटु  —  SAMJNA

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — first **hal** belonging to **cuṭ** (``CUTU``) in the
  upadeśa is *it*.

• **Scope:** Non-**dhātu**, **sup**-primary term list (same as **1.3.5**).

• **v2 reference:** ``~/Documents/panini_engine_v2/core/it_rules.py``
  ``cond_1_3_7`` /
  ``act_1_3_7``.
"""
from __future__ import annotations

from typing import Optional

from engine        import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state  import State
from phonology     import CUTU
from phonology.varna import HAL_DEV

from sutras.adhyaya_1.pada_3.sutra_1_3_9 import IT_LOPA_TAGS

# **corrected-v2 P004-B:** *ñya* ``Yya`` — initial ``Y`` (ञ्) is *cuṭ*-class *it*; must
# win over *prātipadika*-initial ``S`` (श्) on the stem (also *cuṭ*).
META_P004_B_Yya_CUTU = "corrected_v2_P004_B_Yya_cuTu_arm"
_UPA_Yya = "Yya"


def _eligible_p004_b_yya(state: State):
    if not state.meta.get(META_P004_B_Yya_CUTU):
        return
    for ti, t in enumerate(state.terms):
        if "taddhita" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != _UPA_Yya:
            continue
        vs = t.varnas
        j = _first_hal_idx(vs)
        if j is None:
            continue
        v = vs[j]
        if v.slp1 not in CUTU:
            continue
        if v.tags & IT_LOPA_TAGS:
            continue
        yield ti, t, j


def _terms_sup_or_primary(state: State):
    # P025 *ṇic* ``Term`` (``meta['P025_Nic_pratyaya']``) must win over a leading
    # *prātipadika* stem so **1.3.7** *cuṭu* tags the initial ``N`` of ``Nic``.
    nic_p025 = [
        t
        for t in state.terms
        if t.kind == "pratyaya" and t.meta.get("P025_Nic_pratyaya")
    ]
    if nic_p025:
        return nic_p025
    cand = [
        t
        for t in state.terms
        if "sup" in t.tags
        and "taddhita" not in t.tags
        and not term_is_sup_luk_ghost(t)
    ]
    if cand:
        return cand
    krt = [
        t for t in state.terms
        if "krt" in t.tags and "upadesha" in t.tags
    ]
    if krt:
        return krt
    # **3.1.26** *ṇic* ``Ric`` / **2.1.26** *Nic*: *cuṭū* must target the affix’s
    # initial ``R`` (ण्), not the preceding *dhātu*’s first *hal* (e.g. ``p`` of ``pA``).
    # Restrict to pratyayas whose **first** upadeśa *hal* is ``R`` so other *nic* frames
    # (e.g. *śuk* augment paths) keep the legacy *cuṭū* competition logic.
    nic_ric: list = []
    for t in state.terms:
        if t.kind != "pratyaya" or "nic" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up.endswith("~"):
            up = up[:-1]
        if up not in {"Ric", "Nic"}:
            continue
        vs = t.varnas
        j = _first_hal_idx(vs)
        if j is not None and vs[j].slp1 == "R":
            nic_ric.append(t)
    if nic_ric:
        return nic_ric
    # *luṭ* *ḍā* residue (**qA**): *cuṭ* *it* on ``q`` (recipe ``1_3_7_lut_qA_arm``).
    if state.meta.get("1_3_7_lut_qA_arm"):
        qa = [
            t for t in state.terms
            if "upadesha" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "qA"
        ]
        if qa:
            return qa
    # **P017** (*paṭapaṭāyati*): **``qAc``** (डाच्) must win over preceding *prātipadika*
    # ``pawapawat`` so **1.3.7** *cuṭū* tags initial ``q``, not ``p``.
    if state.meta.get("corrected_v2_P017_1_3_7_qAc_arm"):
        qac = [
            t
            for t in state.terms
            if "upadesha" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "qAc"
        ]
        if qac:
            return qac
    if state.terms:
        return [state.terms[0]]
    return []


def _first_hal_idx(varnas) -> Optional[int]:
    # Use canonical hal inventory (includes ``R`` = ण्), not only ``pratyahara.HAL``.
    for j, v in enumerate(varnas):
        if v.slp1 in HAL_DEV:
            return j
    return None


def _eligible(state: State):
    if not any("upadesha" in t.tags for t in state.terms):
        return
    p04 = next(_eligible_p004_b_yya(state), None)
    if p04 is not None:
        yield p04
        return
    for term in _terms_sup_or_primary(state):
        if "dhatu" in term.tags:
            continue
        try:
            ti = state.terms.index(term)
        except ValueError:
            continue
        vs = term.varnas
        j = _first_hal_idx(vs)
        if j is None:
            continue
        v = vs[j]
        if v.slp1 not in CUTU:
            continue
        if v.tags & IT_LOPA_TAGS:
            continue
        yield ti, term, j


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    got = next(_eligible(state), None)
    if got is None:
        return state
    ti, term, j = got
    v = term.varnas[j]
    v.tags.add("it_candidate_cutu")
    # Include current upadeśa identity in the key so a later pratyaya-substitution
    # that reintroduces a cuṭu-initial hal at the same (ti,j) still records a
    # distinct saṃjñā event (avoids R2 false-positive on re-fires).
    upa = term.meta.get("upadesha_slp1")
    state.samjna_registry[("it_cutu", ti, j, upa)] = frozenset({v.slp1})
    if (
        state.meta.get(META_P004_B_Yya_CUTU)
        and "taddhita" in term.tags
        and (term.meta.get("upadesha_slp1") or "").strip() == _UPA_Yya
    ):
        state.meta.pop(META_P004_B_Yya_CUTU, None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.7",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "cuwu",
    text_dev       = "चुटु",
    padaccheda_dev = "चुटु",
    why_dev        = "चवर्ग-टवर्गीयः प्रथमः हल् ‘इत्’ संज्ञकः; लोपः १.३.९।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
