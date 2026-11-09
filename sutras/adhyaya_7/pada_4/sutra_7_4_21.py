"""
7.4.21  शीङः सार्वधातुके गुणः  —  VIDHI

Padaccheda: शीङः सार्वधातुके गुणः

शीङः सार्वधातुके गुणः (7.4.21)
Pāṭha: ashtadhyayi.com data.txt row i=74021 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    """शीङ् before a sārvadhātuka: the dhātu whose final ī takes guṇa — शेते, शयाते, शेरते (Kāśikā; cf. शिश्ये, ārdhadhātuka-like liṭ)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" in t.tags and "abhyasa" not in t.tags and (t.meta.get("upadesha_slp1") or "").replace("~", "").strip() == "SIN":
            if t.varnas and t.varnas[-1].slp1 == "I" and any(u.tags & {"sarvadhatuka", "sarvadhatuka_3_4_113"} for u in state.terms[i + 1:]):
                return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    _find(state).varnas[-1] = mk("e")      # guṇa, though kṅiti ca (1.1.5) would stop 7.3.84: this sūtra is its apavāda
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.21",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "SINaH sArvaDAtuke guRaH",
    text_dev              = "शीङः सार्वधातुके गुणः",
    samagra_slp1          = "aNgasya SINaH sArvaDAtuke guRaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य शीङः सार्वधातुके गुणः",
    padaccheda_dev        = "शीङः सार्वधातुके गुणः",
    why_dev               = "(सूत्रम् 7.4.21) शीङः सार्वधातुके गुणः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
