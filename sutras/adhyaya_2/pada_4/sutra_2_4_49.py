"""
2.4.49  गाङ् लिटि  —  VIDHI

Kāśikā 2.4.49: "गाङादेशो भवतीङो लिटि परतः। अधिजगे, अधिजगाते, अधिजगिरे।" (iṅ → gāṅ before liṭ; the ṅ is spoken so 1.2.1 sees it.)

Engine: the root ``iN`` (adhyayane) becomes ``gAN`` when the lakāra on the tape is liṭ; same shape as 2.4.45
(iṇ → gā in luṅ), kept in its own file (one sūtra, one file).

Pāṭha: ashtadhyayi.com data.txt row i=24049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_DONE = "2_4_49_iNo_gAN_done"


def _iN(state: State):
    for t in state.terms:
        if "dhatu" in t.tags and "abhyasa" not in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "iN" \
                and not t.meta.get(_DONE):
            return t
    return None


def _liT(state: State) -> bool:
    return any(
        (t.meta.get("source_lakara_upadesha") or "").strip() == "liT" for t in state.terms)


def cond(state: State) -> bool:
    return _liT(state) and _iN(state) is not None


def act(state: State) -> State:
    dh = _iN(state)
    dh.varnas = list(parse_slp1_upadesha_sequence("gAN"))
    dh.meta["upadesha_slp1"] = "gAN"
    dh.meta[_DONE] = True
    dh.tags.add("upadesha")      # the ādeśa is a fresh upadeśa: 1.3.3 names its ṅ, 1.3.9 drops it (the root is gA again, 1.2.1 has seen gAN)
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gAN liwi",
    text_dev              = "गाङ् लिटि",
    samagra_slp1          = "ArDaDAtuke iNaH gAN liwi",
    samagra_dev           = "आर्धधातुके इङः गाङ् लिटि",
    padaccheda_dev        = "गाङ् लिटि",
    why_dev               = "इङो लिटि परतो गाङादेशः (अधिजगे) — काशिका २.४.४९।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
