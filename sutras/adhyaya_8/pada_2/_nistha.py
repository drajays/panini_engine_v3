"""Shared reader for 8.2.42-8.2.57 (the niṣṭhā-ta of a dhātu): where the ta stands and which dhātu it follows.

Two tape shapes carry the same facts:
  * the loose tape: a dhātu Term then the niṣṭhā Term (kta / ktavatu) whose first varṇa is t (the recipes: bhinna, svinna);
  * the merged pada of a kṛdanta stem (pipelines/krdanta.derive_krdanta): the t of the niṣṭhā carries the varṇa tag
    ``nistha_t_v`` and the dhātu's letters carry ``dhatu_v`` — facts of the tape's own history, stamped where the loop
    built the stem, the same way ``pratyaya_start_v`` is stamped by the pada merge. The dhātu's upadeśa is the
    ``origin_dhatu:`` tag (engine/origin.py).
Nothing here reads the Kāśikā; the dhātu lists are the Dhātupāṭha's own rows (lvādi = 9.16-9.40) or named by upadeśa.
"""
from __future__ import annotations

from functools import lru_cache

from phonology import HAL, mk

NISTHA_T = "nistha_t_v"
BAR = "nistha_na_barred_v"            # 8.2.57 has settled this ta: no na, no ma, no ka, no va for it
DONE = "nistha_done_v"
_NISTHA = frozenset({"kta", "ktavatu", "ktavatu~"})
_ORIGIN = "origin_dhatu:"


def base(up: str) -> str:
    """The upadeśa without its accent and anubandha marks of the Dhātupāṭha's spelling (lUY stays, Suza~ → Suza)."""
    return (up or "").replace("~", "").replace("\\", "").replace("^", "").strip()


class Site:
    __slots__ = ("pre", "t", "up", "_put")

    def __init__(self, pre, t, up, put):
        self.pre, self.t, self.up, self._put = pre, t, up, put

    @property
    def root(self) -> str:
        """The dhātu's upadeśa with it-marks removed from the spelling; the letters before t are in ``pre``."""
        return base(self.up)

    def put(self, slp1: str) -> None:
        """Replace the niṣṭhā's t by ``slp1`` (a sthānin → ādeśa swap on the varṇa itself)."""
        self._put(slp1)
        self.t.tags.add(DONE)


def swap(v, slp1: str) -> None:
    n = mk(slp1)
    v.slp1, v.dev = n.slp1, n.dev


def sites(state):
    """Every niṣṭhā-ta not yet settled, inside the tripāḍī zone."""
    if not state.tripadi_zone:
        return []
    out = []
    for a, b in zip(state.terms, state.terms[1:]):                     # the loose tape
        if "dhatu" not in a.tags or "abhyasa" in a.tags or not a.varnas or not b.varnas:
            continue
        if (b.meta.get("upadesha_slp1") or "").strip() not in _NISTHA or b.varnas[0].slp1 != "t" or DONE in b.varnas[0].tags:
            continue
        v = b.varnas[0]
        out.append(Site(list(a.varnas), v, a.meta.get("upadesha_slp1") or "", lambda s, v=v: swap(v, s)))
    for term in state.terms:                                            # the merged pada
        for i, v in enumerate(term.varnas):
            if NISTHA_T not in v.tags or DONE in v.tags or v.slp1 != "t":
                continue
            pre = list(term.varnas[:i])                                  # the stem is dhātu + ta: the stamp is only made when no iṭ stands between
            if not pre:
                continue
            ups = {t[len(_ORIGIN):] for t in term.tags if t.startswith(_ORIGIN)}
            out.append(Site(pre, v, next(iter(ups)) if len(ups) == 1 else "", lambda s, v=v: swap(v, s)))
    return [s for s in out if BAR not in s.t.tags]


# 8.2.56 names nud, vid, und, trā, ghrā, hrī: for them na is a vibhāṣā, so the nitya 8.2.42 / 8.2.43 leave the ta alone
# (nuttaḥ beside nunnaḥ, trātaḥ beside trāṇaḥ). Upadeśas as the Dhātupāṭha spells them (anubandha marks removed).
VIBHASHA_ROOTS = frozenset({"Nuda", "nuda", "undI", "vida", "trE", "trEN", "GrA", "hrI"})


def free(state):
    """Sites for the nitya rules 8.2.42-8.2.53: not a dhātu of 8.2.56's vibhāṣā list."""
    return [s for s in sites(state) if s.root not in VIBHASHA_ROOTS]


@lru_cache(maxsize=None)
def lvadi() -> frozenset:
    """8.2.44: the dhātus from lūñ chedane (9.16) to vrī varaṇe (9.40), as their upadeśas (Dhātupāṭha, kryādi)."""
    from pipelines.dhatupatha import iter_dhatu_entries
    return frozenset(base(e["upadesha_slp1"]) for e in iter_dhatu_entries()
                     if "09.0016" <= (e.get("dhatupatha_id") or "") <= "09.0040")


def is_hal(v) -> bool:
    return v.slp1 in HAL
