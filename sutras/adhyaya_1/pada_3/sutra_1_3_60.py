"""
1.3.60  शदेः शितः  —  VIDHI

*Padaccheda:* *śadeḥ* / *śitaḥ*; anuvṛtti *ātmanepadam* (1.3.12).

Kāśikā 1.3.60: "शद्ऌ शातने (धा० पा० १८५५) परस्मैपदी, तस्मादात्मनेपदं विधीयते। शदिर्यः शित्, शिद्भावी शितो वा
संबन्धी, तस्मादात्मनेपदं भवति। शीयते … शित इति किम्? अशत्स्यत्। शत्स्यति। शिशत्सति।"

Engine: the dhātu is ``Sadx~`` (the parasmaipadī śad). A śit is on the way when the lakāra is sārvadhātuka
(laṭ/loṭ/laṅ/vidhiliṅ — the lakāra tag tape init puts on the dhātu Term, not a caller pada). ``act`` licenses
ātmanepada on the dhātu (``kartari_atmanepada_licensed``), which 1.3.78's gate reads to pick the pada before
the tiṅ ādeśa. Not śit (liṭ/lṛṭ/lṛṅ/luṅ/luṭ/āśīrliṅ): no fire, parasmaipada stays.
Pāṭha: ashtadhyayi.com data.txt row i=13060 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import ATMANE_LICENSE_META_KEY

# the sārvadhātuka lakāras (laṭ loṭ laṅ vidhiliṅ) take śap/śyan/…: a śit follows (3.1.68 / 3.4.113)
_SIT_LAKARA = frozenset({"lat_derivation", "lot_derivation", "lag_derivation", "lig_derivation"})

_ROOT = "Sadx~"


def _dhatu(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    d = _dhatu(state)
    return (d is not None and "kartari" in d.tags and (d.meta.get("upadesha_slp1") or "") == _ROOT
            and bool(_SIT_LAKARA & d.tags) and d.meta.get(ATMANE_LICENSE_META_KEY) is not True)


def act(state: State) -> State:
    _dhatu(state).meta[ATMANE_LICENSE_META_KEY] = True
    state.samjna_registry["1_3_60_Sad_Sit_Atmanepada"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.60",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="SadeH SitaH",
    text_dev="शदेः शितः",
    samagra_slp1="SadeH SitaH Atmanepadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="शदेः शितः आत्मनेपदम्",
    padaccheda_dev="शदेः (षष्ठी-एकवचन) / शितः (षष्ठी-एकवचन)",
    why_dev=(
        "शद्-धातोः शित्-प्रत्यये परे आत्मनेपदम् — "
        "SIyate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
