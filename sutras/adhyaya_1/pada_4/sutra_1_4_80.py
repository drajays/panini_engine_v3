"""
1.4.80  ते प्राग्धातोः  —  SAMJNA

Those (gatis enumerated in the preceding sūtras 1.4.60–1.4.79) occur
before (prāk) the dhātu (verb root).  This sūtra restricts the domain
of gati-saṃjñā: the gati must precede the dhātu in the phonological string.

v3: registers the gate "1_4_80_gati_prag_dhatu" = True to mark that this
    positional requirement has been noted.  The actual positional check is
    enforced by the recipe/pipeline when applying sandhi and kṛt rules.
Pāṭha: ashtadhyayi.com data.txt row i=14080 (Art. 14).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return state.samjna_registry.get("1_4_80_gati_prag_dhatu") is None


def act(state: State) -> State:
    state.samjna_registry["1_4_80_gati_prag_dhatu"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.80",
    sutra_type=SutraType.SAMJNA,
    text_slp1='te prAgDAtoH',
    text_dev='ते प्राग्धातोः',
    samagra_slp1="upasargAH  gatiH prAk DAtoH",
    samagra_dev="उपसर्गाः , गतिः प्राक् धातोः",
    padaccheda_dev="ते / प्राक् / धातोः",
    why_dev="गति-संज्ञकाः धातोः प्राक् भवन्ति — स्थान-नियमः संज्ञारजिस्ट्रीयां नोद्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
