"""
6.4.20  ज्वरत्वरस्रिव्यविमवामुपधायाश्च  —  VIDHI

Padaccheda: ज्वर-त्वर-स्रिवि-अवि-मवाम् उपधायाः च

ज्वरत्वरश्रिव्यविमवामुपधायाश्च (6.4.20)
Pāṭha: ashtadhyayi.com data.txt row i=64020 (Art. 14).
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


_ROOTS = frozenset({"jvar", "tvar", "sriv", "av", "mav"})      # ज्वर त्वर स्रिवि अव मव: the v and the upadhā give way to ū


# SHORTCUT S82: the pratyaya is read by its upadeśa name and the root by its flat spelling (no kṛt-family / root-class tag yet) — Lexicon tables (S14)
def _site(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "anga" not in t.tags or t.meta.get("6_4_20_uth_done") or _flat(t) not in _ROOTS:
            continue
        if _kvi_or_jhal_kngit(_head(state, i)):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    flat = _flat(t)
    v = next(k for k, x in enumerate(t.varnas) if x.slp1 == "v")
    lo, hi = (v, v + 2) if flat in ("jvar", "tvar") else (len(t.varnas) - 2, len(t.varnas))      # jvara: va → ū; srivu / ava / mava: (upadhā + v) → ū
    t.varnas[lo:hi] = [mk("U")]
    t.meta["6_4_20_uth_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'jvaratvarasrivyavimavAmupaDAyASca',
    text_dev              = 'ज्वरत्वरस्रिव्यविमवामुपधायाश्च',
    samagra_slp1          = "aNgasya jvara-tvara-srivi-avi-mavAm upaDAyAH ca kvi-JaloH kNiti Sa-UW cC-voH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ज्वर-त्वर-स्रिवि-अवि-मवाम् उपधायाः च क्वि-झलोः क्ङिति श-ऊठ् च्छ्-वोः",
    padaccheda_dev        = "ज्वर-त्वर-स्रिवि-अवि-मवाम् उपधायाः च",
    why_dev               = "(सूत्रम् 6.4.20) ज्वरत्वरश्रिव्यविमवामुपधायाश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
