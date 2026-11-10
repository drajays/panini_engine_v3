"""
6.1.46  न व्यो लिटि  —  VIDHI

Padaccheda: न व्यः लिटि

न व्यो लिटि (6.1.46)
Pāṭha: ashtadhyayi.com data.txt row i=61046 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# Kāśikā 6.1.46: "व्येञ् इत्येतस्य धातोर्लिटि परत आकारादेशो न भवति। संविव्याय। संविव्ययिथ।
# लिट्यभ्यासस्योभयेषाम् (6.1.17) इत्यभ्यासस्य संप्रसारणम्। णलि अचो ञ्णिति (7.2.115) इति वृद्धिः।"
# The prohibition is a tag on the root (6.1.45 reads it), settled before the rules contend (Art. 21 ladder 1).
TAG = "na_vyo_liTi_6_1_46"


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or TAG in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "vyeY" or not t.varnas \
                or t.varnas[-1].slp1 != "e" or "mula_dhatu_v" not in t.varnas[-1].tags:
            continue
        if any("pratyaya" in u.tags and (u.meta.get("source_lakara_upadesha") or "").strip() == "liT"
               for u in state.terms[i + 1:]):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.tags.add(TAG)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.46",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na vyo liwi",
    text_dev              = "न व्यो लिटि",
    samagra_slp1          = "na vyaH liwi At ecaH upadeSe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न व्यः लिटि आत् एचः उपदेशे",
    padaccheda_dev        = "न व्यः लिटि",
    why_dev               = "(सूत्रम् 6.1.46) न व्यो लिटि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
