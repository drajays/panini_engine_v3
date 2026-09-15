"""
5.4.154  शेषाद्विभाषा  —  VIDHI (narrow for P027)

P027 bahuvrīhi: *bahu* + *khaṭvā* → samāsānta **kap** (taken here, not declined).

v3 narrow slice:
  • recipe arms ``state.meta['P027_5_4_154_kap_arm']``
  • requires bahuvrīhi saṃjñā registry from **2.2.24**
  • expects two samāsa members: ``bahu`` + ``KaTvA`` (upadeśa snapshots)
  • appends a kap residue as phonetic ``ka`` (upadeśa stored as ``kap``)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 54154 · शेषाद्विभाषा
              padaccheda: शेषात् विभाषा
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः | 54068: समासान्ताः | 54113: बहुव्रीहौ | 54151: कप्
  Source #2 — Kāśikā 5.4.154 udāharaṇa:
                बह्व्यः खट्वा अस्मिन् बहुखट्वकः
                बहुमालकः
                बहुवीणकः
  Cross-check — surface pinned by: tests/unit/test_bahuKaTvakaH_bahuvrihi.py
  Reference record: sutra_ref_out/5_4_154.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    if not state.meta.get("P027_5_4_154_kap_arm"):
        return None
    if state.meta.get("P027_5_4_154_kap_done"):
        return None
    if not state.samjna_registry.get("2.2.24_anekam_anyapadartha"):
        return None
    if len(state.terms) != 2:
        return None
    a, b = state.terms[0], state.terms[1]
    if a.kind != "prakriti" or b.kind != "prakriti":
        return None
    if "samasa_member" not in a.tags or "samasa_member" not in b.tags:
        return None
    if (a.meta.get("upadesha_slp1") or "").strip() != "bahu":
        return None
    if (b.meta.get("upadesha_slp1") or "").strip() != "KaTvA":
        return None
    return True


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    kap = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ka")),
        tags={"pratyaya", "upadesha", "taddhita"},
        meta={"upadesha_slp1": "kap", "P027_kap_residue": True},
    )
    state.terms.append(kap)
    state.meta["P027_5_4_154_kap_done"] = True
    state.meta.pop("P027_5_4_154_kap_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="5.4.154",
    sutra_type=SutraType.VIDHI,
    text_slp1="SezAd viBAzA",
    text_dev="शेषाद्विभाषा",
    padaccheda_dev="शेषात् / विभाषा",
    why_dev="समासान्ते शेष-विषये कप्-प्रत्ययः विभाषा (P027 — बहु+खट्वा)।",
    anuvritti_from=("5.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

