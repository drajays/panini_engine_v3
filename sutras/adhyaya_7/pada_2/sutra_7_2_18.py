"""
7.2.18  क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु  —  VIDHI

Padaccheda: क्षुब्ध-स्वान्त-ध्वान्त-लग्न-म्लिष्ट-विरिब्ध-फाण्ट-बाढानि मन्थ-मनः-तमः-सक्त-अविस्पष्ट-स्वर-अनायास-भृशेषु

क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु (7.2.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_18_kzubDasvAn_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzubDasvAntaDvAntalagnamlizwaviribDaPARwabAQAni manTamanastamaHsaktAvispazwasvarAnAyAsaBfSezu",
    text_dev              = "क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु",
    padaccheda_dev        = "क्षुब्ध-स्वान्त-ध्वान्त-लग्न-म्लिष्ट-विरिब्ध-फाण्ट-बाढानि मन्थ-मनः-तमः-सक्त-अविस्पष्ट-स्वर-अनायास-भृशेषु",
    why_dev               = "(सूत्रम् 7.2.18) क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
