"""
6.4.50  क्यस्य विभाषा  —  VIBHASHA

Padaccheda: क्यस्य विभाषा

क्यस्य विभाषा (6.4.50)
Pāṭha: ashtadhyayi.com data.txt row i=64050 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


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


_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")


# SHORTCUT S84: exercised on the tape only: the loop does not yet attach yaṅ / kyac (3.1.22, 3.1.11 are adhikāra only) — attach them, then add loop cases
def _site(state: State):
    """A ya (kyac / kyaṅ: ``True``) that stands right after a hal-final aṅga and before an ārdhadhātuka pratyaya."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or t.meta.get("6_4_50_lopa_done") or i == 0 or not t.varnas:
            continue
        if _flat(t) not in ("ya", "y") or (_name(t) in ("kyac", "kyaN")) != True:
            continue
        prev = next((u for u in reversed(state.terms[:i]) if u.varnas), None)
        if prev is None or prev.varnas[-1].slp1 not in _HAL:
            continue
        if any("ardhadhatuka" in u.tags for u in state.terms[i + 1:] if u.kind == "pratyaya"):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    t.varnas.clear()        # क्यच् / क्यङ् after a hal: समिधिता (the vā leaves समिध्यिता)
    t.meta["6_4_50_lopa_done"] = True
    t.meta["lopa_6_4_50"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.50",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "kyasya viBAzA",
    text_dev              = "क्यस्य विभाषा",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke kyasya viBAzA nalopaH lopaH halaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके क्यस्य विभाषा नलोपः लोपः हलः",
    padaccheda_dev        = "क्यस्य विभाषा",
    why_dev               = "(सूत्रम् 6.4.50) क्यस्य विभाषा।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.49',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
