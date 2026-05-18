"""
1.4.82  व्यवहिताश्च  (vyavahitāś ca)  —  SAMJNA

In the Vedic language (anuvritti from 1.4.81 chandasi), gatis that are
separated (vyavahita) from the dhātu by intervening elements also retain
their gati-saṃjñā.  This further extends the Vedic relaxation from 1.4.81.

v3: registers samjna_registry["1_4_82_gati_vyavahita_chandasi"] = True to
    mark that separated-gati usage is allowed in Vedic contexts.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return state.samjna_registry.get("1_4_82_gati_vyavahita_chandasi") is None


def act(state: State) -> State:
    state.samjna_registry["1_4_82_gati_vyavahita_chandasi"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.82",
    sutra_type=SutraType.SAMJNA,
    text_slp1="vyavahitAS ca",
    text_dev="व्यवहिताश्च",
    padaccheda_dev="व्यवहिताः / च",
    why_dev="छन्दसि व्यवहितेऽपि गति-संज्ञा — व्यवहित-गति-द्वारं स्थाप्यते।",
    anuvritti_from=("1.4.60", "1.4.81"),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
