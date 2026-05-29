"""
3.4.107  सुट् तिथोः  —  VIDHI (āśīr-liṅ: full 9-cell)

Insert the augment **suṭ** (surface ``s``) immediately before a tiṅ ādeśa
that begins with dental **t** or **tha** (= SLP1 't' or 'T') in āśīr-liṅ.

This fires for: 3sg (t), 3du (tāṃ), 2du (tam), 2pl (ta) — all t-initial.
Does NOT fire for: 3pl (us), 2sg (s), 1sg (am), 1du (va), 1pl (ma).

Engine:
  - arm ``state.meta['suw_recipe']`` + ``state.meta['ashir_liG']``.
  - suṭ Term tagged ``suw_agama``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk


def _find_tin_t_initial(state: State) -> int | None:
    """Find the rightmost tiṅ ādeśa whose first varṇa is dental t or T."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if not t.varnas:
            continue
        if t.varnas[0].slp1 not in ('t', 'T'):
            continue
        # Idempotency: skip if suṭ is already before this tiṅ
        if i > 0 and "suw_agama" in state.terms[i - 1].tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("suw_recipe"):
        return False
    if not state.meta.get("ashir_liG"):
        return False
    return _find_tin_t_initial(state) is not None


def act(state: State) -> State:
    idx = _find_tin_t_initial(state)
    if idx is None:
        return state
    suw = Term(
        kind="pratyaya",
        varnas=[mk("s")],
        tags={"pratyaya", "suw_agama"},
        meta={"upadesha_slp1": "s", "suw_agama": True},
    )
    state.terms.insert(idx, suw)
    state.meta["suw_recipe"] = False
    state.samjna_registry["3.4.107_suw_inserted"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.107",
    sutra_type=SutraType.VIDHI,
    text_slp1="suw tiToH",
    text_dev="सुट् तिथोः",
    padaccheda_dev="सुट् / तिथोः",
    why_dev=(
        "आशीर्-लिङि त-थ-प्रारम्भ-तिङ्-आदेशात् पूर्वं सुट्-आगमः — "
        "३सग (त्), ३द्वि (ताम्), २द्वि (तम्), २बहु (त)।"
    ),
    anuvritti_from=("3.4.77",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
