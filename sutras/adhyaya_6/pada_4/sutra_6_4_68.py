"""
6.4.68  वाऽन्यस्य संयोगादेः  —  VIBHASHA

Padaccheda: वा अन्यस्य संयोग-आदेः

वाऽन्यस्य संयोगादेः (6.4.68)
Pāṭha: ashtadhyayi.com data.txt row i=64068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk

_NASAL = frozenset("mnNRY")                      # anunāsika-final: m n ṅ ṇ ñ
_JHAL = frozenset("JBGQDjbgqdKPCWTcwtkpSzsh")


def _head(state: State, i: int):
    """The pratyaya that stands right after the aṅga at ``i`` (an āgama belongs to the affix it precedes; a lopa ghost still counts)."""
    return next((u for u in state.terms[i + 1:] if "agama" not in u.tags), None)


def _name(t) -> str:
    return (t.meta.get("upadesha_slp1") or "").strip()


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _kvi_or_jhal_kngit(h) -> bool:
    """क्विझलोः क्ङिति: a kvip, or a kṅit pratyaya that begins with a jhal."""
    return h is not None and (_name(h) == "kvip" or ("kngiti" in h.tags and bool(h.varnas) and h.varnas[0].slp1 in _JHAL))


_GHU_MA_STHA = frozenset({"dA", "DA", "mA", "sTA", "gA", "pA", "hA", "so"})      # 6.4.66: घु-मा-स्था-गा-पा-जहाति-सा — these keep आ before liṅ


# SHORTCUT S82: the pratyaya is read by its upadeśa name and the root by its flat spelling (no kṛt-family / root-class tag yet) — Lexicon tables (S14)
def _site(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "anga" not in t.tags or t.meta.get("6_4_68_etva_done") or len(t.varnas) < 3:
            continue
        if t.varnas[-1].slp1 != "A" or t.varnas[-2].slp1 in "aAiIuUfFxXeEoO" or _flat(t) in _GHU_MA_STHA:
            continue
        h = _head(state, i)
        if h is not None and "kngiti" in h.tags and _name(h) in ("yAsuw", "yAs", "yAsuT", "yAsuw~"):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    t.varnas[-1] = mk("e")  # ग्लै + यासुट्: ग्लेयात् (the vā leaves ग्लायात्)
    t.meta["6_4_68_etva_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.68",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'vAnyasya saMyogAdeH',
    text_dev              = 'वाऽन्यस्य संयोगादेः',
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke vA anyasya saMyogAdeH kNiti AtaH Gu-mA-sTA-gA-pA-jahAti-sAm eH liNi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके वा अन्यस्य संयोगादेः क्ङिति आतः घु-मा-स्था-गा-पा-जहाति-साम् एः लिङि",
    padaccheda_dev        = "वा अन्यस्य संयोग-आदेः",
    why_dev               = "(सूत्रम् 6.4.68) वाऽन्यस्य संयोगादेः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
