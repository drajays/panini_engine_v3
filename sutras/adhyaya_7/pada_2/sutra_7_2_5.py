"""
7.2.5  ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्  —  PRATISHEDHA

Padaccheda: ह्-म्-य्-अन्त-क्षण-श्वस-जागृ-णि-श्वि-एदिताम्

ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम् (7.2.5)
Pāṭha: ashtadhyayi.com data.txt row i=72005 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

def _sic_dhatu(state: State, names, ends=()):
    """The dhātu (upadeśa in ``names``, or ending in one of ``ends``) that stands before a sic."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        raw = (t.meta.get("upadesha_slp1") or "").strip().replace("^", "").replace("\\", "")
        if not (raw.replace("~", "") in names or (ends and raw.endswith(ends))):
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and (nxt.meta.get("upadesha_slp1") or "").strip() == "sic" and "it_agama" in nxt.varnas[0].tags:
            return t      # only a sic that has its iṭ: an aniṭ root keeps its vṛddhi (अपाक्षीत्)
    return None

_NAMES = frozenset({"jAgf","kzaRu","Svasa","Svi","wuoSvi"})


def _site(state: State):
    """ह्म्यन्त-क्षण-श्वस-जागृ-णि-श्वि-एदित्: no vṛddhi of the aṅga before sic (अरहिष्ट, अश्वयीत्)."""
    t = _sic_dhatu(state, _NAMES, "a~")
    return None if t is None or t.meta.get("7_2_1_sici_vrddhi_done") else t


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.meta["7_2_1_sici_vrddhi_done"] = True      # 7.2.1 / 7.2.3 read this: no vṛddhi
        t.tags.add("no_sici_vrddhi")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.5",
    sutra_type            = SutraType.PRATISHEDHA,
    text_slp1             = "hmyantakzaRaSvasajAgfRiSvyeditAm",
    text_dev              = "ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्",
    samagra_slp1          = "aNgasya hmyantakzaRaSvasajAgfRiSvyeditAm sici vfdDiH parasmEpadezu na iwi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम् सिचि वृद्धिः परस्मैपदेषु न इटि",
    padaccheda_dev        = "ह्-म्-य्-अन्त-क्षण-श्वस-जागृ-णि-श्वि-एदिताम्",
    why_dev               = "(सूत्रम् 7.2.5) ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
