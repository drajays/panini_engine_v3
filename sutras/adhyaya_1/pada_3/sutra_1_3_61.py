"""
1.3.61  म्रियतेर्लुङ्लिङोश्च  —  VIDHI (niyama)

*Padaccheda:* *mriyateḥ* / *luṅ-liṅoḥ* / *ca*; anuvṛtti *śitaḥ* (1.3.60), *ātmanepadam* (1.3.12).

Kāśikā 1.3.61: "ङित्त्वादात्मनेपदमत्र सिद्धमेवेति नियमार्थमिदं वचनम्। म्रियतेर्लुङ्लिङोः शितश्चात्मनेपदं भवति,
अन्यत्र न भवति। अमृत। मृषीष्ट। शितः खल्वपि — म्रियते … नियमः किमर्थः? मरिष्यति। अमरिष्यत्।"

Engine: ``mfN`` is ṅit, so 1.3.12 licenses ātmanepada; this niyama withdraws the licence unless the lakāra is
luṅ, āśīrliṅ, or a śit one (sārvadhātuka). So liṭ/luṭ/lṛṭ/lṛṅ → licence off → 1.3.78 gives parasmaipada
(mamāra, mariṣyati). Reads the lakāra tag on the dhātu Term; writes the licence key 1.3.78's gate reads.
Pāṭha: ashtadhyayi.com data.txt row i=13061 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import ATMANE_LICENSE_META_KEY

# the sārvadhātuka lakāras (laṭ loṭ laṅ vidhiliṅ) take śap/śyan/…: a śit follows (3.1.68 / 3.4.113)
_SIT_LAKARA = frozenset({"lat_derivation", "lot_derivation", "lag_derivation", "lig_derivation"})

_ROOT = "mfN"
_NOT_NIYAMA = _SIT_LAKARA | {"lug_derivation", "asirlig_derivation"}


def _dhatu(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    d = _dhatu(state)
    return (d is not None and "kartari" in d.tags and (d.meta.get("upadesha_slp1") or "") == _ROOT
            and not (_NOT_NIYAMA & d.tags) and d.meta.get(ATMANE_LICENSE_META_KEY) is True)


def act(state: State) -> State:
    _dhatu(state).meta[ATMANE_LICENSE_META_KEY] = False
    state.samjna_registry["1_3_61_mf_niyama"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.61",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='mriyaterluNliNoSca',
    text_dev='म्रियतेर्लुङ्लिङोश्च',
    samagra_slp1="mriyateH luN-liNoH ca Atmanepadam SitaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="म्रियतेः लुङ्-लिङोः च आत्मनेपदम् शितः",
    padaccheda_dev="म्रियतेः (षष्ठी-एकवचन) / लुङ्-लिङोः (सप्तमी-द्विवचन) / च",
    why_dev=(
        "मृ-धातोः लुङ्-लिङ्-लकारयोः आत्मनेपदम् — "
        "amfta, mriyeta इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
