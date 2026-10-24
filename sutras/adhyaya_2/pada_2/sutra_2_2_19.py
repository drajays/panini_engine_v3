"""
2.2.19  उपपदमतिङ्  —  SAMJNA (upapada compound)

Śāstra summary: an *upapada* is compounded with a related *pada* that does not end
in a *tiṅ* affix — licensing *samāsa* of the *upapada* frame (e.g. *ratna* + *śas*
with *√dhā* + *kvip* in ``prakriya_22``).

Fires when any Term carries the ``upapada`` tag (structural environment set by
the pipeline before calling this sūtra).
Pāṭha: ashtadhyayi.com data.txt row i=22019 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _kft_upapada(state: State):
    """An upapada followed by the dhātu and the kṛt that stands for it (kumbha + kṛ + aṇ): not yet a compound."""
    if len(state.terms) >= 3 and "upapada" in state.terms[0].tags and "dhatu" in state.terms[1].tags \
            and "krt" in state.terms[2].tags and not state.terms[0].meta.get("samasa"):
        return state.terms[0]
    return None


def cond(state: State) -> bool:
    if _kft_upapada(state) is not None:
        return True
    if not any("upapada" in t.tags for t in state.terms):
        return False
    return not bool(state.samjna_registry.get("2.2.19_upapada_atiNg"))


def act(state: State) -> State:
    up = _kft_upapada(state)
    if up is not None:
        up.meta["samasa"] = "tatpuruzaH"            # upapada-tatpuruṣa, before any sup (prāk subutpatteḥ): the whole is one prātipadika (1.2.46)
        return state
    state.samjna_registry["2.2.19_upapada_atiNg"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.19",
    sutra_type=SutraType.VIDHI,
    text_slp1='upapadamatiN',
    text_dev='उपपदमतिङ्',
    samagra_slp1="AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH upapadam atiN nityaM",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः उपपदम् अतिङ् नित्यं",
    padaccheda_dev="उपपदम् / अतिङ्खि",
    why_dev="उपपद-समासार्थं संज्ञा-अनुमोदनम् (प्रक्रिया-२२)।",
    anuvritti_from=("2.1.3",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
