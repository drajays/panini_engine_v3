"""
2.2.24  अनेकमन्यपदार्थे  —  SAMJNA (bahuvrīhi)

Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com ``data.txt`` i=22024):
  *anekam anyapadārthe* — names the *bahuvrīhi* class when several members
  denote another entity’s meaning.

Fires when any Term carries the ``bahuvrIhi`` tag (structural environment).
Kāśikā: अनेकं सुबन्तमन्यपदार्थे वर्तमानं सह समस्यते, बहुव्रीहिश्च समासो भवति।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _old_cond(state: State) -> bool:
    if not any("bahuvrIhi" in t.tags for t in state.terms):
        return False
    return not bool(state.samjna_registry.get("2.2.24_anekam_anyapadartha"))


def _old_act(state: State) -> State:
    state.samjna_registry["2.2.24_anekam_anyapadartha"] = True
    return state


from engine.samasa_attach import run, mark
from engine.vivaksha import vivaksita


def _site(state: State):
    """Several members that together name something else (anyapadārtha, the speaker's vivakṣā)."""
    idx = run(state, "2.2.24")
    return idx if idx is not None and vivaksita(state, "arthaViSeSa", "anyapadArTa") else None


def cond(state: State) -> bool:
    return _site(state) is not None or _old_cond(state)


def act(state: State) -> State:
    s = _site(state)
    return mark(state, s, "bahuvrihi", "2.2.24") if s is not None else _old_act(state)


SUTRA = SutraRecord(
    sutra_id="2.2.24",
    sutra_type=SutraType.VIDHI,
    text_slp1='anekamanyapadArTe',
    text_dev='अनेकमन्यपदार्थे',
    samagra_slp1="AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA anekam anyapadArTe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा अनेकम् अन्यपदार्थे",
    padaccheda_dev="अनेकम् / अन्य-पद-अर्थे",
    why_dev="बहुव्रीहौ अनेकेन अन्य-पदार्थे (P024 डेमो) — संज्ञा-चिह्ननम्।",
    anuvritti_from=("2.2.23",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
