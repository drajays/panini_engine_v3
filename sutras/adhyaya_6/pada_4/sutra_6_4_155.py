"""
6.4.155  टेः  —  VIDHI (narrow P025 *ṭi*-lopa)

Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com ``data.txt`` i=604155):
  *iṣṭhavadbhāvaḥ* — *ṭi*-portion behaviour like *iṣṭha*; in P025 the final ``u``
  of *paṭu* is elided before the *ṇic* residue ``i``.

v3 narrow slice:
  • ``state.meta["P025_6_4_155_Ti_lopa_arm"] == True``
  • first ``Term`` is *dhātu* *paṭu* (``upadesha_slp1 == "paTu"``) whose *varṇa*s
    end in ``…paTu``
  • second ``Term`` is the *ṇic* ``pratyaya`` (``meta["P025_Nic_pratyaya"]``),
    which after **1.3.9** surfaces as ``i``
  • *act*: delete the final ``u`` of the stem (``paTu`` → ``paT``).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64155 · टेः
              padaccheda: टेः
              anuvṛtti:   64001: अङ्गस्य | 64129: भस्य | 64147: लोपः | 64154: इष्ठेमेयस्सु
  Source #2 — Kāśikā 6.4.155 udāharaṇa:
                पटु — पटिष्ठः
                पटिमा
                पटीयान्
  Cross-check — surface pinned by: tests/unit/test_paTayati_paTu_Nic.py
  Reference record: sutra_ref_out/6_4_155.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State):
    if len(state.terms) < 2:
        return None
    ang, nic = state.terms[0], state.terms[1]
    if "dhatu" not in ang.tags:
        return None
    if (ang.meta.get("upadesha_slp1") or "").strip() != "paTu":
        return None
    if not ang.varnas or ang.varnas[-1].slp1 != "u":
        return None
    if "".join(v.slp1 for v in ang.varnas) != "paTu":
        return None
    if nic.kind != "pratyaya":
        return None
    if not nic.meta.get("P025_Nic_pratyaya"):
        return None
    if not nic.varnas or nic.varnas[0].slp1 != "i":
        return None
    return 0


def _legacy_cond(state: State) -> bool:
    return _site(state) is not None


def _legacy_act(state: State) -> State:
    ti = _site(state)
    if ti is None:
        return state
    ang = state.terms[ti]
    del ang.varnas[-1]
    ang.meta["upadesha_slp1"] = "paT"
    return state


from engine.state import State, Term
from phonology import mk

_PR = ("izWan", "imanic", "Iyasu~n")      # iṣṭhan, imanic, īyasun
_FAM = "6_4_155_family_done"                # the ṭi of this aṅga has been dealt with by one of 6.4.154 – 159 / 5.3.61 – 64
_AC = frozenset("aAiIuUfFxXeEoO")
_DONE = {_FAM: True, "6_4_143_dit_done": True, "6_4_148_lopa_done": True}      # the aṅga's ṭi is dealt with: the existing guards of 6.4.148 / 6.4.134 keep them from acting on it again


def _flat(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _ti_site(state: State, prs=_PR):
    """The bha aṅga Term standing before iṣṭhan / imanic / īyasun (its pratyaya Term follows it), not yet dealt with by the ṭi-lopa family."""
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if {"anga", "bha"} <= t.tags and not t.meta.get(_FAM) and "taddhita" in pr.tags and any(f"origin_pratyaya:{u}" in pr.tags for u in prs):
            return i
    return None


def _new_cond(state: State) -> bool:
    i = _ti_site(state)
    return i is not None and any(v.slp1 in _AC for v in state.terms[i].varnas)


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    t = state.terms[_ti_site(state)]
    j = max(k for k, v in enumerate(t.varnas) if v.slp1 in _AC)      # 1.1.64 aco 'ntyādi ṭi: the last vowel and what follows it
    del t.varnas[j:]
    t.meta.update(_DONE)
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.155",
    sutra_type=SutraType.VIDHI,
    text_slp1='weH',
    text_dev='टेः',
    samagra_slp1="aNgasya asidDavadatrABAt Basya weH lopaH izWa-iman-Iyassu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="अङ्गस्य असिद्धवदत्राभात् भस्य टेः लोपः इष्ठ-इमन्-ईयस्सु",
    padaccheda_dev="इष्ठवत्-भावः",
    why_dev="पटु-अन्त्य-उ-कार-लोपः णिच्-पूर्वम् (P025)।",
    anuvritti_from=("6.4.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
