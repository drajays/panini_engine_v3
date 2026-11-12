"""
3.1.61  दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्  —  VIBHASHA

Kāśikā 3.1.61: "चिण् त इति वर्तते। दीपी दीप्तौ, जनी प्रादुर्भावे, बुध अवगमने, पूरी आप्यायने, तायृ संतानपालनयोः,
ओप्यायी वृद्धौ एतेभ्यः परस्य च्लेस्तशब्दे परतोऽन्यतरस्यां चिणादेशो भवति। अदीपि, अदीपिष्ट। अजनि, अजनिष्ट।
अबोधि, अबुद्ध। अपूरि, अपूरिष्ट। अतायि, अतायिष्ट। अप्यायि, अप्यायिष्ट॥"

Engine: the swap of 3.1.60 (cli → ciṇ before ``ta``), optional, for dIpI, janI, buDa, pUrI, tAyf, o~pyAyI.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_3.pada_1.sutra_3_1_60 import cli_before_ta, swap_cli_cin

_ROOTS = frozenset({"dIpI", "janI", "buDa", "pUrI", "tAyf", "opyAyI"})


def cond(state: State) -> bool:
    return cli_before_ta(state, _ROOTS) is not None


def act(state: State) -> State:
    return swap_cli_cin(state, cli_before_ta(state, _ROOTS))


SUTRA = SutraRecord(
    sutra_id              = "3.1.61",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'dIpajanabuDapUritAyipyAyiByonyatarasyAm',
    text_dev              = 'दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH dIpa-jana-buDa-pUri-tAyi-pyAyiByaH anyatarasyAm luNi cleH ciR te",
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः दीप-जन-बुध-पूरि-तायि-प्यायिभ्यः अन्यतरस्याम् लुङि च्लेः चिण् ते",
    padaccheda_dev        = "दीप-जन-बुध-पूरि-तायि-प्यायिभ्यः अन्यतरस्याम्",
    why_dev               = "दीपादिभ्यः लुङि तशब्दे परे च्लेः चिण् वा (अदीपि / अदीपिष्ट) — काशिका ३.१.६१।",
    anuvritti_from        = ('3.1.60',),
    apavada_of            = ('3.1.44',),
    vibhasha_default      = False,
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
