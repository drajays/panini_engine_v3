"""
1.3.49  अनोरकर्मकात्  —  VIDHI

*Padaccheda:* *anoḥ* (पञ्चमी) / *akarmakāt* (पञ्चमी).

*Anuvṛtti:* ātmanepada 1.3.12; vadaḥ 1.3.47; vyaktavācām 1.3.48 (samuccāraṇe does not continue: Kāśikā "वदः इति व्यक्तवाचामिति च वर्तते").

*Content:* after anu, vad used with no object meant takes ātmanepada when the speakers are articulate: anuvadate kaṭhaḥ kalāpasya
(Kāśikā: अनुः सादृश्ये, "यथा कलापोऽधीयानो वदति तथा कठ इत्यर्थः").

*Engine (AMENDMENT 30):* the upasarga Term ``anu`` is on the tape; ``vyaktavAk`` and ``karmakatva=akarmaka`` are context facts read through
``vivaksita``. The dhātu's lexical karmakatva is not enough on its own: vad is sakarmaka in the dhātupāṭha, and Kāśikā's
"अकर्मकादिति किम्? पूर्वमेव यजुरुदितमनुवदति" shows the same root with an object stays parasmaipada, so akarmaka is the use meant.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com data.txt row i = 13049.
  Source #2 — Kāśikā 1.3.49: अनुवदते कठः कलापस्य। अनुवदते मौद्गः पैप्पलादस्य। ... व्यक्तवाचामित्येव — अनुवदति वीणा.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita

_REGISTRY_KEY = "1_3_49_anoH_akarmakAt"
_STAMP_KEY    = "Atmanepada_1_3_49"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada" or state.meta.get(_STAMP_KEY):
        return False
    if not any("dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "vada~" and t.meta.get("gana") == 1
               for t in state.terms):
        return False
    if not any(t.kind == "upasarga" and (t.meta.get("upadesha_slp1") or "").strip() == "anu" for t in state.terms):
        return False
    return vivaksita(state, "vyaktavAk", "vyaktavAc") and vivaksita(state, "karmakatva", "akarmaka")


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.49",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='anorakarmakAt',
    text_dev='अनोरकर्मकात्',
    samagra_slp1="anoH akarmakAt Atmanepadam vadaH vyaktavAcAM samuccAraRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="अनोः अकर्मकात् आत्मनेपदम् वदः व्यक्तवाचां समुच्चारणे",
    padaccheda_dev="अनोः (पञ्चमी) / अकर्मकात् (पञ्चमी)",
    why_dev=(
        "अनु-पूर्वात् अकर्मकात् वद्-धातोः व्यक्तवाग्विषये आत्मनेपदम् — "
        "अनुवदते कठः कलापस्य; "
        "१.३.४७ इत्यतः वदः, १.३.४८ इत्यतः व्यक्तवाचाम्, १.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.47", "1.3.48"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
