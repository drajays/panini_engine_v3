"""
6.4.144  नस्तद्धिते  —  VIDHI (narrow)

**Pāṭha:** *nas taddhite* — *ṭi* portion of **-an** bases before *taddhita*.

Narrow v3 (``prakriya_18`` audit):
  • Fires only when ``state.meta['prakriya_18_6_4_144_attempt_arm']`` **and**
    **6.4.168** has **not** already registered ``6_4_168_yat_prakritibhava_sAman``
    (so the *sāmanyaḥ* recipe records **COND-FALSE** after **6.4.168** blocks
    *ṭi-lopa*).
  • ``act`` — narrow *lopa* of final ``n`` on ``sAman`` when unblocked (not used
    in the default ``sāmanyaḥ`` trace; kept for symmetry with **6.4.144** text).
Pāṭha: ashtadhyayi.com data.txt row i=64144 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_6.pada_4.sutra_6_4_164 import barred as _barred_164
from sutras.adhyaya_6.pada_4.sutra_6_4_167 import barred as _barred_167
from sutras.adhyaya_6.pada_4.sutra_6_4_169 import barred as _barred_169


def _eligible(state: State) -> bool:
    if "6_4_168_yat_prakritibhava_sAman" in state.samjna_registry:
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if (t0.meta.get("upadesha_slp1") or "").strip() != "sAman":
        return False
    if not t0.varnas or t0.varnas[-1].slp1 != "n":
        return False
    return True


def _in_site(state: State):
    """नस्तद्धिते for the in- and an-stems (pakṣin + ika → pākṣikaḥ, karman + ukañ → kārmukam): the ṭi (in / an) of a bha aṅga goes before a taddhita; 6.4.164 keeps it before a non-apatya aṇ."""
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if not ({"bha", "anga"} <= t.tags and "taddhita" in pr.tags and "pratyaya" in pr.tags) or t.meta.get("6_4_144_ti_done"):
            continue
        if t.meta.get("6_4_148_lopa_done") or len(t.varnas) < 3 or t.varnas[-1].slp1 != "n" or t.varnas[-2].slp1 not in ("i", "a"):      # the in of dANqAjin is what 6.4.148 left of a-stem, not an in-stem; ṭi = in / an
            continue
        if t.varnas[-2].slp1 == "a" and (_an_barred(state, t, pr) or "q" in (pr.meta.get("it_markers") or ()) or t.meta.get("6_4_143_dit_done")):
            continue                      # (a ḍit taddhita: 6.4.143 takes the same ṭi)
        if _barred_164(state, t, pr):
            continue                      # 6.4.164 inaṇyanapatye: prakṛtibhāva
        return t
    return None


def _an_barred(state: State, t, pr) -> bool:
    """The prakṛtibhāva exceptions to 6.4.144 for an-stems: 6.4.145 ahan keeps its ṭi except before ṭ / kha, 6.4.167 an before aṇ (apatya or not),
    6.4.168 an before a y-initial taddhita unless the sense is bhāva / karman (the frames 5.1.119 – 136), 6.4.169 ātman / adhvan before kha.
    SHORTCUT S21b: the bhāva / karman sense is read off the open frame (5.1.119 – 136), not asked as a vivakṣā value."""
    up = pr.meta.get("upadesha_slp1") or ""
    if "".join(v.slp1 for v in t.varnas) == "ahan":
        org = next((x.split(":", 1)[1] for x in pr.tags if x.startswith("origin_pratyaya:")), up)      # kha may already stand as īna (7.1.2)
        return not (org.startswith("w") or org == "Ka")
    if _barred_167(state, t, pr) or _barred_169(state, t, pr):      # the exceptions 6.4.167 / 6.4.169 each hold their own condition
        return True
    return up.startswith("y") and not any("5.1.119" <= e.get("id", "") <= "5.1.136" and e.get("artha") for e in state.adhikara_stack)      # 6.4.168 (string order is fine within 5.1.1xx)


an_barred = _an_barred      # read by 6.4.134 as well: the same prakṛtibhāva exceptions keep the an-aṅga whole before a taddhita


def cond(state: State) -> bool:
    return _eligible(state) or _in_site(state) is not None


def act(state: State) -> State:
    t = _in_site(state)
    if t is not None:
        del t.varnas[-2:]
        t.meta["6_4_144_ti_done"] = True
        return state
    if not _eligible(state):
        return state
    t0 = state.terms[0]
    if t0.varnas and t0.varnas[-1].slp1 == "n":
        t0.varnas.pop()
    state.meta["6_4_144_nas_taddhite_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.144",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'nastadDite',
    text_dev       = 'नस्तद्धिते',
    samagra_slp1   = "naH Basya aNgasya weH tadDite lopaH",
    samagra_dev    = "नः भस्य अङ्गस्य टेः तद्धिते लोपः",
    padaccheda_dev = "नः तद्धिते",
    why_dev        = "अन्-ान्ताद् यत्-परे टि-लोपः (प्रकृतिभावेन बाध्यते इति अङ्कनम्)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
