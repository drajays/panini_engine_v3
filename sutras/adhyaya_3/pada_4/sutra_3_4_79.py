"""
3.4.79  टित आत्मनेपदानां टेरे  —  VIDHI

For every ātmanepada tiṅ ādeśa (tagged tin_adesha_3_4_78), replace the
ṭi (last vowel + whatever follows it) with the single vowel `e`.

  ta    → te      (3sg: a → e)
  Atam  → Ate     (3du: am → e; called āte in Devanāgarī)
  Ja    → Je      (3pl jha: a → e; 7.1.3 then gives ante)
  ATAm  → ATe     (2du āthāṃ: Am → e)
  Dvam  → Dve     (2pl dhvam: am → e)
  i     → e       (1sg: after iṭ IT-lopa leaves i; i → e)
  vahi  → vahe    (1du: i → e)
  mahi  → mahe    (1pl: after mahiṅ IT-lopa; i → e)

  TAs (thās, 2sg): handled by 3.4.80, skipped here.

The ṭi is defined by 1.1.64 ācas ca ṭi: the last AC (vowel) + rest.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_AC = frozenset("aAiIuUeEoOfFxX")
_THAS = frozenset({"TAs"})


def _find(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if t.meta.get("3_4_79_ter_done"):
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _THAS:
            continue
        # Find the last vowel (start of ṭi by 1.1.64)
        last_vi = None
        for vi, v in enumerate(t.varnas):
            if v.slp1 in _AC:
                last_vi = vi
        if last_vi is None:
            continue
        # Already just ‘e’ — no-op
        if len(t.varnas) == last_vi + 1 and t.varnas[last_vi].slp1 == "e":
            continue
        return (ti, last_vi)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    t.meta["upadesha_slp1_original"] = t.meta.get("upadesha_slp1_original", t.meta.get("upadesha_slp1"))
    # Replace from vi (last vowel) onward with single ‘e’
    t.varnas = list(t.varnas[:vi]) + [mk("e")]
    # Update upadesha to reflect new form
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["3_4_79_ter_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="Tita AtmanepAdAnAM were",
    text_dev="टित आत्मनेपदानां टेरे",
    padaccheda_dev="टित् / आत्मनेपदानाम् / टेरे",
    why_dev=(
        "आत्मनेपद-प्रत्ययस्य टि-भागे (अन्तिम-स्वर + अनन्तर) ‘ए’-आदेशः — "
        "ते, आते, जे, आथे, ध्वे, ए, वहे, महे।"
    ),
    anuvritti_from=("3.4.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

