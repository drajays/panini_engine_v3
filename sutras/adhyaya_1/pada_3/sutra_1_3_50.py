"""
1.3.50  विभाषा विप्रलापे  —  VIBHASHA

*Padaccheda:* *vibhāṣā* (अव्यय) / *vipralāpe* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada 1.3.12; vadaḥ 1.3.47; vyaktavācām samuccāraṇe 1.3.48.

*Content:* when articulate speakers speak together contradicting one another (vipralāpa), vad takes ātmanepada optionally:
vipravadante sāṃvatsarāḥ / vipravadanti sāṃvatsarāḥ. Kāśikā: प्राप्तविभाषेयम्, the option on what 1.3.48 would give.

*Engine (AMENDMENT 30):* the three context facts ``vyaktavAk``, ``samuccAraRa``, ``vipralApa`` (read through ``vivaksita``) are its scope; within it
the sūtra is a vibhāṣā, so ``vikalpa.explore`` shows both readings. Its firing is the ātmanepada reading; declining leaves 1.3.78's parasmaipada.
1.3.48 steps aside in this case and this later sūtra decides (vipratiṣedha, 1.4.2).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com data.txt row i = 13050.
  Source #2 — Kāśikā 1.3.50: विप्रवदन्ते सांवत्सराः, विप्रवदन्ति सांवत्सराः। विप्रवदन्ते मौहूर्ताः, विप्रवदन्ति मौहूर्ताः।
              विप्रलाप इति किम्? संप्रवदन्ते ब्राह्मणाः। व्यक्तवाचामित्येव — विप्रवदन्ति शकुनयः।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita

_REGISTRY_KEY = "1_3_50_vipralApa_vibhASA"
_STAMP_KEY    = "Atmanepada_vibhASA_1_3_50"


def scope(state: State) -> bool:
    """The vipralāpa case: vad, articulate speakers, speaking together, contradicting."""
    if not any("dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "vada~" and t.meta.get("gana") == 1
               for t in state.terms):
        return False
    return (vivaksita(state, "vyaktavAk", "vyaktavAc") and vivaksita(state, "samuccAraRa", "samuccAraRa")
            and vivaksita(state, "vipralApa", "vipralApa"))


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada" or state.meta.get(_STAMP_KEY):
        return False
    return scope(state)


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.meta["pada_by_sense"] = True      # a sense-gated decision: the recipe resolver lets it override the 1.3.78 gate
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.50",
    sutra_type=SutraType.VIBHASHA,
    vibhasha_default=True,
    vibhasha_scope=scope,
    r1_form_identity_exempt=True,
    text_slp1='viBAzA vipralApe',
    text_dev='विभाषा विप्रलापे',
    samagra_slp1="viBAzA vipralApe Atmanepadam vadaH vyaktavAcAM samuccAraRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="विभाषा विप्रलापे आत्मनेपदम् वदः व्यक्तवाचां समुच्चारणे",
    padaccheda_dev="विभाषा (अव्यय) / विप्रलापे (सप्तमी-एकवचन)",
    why_dev=(
        "विप्रलापे व्यक्तवाचां समुच्चारणे वद्-धातोः विभाषा आत्मनेपदम् — "
        "विप्रवदन्ते / विप्रवदन्ति सांवत्सराः; "
        "१.३.४७-४८ इत्यतः वदः व्यक्तवाचां समुच्चारणे, १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.47", "1.3.48"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
