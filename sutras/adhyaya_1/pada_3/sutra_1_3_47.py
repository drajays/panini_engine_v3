"""
1.3.47  भासनोपसम्भाषाज्ञानयत्नविमत्युपमन्त्रणेषु वदः  —  VIDHI

*Padaccheda:* *bhāsana-upasambhāṣā-jñāna-yatna-vimati-upāmantraṇeṣu* (सप्तमी-बहुवचन)
              / *vadaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root vad (√vad, to speak) takes ātmanepada in the senses of:
  1. bhāsana   — illuminating/shining forth (light-metaphor for speech)
  2. upasambhāṣā — addressing/conversing with
  3. jñāna     — expressing knowledge/understanding
  4. yatna     — expressing effort/attempt
  5. vimati    — expressing disagreement/different opinion
  6. upāmantraṇa — inviting/summoning (respectful address)

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) the
idempotency stamp "Atmanepada_1_3_47" is absent, and (c) a dhātu Term
whose upadesha_slp1 is in _VAD_ROOTS and which carries the tag "BAsana_usage"
(the umbrella tag for all six senses listed).
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_VAD_ROOTS: frozenset[str] = frozenset({"vada~", "vad"})

# All six semantic senses from the sūtra
_SENSE_TAGS: frozenset[str] = frozenset({
    "BAsana_usage",
    "upasaMBAzA_usage",
    "jYAna_usage",
    "yatna_usage",
    "vimati_usage",
    "upAmantrana_usage",
})

_REGISTRY_KEY = "1_3_47_vad_BAsana"
_STAMP_KEY    = "Atmanepada_1_3_47"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _VAD_ROOTS and not _SENSE_TAGS.isdisjoint(t.tags):
            return True
    return False


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.47",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="BAsanopasaMBAzAjYAnayatnavimatiupAmantraneSu vadaH",
    text_dev="भासनोपसम्भाषाज्ञानयत्नविमत्युपमन्त्रणेषु वदः",
    padaccheda_dev=(
        "भासन-उपसम्भाषा-ज्ञान-यत्न-विमति-उपमन्त्रणेषु (सप्तमी-बहुवचन) / "
        "वदः (षष्ठी-एकवचन)"
    ),
    why_dev=(
        "वद्-धातोः भासन-उपसम्भाषा-ज्ञान-यत्न-विमति-उपमन्त्रण-अर्थेषु आत्मनेपदम् — "
        "vadata, vadete इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
