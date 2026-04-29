"""
6.4.10  सान्तमहतः संयोगस्य  —  VIDHI (narrow demo)

Demo slice (यशांसि.md):
  After 7.1.72 inserts nuṃ on a neuter `…as` stem (yasas), a consonant cluster
  `n + s` arises. With sarvanāmasthāna (`i`) following, lengthen the vowel
  immediately before that cluster: a → A.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    if len(state.terms) < 2:
        return None
    anga = state.terms[-2]
    pr = state.terms[-1]
    if "anga" not in anga.tags:
        return None
    if "sup" not in pr.tags or "sarvanamasthana" not in pr.tags:
        return None
    if anga.meta.get("6_4_10_santa_mahat_dirgha_done"):
        return None
    vs = anga.varnas
    # Expect ... a n s
    if len(vs) < 3:
        return None
    if vs[-1].slp1 != "s" or vs[-2].slp1 != "n":
        return None
    if vs[-3].slp1 != "a":
        return None
    return len(vs) - 3


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    anga = state.terms[-2]
    anga.varnas[i] = mk("A")
    anga.meta["6_4_10_santa_mahat_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.10",
    sutra_type=SutraType.VIDHI,
    text_slp1="sAntamahataH saMyogasya",
    text_dev="सान्तमहतः संयोगस्य",
    padaccheda_dev="सान्त-महतः / संयोगस्य",
    why_dev="सकारान्त-संयोगे (न्+स्) सर्वनामस्थाने परे उपधा-दीर्घः (यशांसि)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

