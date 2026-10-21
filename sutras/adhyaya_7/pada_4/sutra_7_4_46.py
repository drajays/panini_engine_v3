"""
7.4.46  दो दद् घोः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=74046 · padaccheda दः दद् घोः · samagra "अङ्गस्य दः दथ् घोः ति किति" (ति किति from 7.4.40)
- Kāśikā: "दा इत्येतस्य घुसंज्ञकस्य ददित्ययमादेशो भवति तकारादौ किति प्रत्यय परतः। दत्तः। दत्तवान्। दत्तिः। …
  अयमादेशः थान्तः इष्यते।"
  pratyudāharaṇa: "दः इति किम्? धीतः। … घोः इति किम्? दाप् लवने दातं बर्हिः। दैप् शोधने अवदातम् मुखम्।"
- SK: "घुसंज्ञकस्य दा इत्यस्य दथ् स्यात्तादौ किति। चर्त्वम्। दत्तः।"
- Owner ruling 2026-10-21: the ādeśa is दथ् (SK / Kāśikā iṣṭi); apavāda of 6.4.66 by येन नाप्राप्ते (PŚ) — wherever
  दा + तादि कित् stands, 6.4.66 (घु + हलादि क्ङित्) has already applied.
- Cross-validation: tests/regression/test_ktva_loop.py (दत्त्वा: दथ् + त्वा, 8.4.55 खरि च)

Site: the दा-form ghu dhātu (डुदाञ्, दाण् दाने) right before a kit affix beginning with t. The whole dhātu becomes दथ्
(1.1.55 अनेकाल्शित्सर्वस्य). दो and देङ् are not taken yet (7.4.40 / owner question pending).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_DA_GHU = frozenset({"qudAY", "dAR"})          # डुदाञ् दाने (03.0010), दाण् दाने (01.1079)
_DONE = "7_4_46_daT_done"


def _site(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get(_DONE):
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in _DA_GHU:
            continue
        nxt = state.terms[i + 1]
        if not (nxt.kind == "pratyaya" or "pratyaya" in nxt.tags) or not nxt.varnas or nxt.varnas[0].slp1 != "t":
            continue
        if {"it:kit", "kit"} & nxt.tags or "k" in (nxt.meta.get("it_markers") or ()):
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    state.terms[i].varnas = list(parse_slp1_upadesha_sequence("daT"))
    state.terms[i].meta[_DONE] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.46",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "do dad GoH",
    text_dev              = "दो दद् घोः",
    samagra_slp1          = "aNgasya daH daT GoH ti kiti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य दः दथ् घोः ति किति",
    padaccheda_dev        = "दः दद् घोः",
    why_dev               = "घुसंज्ञकस्य दा-रूपस्य तादौ किति दथ् (दत्तः, दत्त्वा)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
    apavada_of            = ("6.4.66",),
)

register_sutra(SUTRA)
