"""
1.3.10  समानामनुदेशः यथासङ्ख्यम्  —  PARIBHASHA (*anudeśa-paddhati*)

**Padaccheda:** *yathāsaṅkhyam* (avyayam), *anudeśaḥ* (prathamā ekavacanam),
*samānām* (ṣaṣṭhī bahuvacanam).

**Anuvṛtti:** none in the short *pāṭha* (full reading lists all three items).

**Adhikāra:** none named separately (general *paribhāṣā* in **1.3**).

**Śāstra (laghu):** when a rule states a relation (*anudeśaḥ*) between two lists
of **equal** length, that relation holds **yathāsaṅkhyam** — item *i* of the first
set with item *i* of the second (e.g. **6.1.78** *eco ’yavāyāvḥ* with *e*→*ay*,
*o*→*av*, *ai*→*āy*, *au*→*āv*; **3.1.134** *lyu-ṇini-ac* with three *gaṇa*s;
**1.1.46** *ṭit* before / *kit* after the *āgamin*).  When cardinalities differ
(e.g. **8.2.39** *jhalām jaś* with 24 *jhal* vs five *jaś*), **1.3.10** does not
apply and **1.1.50** *antaratama* (etc.) may decide.

**English (one line):** when a relation is taught between two same-sized groups,
it links corresponding positions only (*respectively*).

**Engine:** sets ``paribhasha_gates[YATHASANKHYAM_GATE]`` once per derivation when
the rule is scheduled (after the first **1.3.9** *it*-*lopa* pass in standard
pipelines).  Individual *vidhi* *cond*/*act* still encode their own pairings;
this gate records that the *paribhāṣā* is acknowledged for future checks.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.yathasankhyam_1_3_10 import YATHASANKHYAM_GATE


def cond(state: State) -> bool:
    return YATHASANKHYAM_GATE not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[YATHASANKHYAM_GATE] = True
    return state


_WHY = (
    "द्वयोः समसङ्ख्यक-गणयोः मध्ये अनुदेशः यदा, तदा सः सदस्येषु क्रमेण — "
    "यथा ६.१.७८ (ए→अय्, ऐ→आय्), ३.१.१३४ (ल्यु्-णिनि-अच्), १.१.४६ (टित्-कित्)। "
    "असमसङ्ख्ये (८.२.३९) न; अन्तरतमम् १.१.५० आदि।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.3.10",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "samAnAm anudeSaH yathAsaNKyam",
    text_dev       = "समानामनुदेशः यथासङ्ख्यम्",
    padaccheda_dev = (
        "यथासङ्ख्यम् (अव्ययम्) / अनुदेशः (प्रथमा-एकवचनम्) / समानाम् (षष्ठी-बहुवचनम्)"
    ),
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
