"""
3.1.28  गुपूधूपविच्छिपणिपनिभ्य आयः  —  VIDHI

Kāśikā: "… इत्येतेभ्यो धातुभ्य आयप्रत्ययो भवति। गोपायति। धूपायति। विच्छायति। पणायति। पनायति।"
(sārvadhātuka: nitya; in the ārdhadhātuka it is optional, 3.1.31 — gopitā / gopāyitā.)
Aya goes after the dhātu as a sanādi pratyaya (ārdhadhātuka, no it); the recipe then fuses dhātu + Aya into one dhātu (3.1.32,
`pipelines.tinanta._aya_dhatu`), exactly as for ṇic. The sārvadhātuka / ārdhadhātuka question is read from the lakāra
vivakṣā tag the recipe's tape init puts on the dhātu (`lat_derivation` …), ledger S169.

Pāṭha: ashtadhyayi.com data.txt row i=31028 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

LISTED = frozenset({"gupU~", "DUpa~", "vicCa~", "paRa~", "pana~"})    # the sūtra's own list (dhātupāṭha upadeśa)
_SARVA = frozenset({"lat_derivation", "lot_derivation", "lag_derivation", "lig_derivation"})
_ARDHA = frozenset({"lit_derivation", "lut_derivation", "lrt_derivation", "lug_derivation", "lrg_derivation",
                    "lrn_derivation", "asirlig_derivation"})


def aya_site(state: State, lakara_tags: frozenset) -> int | None:
    """Index of a listed dhātu not yet given Aya, whose lakāra vivakṣā tag is in ``lakara_tags``."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in LISTED or t.meta.get("3_1_28_aya_done"):
            return None
        return i if t.tags & lakara_tags and i == len(state.terms) - 1 else None
    return None


def insert_aya(state: State, i: int) -> State:
    state.terms.insert(i + 1, Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("Aya")),
                                   tags={"pratyaya", "upadesha", "sanadi", "ardhadhatuka"},
                                   meta={"upadesha_slp1": "Aya"}))
    state.terms[i].meta["3_1_28_aya_done"] = True
    return state


def cond(state: State) -> bool:
    return aya_site(state, _SARVA) is not None


def act(state: State) -> State:
    i = aya_site(state, _SARVA)
    return state if i is None else insert_aya(state, i)


SUTRA = SutraRecord(
    sutra_id              = "3.1.28",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "gupUDUpavicCipaRipaniBya AyaH",
    text_dev              = "गुपूधूपविच्छिपणिपनिभ्य आयः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH gupU-DUpa-vicCi-paRi-paniByaH AyaH",
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः गुपू-धूप-विच्छि-पणि-पनिभ्यः आयः",
    padaccheda_dev        = "गुपू-धूप-विच्छि-पणि-पनिभ्यः आयः",
    why_dev               = "गुपू-धूप-विच्छ-पण-पन-धातोः सार्वधातुके नित्यम् आयः (गोपायति)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
