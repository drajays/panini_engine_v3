"""
4.1.137  राजश्वशुराद्यत्  —  VIDHI

Padaccheda: राज-श्वशुरात् यत्

राजश्वशुराद्यत् (4.1.137)
Pāṭha: ashtadhyayi.com data.txt row i=41137 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401
from engine.vartika import Vartika


def _site(state: State):
    return taddhita_site(state, "apatya", final=lambda f: f in ("rAjan", "SvaSura"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "yat")


# Art. 25 / AMENDMENT 29: the vārttika of 4.1.137 lives here: rājño jātāv eveti vācyam (Bhāṣya: rājanyo nāma jātiḥ; rājano 'nyaḥ, the aṇ stays otherwise).
# jāti is the caller's Lexicon fact (lex:jAti), as for the other jāti-conditioned sūtras.
def _not_jati_cond(state: State) -> bool:
    return taddhita_site(state, "apatya", final=lambda f: f == "rAjan", lacks=("jAti",)) is not None


VARTIKAS = (
    Vartika(id="4.1.137.v1", source="Kātyāyana vā. on 4.1.137 (Bhāṣya 4.1.137: rājñaḥ apatye jātigrahaṇam)", tier="T1", relation="restriction",
            text_dev="राज्ञो जातावेवेति वाच्यम्", cond=_not_jati_cond, act=lambda state: state),
)

SUTRA = SutraRecord(
    sutra_id              = "4.1.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAjaSvaSurAdyat",
    text_dev              = "राजश्वशुराद्यत्",
    samagra_slp1          = "tasya apatyam iti rAja-SvaSurAt yat",
    samagra_dev           = "'तस्य अपत्यम्' (इति) राज-श्वशुरात् यत्",
    padaccheda_dev        = "राज-श्वशुरात् यत्",
    why_dev               = "(सूत्रम् 4.1.137) राजश्वशुराद्यत्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.1.95'),
    vartikas              = VARTIKAS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
