"""One source of kṅit for the whole engine (owner ruling 2026-10-21): the it-saṃjñā k / ṅ of a *pratyaya* makes it
kṅit for every rule that asks (1.1.5 क्ङिति च), and 1.2.18 न क्त्वा सेट् withdraws it from a ktvā that took iṭ
(Kāśikā: देवित्वा, वर्तित्वा; सेडिति किम्? कृत्वा). An āgama's k (vuk, tuk) is no kit affix.
"""
from __future__ import annotations

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.state import Term
from engine.tape_init.krdanta import PURVAKALA_SAMANAKARTRKA
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.krdanta import build_dhatu_state


def _ktva_after_it_lopa(ref: str):
    s = build_dhatu_state(ref, **PURVAKALA_SAMANAKARTRKA)
    for sid in ("1.3.2", "1.3.9", "3.4.21", "1.3.8", "1.3.9"):
        s = apply_rule(sid, s)
    return s


def test_kit_pratyaya_is_kngit():
    ktva = _ktva_after_it_lopa("qukfY").terms[-1]
    assert {"it:kit", "kngiti"} <= ktva.tags


def test_agama_k_is_not_kngit():
    from engine.it_samjna import record_it_lopa
    vuk = Term(kind="agama", varnas=list(parse_slp1_upadesha_sequence("vuk")), tags={"agama", "upadesha"},
               meta={"upadesha_slp1": "vuk"})
    k = vuk.varnas[-1]
    k.tags.add("it_halantyam")
    vuk.varnas.pop()
    record_it_lopa(vuk, [(2, k)], 3)
    assert "it:kit" in vuk.tags and "kngiti" not in vuk.tags


def test_1_2_18_withdraws_kit_from_set_ktva_only():
    s = _ktva_after_it_lopa("divAdi_04_0001")          # दिवुँ — seṭ
    s = apply_rule("3.4.114", s)
    s = apply_rule("7.2.35", s)
    assert SUTRA_REGISTRY["1.2.18"].cond(s)
    s = apply_rule("1.2.18", s)
    assert not {"kngiti", "it:kit"} & s.terms[-1].tags
    assert not SUTRA_REGISTRY["1.2.18"].cond(_ktva_after_it_lopa("qukfY"))     # कृत्वा: aniṭ, stays kit
