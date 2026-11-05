"""
6.3.47  द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः  —  VIDHI

Padaccheda: द्वि-अष्टनः संख्यायाम् अ-बहुव्रीहि-अशीत्योः

द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः (6.3.47)
Pāṭha: ashtadhyayi.com data.txt row i=63047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_3_47_dvyazwanaH_47"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.47", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.47"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _uttara(state: State, i: int):
    """The uttarapada of the pūrvapada at ``i``: the next Term with a sound that is not a sup."""
    return next((u for u in state.terms[i + 1:] if u.varnas and "sup" not in u.tags), None)

# SHORTCUT S112: vārttika "prāk śatāt" (6.3.47 – 48: not before śata and what is beyond a hundred) as a list of the numerals from 100 up
_SATADI = frozenset({"Sata", "sahasra", "ayuta", "lakza", "koti", "prayuta", "arbuda"})


def _pur(state: State, pu: str):
    """(index, uttarapada) of a saṃkhyā compound whose pūrvapada is the stem ``pu`` and which is not a bahuvrīhi, not before aśīti, not beyond śata."""
    for i, t in enumerate(state.terms[:-1]):
        if "samasa_purvapada" not in t.tags or "bahuvrihi" in t.tags or _flat(t) != pu or t.meta.get("6_3_47_48_done"):
            continue
        u = _uttara(state, i)
        if u is not None and "saMKyA" in u.tags and _flat(u) != "aSIti" and _flat(u) not in _SATADI:
            return t
    return None


def _site(state: State):
    """द्व्यष्टनः संख्यायाम् अबहुव्रीह्यशीत्योः: dvi / aṣṭan become dvā / aṣṭā (last sound, 1.1.52) before a numeral: dvādaśa, dvāviṃśatiḥ, aṣṭādaśa."""
    return _pur(state, "dvi") or _pur(state, "azwan")


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    t.varnas[-1] = mk("A")               # the last sound i / n goes to ā (1.1.52); a + ā is 6.1.101's
    t.meta["6_3_47_48_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyazwanaH saMKyAyAmabahuvrIhyaSItyoH",
    text_dev              = "द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः",
    samagra_slp1          = "dvi-azwanaH saNKyAyAmuttarapade abahuvrIhi-aSItyoH At",
    samagra_dev           = "द्वि-अष्टनः सङ्ख्यायामुत्तरपदे अबहुव्रीहि-अशीत्योः आत्",
    padaccheda_dev        = "द्वि-अष्टनः संख्यायाम् अ-बहुव्रीहि-अशीत्योः",
    why_dev               = 'संख्यावाचिन्युत्तरपदे बहुव्रीहिं अशीतिं च वर्जयित्वा द्वि-अष्टन्-शब्दयोः अन्त्यस्य आकारादेशः — द्वादश, अष्टादश।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
