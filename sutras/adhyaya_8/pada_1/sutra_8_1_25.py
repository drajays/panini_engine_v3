"""
8.1.25  पश्यार्थैश्चानालोचने  —  PRATISHEDHA

No ādeśa when the pronoun is *yukta* with a verb of seeing (paśyārtha) used in a sense other than
ālocana (cakṣurvijñāna, seeing with the eye): ग्रामस्तव स्वं समीक्ष्यागतः, ग्रामो मम स्वं समीक्ष्यागतः
(samīkṣya = having considered). With ālocana the ādeśa stands: ग्रामस्ते स्वं पश्यति.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com 8.1.25 
  Source #2 — Kāśikā 8.1.25: "दर्शनं ज्ञानम्। आलोचनं चक्षुर्विज्ञानम्। ग्रामस्तव स्वं समीक्ष्यागतः।
              ग्रामो मम स्वं समीक्ष्यागतः"

Engine: the *yukta* relation (syntactic sambandha) is INPUT on the tape — a following verb Term tagged
``paSyArTa`` (dhātu meaning दर्शन) and ``yukta_pronoun``, and not ``AlocanArTa``. Deriving *yukta* from
kāraka analysis is out of scope (Art. 17: analysis proposes, generation verifies).
Pāṭha: ashtadhyayi.com data.txt row i=81025 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_8.pada_1.enclitic_common import ADESHA_SUTRAS, target
from engine.state import State


def _site(state: State):
    i = target(state, "8.1.25")
    if i is None:
        return None
    return i if any({"paSyArTa", "yukta_pronoun"} <= t.tags and "AlocanArTa" not in t.tags
                    for t in state.terms[i + 1:]) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.25",
    sutra_type=SutraType.PRATISHEDHA,
    text_slp1="pazyArTEScAnAlocane",
    text_dev="पश्यार्थैश्चानालोचने",
    samagra_slp1="padasya padAt anudAttaM sarvamApAdAdO paSyArTEH ca anAlocane yuzmadasmadoH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="पदस्य पदात् अनुदात्तं सर्वमापादादौ पश्यार्थैः च अनालोचने युष्मदस्मदोः न",
    padaccheda_dev="पश्यार्थैः च अनालोचने",
    why_dev="आलोचन से भिन्न अर्थ में पश्यार्थ धातु से युक्त युष्मद्-अस्मद् पद पर ८.१.२०–२३ के आदेश नहीं होते।",
    anuvritti_from=("8.1.17", "8.1.18", "8.1.20", "8.1.24"),
    blocks_sutra_ids=ADESHA_SUTRAS,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
