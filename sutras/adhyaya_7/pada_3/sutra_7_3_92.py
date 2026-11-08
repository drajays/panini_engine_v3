"""
7.3.92  तृणह इम्  —  VIDHI

Padaccheda: तृणहः इम्

तृणह इम् (7.3.92)
Pāṭha: ashtadhyayi.com data.txt row i=73092 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from phonology.varna import parse_slp1_upadesha_sequence
from engine.state import State

_AC = frozenset("aAiIuUfFxXeEoO")

_PIT_TIN_UPADESHA: frozenset = frozenset({"tip", "sip", "mip"})
_DONE = "7_3_92_im_agama_done"


def _target(state: State):
    """तृणह इम् — the tṛṇah of tṛha~ (tṛṇa-infixed) takes the mit īm before a hal-initial pit sārvadhātuka: तृणेढि, तृणेह्मि."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or t.meta.get(_DONE) or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").replace("~", "") != "tfha" or not t.varnas or t.varnas[-1].slp1 != "h":
            continue
        tin = state.terms[i + 1]
        if "pratyaya" in tin.tags and tin.varnas and tin.varnas[0].slp1 not in _AC \
                and (tin.meta.get("upadesha_slp1") or "").strip() in _PIT_TIN_UPADESHA:
            return t
    return None


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    t = _target(state)
    if t is not None:
        t.varnas.insert(len(t.varnas) - 1, parse_slp1_upadesha_sequence("i")[0])      # mit: after the root's last vowel (6.1.87 then a + i → e)
        t.meta[_DONE] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tfRaha im",
    text_dev              = "तृणह इम्",
    samagra_slp1          = "aNgasya tfRahaH im piti sArvaDAtuke hali",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य तृणहः इम् पिति सार्वधातुके हलि",
    padaccheda_dev        = "तृणहः इम्",
    why_dev               = "(सूत्रम् 7.3.92) तृणह इम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
