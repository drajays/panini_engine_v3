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


def _aG_luG_term(state: State):
    """*luṅ* *aṅ* vikaraṇa — ārdhadhātuka *śeṣa* per clip.
    Structural: upadeśa 'aG' only appears as the luṅ cli vikaraṇa."""
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "aG":
            continue
        if "ardhadhatuka" in t.tags:
            return None
        return t
    return None


def _sic_luG_term(state: State):
    """luṅ *sic* vikaraṇa — structural gate: `cli_luG_recipe` set by all luṅ recipes."""
    if not state.meta.get("cli_luG_recipe"):
        return None
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        return t
    return None


def _sya_lrt_term(state: State):
    """lṛṭ *sya* vikaraṇa: `lrt_vikarana` meta key is the structural signal."""
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if not t.meta.get("lrt_vikarana"):
            continue
        if "ardhadhatuka" in t.tags:
            return None
        return t
    return None


def _sya_lRG_term(state: State):
    """lṛṅ *sya* vikaraṇa: `lRG_vikarana` meta key is the structural signal."""
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if not t.meta.get("lRG_vikarana"):
            continue
        if "ardhadhatuka" in t.tags:
            return None
        return t
    return None


def _tasi_lut_term(state: State):
    """*Luṭ* *tāsi* *vikaraṇa* — structural: `tAsi_vikaraṇa` key is only set in luṭ."""
    for t in state.terms:
        if t.meta.get("tAsi_vikaraṇa") and "ardhadhatuka" not in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    if _tasi_lut_term(state) is not None:
        return True
    pr = _krt_term(state)
    if pr is not None and "ardhadhatuka" not in pr.tags:
        upa = (pr.meta.get("upadesha_slp1") or "").strip()
        if upa in {"tfc", "gsnuC", "snu", "kta", "ktavatu~", "lyuw", "athuc", "ktri", "ktrim"}:
            return True
    if _aG_luG_term(state) is not None:
        return True
    pr2 = _sic_luG_term(state)
    if pr2 is not None and "ardhadhatuka" not in pr2.tags:
        return True
    if _sya_lrt_term(state) is not None:
        return True
    if _sya_lRG_term(state) is not None:
        return True
    return False


def act(state: State) -> State:
    pr_tasi = _tasi_lut_term(state)
    if pr_tasi is not None:
        pr_tasi.tags.add("ardhadhatuka")
        state.samjna_registry["3.4.114_ardhadhatuka_tasi_lut"] = True
        return state
    pr = _krt_term(state)
    if pr is not None and "ardhadhatuka" not in pr.tags:
        upa = (pr.meta.get("upadesha_slp1") or "").strip()
        if upa in {"tfc", "gsnuC", "snu", "kta", "ktavatu~", "lyuw", "athuc", "ktri", "ktrim"}:
            pr.tags.add("ardhadhatuka")
            state.samjna_registry["3.4.114_ardhadhatuka"] = True
    pr_aG = _aG_luG_term(state)
    if pr_aG is not None:
        pr_aG.tags.add("ardhadhatuka")
        state.samjna_registry["3.4.114_ardhadhatuka_aG_luG"] = True
    pr2 = _sic_luG_term(state)
    if pr2 is not None and "ardhadhatuka" not in pr2.tags:
        pr2.tags.add("ardhadhatuka")
        state.samjna_registry["3.4.114_ardhadhatuka"] = True
    pr3 = _sya_lrt_term(state)
    if pr3 is not None:
        pr3.tags.add("ardhadhatuka")
        state.samjna_registry["3.4.114_ardhadhatuka_sya_lrt"] = True
    pr4 = _sya_lRG_term(state)
    if pr4 is not None:
        pr4.tags.add("ardhadhatuka")
        state.samjna_registry["3.4.114_ardhadhatuka_sya_lRG"] = True
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
