"""
3.1.82  स्तन्भुस्तुन्भुस्कन्भुस्कुन्भुस्कुञ्भ्यः श्नुश्च  —  VIBHASHA (the "ca": both vikaraṇas are valid)

Kāśikā 3.1.82: "आद्याश्चत्वारो धातवः सौत्राः, स्कुञ् आप्रवणे एतेभ्यः श्नाप्रत्ययो भवति श्नुश्च। स्तभ्नाति, स्तभ्नोति।
स्तुभ्नाति, स्तुभ्नोति। स्कभ्नाति, स्कभ्नोति। स्कुभ्नाति, स्कुभ्नोति। स्कुनाति, स्कुनोति।"

The five roots (stanBu, stunBu, skanBu, skunBu, skuY; all gaṇa 9) take śnā (3.1.81) and also śnu.
Engine: after 3.1.81 has put śnā next to the root, this rule may swap it for śnu; the default reading keeps
śnā, explore() gives the śnu one.  (A real two-way choice, so typed VIBHASHA.)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_ROOTS = frozenset({"stanBu", "stunBu", "skanBu", "skunBu", "skuY"})


def _site(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip().replace("~", "") not in _ROOTS:
            continue
        v = state.terms[i + 1]
        if "vikarana" in v.tags and (v.meta.get("upadesha_slp1") or "").strip() == "SnA":
            return i + 1
        return None
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    j = _site(state)
    state.terms[j] = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("Snu")),
                          tags={"pratyaya", "vikarana", "upadesha"}, meta={"upadesha_slp1": "Snu"})
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.82",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = 'stanBustunBuskanBuskunBuskuYByaH SnuSca',
    text_dev              = 'स्तन्भुस्तुन्भुस्कन्भुस्कुन्भुस्कुञ्भ्यः श्नुश्च',
    samagra_slp1          = "karttari sArvaDAtuke stanBu~-stunBu~-skanBu~-skunBu~-skuYByaH DAtoH paraH SnuH SnA ca",
    samagra_dev           = "कर्त्तरि सार्वधातुके स्तन्भुँ-स्तुन्भुँ-स्कन्भुँ-स्कुन्भुँ-स्कुञ्भ्यः धातोः परः श्नुः श्ना च",
    padaccheda_dev        = "स्तम्भु-स्तुम्भु-स्कम्भु-स्कुम्भु-स्कुञ्भ्यः श्नुः च",
    why_dev               = "स्तम्भ्वादिभ्यः श्ना श्नुश्च (स्तभ्नाति / स्तभ्नोति) — काशिका ३.१.८२।",
    anuvritti_from        = ('3.1.81',),
    vibhasha_default      = False,
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
