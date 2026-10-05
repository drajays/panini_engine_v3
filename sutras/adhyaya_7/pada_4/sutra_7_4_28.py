"""
7.4.28  रिङ् शयग्लिङ्क्षु  —  VIDHI

Padaccheda: रिङ् श-यक्-लिङ्‍क्षु

रिङ् शयग्लिङ्क्षु (7.4.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

# श-यक्-लिङ्क्षु: before śa (tudādi vikaraṇa), yak (3.1.67) and the y of liṅ
# (yāsuṭ / yak-less liṅ āgama). Upadeśa identity of the following term.
_NIMITTA = frozenset({"Sa", "yak", "ya", "yAsuw", "yAs"})


def _find(state: State) -> int | None:
    """Index of an aṅga ending in short ṛ (ऋतः, 7.4.27) right before a nimitta."""
    for i, t in enumerate(state.terms[:-1]):
        if "anga" not in t.tags and "dhatu" not in t.tags:
            continue
        if t.meta.get("7_4_28_riN_done") or not t.varnas or t.varnas[-1].slp1 != "f":
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None:
            continue
        if ((nxt.meta.get("upadesha_slp1") or "").strip() in _NIMITTA or "yak" in nxt.tags
                or "yasut_agama" in nxt.tags):
            if "yasut_agama" in nxt.tags or (nxt.meta.get("upadesha_slp1") or "").strip() in {"yAsuw", "yAs"}:
                tin = next((u for u in state.terms[i + 1:] if "tin_adesha_3_4_78" in u.tags), None)
                if tin is not None and "ashir_liG" not in tin.tags and "ardhadhatuka" not in tin.tags:
                    continue            # riṅ before the liṅ of *āśīr* only (kriyAt); vidhi-liṅ keeps ṛ (jaGfyAt, kuryAt)
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    # riṅ replaces the final ṛ only (1.1.53 ङिच्च): कृ → क्रि (क्रियते)
    t.varnas = list(t.varnas[:-1]) + [mk("r"), mk("i")]
    t.meta["7_4_28_riN_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.28",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "riN SayagliNkzu",
    text_dev              = "रिङ् शयग्लिङ्क्षु",
    padaccheda_dev        = "रिङ् श-यक्-लिङ्‍क्षु",
    why_dev               = "ऋदन्तस्य अङ्गस्य रिङ् आदेशः श-यक्-लिङ्क्षु परेषु (कृ + यक् → क्रियते)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
