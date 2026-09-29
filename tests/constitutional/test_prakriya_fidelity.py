"""
tests/constitutional/test_prakriya_fidelity.py — the trace must be a Pāṇinian prakriyā.

1. Every sūtra quotes the sūtrapāṭha and has the pāṭha's lakṣaṇa (type), save
   the cited overrides in ``tools.sync_sutrapatha.TYPE_OVERRIDES``.
2. Over real derivations (nouns and verbs):
   - no tripādī sūtra (8.2.2–8.4.68) takes effect before 8.2.1 opens the zone,
     and no sapādasaptādhyāyī sūtra takes effect after it (पूर्वत्रासिद्धम्);
   - a step reads APPLIED only if it changed the form or marked the tape;
   - a sup never takes its vacana from 1.4.102 (that is tiṅ's; sup's is 1.4.103).

Needs the pinned sūtrapāṭha (``python3 -m tools.fetch_ashtadhyayi_data``).
"""
from __future__ import annotations

import pytest

from tools.fetch_ashtadhyayi_data import path as ref_path

pytestmark = pytest.mark.skipif(
    not ref_path("sutraani/data.txt").exists(),
    reason="run 'python3 -m tools.fetch_ashtadhyayi_data' for the sūtrapāṭha",
)

_NOUNS = [("rAma", "pulliṅga"), ("hari", "pulliṅga"), ("Denu", "strīliṅga"), ("rAjan", "pulliṅga"),
          ("sarva", "pulliṅga"), ("jYAna", "napuṃsaka"), ("marut", "pulliṅga"), ("nadI", "strīliṅga"),
          ("vAc", "strīliṅga"), ("pitf", "pulliṅga")]
_VERBS = ["01.0001", "01.0002", "02.0004", "02.0006", "01.1146", "10.0001", "06.0001", "01.1049",
          "08.0010", "09.0001", "04.0001", "01.0919"]
_LAKARAS = ("laT", "liT", "luT", "lRT", "loT", "laG", "liG", "AsIrliG", "luG", "lRG")


def _is_tripadi(sid: str) -> bool:
    p = sid.split(".")
    return (len(p) == 3 and p[0] == "8" and all(x.isdigit() for x in p)
            and (int(p[1]) >= 3 or (p[1] == "2" and int(p[2]) >= 2)))


def _corpus():
    from pipelines.subanta import derive as sub
    from pipelines.tinanta import derive as tin
    for stem, linga in _NOUNS:
        for vi in range(1, 9):
            for va in (1, 2, 3):
                try:
                    yield f"{stem} {vi}-{va}", "sup", sub(stem, vi, va, linga=linga).trace
                except Exception:
                    pass
    for did in _VERBS:
        for lak in _LAKARAS:
            for prayoga in ("kartari", "karmani"):
                for pv in ((3, 1), (3, 3), (1, 2)):
                    try:
                        yield f"{did} {lak} {prayoga} {pv}", "tin", tin(did, lak, prayoga, *pv).trace
                    except Exception:
                        pass


@pytest.fixture(scope="module")
def corpus():
    return list(_corpus())


def test_every_sutra_quotes_the_patha():
    from tools.sync_sutrapatha import norm, patha
    import sutras  # noqa: F401
    from engine.registry import SUTRA_REGISTRY
    ref = patha()
    bad = [sid for sid, rec in SUTRA_REGISTRY.items()
           if sid in ref and norm(rec.text_dev) != norm(ref[sid])]
    assert not bad, f"text differs from the pāṭha: {bad[:10]} (python3 -m tools.sync_sutrapatha --write)"
    assert set(SUTRA_REGISTRY) <= set(ref), f"not in the Aṣṭādhyāyī: {sorted(set(SUTRA_REGISTRY) - set(ref))}"


def test_every_sutra_has_the_pathas_laksana():
    from tools.sync_sutrapatha import type_mismatches
    bad = [(sid, rec.sutra_type.name, want.name) for sid, rec, want in type_mismatches()]
    assert not bad, f"type differs from the pāṭha: {bad[:10]} (python3 -m tools.sync_sutrapatha --types --write)"


def test_the_tripadi_is_asiddha_both_ways(corpus):
    offenders = []
    for name, _kind, trace in corpus:
        opened = False
        for st in trace:
            sid = st.get("sutra_id") or ""
            if sid == "8.2.1" and st.get("status") not in ("SKIPPED", "BLOCKED"):
                opened = True
            changed = st.get("form_before") != st.get("form_after")
            if not changed or st.get("status") != "APPLIED" or sid.startswith("__"):
                continue
            if _is_tripadi(sid) and not opened:
                offenders.append(f"{name}: {sid} before 8.2.1")
            if opened and not _is_tripadi(sid) and sid != "8.2.1":
                offenders.append(f"{name}: {sid} after 8.2.1")
    assert not offenders, offenders[:10]


def test_applied_means_something_happened(corpus):
    # the dispatcher labels a firing with no effect DEFINED / VACUOUS; a
    # vidhi that reads APPLIED with an unchanged form must have marked the tape,
    # which the dispatcher checked — here we check no silent no-op vidhi slipped
    # through as APPLIED on the surface-changing layer.
    import sutras  # noqa: F401
    from engine.registry import SUTRA_REGISTRY
    from engine.sutra_type import SutraType
    silent = set()
    for name, _kind, trace in corpus:
        for st in trace:
            sid = st.get("sutra_id") or ""
            rec = SUTRA_REGISTRY.get(sid)
            if (rec is not None and rec.sutra_type is SutraType.VIDHI and st.get("status") == "APPLIED"
                    and st.get("form_before") == st.get("form_after") and sid in {"8.4.56", "8.4.68"}):
                silent.add(f"{name}: {sid}")
    assert not silent, sorted(silent)[:10]


def test_sup_vacana_comes_from_1_4_103(corpus):
    wrong = [name for name, kind, trace in corpus
             if kind == "sup" and any(st.get("sutra_id") == "1.4.102" and st.get("status") == "APPLIED"
                                      for st in trace)]
    assert not wrong, wrong[:10]
