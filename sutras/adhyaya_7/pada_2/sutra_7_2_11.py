"""
7.2.11  श्र्युकः किति  —  PRATISHEDHA

Sources consulted:
- ashtadhyayi.com data.txt row i=72011 · padaccheda श्रि-उकः किति · anuvṛtti न इट् (7.2.8), एकाचः (7.2.10)
- Kāśikā: "श्रि इत्येतस्योगन्तानां च किति प्रत्यये परत इडागमो न भवति। श्रित्वा। श्रितः। श्रितवान्। उगन्तानां च — युत्वा।
  युतः। युतवान्। लूत्वा। लूनः। लूनवान्। वृत्वा। वृतः। वृतवान्। तीर्त्वा। तीर्णः। तीर्णवान्।"
  pratyudāharaṇa: "श्र्युक इति किम्? विदितः। कितीति किम्? श्रयिता। श्रयितुम्। श्रयितव्यम्।"
- Cross-validation: tests/regression/test_ktva_loop.py (भूत्वा, श्रुत्वा; Vidyut floor lists 7.2.11 for yutaH, vftaH)

The iṭ this sūtra forbids is the one 7.2.35 आर्धधातुकस्येड् वलादेः teaches, as for 7.2.10. Site: an ekāc dhātu that is
श्रिञ् or ends in uk (u, ṛ, ḷ and their long forms, 1.1.69) immediately before a kit affix — kit read from the
it-letter the it-prakaraṇa recorded (ktvā, kta, ktavatu: it:kit). ṅit is not kit (कितीति किम्). A liṭ affix is left to
the niyama 7.2.13 (Kāśikā: "क्रादय एव लिट्यनिटस्ततोऽन्ये सेट इति … लुलुविव"; SK 7.2.11: क्रादिनियमान्नित्यमिट्) — बभूविव.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_SRI = "SriY"                                  # श्रिञ् सेवायाम् (01.1044)
_UK = frozenset("uUfFxX")
_AC = frozenset("aAiIuUfFxXeEoO")              # अच् with its savarṇas (1.1.69)


def _kit(t) -> bool:
    return "it:kit" in t.tags or "kit" in t.tags or "k" in (t.meta.get("it_markers") or ())


def _site(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas:
            continue
        if sum(v.slp1 in _AC for v in t.varnas) != 1:
            continue
        if t.varnas[-1].slp1 not in _UK and (t.meta.get("upadesha_slp1") or "").strip() != _SRI:
            continue
        nxt = state.terms[i + 1]
        if not (nxt.kind == "pratyaya" or "pratyaya" in nxt.tags) or "agama" in nxt.tags:
            continue                           # किति प्रत्यये: an āgama's k (6.4.88 vuk) is no kit affix
        if (nxt.meta.get("source_lakara_upadesha") or "").strip() == "liT":
            continue                           # liṭ's iṭ is 7.2.13's niyama: क्रादय एव लिट्यनिटः (लुलुविव)
        if _kit(nxt):
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None and "7.2.35" not in state.blocked_sutras


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.11",
    sutra_type            = SutraType.PRATISHEDHA,
    text_slp1             = "SryukaH kiti",
    text_dev              = "श्र्युकः किति",
    samagra_slp1          = "aNgasya SryukaH kiti na iw ekAcaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य श्र्युकः किति न इट् एकाचः",
    padaccheda_dev        = "श्रि-उकः किति",
    why_dev               = "श्रिञ उगन्ताच्चैकाचः किति प्रत्यये इडागमो न।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
    blocks_sutra_ids      = ("7.2.35",),
)

register_sutra(SUTRA)
