"""
6.4.98  गमहनजनखनघसां लोपः क्ङित्यनङि  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=64098
- Kāśikā: «गमहनजनखनघसां लोपः क्ङित्यनङि» (घस् → घ्स् in *liṭ* reduplication)
- Cross-validation: tests/unit/test_tinanta_ad_lit_kartari.py (जक्षतुः …)

*Liṭ* + *kṅit* (1.2.5 *kit* on the tiṅ ādeśa): non-*abhyāsa* *ghas* (**G-a-s**) loses
penultimate *a* → **G-s** (घ्स्).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GAMAHANA = frozenset({"gam", "han", "Gan", "jan", "Kan", "Gas"})      # Gan: han after 7.3.55 (abhyāsāc ca)
_AC = frozenset("aAiIuUfFxXeEoO")


def _find_general(state: State) -> int | None:
    """गमहनजनखनघसां लोपः क्ङित्यनङि: the upadhā a of these five dhātus drops before
    a kit/ṅit vowel-initial affix other than aṅ — जग्मतुः, जघ्नुः, जज्ञे."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("6_4_98_gas_upadha_done"):
            continue
        flat = "".join(v.slp1 for v in t.varnas if "aT_agama_v" not in v.tags)    # the aṭ stands in the same pada
        if flat not in _GAMAHANA:
            return None
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or nxt.varnas[0].slp1 not in _AC:
            return None
        if (nxt.meta.get("upadesha_slp1") or "").strip() in ("aN", "aG"):
            return None
        # क्ङिति: the *affix that follows the aṅga* is kit/ṅit. An āgama (iṭ) belongs to the affix it stands
        # before, so the head is the first non-āgama term — gam+iṭ+sya+tas: sya is not ṅit, the tiṅ after
        # it does not count (गमिष्यति, not *ग्मिष्यति).
        head = next((u for u in state.terms[i + 1:] if u.varnas and "agama" not in u.tags), None)
        if head is None or "kngiti" not in head.tags:
            return None
        return i
    return None


def cond(state: State) -> bool:
    return _find_general(state) is not None


def act(state: State) -> State:
    i = _find_general(state)
    if i is None:
        return state
    t = state.terms[i]
    j = next((k for k, v in enumerate(t.varnas) if "aT_agama_v" not in v.tags), 0)
    del t.varnas[j + 1]                # the upadhā a (after any aṭ)
    t.meta["6_4_98_gas_upadha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gamahanajanaKanaGasAM lopaH kNityanaNi",
    text_dev              = "गमहनजनखनघसां लोपः क्ङित्यनङि",
    samagra_slp1          = "gama-hana-jana-Kana-GasAmupaDAyAH kNiti aci lopaH anaNi",
    samagra_dev           = "गम-हन-जन-खन-घसामुपधायाः क्ङिति अचि लोपः अनङि",
    padaccheda_dev        = "गम-हन-जन-खन-घसाम् लोपः क्ङिति अन्-अङि",
    why_dev               = "(सूत्रम् 6.4.98) गमहनजनखनघसां लोपः क्ङित्यनङि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
