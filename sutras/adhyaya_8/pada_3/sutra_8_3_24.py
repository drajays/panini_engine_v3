"""
8.3.24  नश्चापदान्तस्य झलि  —  VIDHI

Anuvṛtti: मः (8.3.23 मोऽनुस्वारः) — the च adds न् to म्.

Sources consulted:
- ashtadhyayi.com data.txt row i=83024
- Kāśikā: "पयांसि। यशांसि। सर्पींषि। धनूंषि। आक्रंस्यते।"
- Cross-validation: Vidyut surface ✓ for गन्ता (गम् luṭ); regression test:
  tests/unit/test_gam_lrt_7_2_58.py

Within one pada, a न् or म् that is not pada-final and is followed by a jhal
consonant becomes anusvāra: यशन्+सि → यशांसि, गम्+ता → गंता (8.4.58 then
गन्ता), क्रम्+स्यते → क्रंस्यते.

The merged tripādī tape does not mark internal pada boundaries, so म् is
taken only when it belongs to the dhātu (``dhatu_v``) — there it can never be
pada-final. A pūrvapada-final म् (परम्+तपः, मुम् by 6.3.67) is padānta and
belongs to 8.3.23 मोऽनुस्वारः.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import JHAL


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_3_24_nasch_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i + 1].slp1 not in JHAL:
            continue
        if vs[i].slp1 == "n" or (vs[i].slp1 == "m" and "dhatu_v" in vs[i].tags):
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    t.varnas[i] = mk("M")
    t.meta["8_3_24_nasch_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.24",
    sutra_type=SutraType.VIDHI,
    text_slp1='naScApadAntasya Jali',
    text_dev='नश्चापदान्तस्य झलि',
    padaccheda_dev="नः च / अपदान्तस्य / झलि",
    why_dev="अपदान्तस्य नकारस्य मकारस्य च झलि परे अनुस्वारः (यशांसि, आक्रंस्यते)।",
    anuvritti_from=("8.2.1", "8.3.23"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

