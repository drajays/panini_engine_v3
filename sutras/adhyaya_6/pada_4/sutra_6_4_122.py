"""
6.4.122  तॄफलभजत्रपश्च  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=64122
- Kāśikā: "तॄ फल भज त्रप इत्येतेषाम् अङ्गानाम् अत एत्वम् अभ्यासलोपश्च भवति किति लिटि सेटि थलि च" —
  तेरतुः, तेरुः, तेरिथ; फेलतुः, फेलुः, फेलिथ; भेजतुः, भेजुः, भेजिथ; त्रेपे, त्रेपाते, त्रेपिरे
- Cross-validation: tests/regression/test_findings_probe_loop.py (तेरतुः)

The four dhātus tṝ, phal, bhaj, trap get the treatment of 6.4.120 (a → e, the abhyāsa drops) although they fail its
conditions: tṝ's a is the guṇa of 7.4.11 ṛcchatyṝtām, phal and bhaj begin with an ādeśa in the abhyāsa
(8.4.54), trap has a conjunct. Licence as in 6.4.120/6.4.121: a kit liṭ ending, or thal with iṭ.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

from sutras.adhyaya_6.pada_4.sutra_6_4_120 import _ending_licenses

_SHAPES = frozenset({"tar", "Pal", "Baj", "trap"})     # tṝ stands as tar after 7.4.11; the others as taught


def _find(state: State) -> int | None:
    if not any((u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in state.terms):
        return None
    for i in range(1, len(state.terms) - 1):
        ab, t, nxt = state.terms[i - 1], state.terms[i], state.terms[i + 1]
        if "abhyasa" not in ab.tags or "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("6_4_120_done"):
            continue
        shape = "".join(v.slp1 for v in t.varnas)
        if shape not in _SHAPES:
            continue
        if shape == "tar" and (t.meta.get("upadesha_slp1") or "").strip() != "tF":
            continue                       # only the tar of tṝ is named here
        if _ending_licenses(nxt):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    idx = _find(state)
    t = state.terms[idx]
    j = next(j for j, v in enumerate(t.varnas) if v.slp1 == "a")
    t.varnas[j] = mk("e")
    t.meta["6_4_120_done"] = True
    del state.terms[idx - 1]
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.122",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "tFPalaBajatrapaSca",
    text_dev              = "तॄफलभजत्रपश्च",
    samagra_slp1          = "aNgasya asidDavadatrABAt tF-Pala-Baja-trapaH ca kNiti aByAsalopaH ataH Tali sewi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् तॄ-फल-भज-त्रपः च क्ङिति अभ्यासलोपः अतः थलि सेटि",
    padaccheda_dev        = "तॄ-फल-भज-त्रपः च",
    why_dev               = "तॄ-फल-भज-त्रपाम् अत एत्वम् अभ्यासलोपश्च किति लिटि सेटि थलि च (तेरतुः, फेलुः, भेजिथ, त्रेपे)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
