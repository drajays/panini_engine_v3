"""
7.3.103  बहुवचने झल्येत्  —  VIDHI

"In the plural (bahuvacana), when a jhal-initial pratyaya follows,
 the final अ of the aṅga is replaced by ए (e)."

  cell 3-3: rAma + Bis → rAmeBis → rAmEH (later tripadi steps)
  cell 4-3: rAma + Byas → rAmeByas → rAmeByaH
  cell 5-3: rAma + Byas → rAmeByas → rAmeByaH
  cell 7-3: rAma + sup → rAma + su (after 1.3.3 strips p) → rAmesu → rAmeSu

For v3.1 we narrowly detect: aṅga ends in 'a', pratyaya is sup-tagged,
pratyaya upadeśa is one of the plural jhal-initial ones (Bis, Byas, sup),
and the aṅga hasn't already been modified.

This fires BEFORE 7.3.102 supi-ca (which otherwise would make a→ā).
We achieve that by running 7.3.103 earlier in the pipeline.

How does the engine know bahuvacana?  Via upadesha_slp1 of the
pratyaya — only plural sup pratyayas are in the set {Bis, Byas, sup}.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State
from phonology     import mk


# Pratyaya upadeśas that trigger a → e.  These are the plural-jhal set
# from our sup inventory.  (jas starts with 'j' — also jhal, also plural —
# but jas has its own specific substitution path handled elsewhere.)
_TRIGGER_UPADESHAS = frozenset({"Bis", "Byas", "sup", "sAm"})


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    if "anga" not in anga.tags:
        return None
    if "sup" not in pratyaya.tags:
        return None
    upa = pratyaya.meta.get("upadesha_slp1")
    if upa not in _TRIGGER_UPADESHAS:
        return None
    if anga.meta.get("aNga_e_done"):
        return None
    if not anga.varnas:
        return None
    if anga.varnas[-1].slp1 != "a":
        return None
    return len(state.terms) - 2, len(anga.varnas) - 1


def cond(state: State) -> bool:
    if not adhikara_in_effect("7.3.103", state, "6.4.1"):
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("e")
    state.terms[ti].meta["aNga_e_done"] = True
    # Also block 7.3.102 from re-applying to this aṅga.
    state.terms[ti].meta["aNga_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.103",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "bahuvacane Jalyet (aNgasya ataH)",
    text_dev       = "बहुवचने झल्येत्",
    padaccheda_dev = "बहुवचने झलि एत् — अङ्गस्य अतः",
    why_dev        = "झल्-आदि-बहुवचन-सुप्-प्रत्यये परे अदन्त-अङ्गस्य "
                     "अन्त्य-अ-कारस्य 'ए'-आदेशः।",
    anuvritti_from = ("6.4.1", "7.3.102"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
