"""
3.4.114  आर्धधातुकं शेषः  —  SAMJNA

Sources consulted:
- ashtadhyayi.com data.txt row i=34114
- Kāśikā: "तिङः शितश्च वर्जयित्वान्यः प्रत्ययः शेषो धातुसंशब्दनेन विहित आर्धधातुकसंज्ञो भवति। लविता। लवितुम्। लवितव्यम्।"
  pratyudāharaṇa: "धातोरित्येव — वृक्षत्वम्, वृक्षतास्ति। लूभ्याम्, लूभिः।"
- Cross-validation: tests/regression/test_ktva_loop.py (ktvā: पठित्वा takes iṭ, भूत्वा / गत्वा do not);
  tests/forward/test_forward_krdanta_trc.py

Śeṣa pratyayas that are not sārvadhātuka (3.4.113) are ārdhadhātuka. A *kṛt* — taught after a dhātu (3.1.91) — is
ārdhadhātuka unless it is śit (śatṛ, śānac, śa …: 3.4.113), so **7.2.35** / **7.3.84** read ``ardhadhatuka``. The
vikaraṇas sic, aṅ, sya, tāsi are named the same way.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_4.sutra_3_4_113 import SIT_KRT_SARVADHATUKA_SLP1


def _krt_term(state: State):
    for t in state.terms:
        if t.kind == "pratyaya" and "krt" in t.tags:
            return t
    return None


def _sesa_krt(pr) -> bool:
    """तिङ्शिद्भ्योऽन्यः: a kṛt not yet named, and not śit (its upadeśa's initial ś is an it, 1.3.8)."""
    if pr is None or "ardhadhatuka" in pr.tags or "sarvadhatuka_3_4_113" in pr.tags:
        return False
    up = (pr.meta.get("upadesha_slp1_original") or pr.meta.get("upadesha_slp1") or "").strip()
    return not (up.startswith("S") or up in SIT_KRT_SARVADHATUKA_SLP1 or "S" in (pr.meta.get("it_markers") or ()))


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
    """luṅ *sic* vikaraṇa — a pratyaya that is neither tiṅ nor śit, hence ārdhadhātuka śeṣa."""
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
    if _sesa_krt(_krt_term(state)):
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
    if _sesa_krt(pr):
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
    samagra_slp1   = "tiN-Sit-SezaH DAtoH paraH pratyayaH ArDaDAtukaH",
    samagra_dev    = "तिङ्-शित्-शेषः धातोः परः प्रत्ययः आर्धधातुकः",
    padaccheda_dev = "आर्धधातुकं शेषः",
    why_dev        = "शेषः प्रत्यय आर्धधातुक-संज्ञकः (तृच् इत्यादौ)।",
    anuvritti_from = ("3.4.113",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
