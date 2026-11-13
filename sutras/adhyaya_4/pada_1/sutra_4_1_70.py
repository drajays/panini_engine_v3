"""
4.1.70  संहितशफलक्षणवामादेश्च  —  VIDHI

Padaccheda: संहित-शफ-लक्षण-वाम-आदेः च

संहितशफलक्षणवामादेश्च (4.1.70)
Pāṭha: ashtadhyayi.com data.txt row i=41070 (Art. 14).
Kāśikā: संहित शफ लक्षण वाम इत्येवमादेः प्रातिपदिकादूरूत्तरपदात् स्त्रियामूङ् प्रत्ययो भवति।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

def _wanted(t) -> bool:
    """a compound whose last member is ūru and whose first member is saṃhita, śapha, lakṣaṇa, vāma …: ūṅ (the comparison is not meant)."""
    f = "".join(v.slp1 for v in t.varnas)
    return f.endswith("Uru") and f[:-3] in ("saMhita", "Sapa", "lakzaRa", "vAma", "sahita", "saha")

def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "UN") if _site(state) is not None else state


SUTRA = SutraRecord(
    sutra_id              = "4.1.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMhitaSaPalakzaRavAmAdeSca",
    text_dev              = "संहितशफलक्षणवामादेश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt saMhita-SaPalakzaRa-vAmAdeH ca UN UrU-uttarapadAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् संहित-शफलक्षण-वामादेः च ऊङ् ऊरू-उत्तरपदात्",
    padaccheda_dev        = "संहित-शफ-लक्षण-वाम-आदेः च",
    why_dev               = "(सूत्रम् 4.1.70) संहितशफलक्षणवामादेश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
