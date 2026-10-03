"""
6.4.88  भुवो वुग्लुङ्लिटोः  —  VIDHI

Padaccheda: भुवः वुक् लुङ्-लिटोः

For bhū in luṅ/liṭ, insert vuk (= v, after IT lopa of u and k) as an āgama
immediately after the dhātu term.  vuk's u and k are both it → only v survives.

cond (structural — no lakāra read):
  - dhātu upadesha is BU/BU~
  - luṅ context: dhātu has ``aT_agama_context`` tag (set by 3.2.110)
    OR liṭ context: an abhyāsa term is on the tape (set by 6.1.4 dvitva)
  - vuk not already inserted

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64088 · भुवो वुग्लुङ्लिटोः
              padaccheda: भुवः वुक् लुङ्-लिटोः
              anuvṛtti:   64001: अङ्गस्य | 64077: अचि
  Source #2 — Kāśikā 6.4.88 udāharaṇa:
                अभूवन्
                अभूवम्
                लिटि — बभूव
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhut_lung.py
  Reference record: sutra_ref_out/6_4_88.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import mk


def _find_dhatu_index(state: State) -> int | None:
    for i in range(len(state.terms) - 1, -1, -1):
        if "dhatu" in state.terms[i].tags and "abhyasa" not in state.terms[i].tags:
            return i
    return None


def _already_done(state: State) -> bool:
    return state.samjna_registry.get("6_4_88_vuk_inserted") is True


def _is_bhu_dhatu(state: State) -> bool:
    di = _find_dhatu_index(state)
    if di is None:
        return False
    up = (state.terms[di].meta.get("upadesha_slp1") or "").strip()
    return up in {"BU", "BU~"}


def _lakara_identities(state: State) -> set[str]:
    """The lakāras the affixes on the tape come from — read from the affixes' own upadeśa (the lakāra
    placeholder before 3.4.78, ``source_lakara_upadesha`` after it), never from a coordinate (Art. 2)."""
    from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import LAKAARA_UPADESHA_SLP1

    out: set[str] = set()
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        for key in ("source_lakara_upadesha", "upadesha_slp1"):
            up = (t.meta.get(key) or "").strip()
            if up in LAKAARA_UPADESHA_SLP1:
                out.add(up)
    return out


def _luN_or_liT_context(state: State) -> bool:
    """True when luṅ or liṭ is the nimitta (भुवो वुग्लुङ्लिटोः).

    The lakāra comes from the affix. When the tape carries no lakāra identity (recipes that build the
    tape by hand) the older structural witnesses decide: luṅ — ``aT_agama_context`` / ``aT_agama_6_4_71_done``
    (but laṅ has those too, so they are only used when no lakāra is known); liṭ — an ``abhyasa`` term.
    """
    ids = _lakara_identities(state)
    if ids:
        return bool(ids & {"luG", "liT"})
    for t in state.terms:
        if "aT_agama_context" in t.tags or t.meta.get("aT_agama_6_4_71_done"):
            return True
    return any("abhyasa" in t.tags for t in state.terms)


def cond(state: State) -> bool:
    if _already_done(state):
        return False
    if not _is_bhu_dhatu(state):
        return False
    if not _luN_or_liT_context(state):
        return False
    di = _find_dhatu_index(state)
    if di is None:
        return False
    if di + 1 < len(state.terms) and state.terms[di + 1].meta.get("vuk_6_4_88"):
        return False
    return True


def act(state: State) -> State:
    di = _find_dhatu_index(state)
    if di is None:
        return state

    v_varna = mk("v")
    u_varna = mk("u")
    u_varna.tags.add("it_candidate_halantyam")
    k_varna = mk("k")
    k_varna.tags.add("it_candidate_halantyam")

    vuk_term = Term(
        kind="agama",
        varnas=[v_varna, u_varna, k_varna],
        tags={"agama", "pratyaya"},
        meta={"upadesha_slp1": "vuk", "vuk_6_4_88": True},
    )
    state.terms.insert(di + 1, vuk_term)
    state.samjna_registry["6_4_88_vuk_inserted"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Buvo vugluNliwoH",
    text_dev              = "भुवो वुग्लुङ्लिटोः",
    padaccheda_dev        = "भुवः वुक् लुङ्-लिटोः",
    why_dev               = "भू-धातोः लुङि लिटि च वुक्-आगमः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
