"""
6.4.33  भञ्जेश्च चिणि  —  VIBHASHA

Padaccheda: भञ्जेः च चिणि

भञ्जेश्च चिणि (6.4.33)
Pāṭha: ashtadhyayi.com data.txt row i=64033 (Art. 14).
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


# SHORTCUT S82: the pratyaya is read by its upadeśa name and the root by its flat spelling (no kṛt-family / root-class tag yet) — Lexicon tables (S14)
def _site(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or t.meta.get("6_4_33_nalopa_done") or _flat(t) != "BaYj":
            continue
        h = _head(state, i)
        if h is not None and _name(h) == "ciR":
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    del t.varnas[-2]        # भञ्ज् + चिण्: अभाजि (the vā leaves अभञ्जि)
    t.meta["6_4_33_nalopa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.33",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "BaYjeSca ciRi",
    text_dev              = "भञ्जेश्च चिणि",
    samagra_slp1          = "aNgasya asidDavadatrABAt BaYjeH ca ciRi nalopaH upaDAyAH na jAnta-naSAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भञ्जेः च चिणि नलोपः उपधायाः न जान्त-नशाम्",
    padaccheda_dev        = "भञ्जेः च चिणि",
    why_dev               = "(सूत्रम् 6.4.33) भञ्जेश्च चिणि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
