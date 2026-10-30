"""
6.4.47  भ्रस्जो रोपधयोः रमन्यतरस्याम्  —  VIBHASHA

Padaccheda: भ्रस्जः र-उपधयोः रम् अन्यतरस्याम्

भ्रस्जो रोपधयोः रमन्यतरस्याम् (6.4.47)
Pāṭha: ashtadhyayi.com data.txt row i=64047 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk

_NASAL = frozenset("mnNRY")                      # anunāsika-final: m n ṅ ṇ ñ
_JHAL = frozenset("JBGQDjbgqdKPCWTcwtkpSzsh")


def _head(state: State, i: int):
    """The pratyaya that stands right after the aṅga at ``i`` (an āgama belongs to the affix it precedes; a lopa ghost still counts)."""
    return next((u for u in state.terms[i + 1:] if "agama" not in u.tags), None)


def _name(t) -> str:
    return (t.meta.get("upadesha_slp1") or "").strip()


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _kvi_or_jhal_kngit(h) -> bool:
    """क्विझलोः क्ङिति: a kvip, or a kṅit pratyaya that begins with a jhal."""
    return h is not None and (_name(h) == "kvip" or ("kngiti" in h.tags and bool(h.varnas) and h.varnas[0].slp1 in _JHAL))


# SHORTCUT S83: the āgama / count is shown as its bare letter or upasarga tags, without an upadeśa Term of its own — a real āgama Term (S72)
def _site(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or t.meta.get("6_4_47_ram_done") or _flat(t) != "Brasj":
            continue
        h = _head(state, i)
        if h is not None and "ardhadhatuka" in h.tags and "kngiti" not in h.tags:      # before a kṅit the samprasāraṇa takes it (पूर्वविप्रतिषेध): भृष्टः
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    r = mk("r")
    r.tags.add("agama")
    del t.varnas[-2]            # भ्रस्ज्: the upadhā s and the repha go ...
    del t.varnas[1]
    k = max(j for j, v in enumerate(t.varnas) if v.slp1 in "aAiIuUfFxXeEoO")
    t.varnas.insert(k + 1, r)   # ... and the mit आगम् रम् (the r) stands after the last ac: भ्रस्ज् → भर्ज्
    t.meta["6_4_47_ram_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.47",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "Brasjo ropaDayoH ramanyatarasyAm",
    text_dev              = "भ्रस्जो रोपधयोः रमन्यतरस्याम्",
    samagra_slp1          = "BrasjaH ra-upaDayoH anyatarasyAm ramArDaDAtuke",
    samagra_dev           = "भ्रस्जः र-उपधयोः अन्यतरस्याम् रमार्धधातुके",
    padaccheda_dev        = "भ्रस्जः र-उपधयोः रम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.4.47) भ्रस्जो रोपधयोः रमन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
