"""
3.4.114  आर्धधातुकं शेषः  —  SAMJNA

Śeṣa pratyayas that are not sārvadhātuka (3.4.113) are ārdhadhātuka.
Narrow v3 use: tag a *kṛt* pratyaya (**tfc**, **gsnuC**/**snu**, **kta**, …) so
**7.2.35** / **7.3.84** can key off ``ardhadhatuka`` without reading string goals.

When a recipe sets ``state.meta['3_4_114_luN_sic_samjna_arm']``, the *luṅ* *sic*
vikaraṇa placeholder is likewise tagged **ārdhadhātuka** (P026).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _krt_term(state: State):
    for t in state.terms:
        if t.kind == "pratyaya" and "krt" in t.tags:
            return t
    return None


def _sic_luG_term(state: State):
    """
    luṅ *sic* vikaraṇa (P026): recipe arms ``3_4_114_luN_sic_samjna_arm`` so
    ``cond`` does not infer *lakāra* from string goals (CONSTITUTION Art. 2).
    """
    if not state.meta.get("3_4_114_luN_sic_samjna_arm"):
        return None
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        return t
    return None


def cond(state: State) -> bool:
    pr = _krt_term(state)
    if pr is not None and "ardhadhatuka" not in pr.tags:
        upa = (pr.meta.get("upadesha_slp1") or "").strip()
        if upa in {"tfc", "gsnuC", "snu", "kta", "ktavatu~", "lyuw"}:
            return True
    pr2 = _sic_luG_term(state)
    if pr2 is not None and "ardhadhatuka" not in pr2.tags:
        return True
    return False


def act(state: State) -> State:
    pr = _krt_term(state)
    if pr is not None and "ardhadhatuka" not in pr.tags:
        upa = (pr.meta.get("upadesha_slp1") or "").strip()
        if upa in {"tfc", "gsnuC", "snu", "kta", "ktavatu~", "lyuw"}:
            pr.tags.add("ardhadhatuka")
            state.samjna_registry["3.4.114_ardhadhatuka"] = True
    pr2 = _sic_luG_term(state)
    if pr2 is not None and "ardhadhatuka" not in pr2.tags:
        pr2.tags.add("ardhadhatuka")
        state.samjna_registry["3.4.114_ardhadhatuka"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.114",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "ArDaDAtukaM SezaH",
    text_dev       = "आर्धधातुकं शेषः",
    padaccheda_dev = "आर्धधातुकं शेषः",
    why_dev        = "शेषः प्रत्यय आर्धधातुक-संज्ञकः (तृच् इत्यादौ)।",
    anuvritti_from = ("3.4.113",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
