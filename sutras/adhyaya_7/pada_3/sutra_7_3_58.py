"""
7.3.58  विभाषा चेः  —  VIBHASHA

Sources consulted:
- Kāśikā 7.3.58: "चिनोतेरङ्गस्य सन्लिटोरभ्यासादुत्तरस्य विभाषा कवर्गादेशो भवति। चिचीषति, चिकीषति, चिचाय, चिकाय।"
  (not before yaṅ: चेचीयते)
- Cross-validation: Vidyut ci liṭ ātmanepada cikye

After the abhyāsa of the dhātu ci, its c may become k (ku, 1.1.50) when the abhyāsa is due to san or liṭ: a following
san, or a tiṅ that replaced liṭ (its `source_lakara_upadesha`). The default reading keeps c (cicāya); choose / explore give cikāya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _san_or_lit(t) -> bool:
    return (t.meta.get("upadesha_slp1") or "").strip() == "san" or \
        (t.meta.get("source_lakara_upadesha") or "").strip() == "liT"


def _site(state: State):
    for i, t in enumerate(state.terms[1:], start=1):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or "abhyasa" not in state.terms[i - 1].tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "c" or (t.meta.get("upadesha_slp1") or "").strip() != "ciY" or t.meta.get("gana") != 5:      # ci~ cayane (svādi: cinoti), not the curādi ciY
            continue
        if any(_san_or_lit(u) for u in state.terms[i + 1:]):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[0] = mk("k")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.58",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "viBAzA ceH",
    text_dev              = "विभाषा चेः",
    samagra_slp1          = "aNgasya viBAzA ceH ku cajoH aByAsAt ca sanliwoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य विभाषा चेः कु चजोः अभ्यासात् च सन्लिटोः",
    padaccheda_dev        = "विभाषा चेः",
    why_dev               = "सनि लिटि च अभ्यासात् परस्य चेः चकारस्य वा कुत्वम् (चिकाय/चिचाय, चिकीषति)।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # cicāya is the default reading; choose({"7.3.58": True}) / explore() give cikāya
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
