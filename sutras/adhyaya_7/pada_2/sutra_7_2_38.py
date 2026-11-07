"""
7.2.38  वॄतो वा  —  VIDHI

Padaccheda: वॄतः वा

वॄतो वा (7.2.38)
Pāṭha: ashtadhyayi.com data.txt row i=72038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _site(state: State):
    """vṛ (vṛñ, vṛṅ) and the ṝ-final dhātus (tṝ, jṝ, śṝ …), directly followed by their iṭ (7.2.35), in any lakāra but liṭ: the iṭ may be ī
    (varitā / varītā, taritā / tarītā; Kāśikā 7.2.38: 'ṝkārāntebhyaḥ'; kariṣyati, hariṣyati — short ṛ — keep the short iṭ). The āśīrliṅ is barred by 7.2.39."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas:
            continue
        if t.varnas[-1].slp1 != "F" and (t.meta.get("upadesha_slp1") or "").strip() not in ("vfY", "vfN"):      # vṛ is named by the sūtra: vṛñ, vṛṅ
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas or nxt.varnas[0].slp1 != "i" or "it_agama" not in nxt.varnas[0].tags:
            return None
        if any((u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in state.terms):
            return None
        return nxt
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    nxt = _site(state)
    nxt.varnas[0] = mk("I")
    nxt.varnas[0].tags.add("it_agama")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.38",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "vFto vA",
    text_dev              = "वॄतो वा",
    samagra_slp1          = "aNgasya vFtaH vA valAdeH iw ArDaDAtukasya grahaH aliwi dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य वॄतः वा वलादेः इट् आर्धधातुकस्य ग्रहः अलिटि दीर्घः",
    padaccheda_dev        = "वॄतः वा",
    why_dev               = "(सूत्रम् 7.2.38) वॄतो वा।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # varitā is the default reading; choose({"7.2.38": True}) / explore() give varītā
    vibhasha_scope        = cond,      # asked only of a ṛ-final dhātu with its iṭ
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
