"""
3.1.52  अस्यतिवक्तिख्यातिभ्योऽङ्  —  VIDHI

Padaccheda: अस्यति-वक्ति-ख्यातिभ्यः अङ्

Krt suffix rule from dhatu: अस्यतिवक्तिख्यातिभ्यः अङ् (52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_ANG_ALL = frozenset({"vac", "KyA"})                    # 3.1.52 वक्ति (also brū's vac), ख्याति — asyati (asu~) needs thuk (7.4.17), not yet
_ANG_PARASMAI = frozenset({"lip", "sic", "hvA", "hve"})        # 3.1.53 लिपिसिचिह्वश्च (ātmanepada: optional, 3.1.54 — one output only)


def _cli_and_root(state: State):
    cli = next((t for t in state.terms if (t.meta.get("upadesha_slp1") or "").strip() == "cli"), None)
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if cli is None or dh is None or "kartari" not in dh.tags:
        return None
    flat = "".join(v.slp1 for v in dh.varnas)
    parasmai = not any("atmanepada" in t.tags or ("tin_adesha_3_4_78" in t.tags and "parasmaipada" not in t.tags) for t in state.terms)
    if flat in _ANG_ALL or (flat in _ANG_PARASMAI and parasmai and (dh.meta.get("upadesha_slp1") or "").strip() in
                           ("lipa~", "zica~", "hveY", "hvAY", "hve~")):
        return cli, dh
    return None


def cond(state: State) -> bool:
    return _cli_and_root(state) is not None


def act(state: State) -> State:
    hit = _cli_and_root(state)
    if hit is None:
        return state
    cli, dh = hit
    cli.varnas = [mk("a")]
    cli.meta["upadesha_slp1"] = "aG"
    cli.meta["it_markers"] = {"G"}
    cli.kind = "pratyaya"
    cli.tags |= {"pratyaya", "vikarana", "kngiti", "ardhadhatuka", "anit_ardhadhatuka"}
    if "".join(v.slp1 for v in dh.varnas) == "vac" and not any("aT_agama_v" in v.tags for v in dh.varnas[:1]) or \
            "".join(v.slp1 for v in dh.varnas if "aT_agama_v" not in v.tags) == "vac":
        # 7.4.20 वच उम् (अङि): the um (u) after the a of vac, and 6.1.87 guṇa → voc (अवोचत्)
        j = next(k for k, v in enumerate(dh.varnas) if v.slp1 == "a" and k and dh.varnas[k - 1].slp1 == "v")
        dh.varnas[j] = mk("o", *dh.varnas[j].tags)
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = 'asyativaktiKyAtiByoN',
    text_dev              = 'अस्यतिवक्तिख्यातिभ्योऽङ्',
    padaccheda_dev        = "अस्यति-वक्ति-ख्यातिभ्यः अङ्",
    why_dev               = "धातोः [अस्यतिवक्तिख्यातिभ्यः अङ्]-प्रत्ययः विहितः (३.१.52)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
