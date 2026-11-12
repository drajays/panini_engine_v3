"""
7.3.36  अर्तिह्रीव्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ  —  VIDHI

Padaccheda: अर्त्ति-ह्री-व्ली-री-क्नूयी-क्ष्मायी-आताम् पुक् णौ

Kāśikā 7.3.36: arti (ṛ), hrī, vlī, rī, knūyī, kṣmāyī and every ā-final aṅga take puk before ṇic
(arpayati, hrepayati, vlepayati, repayati, knopayati, kṣmāpayati, dāpayati, dhāpayati).
puk is a kit āgama placed at the END of the aṅga (pūrvānta-karaṇa, so the upadhā stays short: adīdapat).
Engine: the sūtra's own list read off the aṅga's surface (after it-lopa) + the ā-final class; the augment p is
appended like the yuk of 7.3.37. Idempotent via Term.meta['7_3_36_puk_done'].
Pāṭha: ashtadhyayi.com data.txt row i=73036 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk

_NAMED = frozenset({"f", "hrI", "vlI", "rI", "knUyI", "kzmAyI"})     # arti (both ṛ), hrī, vlī, rī, knūyī, kṣmāyī


def _is_nic(state: State, di: int) -> bool:
    if di + 1 >= len(state.terms):
        return False
    nxt = state.terms[di + 1]
    return ("nic" in nxt.tags or "sanadi" in nxt.tags) and (nxt.meta.get("upadesha_slp1") or "").strip().rstrip("~") in ("Ric", "Nic")


def _find(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("7_3_36_puk_done") or not t.varnas:
            continue
        surf = "".join(v.slp1 for v in t.varnas)
        if (surf in _NAMED or surf[-1] == "A") and _is_nic(state, i):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = state.terms[_find(state)]
    t.varnas.append(mk("p"))
    t.meta["7_3_36_puk_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'artihrIvlIrIknUyIkzmAyyAtAM puNRO',
    text_dev              = 'अर्तिह्रीव्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ',
    samagra_slp1          = "aNgasya artihrIvlIrIknUyIkzmAyyAtAm puk RO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अर्तिह्रीव्लीरीक्नूयीक्ष्माय्याताम् पुक् णौ",
    padaccheda_dev        = "अर्त्ति-ह्री-व्ली-री-क्नूयी-क्ष्मायी-आताम् पुक् णौ",
    why_dev               = "(सूत्रम् 7.3.36) अर्त्तिह्रीब्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
