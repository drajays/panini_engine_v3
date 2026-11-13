"""
1.3.91  द्युद्भ्यो लुङि  —  VIBHASHA

*Padaccheda:* *dyudbhyaḥ* / *luṅi*; anuvṛtti *vā* (1.3.90), *kartari parasmaipadam* (1.3.78).
(The old file read this as "ātmanepada" — wrong: the roots are already ātmanepadī; the sūtra gives them an
optional *parasmaipada*.)

Kāśikā 1.3.91: "अनुदात्तेत्त्वान्नित्यमेवात्मनेपदे प्राप्ते, द्युतादिभ्यो लुङि वा परस्मैपदं भवति। व्यद्युतत्,
व्यद्योतिष्ट। अलुठत्, अलोठिष्ट। लुङीति किम्? द्योतते।"

Engine: the dhātu Term carries the dhātupāṭha antargaṇa ``द्युतादिः`` (tape init) and the luṅ lakāra tag; the
rule makes the dhātu ubhayapadī for this derivation (``kartari_atmanepada_licensed='ubhaya'``), which 1.3.78's
gate reads. VIBHASHA, default off: derive() keeps the ātmanepada reading; the other is reached through
``engine.vikalpa.explore`` / ``derive_all_readings``. Pāṭha: ashtadhyayi.com data.txt row i=13091 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import ATMANE_LICENSE_META_KEY

_ANTARGANA = "द्युतादिः"


def _dhatu(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    d = _dhatu(state)
    return (d is not None and "kartari" in d.tags and "lug_derivation" in d.tags
            and _ANTARGANA in d.meta.get("antarganas", ()) and d.meta.get(ATMANE_LICENSE_META_KEY) is True)


def act(state: State) -> State:
    _dhatu(state).meta[ATMANE_LICENSE_META_KEY] = "ubhaya"
    state.samjna_registry["1_3_91_dyut_lUN_parasmai_vA"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.91",
    sutra_type=SutraType.VIBHASHA,
    r1_form_identity_exempt=True,
    vibhasha_default=False,
    vibhasha_scope=cond,           # offered only where the rule's own site exists (no phantom option on every derivation)
    text_slp1='dyudByo luNi',
    text_dev='द्युद्भ्यो लुङि',
    samagra_slp1="dyudByaH luNi kartari parasmEpadam vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="द्युद्भ्यः लुङि कर्तरि परस्मैपदम् वा",
    padaccheda_dev="द्युद्भ्यः (पञ्चमी-बहुवचन) / लुङि (सप्तमी-एकवचन)",
    why_dev=(
        "द्युतादि-धातूनां लुङि वा परस्मैपदम् — "
        "vyadyutat / vyadyotizwa; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
