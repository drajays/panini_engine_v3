"""
1.3.66  भुजोऽनवने  —  VIDHI

*Padaccheda:* *bhujaḥ* (षष्ठी-एकवचन) / *anavane* (सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* the rudhādi bhuj (bhuja pālanābhyavaharaṇayoḥ) takes ātmanepada when the sense is other than protecting: bhuṅkte, bhuñjāte, bhuñjate.

*Engine (AMENDMENT 30):* the sūtra's own word is the sense ``BujArTa=anavana``, read through ``vivaksita``. Which root is meant is the dhātu
id, not a vivakṣā: the rudhādi bhuj (gaṇa 7, 07.0017) only. Kāśikā: "अनवन इति प्रतिषेधेन रौधादिकस्यैव ग्रहणं विज्ञायते, न तौदादिकस्य
भुजो कौटिल्ये (धा० पा० १४१८) इत्यस्य, तेनेह न भवति — विभुजति पाणिम्." With the sense unmarked it declines and 1.3.78 gives
parasmaipada (bhunakty enam agnir āhitaḥ, protecting).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com data.txt row i = 13066.
  Source #2 — Kāśikā 1.3.66: भुङ्क्ते, भुञ्जाते, भुञ्जते। अनवने इति किम्? भुनक्त्येनमग्निराहितः।
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita

_REGISTRY_KEY = "1_3_66_Buj_anavana"
_STAMP_KEY    = "Atmanepada_1_3_66"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada" or state.meta.get(_STAMP_KEY):
        return False
    if not any("dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "Buja~" and t.meta.get("gana") == 7
               for t in state.terms):
        return False
    return vivaksita(state, "BujArTa", "anavana")


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.66",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='Bujonavane',
    text_dev='भुजोऽनवने',
    samagra_slp1="BujaH anavane Atmanepadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="भुजः अनवने आत्मनेपदम्",
    padaccheda_dev="भुजः (षष्ठी-एकवचन) / अनवने (सप्तमी-एकवचन)",
    why_dev=(
        "रौधादिकस्य भुज्-धातोः अपालनार्थे विवक्षिते आत्मनेपदम् — "
        "भुङ्क्ते, भुञ्जाते, भुञ्जते; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
