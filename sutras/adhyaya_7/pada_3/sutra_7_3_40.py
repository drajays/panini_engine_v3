"""
7.3.40  भियो हेतुभये षुक्  —  VIDHI

Glass-box demo slice (भीषयते .md):
  When `bhI` takes ṇic (causative in the sense of fear-causation), insert the
  augment `zuk` (kit) after the aṅga per 1.1.46.

Engine:
  - recipe-armed by ``state.meta['7_3_40_zuk_arm']``.
  - inserts a pratyaya Term ``zu~k`` between dhātu and nic once.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("7_3_40_zuk_arm"):
        return False
    if len(state.terms) < 2:
        return False
    dh = state.terms[0]
    pr = state.terms[1]
    if "dhatu" not in dh.tags or "anga" not in dh.tags:
        return False
    if dh.meta.get("upadesha_slp1") not in {"BI"}:
        return False
    if "nic" not in pr.tags:
        return False
    if any(t.meta.get("upadesha_slp1") == "zuk" for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    zuk = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("zu~k")),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "zuk"},
    )
    # Place after the dhātu (kit → after āgamin; 1.1.46 gate already available).
    state.terms.insert(1, zuk)
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.40",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="Biyo hetuBaye zuk",
    text_dev="भियो हेतुभये षुक्",
    padaccheda_dev="भियः / हेतु-भये / षुक्",
    why_dev="भि-धातोः (भय-हेतौ) णिचि परे षुक्-आगमः।",
    anuvritti_from=("7.3.39",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

