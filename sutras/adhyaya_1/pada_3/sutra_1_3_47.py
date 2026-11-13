"""
1.3.47  भासनोपसम्भाषाज्ञानयत्नविमत्युपमन्त्रणेषु वदः  —  VIDHI

*Padaccheda:* *bhāsana-upasambhāṣā-jñāna-yatna-vimati-upāmantraṇeṣu* (सप्तमी-बहुवचन)
              / *vadaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* the root vad (bhvādi, vyaktāyāṃ vāci) takes ātmanepada when the speaker means one of six senses.

*Engine (AMENDMENT 30):* the six senses are the vivakṣā key ``vadArTa`` (BAsana, upasamBAzA, jYAna, yatna, vimati, upamantraRa), each
the sūtra's own word; the cond reads them only through ``vivaksita``. With no sense meant (``yatkiMcid vadati``, Kāśikā's
"एतेष्विति किम्?") it declines and 1.3.78 gives parasmaipada. The act records the pada on the state; the recipe's pada-nirṇaya reads it.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com data.txt row i = 13047.
  Source #2 — Kāśikā 1.3.47 (ashtadhyayi.db, texts): भासनम् = दीप्तिः, वदते चार्वी लोकायते; उपसंभाषा = उपसान्त्वनम्, कर्मकरानुपवदते;
              ज्ञानम्, वदते चार्वी लोकायते; यत्नः, क्षेत्रे वदते, गेहे वदते; विमतिः, क्षेत्रे विवदन्ते, गेहे विवदन्ते;
              उपमन्त्रणम् = रहस्युपच्छन्दनम्, कुलभार्यामुपवदते, परदारानुपवदते. एतेष्विति किम्? यत्किंचिद्वदति.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita

_REGISTRY_KEY = "1_3_47_vad_BAsana"
_STAMP_KEY    = "Atmanepada_1_3_47"
_VAD = "vada~"          # bhvādi vada vyaktāyāṃ vāci (gaṇa 1); the curādi vada~ (sandeśavacane) is another root


def _vad(state: State):
    for t in state.terms:
        if "dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == _VAD and t.meta.get("gana") == 1:
            return t
    return None


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada" or state.meta.get(_STAMP_KEY):
        return False
    if _vad(state) is None:
        return False
    return (vivaksita(state, "vadArTa", "BAsana") or vivaksita(state, "vadArTa", "upasamBAzA")
            or vivaksita(state, "vadArTa", "jYAna") or vivaksita(state, "vadArTa", "yatna")
            or vivaksita(state, "vadArTa", "vimati") or vivaksita(state, "vadArTa", "upamantraRa"))


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.47",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='BAsanopasamBAzAjYAnayatnavimatyupamantraRezu vadaH',
    text_dev='भासनोपसम्भाषाज्ञानयत्नविमत्युपमन्त्रणेषु वदः',
    samagra_slp1="BAsana-upasamBAzA-jYAna-yatna-vimati-upamantraRezu vadaH Atmanepadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="भासन-उपसम्भाषा-ज्ञान-यत्न-विमति-उपमन्त्रणेषु वदः आत्मनेपदम्",
    padaccheda_dev=(
        "भासन-उपसम्भाषा-ज्ञान-यत्न-विमति-उपमन्त्रणेषु (सप्तमी-बहुवचन) / "
        "वदः (षष्ठी-एकवचन)"
    ),
    why_dev=(
        "वद्-धातोः भासन-उपसम्भाषा-ज्ञान-यत्न-विमति-उपमन्त्रण-अर्थेषु विवक्षितेषु आत्मनेपदम् — "
        "वदते, विवदन्ते इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
