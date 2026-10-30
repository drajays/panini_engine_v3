"""
6.4.6  नृ च  —  VIBHASHA

Padaccheda: नृ (लुप्तषष्ठ्यन्तनिर्देशः) च

नृ च (6.4.6)
Pāṭha: ashtadhyayi.com data.txt row i=64006 (Art. 14).
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


_DIRGHA = {"f": "F"}


def _site(state: State):
    if len(state.terms) < 2:
        return None
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "sup" not in pr.tags or _name(pr) != "Am" or pr.meta.get("nami_dirgha_done"):
        return None
    if _flat(anga) != "nf" or not pr.varnas or "nut_agama_inserted" not in pr.varnas[0].tags:
        return None
    return anga, pr


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return state
    anga, pr = s
    anga.varnas[-1] = mk(_DIRGHA[anga.varnas[-1].slp1])      # नृ + नाम्: the long reading (नॄणाम्); the vā leaves नृणाम्
    pr.meta["nami_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.6",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nf ca",
    text_dev              = "नृ च",
    samagra_slp1          = "nf-aNgasya nAmi dIrGaH uBayaTA",
    samagra_dev           = "नृ-अङ्गस्य नामि दीर्घः उभयथा",
    padaccheda_dev        = "नृ (लुप्तषष्ठ्यन्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 6.4.6) नृ च।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.3',),      # नृ before नाम्: 6.4.3 would lengthen always; here it is optional
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
