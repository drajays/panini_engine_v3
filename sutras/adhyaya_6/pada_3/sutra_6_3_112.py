"""
6.3.112  सहिवहोरोदवर्णस्य  —  VIDHI

Padaccheda: सहि-वहोः ओत् अ-वर्णस्य

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 63112 · सहिवहोरोदवर्णस्य
              padaccheda: सहि-वहोः ओत् अवर्णस्य
              anuvṛtti:   63111: ढ्रलोपे
  Source #2 — Kāśikā 6.3.112 udāharaṇa:
                सोढा, सोढुम्, सोढव्यम्, वोढा
  Cross-check — ashtadhyayi.com gold सोढा / वोढा (bench/ashtadhyayi_gold.py luṭ);
                tests/unit/test_dho_dhe_lopa_8_3_13.py

Apavāda of 6.3.111: on ढ्-lopa, the अ of सह् / वह् becomes ओ (not आ). The
dhātu is read from its varṇas — the root run ending right before the marked ढ्
is स / व + अ (सह् reached via 6.1.64 carries ``dhatu_adesha_v`` on its स्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

MARK = "Qralopa_para"
_ROOT_V = ("dhatu_v", "mula_dhatu_v", "dhatu_adesha_v")


def _is_root(v) -> bool:
    return any(m in v.tags for m in _ROOT_V) and "abhyasa_v" not in v.tags


def _site(state: State):
    cells = [(t, i) for t in state.terms for i in range(len(t.varnas))]
    for k in range(2, len(cells)):
        u, j = cells[k]
        nxt = u.varnas[j]
        if MARK not in nxt.tags or "6_3_111_done" in nxt.tags:
            continue
        (ta, ia), (tb, ib) = cells[k - 2], cells[k - 1]
        c, a = ta.varnas[ia], tb.varnas[ib]
        if a.slp1 == "a" and c.slp1 in ("s", "v") and _is_root(c) and _is_root(a):
            before = cells[k - 3] if k >= 3 else None
            if before is None or not _is_root(before[0].varnas[before[1]]):
                return tb, ib, nxt
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        t, i, nxt = hit
        t.varnas[i] = mk("o", *t.varnas[i].tags)
        nxt.tags.add("6_3_111_done")
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.3.112",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sahivahorodavarRasya",
    text_dev       = "सहिवहोरोदवर्णस्य",
    samagra_slp1   = "uttarapade Qralope sahi-vahoH avarRasya ot",
    samagra_dev    = "उत्तरपदे ढ्रलोपे सहि-वहोः अवर्णस्य ओत्",
    padaccheda_dev = "सहि-वहोः ओत् अ-वर्णस्य",
    why_dev        = "ढ्-लोपे सह्-वह्-धात्वोः अवर्णस्य ओकारः — सढ्+ढा → सोढा।",
    anuvritti_from = ("6.3.111",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
