"""
7.2.35  आर्धधातुकस्येड् वलादेः  —  VIDHI

Narrow v3: prepend **i** (iṭ āgama) on the **kṛt** ``Term`` so it stands
immediately before a following pratyaya that begins with a **velar-class**
(varga) obstruent — approximated as the first pratyaya letter in ``HAL`` but
not in ``YAN``.

Blocked by **7.2.10** via ``state.blocked_sutras`` for ekāc **anudātta** dhātus.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL, mk
from phonology.pratyahara import YAN


def _val_initial(pr_first: str) -> bool:
    if pr_first not in HAL:
        return False
    if pr_first in YAN:
        return False
    return True


def _target_term(state: State):
    allow_sic = bool(state.meta.get("7_2_35_allow_sic", False))
    if allow_sic:
        for t in state.terms:
            if (t.meta.get("upadesha_slp1") or "").strip() == "sic":
                return t
        return None
    return state.terms[-1] if state.terms else None


def _lut_tasi_vikaranha_index(state: State) -> int | None:
    """
    *luṭ* recipe: *tāsi* *vikaraṇa* ``Term`` (``tAsi_vikaraṇa``) takes initial *iṭ*
    when the following *tiṅ* residue begins with a *valādi* consonant (*tip*
    → ``ti``).
    """
    if not state.meta.get("7_2_35_lut_tAsi_it_arm"):
        return None
    for j in range(len(state.terms) - 1):
        t = state.terms[j]
        if not t.meta.get("tAsi_vikaraṇa"):
            continue
        if "ardhadhatuka" not in t.tags:
            continue
        if t.meta.get("it_agama_7_2_35_done"):
            continue
        nxt = state.terms[j + 1]
        if not nxt.varnas:
            continue
        if not _val_initial(nxt.varnas[0].slp1):
            continue
        return j
    return None


def cond(state: State) -> bool:
    j = _lut_tasi_vikaranha_index(state)
    if j is not None:
        return True
    if len(state.terms) < 2:
        return False
    d0 = state.terms[0]
    if "dhatu" not in d0.tags:
        return False
    # v3 default: kṛt only. Pipelines may opt-in for sic in luṅ.
    allow_sic = bool(state.meta.get("7_2_35_allow_sic", False))
    pr = _target_term(state)
    if pr is None:
        return False
    if "krt" not in pr.tags:
        if not allow_sic:
            return False
        # In luṅ pipelines, iṭ is applied to the sic-term (not the final tiṅ residue).
        if (pr.meta.get("upadesha_slp1") or "").strip() != "sic":
            return False
    if "ardhadhatuka" not in pr.tags:
        # For luṅ-sic use, we key off an explicit pipeline flag so cond()
        # remains mechanically blind about lakāra/prayoga choices.
        if not (allow_sic and state.meta.get("luN_sic_ardhadhatuka", False)):
            return False
    if pr.meta.get("it_agama_7_2_35_done"):
        return False
    if not pr.varnas:
        return False
    return _val_initial(pr.varnas[0].slp1)


def act(state: State) -> State:
    j = _lut_tasi_vikaranha_index(state)
    if j is not None:
        t = state.terms[j]
        it_v = mk("i")
        it_v.tags.add("it_agama")
        t.varnas.insert(0, it_v)
        t.meta["it_agama_7_2_35_done"] = True
        return state
    pr = _target_term(state)
    if pr is None:
        return state
    it_v = mk("i")
    it_v.tags.add("it_agama")
    pr.varnas.insert(0, it_v)
    pr.meta["it_agama_7_2_35_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.35",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ArDaDAtukasyeQ valAdeH",
    text_dev       = "आर्धधातुकस्येड् वलादेः",
    padaccheda_dev = "आर्धधातुकस्य इट् वलादेः",
    why_dev        = "आर्धधातुके परे वल्-प्रथमादौ इट्-आगमः (प्रतिषेधे न)।",
    anuvritti_from = ("7.2.34",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
