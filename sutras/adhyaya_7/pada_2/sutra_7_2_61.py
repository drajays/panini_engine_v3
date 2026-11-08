"""
7.2.61  अचस्तास्वत् थल्यनिटो नित्यम्  —  VIDHI

Padaccheda: अचः तास्-वत् थलि अन्-इटः नित्यम्

अचस्तास्वत् थल्यनिटो नित्यम् (7.2.61)
Pāṭha: ashtadhyayi.com data.txt row i=72061 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_BLOCKS = ("7.2.35",)      # the iṭ before thal


def _site(state: State):
    """ac-final (vowel-ending) nityānit dhātu before thal in liṭ: thal takes no iṭ as tāsi would take none (yayātha, cicetha, juhotha — the other reading of 7.2.63, Kāśikā: 'pūrvayor yogayor vikalpaḥ')."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "Tal" for t in state.terms) \
            or not any((t.meta.get("source_lakara_upadesha") or "").strip() == "liT" for t in state.terms):
        return None
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dh is None or not dh.meta.get("anit_dhatu") or not dh.varnas:      # nityānit: aniṭ, and not one of the veṭ roots
        return None
    up = (dh.meta.get("upadesha_slp1") or "").rstrip("~").rstrip("YN")
    if up.endswith("f"):                      # the ṛ-final roots are 7.2.63's
        return None
    return dh if (dh.varnas[-1].slp1 in "aAiIuUeEoOxX") else None


def cond(state: State) -> bool:
    return _site(state) is not None and "7.2.35" not in state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.61",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "acastAsvat Talyaniwo nityam",
    text_dev              = "अचस्तास्वत् थल्यनिटो नित्यम्",
    samagra_slp1          = "aNgasya acaH tAsvat Tali aniwaH nityam valAdeH iw ArDaDAtukasya na tAsi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अचः तास्वत् थलि अनिटः नित्यम् वलादेः इट् आर्धधातुकस्य न तासि",
    padaccheda_dev        = "अचः तास्-वत् थलि अन्-इटः नित्यम्",
    why_dev               = "(सूत्रम् 7.2.61) अचस्तास्वत् थल्यनिटो नित्यम्।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # the iṭ reading (7.2.63's niyama: yayiTa, pecitha) is the default; choose({"7.2.61": True}) / explore() give the iṭ-less one
    vibhasha_scope        = cond,
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
