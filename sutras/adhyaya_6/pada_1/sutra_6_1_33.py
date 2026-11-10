"""
6.1.33  अभ्यस्तस्य च  —  VIDHI

Padaccheda: अभ्यस्तस्य च

अभ्यस्तस्य च (6.1.33)
Pāṭha: ashtadhyayi.com data.txt row i=61033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_1.pada_1.sutra_1_1_45 import META_TARGETS

# Kāśikā 6.1.33: "ह्व इति वर्तते ... अभ्यस्तकारणस्य ह्वयतेः प्रागेव द्विर्वचनात् संप्रसारणं भवति। जुहाव। जोहूयते। जुहूषति।"
# The root ह्वे that is *about to be doubled* (dvitva nimitta on the tape: liṭ, san, yaṅ) takes samprasāraṇa first;
# 1.1.45 / 6.1.108 then give हु, so ātva (6.1.45) has no ec left to act on (paribhāṣā संप्रसारणं तदाश्रयं च कार्यं बलवत्:
# the resolver withholds 6.1.45 while this rule is a candidate, ORDER_BEFORE in engine/resolver.py).
_DVITVA_NIMITTA_SANADI = frozenset({"san", "yaN"})


def _dvitva_follows(state: State, i: int) -> bool:
    for t in state.terms[i + 1:]:
        if "pratyaya" not in t.tags:
            continue
        if (t.meta.get("source_lakara_upadesha") or "").strip() == "liT":
            return True
        if "sanadi" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() in _DVITVA_NIMITTA_SANADI:
            return True
    return False


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("samprasarana_done"):
            continue
        if "".join(v.slp1 for v in t.varnas) != "hve" or "mula_dhatu_v" not in t.varnas[-1].tags:
            continue
        if not any("abhyasa" in u.tags for u in state.terms) and _dvitva_follows(state, i):
            return i, 1                      # the v of ह्वे
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    site = _site(state)
    if site is not None:
        ti, vi = site
        state.meta[META_TARGETS] = [(ti, vi)]        # 1.1.45 reads it: v -> u; 6.1.108 then absorbs the e
        state.terms[ti].meta["samprasarana_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aByastasya ca",
    text_dev              = "अभ्यस्तस्य च",
    samagra_slp1          = "aByastasya ca hvaH samprasAraRam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अभ्यस्तस्य च ह्वः सम्प्रसारणम्",
    padaccheda_dev        = "अभ्यस्तस्य च",
    why_dev               = "(सूत्रम् 6.1.33) अभ्यस्तस्य च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
