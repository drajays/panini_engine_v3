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


def _legacy_cond(state: State) -> bool:
    return _site(state) is not None


def _legacy_act(state: State) -> State:
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
    return state


import re
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_RX = re.compile(r"[a-zA-Z]+[^fIU]$")      # SHORTCUT S62: the compound is one Term (S30 / S36); its kind and its last member are read off the lex: tags and the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.154", state, "5.4.68") or state.meta.get("kap_barred"):
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: _RX.search(f) is not None)
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('bahuvrIhi',)):
        return None
    return ('kap', '-')


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.154")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.154", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.4.154"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].tags.add("samasanta")
    return state


SUTRA = SutraRecord(
    sutra_id="5.4.154",
    sutra_type=SutraType.VIDHI,
    text_slp1='SezAdviBAzA',
    text_dev='शेषाद्विभाषा',
    samagra_slp1="pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH samAsAntAH vA SezAt viBAzA bahuvrIhO kap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः समासान्ताः वा शेषात् विभाषा बहुव्रीहौ कप्",
    padaccheda_dev="शेषात् / विभाषा",
    why_dev="समासान्ते शेष-विषये कप्-प्रत्ययः विभाषा (P027 — बहु+खट्वा)।",
    anuvritti_from=("5.4.1",),
    also_vidhi     = True,          # the vā reading leaves the tape as it is
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

