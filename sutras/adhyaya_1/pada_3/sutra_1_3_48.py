"""
1.3.48  व्यक्तवाचां समुच्चारणे  —  VIDHI

*Padaccheda:* *vyakta-vācām* (षष्ठी-बहुवचन) / *samuccāraṇe* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12; vad (vadaḥ) from 1.3.47.

*Content:* vad takes ātmanepada when articulate-voiced speakers speak together (samuccāraṇa): saṃpravadante brāhmaṇāḥ.

*Engine (AMENDMENT 30):* two context facts of the sentence, ``vyaktavAk`` and ``samuccAraRa`` (supplied by the caller, never explored),
read through ``vivaksita``. Kāśikā: व्यक्तवाचामिति किम्? ... संप्रवदन्ति कुक्कुटाः. समुच्चारणे इति किम्? ब्राह्मणो वदति।
The case of mutual contradiction (vipralāpa) belongs to the later 1.3.50, which makes this ātmanepada optional there (Kāśikā 1.3.50:
प्राप्तविभाषेयम्; vipratiṣedhe paraṃ kāryam 1.4.2): this sūtra therefore declines when vipralāpa is meant and 1.3.50 decides.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com data.txt row i = 13048.
  Source #2 — Kāśikā 1.3.48: व्यक्तवाचां समुच्चारणं सहोच्चारणम् ... संप्रवदन्ते ब्राह्मणाः। संप्रवदन्ते क्षत्रियाः।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_1.pada_3.sutra_1_3_50 import scope as vipralapa_case

_REGISTRY_KEY = "1_3_48_vyaktavAcAM_samuccAraRa"
_STAMP_KEY    = "Atmanepada_1_3_48"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada" or state.meta.get(_STAMP_KEY):
        return False
    if not any("dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "vada~" and t.meta.get("gana") == 1
               for t in state.terms):
        return False
    if not (vivaksita(state, "vyaktavAk", "vyaktavAc") and vivaksita(state, "samuccAraRa", "samuccAraRa")):
        return False
    return not vipralapa_case(state)       # the later 1.3.50 takes the vipralāpa case (vipratiṣedha 1.4.2); its own scope says which


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.meta["pada_by_sense"] = True      # a sense-gated decision: the recipe resolver lets it override the 1.3.78 gate
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.48",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='vyaktavAcAM samuccAraRe',
    text_dev='व्यक्तवाचां समुच्चारणे',
    samagra_slp1="vyaktavAcAm samuccAraRe Atmanepadam vadaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="व्यक्तवाचाम् समुच्चारणे आत्मनेपदम् वदः",
    padaccheda_dev="व्यक्त-वाचाम् (षष्ठी-बहुवचन) / समुच्चारणे (सप्तमी-एकवचन)",
    why_dev=(
        "व्यक्तवाचां समुच्चारणे वद्-धातोः आत्मनेपदम् — "
        "संप्रवदन्ते ब्राह्मणाः; "
        "१.३.४७ इत्यतः वदः, १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.47"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
