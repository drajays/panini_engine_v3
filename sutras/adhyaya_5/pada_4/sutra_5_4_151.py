"""
5.4.151  उरः प्रभृतिभ्यः कप्  —  VIDHI (narrow for P024)

Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com ``data.txt`` i=504151):
  *uraḥ prabhṛtibhyaḥ kap* — *kap* after stems like *uras-* in the stated class.

v3 narrow slice (P024 महोरस्केन):
  When recipe-armed and the state has two *samāsa* members ``mahat`` + ``uras``,
  append a *kap* residue as phonetic ``ka`` (the *p* *it* of *kap* is not modeled
  as a separate *varṇa* here; the glass-box goal is the attested compound stem
  ``mahoraska`` before *sup*).

  • ``state.meta["P024_5_4_151_kap_arm"] == True``
  • ``terms[0].meta["upadesha_slp1"] == "mahat"`` and ``terms[1]… == "uras"``
  • both tagged ``samasa_member``
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    if not state.meta.get("P024_5_4_151_kap_arm"):
        return None
    if state.meta.get("P024_5_4_151_kap_done"):
        return None
    if len(state.terms) != 2:
        return None
    a, b = state.terms[0], state.terms[1]
    if a.kind != "prakriti" or b.kind != "prakriti":
        return None
    if "samasa_member" not in a.tags or "samasa_member" not in b.tags:
        return None
    if (a.meta.get("upadesha_slp1") or "").strip() != "mahat":
        return None
    if (b.meta.get("upadesha_slp1") or "").strip() != "uras":
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
        meta={"upadesha_slp1": "kap", "P024_kap_residue": True},
    )
    state.terms.append(kap)
    state.meta["P024_5_4_151_kap_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="5.4.151",
    sutra_type=SutraType.VIDHI,
    text_slp1="uraH prabhftiByaH kap",
    text_dev="उरः प्रभृतिभ्यः कप्",
    padaccheda_dev="उरः / प्रभृतिभ्यः / कप्",
    why_dev="उर-आदिभ्यः कप्-प्रत्ययः (P024 — महत्+उरस्)।",
    anuvritti_from=("5.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
