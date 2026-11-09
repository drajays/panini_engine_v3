"""
8.4.39  क्षुभ्नाऽऽदिषु च  —  PRATISHEDHA

kṣubhnādiṣu ca: no ṇatva in kṣubhnā, tṛpnu … (क्षुभ्नाति, तृप्नोति). The kṣubhnādi roots are named by upadeśa (an ākṛtigaṇa in the Kāśikā; S146).
Pāṭha: ashtadhyayi.com data.txt row i=84039 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_8.pada_4.sutra_8_4_2 import _BLOCKERS

TAG = "natva_done"          # the tag 8.4.1 / 8.4.2 already skip: ṇatva is settled for this n (here: barred)
_RASHA = frozenset("rfFz")


def _ns(state: State):
    """Every untagged n that 8.4.1 / 8.4.2 would turn to ṇ: after r / ṛ / ṣ with no blocker between, before a vowel or y v m n, or pada-final."""
    flat = [v for t in state.terms for v in t.varnas]
    out = []
    for k, v in enumerate(flat):
        if v.slp1 != "n" or TAG in v.tags:
            continue
        j = k - 1
        while j >= 0 and flat[j].slp1 not in _RASHA and flat[j].slp1 not in _BLOCKERS:
            j -= 1
        if j >= 0 and flat[j].slp1 in _RASHA:
            out.append((k, v, k == len(flat) - 1))
    return out


# SHORTCUT S146: the ākṛtigaṇa is the two roots the engine can derive (kṣubh, tṛp), named by upadeśa.
_KSUBHNADI = frozenset({"kzuBa~", "tfpa~", "tfpA~", "tfpa"})


def _live(state: State) -> bool:
    return any((t.meta.get("dhatu_upadesha") or "").strip() in _KSUBHNADI for t in state.terms)


def cond(state: State) -> bool:
    return state.tripadi_zone and _live(state) and bool(_ns(state))


def act(state: State) -> State:
    for _k, v, _fin in _ns(state):
        v.tags.add(TAG)
    return state


SUTRA = SutraRecord(
    sutra_id         = "8.4.39",
    sutra_type       = SutraType.PRATISHEDHA,
    text_slp1        = 'kzuBnAxdizu ca',
    text_dev         = 'क्षुभ्नाऽऽदिषु च',
    samagra_slp1     = 'razAByAm naH RaH na kzuBnAxdizu ca',
    samagra_dev      = 'रषाभ्याम् नः णः न क्षुभ्नादिषु च',
    padaccheda_dev   = 'क्षुभ्ना-आदिषु च',
    why_dev          = 'क्षुभ्नादिषु नस्य णत्वं न।',
    anuvritti_from   = ("8.4.1",),
    blocks_sutra_ids = (),   # per-position bar by tag; a wholesale block of the target would stop its other sites
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
