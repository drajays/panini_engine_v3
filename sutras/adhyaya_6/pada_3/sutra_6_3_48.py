"""
6.3.48  त्रेस्त्रयः  —  VIDHI

Padaccheda: त्रेः त्रयः

त्रेस्त्रयः (6.3.48)
Pāṭha: ashtadhyayi.com data.txt row i=63048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_3_48_trestrayaH_48"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.48", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.48"
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
    """त्रेस्त्रयः: tri becomes trayas before a numeral, as above: trayodaśa, trayoviṃśatiḥ, trayastriṃśat."""
    return _pur(state, "tri")


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    t.varnas[:] = [mk(c) for c in "trayas"]        # anekāl: the whole tri (1.1.55)
    t.meta["6_3_47_48_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "trestrayaH",
    text_dev              = "त्रेस्त्रयः",
    samagra_slp1          = "treH saNKyAyAmuttarapade abahuvrIhi-aSItyoH At",
    samagra_dev           = "त्रेः सङ्ख्यायामुत्तरपदे अबहुव्रीहि-अशीत्योः आत्",
    padaccheda_dev        = "त्रेः त्रयः",
    why_dev               = 'संख्यावाचिन्युत्तरपदे बहुव्रीहिं अशीतिं च वर्जयित्वा त्रि-शब्दस्य त्रयसादेशः — त्रयोदश, त्रयस्त्रिंशत्।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
