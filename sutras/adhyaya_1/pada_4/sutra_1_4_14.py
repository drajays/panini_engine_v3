"""
1.4.14  सुप्तिङन्तं पदम् (here: सुप्)  —  SAMJNA

For this file we encode the 'sup' samjñā: the 18 case-pratyayas
[su, O, jas, am, Ow, Sas, wA, ByAm, Bis, Ne, ByAm, Byas, Nasi,
 ByAm, Byas, Nas, os, Am, Ni, os, sup]  (counting all 21 upadeśas
 that collapse to 18 distinct forms)
are registered under the name 'sup'.

SAMJNA writes to state.samjna_registry['sup'] = frozenset(...).
Once registered, a Term may be tagged 'sup' at recipe time and
pratyayas referenced by phonemic shape are recognized as sup.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


_SUP_UPADESHAS = frozenset({
    "s~", "O", "jas",
    "am", "Ow", "Sas",
    "wA", "ByAm", "Bis",
    "Ne",  "ByAm", "Byas",
    "Nasi","ByAm", "Byas",
    "Nas", "os",   "Am",
    "Ni",  "os",   "sup",
})


def cond(state: State) -> bool:
    return state.samjna_registry.get("sup") != _SUP_UPADESHAS


def act(state: State) -> State:
    state.samjna_registry["sup"] = _SUP_UPADESHAS
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.14",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "suptiNantam padam (suP)",
    text_dev       = "सुबन्तं पदम् (सुप्-संज्ञा)",
    padaccheda_dev = "सुप् तिङ्-अन्तं पदम् (अत्र सुप्-संज्ञा केवलम्)",
    why_dev        = "सु-आदयः एकविंशति सुप्-प्रत्ययाः सुप्-संज्ञां लभन्ते।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
