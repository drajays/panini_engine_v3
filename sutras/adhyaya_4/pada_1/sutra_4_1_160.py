"""
4.1.160  प्राचामवृद्धात् फिन् बहुलम्  —  VIDHI

Padaccheda: प्राचाम् अ-वृद्धात् फिन् बहुलम्

प्राचामवृद्धात् फिन् बहुलम् (4.1.160)
Pāṭha: ashtadhyayi.com data.txt row i=41160 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _site(state: State):
    """apatya (4.1.92), the speaker follows the eastern grammarians (prācām), and the stem is avṛddha (1.1.73 has not named it vṛddha)."""
    t = taddhita_site(state, "apatya", ok=vivaksita(state, "arthaViSeSa", "prAcAm") and any(e.get("artha") == "apatya" for e in state.adhikara_stack))
    return t if t is not None and "vṛddha" not in t.tags else None


def cond(state: State) -> bool:
    return _site(state) is not None and not state.meta.get("declined:4.1.160")


def act(state: State) -> State:
    if _site(state) is None:
        return state
    if policy_pick(state, "4.1.160", 2) == 1:        # bahulam: not always (dākṣiḥ, plākṣiḥ keep iñ); the sūtra stands aside in this reading
        state.meta["declined:4.1.160"] = True
        return state
    return attach_taddhita(state, "Pin")      # P -> Ayan (7.1.2); the final n is it (1.3.3), so no ñit vṛddhi: glucukāyani


SUTRA = SutraRecord(
    sutra_id              = "4.1.160",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAcAmavfdDAt Pin bahulam",
    text_dev              = "प्राचामवृद्धात् फिन् बहुलम्",
    samagra_slp1          = "tasya apatyam iti prAcAm avfdDAt bahulam Pin",
    samagra_dev           = "'तस्य अपत्यम्' (इति) प्राचामवृद्धात् बहुलम् फिन्",
    padaccheda_dev        = "प्राचाम् अ-वृद्धात् फिन् बहुलम्",
    why_dev               = "(सूत्रम् 4.1.160) प्राचामवृद्धात् फिन् बहुलम्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.1.83', '4.1.95'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
