"""
6.3.34  स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु  —  VIDHI

Padaccheda: स्त्रियाः पुंवत् भाषितपुंस्कात्-अनूङ् (लुप्तषष्ठीकम्) समानाधिकरणे स्त्रियाम् अ-पूरणी-प्रिया-आदिषु

स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु (6.3.34)
Pāṭha: ashtadhyayi.com data.txt row i=63034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from engine.gana import in_gana

_GATE_KEY: str = "6_3_34_striyAH_34"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.34", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.34"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _alug_sup(state: State, vib: str, ok):
    """A samāsa tape: the pūrvapada stem (``samasa_purvapada``), its sup still on the tape (not yet luk-ed by 2.4.71), then the uttarapada.
    Returns the sup Term when ``ok(stem Term)`` holds and the sup carries the vibhakti saṃjñā ``vib``."""
    for i, t in enumerate(state.terms[:-2]):
        s = state.terms[i + 1]
        if "samasa_purvapada" not in t.tags or "sup" not in s.tags or vib not in s.tags or not s.varnas or s.meta.get("alug"):
            continue
        if any(u.varnas and "sup" not in u.tags for u in state.terms[i + 2:]) and ok(t):
            return s
    return None


_SAMANADHIKARANA = frozenset({"samAnADikaraRa", "karmaDAraya", "bahuvrihi"})


def _site(state: State):
    """स्त्रियाः पुंवत् …: the strī-pratyaya (ṭāp, ṅīp …) of a bhāṣitapuṃska pūrvapada goes before a strīliṅga uttarapada in the same case (darśanīyabhāryaḥ,
    rūpavadbhāryaḥ); not an ūṅ-anta, not before a pūraṇī or a priyādi word."""
    for i, t in enumerate(state.terms[:-2]):
        st = state.terms[i + 1]
        if "samasa_purvapada" not in t.tags or not _SAMANADHIKARANA & t.tags or "lex:BAzitapuMska" not in t.tags:
            continue
        if not ({"stri_pratyaya", "stri_wAp"} & st.tags) or not st.varnas or st.meta.get("6_3_34_done") or st.meta.get("upadesha_slp1") == "UN":
            continue
        u = next((x for x in state.terms[i + 2:] if x.varnas and "sup" not in x.tags), None)
        if u is not None and "strīliṅga" in u.tags and "pUraRI" not in u.tags and not in_gana("priyAdiH", _flat(u)):
            return st
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    st = _site(state)
    if st is None:
        return _legacy_act(state)
    st.varnas.clear()                       # puṃvat: the stem stands as the masculine, the strī-pratyaya is gone
    st.tags.add("puMvat")
    st.meta["6_3_34_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.34",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'striyAH puMvadBAzitapuMskAdanUN samAnADikaraRe striyAmapUraRIpriyAdizu',
    text_dev              = 'स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियाऽऽदिषु',
    samagra_slp1          = "uttarapade striyAH puMvat BAzitapu~skAd anUN samAnADikaraRe striyAm apUraRIpriyAdizu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे स्त्रियाः पुंवत् भाषितपुँस्काद् अनूङ् समानाधिकरणे स्त्रियाम् अपूरणीप्रियाऽऽदिषु",
    padaccheda_dev        = "स्त्रियाः पुंवत् भाषितपुंस्कात्-अनूङ् (लुप्तषष्ठीकम्) समानाधिकरणे स्त्रियाम् अ-पूरणी-प्रिया-आदिषु",
    why_dev               = 'भाषितपुंस्कात् ऊङ्-रहितात् स्त्रीशब्दात् समानाधिकरणे स्त्रीलिङ्गे उत्तरपदे परे पुंवद्भावः — दर्शनीयभार्यः, रूपवद्भार्यः।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
