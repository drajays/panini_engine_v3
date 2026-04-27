"""
3.2.139  ग्लाजिस्थश्च ग्स्नुः  —  VIDHI (narrow: *gsnuC* on *ji* / *glā* / *sthā*)

**Pāṭha:** *glājiṣṭhaś ca gsnūḥ* — *tācchīlye* *gsnuC* after **3.2.134**
(*ākv…* *adhikāra*).

Glass-box v3: when ``state.meta["3_2_139_gsnu_arm"]`` is set and ``terms[0]`` is
a *dhātu* whose *upadeśa* is ``ji``, append a *kṛt* ``Term`` **gsnuC**
(``g`` + ``s`` + ``n`` + ``u`` + ``c`` *it*).  The initial ``g`` is *it* by
**1.3.8** (*laśakvataddhite*); the ``Term`` carries ``kngiti`` so **1.1.5**
blocks **7.3.84** *guṇa* (*gidiavat* behaviour after ``g``-*lopa*).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk


def cond(state: State) -> bool:
    if not state.meta.get("3_2_139_gsnu_arm"):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != "ji":
        return False
    if state.samjna_registry.get("3.2.139_gsnu_attached"):
        return False
    return True


def act(state: State) -> State:
    gsnu = Term(
        kind="pratyaya",
        varnas=[mk("g"), mk("s"), mk("n"), mk("u"), mk("c")],
        tags={"krt", "upadesha", "kngiti"},
        meta={"upadesha_slp1": "gsnuC"},
    )
    state.terms.append(gsnu)
    state.samjna_registry["3.2.139_gsnu_attached"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.139",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "glAji-zWaS ca gsnuH",
    text_dev       = "ग्लाजिस्थश्च ग्स्नुः",
    padaccheda_dev = "ग्ला-जि-स्थः / च / ग्स्नुः",
    why_dev        = "ताच्छील्ये जि-धातोः ग्स्नुच्-प्रत्ययः (ग्लास-बॉक्स्)।",
    anuvritti_from = ("3.2.134",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
