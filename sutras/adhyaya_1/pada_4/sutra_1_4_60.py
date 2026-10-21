"""
1.4.60  गतिश्च  —  SAMJNA

Sources consulted:
- ashtadhyayi.com data.txt row i=14060 · anuvṛtti निपाताः प्रादयः क्रियायोगे (1.4.58, 1.4.59)
- Kāśikā: "गतिसंज्ञकाश्च प्रादयो भवन्ति क्रियायोगे। प्रकृत्य ([[२.२.१८]])। प्रकृतम् ([[६.२.४९]])। … चकारः संज्ञासमावेशार्थः।
  प्रणीतम्। अभिषिक्तम्।"
- Cross-validation: tests/regression/test_ktva_loop.py (प्रकृत्य, आगत्य through the loop);
  tests/unit/test_prakftya_lyap_split_prakriyas.py

The prādis that 1.4.59 named upasarga in kriyāyoga are gati as well — both saṃjñās hold (चकारः संज्ञासमावेशार्थः), so the
term keeps its ``upasarga`` tag and gains ``gati``; 2.2.18 compounds it. The registry list ``gati_set`` is kept for the
later gati sūtras (1.4.61 ff.) that extend it.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

# Gati set = upasargas (from 1.4.58) + additional kriyā-viśeṣaṇas recognized
# as gati by the tradition.  The upasargas are duplicated here so this rule
# can stand alone when 1.4.58's registry entry is absent.
_GATI_SET: frozenset[str] = frozenset({
    # Twenty upasargas
    "pra", "parA", "apa", "sam", "anu", "ava",
    "nis", "nir", "dus", "dur", "vi", "A",
    "ni", "aDi", "api", "ati", "su", "ut", "ud",
    # Additional gatis recognised by the tradition
    "alam", "tiras", "punar", "asTam", "antar",
})


def _upasarga_not_gati(state: State) -> list[int]:
    return [i for i, t in enumerate(state.terms) if "upasarga" in t.tags and "gati" not in t.tags]


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_set") is None or bool(_upasarga_not_gati(state))


def act(state: State) -> State:
    for i in _upasarga_not_gati(state):
        state.terms[i].tags.add("gati")
    state.samjna_registry.setdefault("gati_set", _GATI_SET)
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.60",
    sutra_type=SutraType.SAMJNA,
    text_slp1='gatiSca',
    text_dev='गतिश्च',
    samagra_slp1="nipAtAH prAdayaH kriyAyoge gatiH ca ",
    samagra_dev="निपाताः प्रादयः क्रियायोगे गतिः च ।",
    padaccheda_dev="गतिः / च",
    why_dev="क्रियायोगे प्रादयो गतिसंज्ञका अपि (संज्ञासमावेशः)।",
    anuvritti_from=("1.4.58", "1.4.59"),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
