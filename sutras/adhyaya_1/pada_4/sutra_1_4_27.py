"""
1.4.27  वारणार्थानामीप्सितः  —  SAMJNA (kāraka-saṃjñā)

**Pāṭha (anuvṛtti):** *kārake vāraṇārthānām īpsitaḥ (apādānam)* —
**1.4.23** *kārake*; **1.4.24** *apādānam* (anuvṛtti).

*Śāstra:* For roots meaning "to prevent / ward off" (vār, nivāraṇa, etc.),
the object that is desired (īpsita — what one tries to obtain or reach despite
the prevention) receives the *apādāna* saṃjñā.
Example: *caurād rakṣati* — the thief is the apādāna (what one guards from).

*Engine:* A Term carrying ``"vAraNa_Ipsita"`` (pipeline-set) gets tag ``"apAdAna"``.
``cond`` reads only structural semantic tags (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State

SAMJNA_KEY = "1_4_27_apAdAna_vAraNa"
META_DONE  = "1_4_27_done"

_TRIGGER: frozenset[str] = frozenset({"vAraNa_Ipsita"})


def cond(state: State) -> bool:
    if not adhikara_in_effect("1.4.27", state, "1.4.23"):
        return False
    for t in state.terms:
        if META_DONE in t.meta:
            continue
        if _TRIGGER & t.tags:
            return True
    return False


def act(state: State) -> State:
    for t in state.terms:
        if META_DONE in t.meta:
            continue
        if _TRIGGER & t.tags:
            t.tags.add("apAdAna")
            t.meta[META_DONE] = True
    state.samjna_registry[SAMJNA_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.4.27",
    sutra_type            = SutraType.SAMJNA,
    text_slp1             = "vAraRArTAnAm IpsitaH",
    text_dev              = "वारणार्थानामीप्सितः",
    padaccheda_dev        = "वारणार्थानाम् / ईप्सितः",
    why_dev               = (
        "वारणार्थ-धातूनाम् प्रयोगे योऽभीप्सितः (यस्माद् वारयति) स "
        "अपादान-कारक-संज्ञकः — यथा 'चौरात् रक्षति' इत्यत्र चौरः।"
    ),
    anuvritti_from        = ("1.4.1", "1.4.23", "1.4.24"),
    r1_form_identity_exempt = True,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
