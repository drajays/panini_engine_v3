"""
6.1.32  ह्वः सम्प्रसारणम्  —  VIDHI

Padaccheda: ह्वः सम्प्रसारणम्

ह्वः सम्प्रसारणम् (6.1.32)
Pāṭha: ashtadhyayi.com data.txt row i=61032 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_1.pada_1.sutra_1_1_45 import META_TARGETS

# Kāśikā 6.1.32: ṇau ca sanścaṅoḥ is understood — "san-parā caṅ-parā ca ṇau parato hvaḥ saṃprasāraṇaṃ bhavati: juhāvayiṣati,
# ajūhavat". The root hve before a ṇic that a san or a caṅ follows; 1.1.45 turns its v into u, 6.1.108 absorbs the e (hu).
_NIC = frozenset({"Ric", "Nic"})
_SAN_CAN = frozenset({"san", "caN"})


def _live(state: State, i: int):
    return next((t for t in state.terms[i + 1:] if t.varnas), None)


def _site(state: State):
    for i, t in enumerate(state.terms[:-2]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("samprasarana_done"):
            continue
        if "".join(v.slp1 for v in t.varnas) != "hve" or "mula_dhatu_v" not in t.varnas[-1].tags:
            continue
        nic = _live(state, i)
        if nic is None or (nic.meta.get("upadesha_slp1") or "").strip() not in _NIC:
            continue
        nxt = _live(state, state.terms.index(nic))
        if nxt is not None and (nxt.meta.get("upadesha_slp1") or "").strip() in _SAN_CAN:
            return i, 1                      # the v of ह्वे
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    site = _site(state)
    if site is not None:
        ti, vi = site
        state.meta[META_TARGETS] = [(ti, vi)]        # 1.1.45 reads it: v -> u; 6.1.108 then absorbs the e
        state.terms[ti].meta["samprasarana_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hvaH samprasAraRam",
    text_dev              = "ह्वः सम्प्रसारणम्",
    samagra_slp1          = "hvaH samprasAraRam RO ca san-caNoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ह्वः सम्प्रसारणम् णौ च सन्-चङोः",
    padaccheda_dev        = "ह्वः सम्प्रसारणम्",
    why_dev               = "(सूत्रम् 6.1.32) ह्वः सम्प्रसारणम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
