"""
2.4.79  तनादिभ्यस्तथासोः  —  VIBHASHA

Kāśikā 2.4.79: "तनादिभ्य उत्तरस्य सिचस्तथासोः परतो विभाषा लुग् भवति। अतत। अतथाः। अतनिष्ट। अतनिष्ठाः। असात।
असाथाः। असनिष्ट। असनिष्ठाः। जनसनखनाम्० (6.4.42) इत्यात्वम्। थासा साहचर्यादात्मनेपदस्य तशब्दस्य ग्रहणम्,
परस्मैपदे न भवति — अतनिष्ट यूयम्॥"

Engine: a gaṇa-8 root before a luṅ sic whose next term is the ātmanepada tiṅ ``ta`` or ``TAs``: the sic is
optionally removed (luk, the act of 2.4.77).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_2.pada_4.sutra_2_4_77 import _find_sic_index

_TA_THAS = frozenset({"ta", "TAs"})


def _site(state: State):
    j = _find_sic_index(state)
    if j is None or j == 0 or j + 1 >= len(state.terms):
        return None
    root, nxt = state.terms[j - 1], state.terms[j + 1]
    if "dhatu" not in root.tags or root.meta.get("gana") != 8:
        return None
    if "tin_adesha_3_4_78" in nxt.tags and (nxt.meta.get("upadesha_slp1") or "").strip() in _TA_THAS:
        return j
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    j = _site(state)
    state.terms[j - 1].tags.add("vikarana_luk")
    state.terms.pop(j)
    state.samjna_registry["2.4.79_sic_luk"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.79",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "tanAdiByastaTAsoH",
    text_dev              = "तनादिभ्यस्तथासोः",
    samagra_slp1          = "tan-AdiByaH ta-TAsoH luk sicaH viBAzA",
    samagra_dev           = "तन्-आदिभ्यः त-थासोः लुक् सिचः विभाषा",
    padaccheda_dev        = "तनादिभ्यः त-थासोः",
    why_dev               = "तनादिभ्यः परस्य सिचः त-थासोः परतो विभाषा लुक् (अतत / अतनिष्ट) — काशिका २.४.७९।",
    anuvritti_from        = ('2.4.77',),
    vibhasha_default      = False,
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
