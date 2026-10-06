"""
7.2.76  रुदादिभ्यः सार्वधातुके  —  VIDHI

Padaccheda: रुद-आदिभ्यः सार्वधातुके

रुदादिभ्यः सार्वधातुके (7.2.76)
Pāṭha: ashtadhyayi.com data.txt row i=72076 (Art. 14).
"""
from __future__ import annotations
from phonology import mk
from engine.state import Term

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_76_rudAdiByaH_76"


# रुद्, स्वप्, श्वस्, अन्, जक्ष् (the rudādi five), by upadeśa
_RUDADI = frozenset({"rudi~r", "Yizvapa~", "Svasa~", "ana~", "jakza~"})
_VAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmrlvSzsh")    # hal minus y


def _find(state: State) -> int | None:
    """रुदादिभ्यः सार्वधातुके: iṭ before a val-initial sārvadhātuka ending —
    रोदिति, स्वपिति. (An apṛkta t/s takes īṭ by 7.3.98 instead: not here.)"""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in _RUDADI:
            return None
        tin = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if tin is None or "tin_adesha_3_4_78" not in tin.tags or tin.meta.get("7_2_76_done"):
            return None
        if tin.varnas[0].slp1 not in _VAL or len(tin.varnas) == 1:
            return None
        up = (tin.meta.get("upadesha_slp1") or "").strip()
        sthani = (tin.meta.get("source_lakara_upadesha") or "").strip()
        if up in {"jhi", "Ji", "Ja", "jha"}:
            return None                           # 7.1.3 makes it ac-initial (रुदन्ति)
        if sthani == "loT" and up in {"mip", "vas", "mas"}:
            return None                           # 3.4.92 āṭ makes it ac-initial (रोदानि)
        if sthani.endswith("G") and up == "mip":
            return None                           # 3.4.101 mip → am (अरोदम्)
        if sthani.endswith("G") and up in {"tip", "sip"}:
            return None                           # apṛkta after 3.4.100: 7.3.98 īṭ instead
        return state.terms.index(tin)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    j = _find(state)
    if j is None:
        return state
    # iṭ is an āgama of the ending (ṭit, 1.1.46) — its own term, so the
    # ending's later ādeśas (3.4.101 tas → tām …) still see the ending
    tin = state.terms[j]
    # the āgama is part of its affix (1.1.46): it shares the ending's kṅit-ness,
    # so 1.1.5 still bars the root's guṇa (रुदितः; but रोदिति before pit ti)
    state.terms.insert(j, Term(kind="pratyaya", varnas=[mk("i")],
                               tags={"agama", "it_agama"}
                                    | ({"kngiti", "sarvadhatuka", "sarvadhatuka_3_4_113"} & tin.tags),
                               meta={"upadesha_slp1": "iw", "is_apit": tin.meta.get("is_apit")}))
    state.terms[j + 1].meta["7_2_76_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.2.76",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "rudAdiByaH sArvaDAtuke",
    text_dev              = "रुदादिभ्यः सार्वधातुके",
    samagra_slp1          = "aNgasya rudAdiByaH sArvaDAtuke iw valAdeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य रुदादिभ्यः सार्वधातुके इट् वलादेः",
    padaccheda_dev        = "रुद-आदिभ्यः सार्वधातुके",
    why_dev               = "(सूत्रम् 7.2.76) रुदादिभ्यः सार्वधातुके।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
