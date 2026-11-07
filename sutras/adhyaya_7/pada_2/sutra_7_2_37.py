"""
7.2.37  ग्रहोऽलिटि दीर्घः  —  VIDHI

Padaccheda: ग्रहः अ-लिटि दीर्घः

ग्रहोऽलिटि दीर्घः (7.2.37)
Pāṭha: ashtadhyayi.com data.txt row i=72037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _site(state: State):
    """grah followed directly by an ārdhadhātuka that begins with its iṭ, in any lakāra but liṭ: the iṭ is ī (grahītā, grahīṣyati).
    A ṇic between them (grāhitā) is not 'the iṭ that follows grah' — the sūtra's 'prakṛtasya' (Kāśikā 7.2.37)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or (t.meta.get("upadesha_slp1") or "").strip() != "graha~":
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas or nxt.varnas[0].slp1 != "i" or "it_agama" not in nxt.varnas[0].tags:
            return None
        if any((u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in state.terms):
            return None
        return nxt
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    nxt = _site(state)
    nxt.varnas[0] = mk("I")
    nxt.varnas[0].tags.add("it_agama")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'graholiwi dIrGaH',
    text_dev              = 'ग्रहोऽलिटि दीर्घः',
    samagra_slp1          = "aNgasya grahaH aliwi dIrGaH ArDaDAtukasya iw valAdeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ग्रहः अलिटि दीर्घः आर्धधातुकस्य इट् वलादेः",
    padaccheda_dev        = "ग्रहः अ-लिटि दीर्घः",
    why_dev               = "(सूत्रम् 7.2.37) ग्रहोऽलिटि दीर्घः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
