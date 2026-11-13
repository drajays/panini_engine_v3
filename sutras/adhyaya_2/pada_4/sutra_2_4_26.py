"""
2.4.26  परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः  —  VIDHI

Padaccheda: पर-वत् लिङ्गम् द्वन्द्व-तत्पुरुषयोः

dvandva and tatpurusha take gender of the latter member.
Pāṭha: ashtadhyayi.com data.txt row i=24026 (Art. 14).
Kāśikā: उत्तरपदलिङ्गं द्वन्द्वतत्पुरुषयोर्विधीयते।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_LINGA = ("pulliṅga", "strīliṅga", "napuṃsaka")


def _site(state: State):
    """The uttarapada of a tatpuruṣa / dvandva that does not yet have its compound liṅga: it is that of the last member (para)."""
    if state.meta.get("samasa_kind", "").split(" ")[0] not in ("tatpurusha", "dvandva"):
        return None
    last = next((t for t in reversed(state.terms) if "samasa_uttarapada" in t.tags), None)
    if last is None or any(x.startswith("samasa_linga:") for x in last.tags):
        return None
    return last if any(x in last.tags for x in _LINGA) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    t.tags.add("samasa_linga:" + next(x for x in _LINGA if x in t.tags))
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.26",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = "paravalliNgaM dvandvatatpuruzayoH",
    text_dev              = "परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः",
    samagra_slp1          = "paravat liNgam dvandva-tatpuruzayoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "परवत् लिङ्गम् द्वन्द्व-तत्पुरुषयोः",
    padaccheda_dev        = "पर-वत् लिङ्गम् द्वन्द्व-तत्पुरुषयोः",
    why_dev               = "द्वन्द्व-तत्पुरुषयोः पर-वत् लिङ्गम् (२.४.२६)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
