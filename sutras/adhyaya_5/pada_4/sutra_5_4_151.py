"""
5.4.151  उरःप्रभृतिभ्यः कप्  —  VIDHI (narrow for P024)

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

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 54151 · उरःप्रभृतिभ्यः कप्
              padaccheda: उरः-प्रभृतिभ्यः कप्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः | 54068: समासान्ताः | 54113: बहुव्रीहौ
  Source #2 — Kāśikā 5.4.151 udāharaṇa:
                व्यूढमुरोऽस्य व्यूढोरस्कः
                प्रियसर्पिष्कः
                अवमुक्तोपानत्कः
  Cross-check — surface pinned by: tests/unit/test_mahoraskena_bahuvrihi.py
  Reference record: sutra_ref_out/5_4_151.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    if state.meta.get("P024_5_4_151_kap_done"):
        return None
    if len(state.terms) != 2:
        return None
    a, b = state.terms[0], state.terms[1]
    if a.kind != "prakriti" or b.kind != "prakriti":
        return None
    if "samasa_member" not in a.tags or "samasa_member" not in b.tags:
        return None
    # उरः प्रभृतिभ्यः: the condition is on the *uttarapada* (uras and its
    # class) — not on which pūrvapada precedes it. मह्/व्यूढ both attested
    # in the Kāśikā udāharaṇa above (महोरस्कः, व्यूढोरस्कः).
    if (b.meta.get("upadesha_slp1") or "").strip() != "uras":
        return None
    return True


def _legacy_cond(state: State) -> bool:
    return _site(state) is not None


def _legacy_act(state: State) -> State:
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


import re
from engine import gana
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_MEMBERS = gana.members("uraHpraBftayaH")      # SHORTCUT S62: the compound is one Term; its last member is read off the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.151", state, "5.4.68") or state.meta.get("kap_barred"):
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: any(f.endswith(m) and f != m for m in _MEMBERS))
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('bahuvrIhi',)):
        return None
    return 'kap'


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.151")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.151", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.4.151"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].tags.add("samasanta")
    return state


SUTRA = SutraRecord(
    sutra_id="5.4.151",
    sutra_type=SutraType.VIDHI,
    text_slp1='uraHpraBftiByaH kap',
    text_dev='उरःप्रभृतिभ्यः कप्',
    samagra_slp1="pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA uraHpraBftiByaH kap bahuvrIhO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा उरःप्रभृतिभ्यः कप् बहुव्रीहौ",
    padaccheda_dev="उरः / प्रभृतिभ्यः / कप्",
    why_dev="उर-आदिभ्यः कप्-प्रत्ययः (P024 — महत्+उरस्)।",
    anuvritti_from=("5.4.1",),
    apavada_of     = ('5.4.154',),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
