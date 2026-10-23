"""
6.4.34  शास इदङ्हलोः  —  VIDHI

Padaccheda: शासः इत् अङ्-हलोः

शास इदङ्हलोः (6.4.34)
Pāṭha: ashtadhyayi.com data.txt row i=64034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.ang_adesha import stem
from engine.nimitta_predicates import is_kit
from phonology import HAL, mk
from engine.krt_eligibility import samhita_gate_eligible

def _site(state: State):
    """शास इदङ्हलोः: upadhā ā of śās → i before aṅ or a hal-initial kit/ṅit: अन्वशिषत्, शिष्टः, शिष्मः (not शासति: vowel-initial)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("6_4_34_done") or stem(t) != "SAs" or t.meta.get("dhatu_prefix_slp1"):    # āṅ-śās (icchāyām) is आशास्: āśāste
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None:
            continue
        ang = (nxt.meta.get("upadesha_slp1") or "").strip() == "aG"
        hal_kngit = nxt.varnas[0].slp1 in HAL and bool({"kngiti", "it:kit", "it:Git"} & nxt.tags or is_kit(nxt))
        k = max((n for n, v in enumerate(t.varnas) if v.slp1 == "A"), default=None)
        if (ang or hal_kngit) and k is not None:
            return t, k
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, k = _site(state)
    t.varnas[k] = mk("i")
    t.meta["6_4_34_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.34",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "SAsa idaNhaloH",
    text_dev              = "शास इदङ्हलोः",
    samagra_slp1          = "aNgasya asidDavadatrABAt SAsaH it aN-haloH nalopaH upaDAyAH kNiti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् शासः इत् अङ्-हलोः नलोपः उपधायाः क्ङिति",
    padaccheda_dev        = "शासः इत् अङ्-हलोः",
    why_dev               = "(सूत्रम् 6.4.34) शास इदङ्हलोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
