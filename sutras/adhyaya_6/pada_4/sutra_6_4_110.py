"""
6.4.110  अत उत् सार्वधातुके  —  VIDHI (narrow demo)

Demo slice (कुरुतः):
  After guṇa + r-para (कृ → कर्) under **7.3.84** + **1.1.51**, when a following
  *sārvadhātuka* tiṅ affix is treated as kṅit via **1.2.4**, replace the `a` of
  the aṅga `kar` with `u` → `kur`.

Engine:
  - looks for an aṅga (dhātu term) containing the sequence ``k a r`` at the end
    (after urṇ r-para completion), and a following pratyaya Term tagged
    ``kngiti``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    if len(state.terms) < 2:
        return None
    dh = state.terms[0]
    if "dhatu" not in dh.tags and "anga" not in dh.tags:
        return None
    # Find the next pratyaya carrying kṅiti signal (skip intervening vikaraṇa like `u`).
    kng_pr = None
    for j in range(1, len(state.terms)):
        if "pratyaya" not in state.terms[j].tags:
            continue
        if "kngiti" in state.terms[j].tags:
            kng_pr = state.terms[j]
            break
    if kng_pr is None:
        return None
    if dh.meta.get("6_4_110_at_ut_done"):
        return None
    vs = dh.varnas
    if len(vs) < 3:
        return None
    # Expect ... k a r (narrow demo).
    if vs[-1].slp1 != "r":
        return None
    if vs[-2].slp1 != "a":
        return None
    return len(vs) - 2


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    dh = state.terms[0]
    dh.varnas[i] = mk("u")
    dh.meta["6_4_110_at_ut_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.110",
    sutra_type=SutraType.VIDHI,
    text_slp1="ataH ut sArvaDAtuke",
    text_dev="अत उत् सार्वधातुके",
    padaccheda_dev="अतः / उत् / सार्वधातुके",
    why_dev="कङिति सार्वधातुके परे 'अ' का 'उ' आदेशः (कुरुतः)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

