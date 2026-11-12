"""
3.1.70  वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः  —  VIBHASHA

Kāśikā 3.1.70: "उभयत्र विभाषेयम्" — for BrAS, BlAS, Bram, kram, klam, tras, truw, laz the kartari
sārvadhātuka vikaraṇa is optionally śyan (bhrāśyate / bhrāśate, bhrāmyati / bhramati, krāmyati /
krāmati, trasyati / trasati, truṭyati / truṭati, laṣyati / laṣati).  "Both ways" (ubhayatra): for a
root whose gaṇa gives śap (1) or śa (6) the option is śyan instead of it; for a divādi root
(Bhram, klam, tras) 3.1.69's śyan is itself optional, the other reading is śap.

Engine: the vikaraṇa Term next to the root is swapped (Sap/Sa → SyaN; SyaN → Sap).  The default
reading is the unchanged one; explore() gives the other.  The swap is made once (meta
3_1_70_done); on the divādi side it also bars 3.1.69 from putting śyan back.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_ROOTS = frozenset({"wuBrASf", "wuBlASf", "Bramu", "kramu", "klamu", "trasI", "truwa", "laza"})
_DONE = "3_1_70_done"
SAP_BACK = "3_1_70_sap"


def _site(state: State):
    """(index of the vikaraṇa, its upadeśa) right after a listed root of gaṇa 1/4/6, or None."""
    if state.meta.get(_DONE):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip().replace("~", "") not in _ROOTS:
            continue
        if t.meta.get("gana") not in (1, 4, 6):
            continue
        v = state.terms[i + 1]
        up = (v.meta.get("upadesha_slp1") or "").strip()
        # gaṇa 4 waits for 3.1.69's śyan (then the option is śap); gaṇa 1/6 swap śap/śa for śyan
        want = ("Syan", "SyaN") if t.meta.get("gana") == 4 else ("Sap", "Sa")
        if "vikarana" in v.tags and up in want:
            return i + 1, up
        return None
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    j, up = _site(state)
    if up in ("Syan", "SyaN"):
        new = Term(kind="pratyaya", varnas=parse_slp1_upadesha_sequence("Sap"),
                   tags={"pratyaya", "vikarana", "upadesha", "3_1_68_sap"}, meta={"upadesha_slp1": "Sap"})
        state.meta[SAP_BACK] = True
    else:
        new = Term(kind="pratyaya", varnas=parse_slp1_upadesha_sequence("SyaN"),
                   tags={"pratyaya", "vikarana", "upadesha"}, meta={"upadesha_slp1": "Syan"})
    state.terms[j] = new
    state.meta[_DONE] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.70",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "vA BrASaBlASaBramukramuklamutrasitruwilazaH",
    text_dev              = "वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः",
    samagra_slp1          = "karttari sArvaDAtuke BrASa-BlASa-Bramu-kramu-klamu-trasi-truwi-lazaH DAtoH paraH Syan vA",
    samagra_dev           = "कर्त्तरि सार्वधातुके भ्राश-भ्लाश-भ्रमु-क्रमु-क्लमु-त्रसि-त्रुटि-लषः धातोः परः श्यन् वा",
    padaccheda_dev        = "वा भ्राश-भ्लाश-भ्रमु-क्रमु-क्लमु-त्रसि-त्रुटि-लषः",
    why_dev               = "भ्राशादिभ्यः कर्तरि सार्वधातुके श्यन् वा (भ्राम्यति / भ्रमति) — काशिका ३.१.७०।",
    anuvritti_from        = ('3.1.69',),
    vibhasha_default      = False,
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
    apavada_of            = ('3.1.68', '3.1.77'),
)

register_sutra(SUTRA)
