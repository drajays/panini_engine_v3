"""
6.4.16  अज्झनगमां सनि  —  VIDHI (narrow demo)

Pāṇini: before *san*, certain *aṅga* vowels are lengthened (*dīrgha*).

Narrow v3 (*cicīṣati*):
  In a reduplication frame ``[abhyāsa][dhātu][sanādi `is`]``, lengthen the
  final *hrasva* *i* of the listed non-abhyāsa dhātu to *ī* (SLP1 ``I``), then
  drop the leading ``i`` of ``is`` so the surface presents ``…Iṣ…`` (tripāḍī
  **8.3.59** conditions on *ī* immediately before *s*).

P030 (*vivakṣaka*): same frame, but dhātu ``vac`` after samprasāraṇa presents as
``u`` + ``c`` — lengthen initial ``u`` to ``U`` (``ū``), then drop leading ``i``
from ``is`` → ``s``.

Engine:
  - recipe arms ``state.meta['6_4_16_sani_dirgha_arm']``.
  - applies to ``upadesha_slp1`` in ``{"ci", "vac"}``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk

_DHATU_UPADESHA = frozenset({"ci", "vac"})


def _find_main_ci(state: State) -> int | None:
    if not state.meta.get("6_4_16_sani_dirgha_arm"):
        return None
    ts = state.terms
    if len(ts) < 3:
        return None
    for i in range(1, len(ts) - 1):
        prev, mid, nxt = ts[i - 1], ts[i], ts[i + 1]
        if "abhyasa" not in prev.tags:
            continue
        if "abhyasa" in mid.tags or "dhatu" not in mid.tags:
            continue
        up = (mid.meta.get("upadesha_slp1") or "").strip()
        if up not in _DHATU_UPADESHA:
            continue
        if up == "ci":
            if not mid.varnas or mid.varnas[-1].slp1 != "i":
                continue
        elif up == "vac":
            # Samprasāraṇa + pūrvarūpa: ``u`` + ``c`` on the non-abhyāsa copy.
            if (
                len(mid.varnas) < 2
                or mid.varnas[0].slp1 != "u"
                or mid.varnas[1].slp1 != "c"
            ):
                continue
        else:
            continue
        if mid.meta.get("6_4_16_dirgha_done"):
            continue
        if "sanadi" not in nxt.tags:
            continue
        if (nxt.meta.get("upadesha_slp1") or "").strip() not in {"san", "is"}:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_main_ci(state) is not None


def act(state: State) -> State:
    i = _find_main_ci(state)
    if i is None:
        return state
    mid = state.terms[i]
    up = (mid.meta.get("upadesha_slp1") or "").strip()
    if up == "ci":
        mid.varnas[-1] = mk("I")
    else:
        mid.varnas[0] = mk("U")
    mid.meta["6_4_16_dirgha_done"] = True
    san = state.terms[i + 1]
    if (
        "sanadi" in san.tags
        and (san.meta.get("upadesha_slp1") or "").strip() == "is"
        and len(san.varnas) >= 2
        and san.varnas[0].slp1 == "i"
        and not san.meta.get("6_4_16_san_initial_i_lopa_done")
    ):
        san.varnas = san.varnas[1:]
        san.meta["upadesha_slp1"] = "s"
        san.meta["6_4_16_san_initial_i_lopa_done"] = True
    state.meta["6_4_16_sani_dirgha_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.16",
    sutra_type=SutraType.VIDHI,
    text_slp1="ajJanagamAM sani",
    text_dev="अज्झनगमां सनि",
    padaccheda_dev="अज्झनगमाम् / सनि",
    why_dev="सनि परे अङ्गस्य दीर्घः — चिचीषति (द्वित्वोत्तर-अङ्ग-स्थाने)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
