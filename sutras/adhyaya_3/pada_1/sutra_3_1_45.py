"""
3.1.45  शल इगुपधादनिटः क्सः  —  VIDHI

Padaccheda: शलः इक्-उपधात् अन्-इटः क्सः

Of an अनिट् धातु ending in शल् (श्,ष्,स्,र्,ह्,ल् — māheśvara-sūtra 13-14)
whose उपधा is इक् (here: short इ/उ — see scope note below), चिल् (3.1.43)
is replaced by क्स — not सिच् (3.1.44, the general rule this blocks) — and
the root's own final शल् letter is dropped (it would be redundant: क्स
already carries what 8.3.59 turns into the same ष्/क्ष् shape).

Engine: क्स is written [क्,स्,अ] — no इत् letters here (unlike सिच्'s इ,
which 1.3.9 strips, क्स's अ survives as the affix's substantive vowel;
see शिष्→अशिक्षत्, not अशिक्ष्त् — the अ is not the root's, it belongs to
this प्रत्यय). Root's शल् is deleted outright rather than left to combine:
शिष्+क्स्अ+त् → शि+क्+स्+अ+त् → (8.3.59 आदेशप्रत्ययोः, स् after क्) → शिक्षत्।
Also marks state so 7.3.84 (उपधा गुण) and 8.4.41 (ष्टुत्व on this क्स-born
ष्, which would otherwise wrongly retroflex the following तिङ् त्/द्) both
decline — neither rule fires against this recipe in the ashtadhyayi.com
paradigm data.

Scope note: इगुपध traditionally covers all of इ/ई/उ/ऊ/ऋ/ॠ; restricted here
to short इ/उ, the confirmed single-shape cases (दिश्→अदिक्षत्, विश्→अविक्षत्,
शिष्→अशिक्षत्, दुह्→अधुक्षत्, दिह्→अधिक्षत्, लिह्→अलिक्षत्, क्रुश्→अक्रुक्षत्,
रुह्→अरुक्षत्, मिह्→अमिक्षत्, त्विष्→अत्विक्षत्, द्विष्→अद्विक्षत् — all
पिन्नेद् against ashtadhyayi.com, all 9 cells each). ऋ-उपधा roots (स्पृश्,
मृश्, कृष्...) show this same क्स shape only as one of several ashtadhyayi.
com-listed वैकल्पिक alternates alongside वृद्धि-sic forms; the engine has
no multi-output-per-cell mechanism yet (see docs/FINAL_PLAN_2026-09.md item
6), so widening to those roots is left for when vikalpa output lands.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31045 · शल इगुपधादनिटः क्सः
              padaccheda: शलः इक्-उपधात् अनिटः क्सः
              anuvṛtti:   31043: च्लि लुङि | 31044: (अपवादः)
  Cross-check — surface pinned by: dhātu 06.0003/06.0160/01.0783/02.0004/
                02.0005/02.0006/01.0992/01.0995/01.1147/01.1156/02.0003
                vs ashtadhyayi.com, all 9 cells (अदिक्षत्/अविक्षत्/अशिक्षत्/
                अधुक्षत्/अधिक्षत्/अलिक्षत्/अक्रुक्षत्/अरुक्षत्/अमिक्षत्/
                अत्विक्षत्/अद्विक्षत् paradigms)
  Reference record: sutra_ref_out/3_1_45.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_SHAL = frozenset({"S", "z", "s", "r", "h", "l"})
_SHORT_IK = frozenset({"i", "u"})
_DONE_KEY = "3_1_45_ksa_done"


def _site(state: State):
    """(dhātu_term, sic_term) when the aṅga qualifies for क्स (see module docstring)."""
    sic_i = None
    for i, t in enumerate(state.terms):
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "sic":
            sic_i = i
            break
    if sic_i is None or sic_i == 0:
        return None
    dh = state.terms[sic_i - 1]
    if "dhatu" not in dh.tags or dh.meta.get(_DONE_KEY):
        return None
    if not dh.meta.get("anit_dhatu"):
        return None
    vs = dh.varnas
    if len(vs) < 2 or vs[-1].slp1 not in _SHAL or vs[-2].slp1 not in _SHORT_IK:
        return None
    return dh, state.terms[sic_i]


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is None:
        return state
    dh, sic = hit
    if state.meta.get("cli_luG_recipe"):       # the old recipe stands ksa as sounds and drops the root's śal
        dh.varnas.pop()                      # drop the root's own final शल्
    dh.meta[_DONE_KEY] = True
    sic.varnas = parse_slp1_upadesha_sequence("ksa")   # सिच् (स्+च्) → क्स (क्+स्+अ)
    sic.meta["upadesha_slp1"] = "ksa"
    sic.tags.add("vikarana")   # so 6.1.97 sees क्स-अ + तिङ्-अ the way it sees शप्-अ + तिङ्-अ
    state.meta["_3_1_45_ksa_recipe"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Sala igupaDAdaniwaH ksaH",
    text_dev              = "शल इगुपधादनिटः क्सः",
    padaccheda_dev        = "शलः इक्-उपधात् अन्-इटः क्सः",
    why_dev               = "अनिट्-हल्-अन्त-शल्-धातोः इगुपधात् चिलः क्स-आदेशः (सिचोऽपवादः); "
                             "धातोः अन्त्य-शल् लुप्तः; क्स-प्रकरणे गुण/ष्टुत्वे न (शिष् → अशिक्षत्)।",
    anuvritti_from        = ('3.1.43',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
