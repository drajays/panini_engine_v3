"""
7.2.73  यमरमनमातां सक् च  —  VIDHI

Padaccheda: यम-रम-नम-आताम् सक् च

यमरमनमातां सक् च (7.2.73)
Pāṭha: ashtadhyayi.com data.txt row i=72073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_ROOTS = frozenset({"yama~", "rama~", "Rama~"})   # yam, ram, nam (KV 7.2.73); ā-final aṅgas are the "ātām" part


def _site(state: State):
    """यमरमनमातां सक् च: sak (kit āgama, 1.1.46: at the end of the aṅga) and iṭ before sic in parasmaipada luṅ —
    ayAsIt, aramsIt, anaMsIt (nam: no vṛddhi, since sic with iṭ is kit after a hal-final aṅga, 7.2.4)."""
    sic = next((t for t in state.terms if (t.meta.get("upadesha_slp1") or "").strip() == "sic"), None)
    if sic is None or not sic.varnas:
        return None
    tins = [t for t in state.terms if "tin_adesha_3_4_78" in t.tags]
    if not tins or not any("parasmaipada" in t.tags for t in tins):
        return None
    for dh in state.terms:
        if "dhatu" not in dh.tags or "abhyasa" in dh.tags or dh.meta.get("7_2_73_done") or not dh.varnas:
            continue
        up = (dh.meta.get("upadesha_slp1") or "").strip()
        if up in _ROOTS or dh.varnas[-1].slp1 == "A":
            return dh, sic
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is None:
        return state
    dh, sic = hit
    from phonology import mk
    dh.meta["7_2_73_done"] = True
    s = mk("s")
    s.tags.add("agama")
    dh.varnas.append(s)
    if "it_agama" not in sic.varnas[0].tags:
        v = mk("i")
        v.tags.add("it_agama")
        sic.varnas.insert(0, v)
        sic.meta["it_agama_7_2_35_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "yamaramanamAtAM sak ca",
    text_dev              = "यमरमनमातां सक् च",
    samagra_slp1          = "aNgasya yamaramanamAtAm sak ca valAdeH iw ArDaDAtukasya sici parasmEpadezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य यमरमनमाताम् सक् च वलादेः इट् आर्धधातुकस्य सिचि परस्मैपदेषु",
    padaccheda_dev        = "यम-रम-नम-आताम् सक् च",
    why_dev               = "(सूत्रम् 7.2.73) यमरमनमातां सक् च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
