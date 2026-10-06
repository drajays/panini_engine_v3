"""
3.1.33  स्यतासी लृलुटोः  —  VIDHI (narrow)

Glass-box paths:
  • lṛṭ (``meta["lakara"] == "lRT"``): insert *sya* vikaraṇa (s+y+a) after
    the dhātu, before the tiṅ ādeśa.  The final 'a' is essential for 7.3.101
    (ato dīrgho yañi) in uttama forms.
  • ``tasi_luT_recipe``: luṭ — insert *tāsi* vikaraṇa before luṭ placeholder.
  • ``luN_sy_recipe``: luṅ P019 — insert *sy* (no 'a') before
    existing 'ti' in the *vṛt* context.
  • lṛṅ (``meta["lakara"] == "lRG"``): insert *sya* vikaraṇa after dhātu.

``cond`` is mechanically blind to *puruṣa* / *vacana* (CONSTITUTION Art. 2).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31033 · स्यतासी लृलुटोः
              padaccheda: स्य-तासी लृ-लुटोः
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31022: धातोः
  Source #2 — Kāśikā 3.1.33 udāharaṇa:
                करिष्यति
                अकरिष्यत्
                श्वः कर्ता
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhavisyat_lrg.py, tests/unit/test_tinanta_ad_lrg_kartari.py, tests/unit/test_tinanta_ad_lrt_kartari.py
  Reference record: sutra_ref_out/3_1_33.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _lrng_ṛ_sy_insert_index(state: State) -> int | None:
    """Lṛṅ + ṛ-dhātu (``vft``) + following ``ti`` ādeśa: insert ``sy`` (not ``sya``)."""
    if (state.meta.get("lakara") or "").strip() != "lRG":
        return None
    if state.meta.get("lrng_ṛ_sy_done"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if not any(v.slp1 == "f" for v in t.varnas):
            continue
        nxt = state.terms[i + 1]
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up not in {"ti", "tip"}:
            continue
        if "".join(v.slp1 for v in nxt.varnas) != "ti":
            continue
        return i + 1
    return None


def _p019_sy_insert_index(state: State) -> int | None:
    if not state.meta.get("luN_sy_recipe"):
        return None
    return _lrng_ṛ_sy_insert_index(state)


def _luT_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "luT" and "lakAra_pratyaya_placeholder" in t.tags:
            return i
    return None


def _lrt_dhatu_index(state: State) -> int | None:
    """For lṛṭ: find dhātu position to insert *sya* immediately after it."""
    if (state.meta.get("lakara") or "").strip() != "lRT":
        return None
    if state.meta.get("3_1_33_lrt_sy_done"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i + 1
    return None


def _lRG_dhatu_index(state: State) -> int | None:
    """For lṛṅ: find dhātu position to insert *sya* immediately after it."""
    if (state.meta.get("lakara") or "").strip() != "lRG":
        return None
    if state.meta.get("3_1_33_lRG_sy_done"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i + 1
    return None


_VIKARANA_BY_SOURCE = {"lRT": "sya", "lRG": "sya", "luT": "tAs"}


def _provenance_site(state: State):
    """(index, source lakāra) where the vikaraṇa goes: after the dhātu, before a tiṅ whose *own source
    lakāra* is lṛṭ / lṛṅ (sya) or luṭ (tās). Read from the affix (Art. 2), not from the derivation."""
    for j, tin in enumerate(state.terms):
        source = (tin.meta.get("source_lakara_upadesha") or "").strip()
        if tin.kind != "pratyaya" or "tin_adesha_3_4_78" not in tin.tags or source not in _VIKARANA_BY_SOURCE:
            continue
        if tin.meta.get("3_1_33_done"):
            continue
        di = next((i for i in range(j - 1, -1, -1) if "dhatu" in state.terms[i].tags), None)
        if di is None:
            continue
        between = [(u.meta.get("upadesha_slp1") or "").strip() for u in state.terms[di + 1:j]]
        if {"sya", "sy", "tAs"} & set(between):
            continue
        return di + 1, source
    return None


def cond(state: State) -> bool:
    if _provenance_site(state) is not None:
        return True
    if _lrng_ṛ_sy_insert_index(state) is not None:
        return True
    if (
        not state.meta.get("luN_sy_done")
        and _p019_sy_insert_index(state) is not None
    ):
        return True
    if _lrt_dhatu_index(state) is not None:
        return True
    if _lRG_dhatu_index(state) is not None:
        return True
    if not state.meta.get("tasi_luT_recipe"):
        return False
    if state.meta.get("3_1_33_tasi_lut_done"):
        return False
    return _luT_index(state) is not None


def act(state: State) -> State:
    site = _provenance_site(state)
    if site is not None:
        idx, source = site
        tin = state.terms[idx]
        if _VIKARANA_BY_SOURCE[source] == "tAs":
            vik = Term(kind="pratyaya", varnas=[mk("t"), mk("A"), mk("s")], tags={"pratyaya", "ardhadhatuka"},
                       meta={"upadesha_slp1": "tAs", "tAsi_vikaraṇa": True})
            state.meta["__why_now_dev__"] = "लुटि स्यतासी लृलुटोः — तास् धातोः परं (भवितास्मि, भविता)। (३.१.३३)"
        else:
            vik = Term(kind="pratyaya", varnas=[mk("s"), mk("y"), mk("a")], tags={"pratyaya", "vikarana", "upadesha"},
                       meta={"upadesha_slp1": "sya", {"lRT": "lrt_vikarana", "lRG": "lRG_vikarana"}[source]: True})
            state.meta["__why_now_dev__"] = "लृटि लृङि च स्यतासी लृलुटोः — स्य धातोः परम् (भविष्यति, अभविष्यत्)। (३.१.३३)"
        state.terms.insert(idx, vik)
        state.terms[idx + 1].meta["3_1_33_done"] = True
        state.meta["3_1_33_lrt_sy_done"] = state.meta["3_1_33_lRG_sy_done"] = True      # keep the older branches quiet
        return state
    j_ṛ = _lrng_ṛ_sy_insert_index(state)
    if j_ṛ is not None:
        sy = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("sy")),
            tags={"pratyaya", "vikarana", "ardhadhatuka"},
            meta={"upadesha_slp1": "sy"},
        )
        state.terms.insert(j_ṛ, sy)
        state.meta["lrng_ṛ_sy_done"] = True
        state.meta.pop("luN_sy_recipe", None)
        state.meta.pop("luN_sy_done", None)
        return state
    j_sy = _p019_sy_insert_index(state)
    if j_sy is not None:
        sy = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("sy")),
            tags={"pratyaya", "vikarana", "ardhadhatuka"},
            meta={"upadesha_slp1": "sy"},
        )
        state.terms.insert(j_sy, sy)
        state.meta["luN_sy_done"] = True
        return state
    j_lrt = _lrt_dhatu_index(state)
    if j_lrt is not None:
        sya = Term(
            kind="pratyaya",
            varnas=[mk("s"), mk("y"), mk("a")],
            tags={"pratyaya", "vikarana", "upadesha"},
            meta={"upadesha_slp1": "sya", "lrt_vikarana": True},
        )
        state.terms.insert(j_lrt, sya)
        state.meta["3_1_33_lrt_sy_done"] = True
        return state
    j_lRG = _lRG_dhatu_index(state)
    if j_lRG is not None:
        # lṛṅ vikaraṇa 'sya': same as lṛṭ but tagged lRG_vikarana for 3.4.114.
        sya = Term(
            kind="pratyaya",
            varnas=[mk("s"), mk("y"), mk("a")],
            tags={"pratyaya", "vikarana", "upadesha"},
            meta={"upadesha_slp1": "sya", "lRG_vikarana": True},
        )
        state.terms.insert(j_lRG, sya)
        state.meta["3_1_33_lRG_sy_done"] = True
        return state
    j = _luT_index(state)
    if j is None:
        return state
    t_as = Term(
        kind="pratyaya",
        varnas=[mk("t"), mk("A"), mk("s")],
        tags={"pratyaya", "ardhadhatuka"},
        meta={"upadesha_slp1": "tAs", "tAsi_vikaraṇa": True},
    )
    state.terms.insert(j, t_as)
    state.meta["3_1_33_tasi_lut_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.33",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'syatAsI lfluwoH',
    text_dev       = 'स्यतासी लृलुटोः',
    samagra_slp1   = "sya-tAsI lf-luwoH",
    samagra_dev    = "स्य-तासी लृ-लुटोः",
    padaccheda_dev = "स्य-तासी / लृ-लुटोः",
    why_dev        = "लुट्-परे तासि-आगमः; P019: लृङि ``sy``-विकरणः।",
    anuvritti_from = ("3.1.22",),
    # स्य / तासि are the vikaraṇas of lṛṭ·lṛṅ / luṭ; the sārvadhātuka vikaraṇas (śap, śyan, śnu, śa, śnam, u, śnā)
    # do not stand there. Declared, so the resolver — not a condition inside each of them — decides.
    apavada_of     = ("3.1.68", "3.1.69", "3.1.73", "3.1.77", "3.1.78", "3.1.79", "3.1.81"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
