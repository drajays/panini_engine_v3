"""
6.1.3  न न्द्राः संयोगादयः  —  VIDHI

Padaccheda: न न्-द्-राः संयोग-आदयः

न न्द्राः संयोगादयः (6.1.3)
Pāṭha: ashtadhyayi.com data.txt row i=61003 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    """न न्द्राः संयोगादयः — of an ajādi dhātu, the second ekāc is the one doubled (6.1.2); when that ekāc begins with a saṃyoga whose first
    letter is n, d or r, that letter is not doubled: ūrṇu (ū + rṇu) doubles ṇu, not rṇu → ūrṇunāva."""
    for t in state.terms:
        if "dhatu" not in t.tags or t.meta.get("6_1_3_done") or not t.varnas:
            continue
        if any("abhyasa" in u.tags for u in state.terms):
            continue
        vs = [v.slp1 for v in t.varnas]
        if vs[0] not in _AC:
            continue                                   # ajādeḥ (6.1.2): only an ajādi root has a "second" ekāc
        i2 = next((k for k in range(1, len(vs)) if vs[k] in _AC), None)
        if i2 is None or i2 < 3:
            continue
        cluster = vs[1:i2]                             # the consonants before the second vowel
        if len(cluster) >= 2 and cluster[0] in "ndr":
            return t
    return None


# SHORTCUT S127: see docs/SHORTCUT_LEDGER.md
def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    t.meta["6_1_3_done"] = True
    t.meta["dvitva_skip_6_1_3"] = 1                    # the n / d / r before the rest of the saṃyoga is left out of the doubled part
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.3",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na ndrAH saMyogAdayaH",
    text_dev              = "न न्द्राः संयोगादयः",
    samagra_slp1          = "dvitIyasya ekAcaH saMyogAdayaH ndrAH na dve",
    samagra_dev           = "द्वितीयस्य एकाचः संयोगादयः न्द्राः न द्वे",
    padaccheda_dev        = "न न्-द्-राः संयोग-आदयः",
    why_dev               = "न न्द्राः संयोगादयः — अजादेः द्वितीयस्य एकाचः संयोगादयः न्-द्-राः द्विः न भवन्ति (ऊर्णुनाव)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
