"""
1.3.92  वृद्भ्यः स्यसनोः  —  VIBHASHA

*Padaccheda:* *vṛdbhyaḥ* / *sya-sanoḥ*; anuvṛtti *vā*, *kartari parasmaipadam*.
(The old file read this as "ātmanepada" — wrong: vṛtādi roots are ātmanepadī and get an optional *parasmaipada*.)

Kāśikā 1.3.92: "वृतादयः … एतेभ्यो धातुभ्यः स्ये सनि च परतो वा परस्मैपदं भवति। वृत् — वर्त्स्यति, अवर्त्स्यत्,
विवृत्सति, वर्तिष्यते … स्यसनोरिति किम्? वर्तते।"

Engine: the dhātu Term carries antargaṇa ``वृतादिः`` and the lṛṭ/lṛṅ lakāra tag (the lakāras whose ādeśa follows
*sya*); makes the dhātu ubhayapadī for this derivation, read by 1.3.78's gate. VIBHASHA, default off (derive()
keeps the ātmanepada reading; explore yields both). Pāṭha: ashtadhyayi.com data.txt row i=13092 (Art. 14).
Open: the *san* half (vivṛtsati) — the sanādi spine fixes ātmane itself (_derive_laT_san_atmane).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import ATMANE_LICENSE_META_KEY

_ANTARGANA = "वृतादिः"
_SYA_LAKARA = frozenset({"lrt_derivation", "lrn_derivation"})


def _dhatu(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    d = _dhatu(state)
    return (d is not None and "kartari" in d.tags and bool(_SYA_LAKARA & d.tags)
            and _ANTARGANA in d.meta.get("antarganas", ()) and d.meta.get(ATMANE_LICENSE_META_KEY) is True)


def act(state: State) -> State:
    _dhatu(state).meta[ATMANE_LICENSE_META_KEY] = "ubhaya"
    state.samjna_registry["1_3_92_vfta_sya_parasmai_vA"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.92",
    sutra_type=SutraType.VIBHASHA,
    r1_form_identity_exempt=True,
    vibhasha_default=False,
    vibhasha_scope=cond,           # offered only where the rule's own site exists (no phantom option on every derivation)
    text_slp1='vfdByaH syasanoH',
    text_dev='वृद्भ्यः स्यसनोः',
    samagra_slp1="vfdByaH sya-sanoH kartari parasmEpadam vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="वृद्भ्यः स्य-सनोः कर्तरि परस्मैपदम् वा",
    padaccheda_dev="वृद्भ्यः (पञ्चमी-बहुवचन) / स्य-सनोः (षष्ठी-द्विवचन)",
    why_dev=(
        "वृतादि-धातूनां स्ये सनि च वा परस्मैपदम् — "
        "vartsyati, vivftsati; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
