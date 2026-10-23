"""engine/ang_adesha.py — the cli → aṅ family (3.1.52–3.1.58): one site test and one substitution.

Each sūtra names its own roots and padas; this module only finds the cli and the dhātu on the tape and writes
aṅ (a + ṅ, ṅit: 1.1.5 then blocks guṇa) in cli's place. Roots are read as the dhātu stood after it-lopa
(``it_lopa_done``), never from the tape, which guṇa or an āgama may already have changed (Art. 2)."""
from __future__ import annotations

from engine.state import State, Term
from engine.vikalpa import policy_choice
from phonology import mk


def cli_and_root(state: State):
    """(cli Term, dhātu Term) for a kartari luṅ whose vikaraṇa is still cli, else None."""
    cli = next((t for t in state.terms if (t.meta.get("upadesha_slp1") or "").strip() == "cli"), None)
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if cli is None or dh is None or "kartari" not in dh.tags:
        return None
    return cli, dh


def stem(dh: Term) -> str:
    lopa = dh.meta.get("it_lopa_done")
    return lopa[-1] if lopa else "".join(v.slp1 for v in dh.varnas)


def parasmaipada(state: State) -> bool:
    """परस्मैपदेषु — once a tiṅ stands on the tape it is a parasmaipada one; before that, the pada the dhātu is asked in."""
    tins = [t for t in state.terms if "tin_adesha_3_4_78" in t.tags]
    if tins:
        return any("parasmaipada" in t.tags for t in tins)
    return state.meta.get("pada_asked", "parasmai") == "parasmai"      # no tiṅ yet: the pada the derivation was asked in


def vikalpa_ang(sutra_id: str) -> bool:
    """वा / अन्यतरस्याम्: the reading is a choice (engine.vikalpa.choose({id: True}) takes the aṅ branch); the default keeps sic."""
    return policy_choice(sutra_id, False)


def to_ang(cli: Term) -> None:
    cli.varnas = [mk("a")]
    cli.meta["upadesha_slp1"] = "aG"
    cli.meta["it_markers"] = {"G"}
    cli.kind = "pratyaya"
    cli.tags |= {"pratyaya", "vikarana", "kngiti", "ardhadhatuka", "anit_ardhadhatuka"}
