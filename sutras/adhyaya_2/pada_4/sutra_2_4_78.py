"""
2.4.78  विभाषा घ्राधेट्शाच्छासः  —  VIBHASHA

Kāśikā 2.4.78: "घ्रा धेट् शा छा सा इत्येतेभ्य उत्तरस्य सिचः परस्मैपदेषु विभाषा लुग् भवति। धेटः पूर्वेण नित्ये
प्राप्ते विभाषार्थं वचनम्। परिशिष्टानामप्राप्ते। अघ्रात्, अघ्रासीत्। अधात्, अधासीत्। अशात् अशासीत्। अच्छात्,
अच्छासीत्। असात्, असासीत्।  परस्मैपदेष्वित्येव — अघ्रासातां सुमनसौ देवदत्तेन॥"

Engine: the five roots (GrA, DeW, So, Co, zo) before a luṅ sic in parasmaipada: the sic is optionally
removed (luk, same act as 2.4.77).  DeW leaves 2.4.77's list (the Kāśikā says its nitya luk there is
turned optional here), so the one rule 2.4.78 carries both readings.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_2.pada_4.sutra_2_4_77 import _find_sic_index, _parasmaipada

_ROOTS = frozenset({"GrA", "DeW", "So", "Co", "zo"})


def _root(state: State) -> bool:
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    return dh is not None and (dh.meta.get("upadesha_slp1") or "").strip().replace("~", "") in _ROOTS


def cond(state: State) -> bool:
    return _find_sic_index(state) is not None and _root(state) and _parasmaipada(state)


def act(state: State) -> State:
    j = _find_sic_index(state)
    if j:
        state.terms[j - 1].tags.add("vikarana_luk")      # the aṅga remembers its luk'd vikaraṇa, as in 2.4.77
    state.terms.pop(j)
    state.samjna_registry["2.4.78_sic_luk"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.78",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA GrADewSAcCAsaH",
    text_dev              = "विभाषा घ्राधेट्शाच्छासः",
    samagra_slp1          = "GrA-Dew-SA-CA-saH sicaH parasmEpadezu viBAzA luk",
    samagra_dev           = "घ्रा-धेट्-शा-छा-सः सिचः परस्मैपदेषु विभाषा लुक्",
    padaccheda_dev        = "विभाषा घ्रा-धेट्-शा-छा-सः",
    why_dev               = "घ्रादिभ्यः परस्य सिचः परस्मैपदे विभाषा लुक् (अघ्रात् / अघ्रासीत्) — काशिका २.४.७८।",
    anuvritti_from        = ('2.4.77',),
    vibhasha_default      = False,
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
