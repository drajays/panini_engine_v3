"""
1.3.32  गन्धनावक्षेपणसेवनसाहसिक्यप्रतियत्नप्रकथनोपयोगेषु कृञः  —  VIDHI

*Padaccheda:* *gandhanā-avakṣepaṇa-sevana-sāhasikya-pratiyatna-prakathana-
upayogeṣu* (सप्तमी-बहुवचन) / *kṛñaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for kṛ (to do/make) in the following senses:
  gandhanā (insulting), avakṣepaṇa (throwing down/reproaching),
  sevana (serving), sāhasikya (rashness/boldness), pratiyatna (counter-effort),
  prakathana (narrating), upayoga (using/employing).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 in _KRN_ROOTS and carries at least one
usage tag from _KRNA_USAGES, and (c) the idempotency stamp
"Atmanepada_1_3_32" is absent from state.meta.  No arm flags (CONSTITUTION
Art. 13).  r1_form_identity_exempt=True because no surface phonological
change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_KRNA_USAGES: frozenset[str] = frozenset({
    "gAnDanA_usage",
    "avakzepaNa_usage",
    "sevana_usage",
    "sAhasikya_usage",
    "pratiyatna_usage",
    "prakaTana_usage",
    "upayoga_usage",
})
_KRN_ROOTS: frozenset[str] = frozenset({"qukf~Y", "kf", "kfY"})

_REGISTRY_KEY = "1_3_32_kfY_usages"
_STAMP_KEY    = "Atmanepada_1_3_32"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _KRN_ROOTS
        and not _KRNA_USAGES.isdisjoint(t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.32",
    sutra_type=SutraType.VIDHI,
    text_slp1="ganDanAvakzepaNasevanasAhasikya-pratiyatnaprakaTanopayogezuY kfYaH",
    text_dev="गन्धनावक्षेपणसेवनसाहसिक्यप्रतियत्नप्रकथनोपयोगेषु कृञः",
    padaccheda_dev=(
        "गन्धनावक्षेपण-सेवन-साहसिक्य-प्रतियत्न-प्रकथन-उपयोगेषु (सप्तमी-बहुवचन)"
        " / कृञः (षष्ठी)"
    ),
    why_dev=(
        "गन्धन-आदि-अर्थेषु कृञ्-धातोः प्रयोगे आत्मनेपदम् — "
        "kurute इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
