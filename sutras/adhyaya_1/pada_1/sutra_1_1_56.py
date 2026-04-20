"""
1.1.56  स्थानिवदादेशोऽनल्विधौ  —  PARIBHASHA

"The substitute (ādeśa) behaves like the substituend (sthānin) —
 except for rules involving al (phoneme-based substitution itself)."

PARIBHASHA sets an interpretive gate.  Other sūtras consult
state.paribhasha_gates['sthanivadbhava'] to decide whether to treat
an ādeśa as its sthānin for scope purposes.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    # The gate is set once per derivation.  If already set to True,
    # firing again would be a no-op (R3 catches that), so we refuse.
    return state.paribhasha_gates.get("sthanivadbhava") is not True


def act(state: State) -> State:
    state.paribhasha_gates["sthanivadbhava"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.56",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "sTAnivad AdezоnalviDO",
    text_dev       = "स्थानिवदादेशोऽनल्विधौ",
    padaccheda_dev = "स्थानिवत् आदेशः अनल्विधौ",
    why_dev        = "आदेशः स्थानिनः समानधर्मा भवति, परम् अल्-विधिं विहाय।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
