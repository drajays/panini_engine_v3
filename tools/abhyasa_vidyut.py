"""
tools/abhyasa_vidyut.py — Vidyut, the cross-check for the अभ्यासशाला (docs/ABHYASA_PLAN.md §3).

Runs under the repo's ``.venv`` (the interpreter that has ``vidyut``). Two uses:

* in-process: ``Vidyut()`` (tools/build_abhyasa_bank.py runs engine + Vidyut in one interpreter);
* as a worker: ``.venv/bin/python -m tools.abhyasa_vidyut --serve`` reads one JSON request per line on stdin and
  writes one JSON reply per line (``core/abhyasa.vidyut`` keeps one worker alive for the web UI).

Requests (all SLP1):
  {"op":"subgrid","stem":"rAma","linga":"pulliṅga","nyap":null}               → 24 cells, vibhakti-major: [[forms]…]
  {"op":"tingrid","upadesha":"BU","path_id":"01.0001","lakara":"laT","prayoga":"kartari","pada":null,
   "sanadi":["Ric"],"prefixes":["pra"]}                                         → 9 cells, prathama→uttama × eka→bahu
  {"op":"krt","upadesha":…,"path_id":…,"krts":["kta",…],"sanadi":[],"prefixes":[]}
                                                                               → {krt: {"pum":[…],"stri":[…],"napum":[…]}}
  {"op":"taddhita","stem":"upagu","names":["aR",…]}                            → {name: [forms]}
  {"op":"namadhatu","stem":"putra","pratyaya":"kyac","lakara":"laT"}           → 9 cells
  {"op":"steps", …a subgrid/tingrid cell request + "vibhakti"/"purusha","vacana"} → [{"text","steps":[{code,result}]}]
  {"op":"split","res":"devendra","a":"deva","b":"indra"}                       → true | false | null
  {"op":"lipi","text":"rAma","to":["Brahmi","Grantha",…]}                      → {scheme: text}

Display / cross-check tooling only: never imported by engine / sutras / phonology / pipelines.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LAKARA_VIDYUT = {"laT": "Lat", "liT": "Lit", "luT": "Lut", "lRT": "Lrt", "loT": "Lot", "laG": "Lan",
                 "liG": "VidhiLin", "AsIrliG": "AshirLin", "luG": "Lun", "lRG": "Lrn"}
LINGA_VIDYUT = {"pulliṅga": "Pum", "strīliṅga": "Stri", "napuṃsaka": "Napumsaka"}
VIBHAKTI = {1: "Prathama", 2: "Dvitiya", 3: "Trtiya", 4: "Caturthi", 5: "Panchami", 6: "Sasthi", 7: "Saptami",
            8: "Sambodhana"}
VACANA = {1: "Eka", 2: "Dvi", 3: "Bahu"}
PURUSHA = {1: "Uttama", 2: "Madhyama", 3: "Prathama"}
GANA = {1: "Bhvadi", 2: "Adadi", 3: "Juhotyadi", 4: "Divadi", 5: "Svadi", 6: "Tudadi", 7: "Rudhadi", 8: "Tanadi",
        9: "Kryadi", 10: "Curadi"}


class Vidyut:
    def __init__(self) -> None:
        from vidyut.prakriya import Vyakarana
        self.v = Vyakarana()
        self._splitter = None

    # ── building blocks ──
    def _run(self, pada) -> tuple[set[str], list[set[str]]]:
        try:
            ps = list(self.v.derive(pada))
        except Exception:  # noqa: BLE001 — a request Vidyut cannot build is "no forms"
            return set(), []
        return {p.text for p in ps}, [{s.code.split(":")[0] for s in p.history} for p in ps]

    def _history(self, pada) -> list[dict]:
        try:
            return [{"text": p.text, "steps": [{"code": s.code, "result": list(s.result)} for s in p.history]}
                    for p in self.v.derive(pada)]
        except Exception:  # noqa: BLE001
            return []

    @staticmethod
    def pratipadika(stem: str, linga: str, nyap: bool | None = None):
        from vidyut.prakriya import Pratipadika
        if nyap is None:
            nyap = linga == "strīliṅga" and stem.endswith(("A", "I"))
        return Pratipadika.nyap(stem) if nyap else Pratipadika.basic(stem)

    @staticmethod
    def subanta(pp, linga: str, vib: int, vac: int):
        from vidyut.prakriya import Linga, Pada, Vacana, Vibhakti
        return Pada.Subanta(pratipadika=pp, linga=getattr(Linga, LINGA_VIDYUT[linga]),
                            vibhakti=getattr(Vibhakti, VIBHAKTI[vib]), vacana=getattr(Vacana, VACANA[vac]))

    @staticmethod
    def dhatu(upadesha: str, path_id: str, sanadi=(), prefixes=()):
        from vidyut.prakriya import Dhatu, Gana, Sanadi
        from bench.practice_key import accented
        d = Dhatu.mula(aupadeshika=accented(upadesha, path_id), gana=getattr(Gana, GANA[int(path_id.split(".")[0])]))
        if sanadi:
            d = d.with_sanadi([getattr(Sanadi, s) for s in sanadi])
        if prefixes:
            d = d.with_prefixes(list(prefixes))
        return d

    @staticmethod
    def tinanta(d, lakara: str, pur: int, vac: int, prayoga: str = "kartari", pada: str | None = None):
        from vidyut.prakriya import DhatuPada, Lakara, Pada, Prayoga, Purusha, Vacana
        kw = {"dhatu_pada": getattr(DhatuPada, pada.capitalize() + "pada")} if pada else {}
        return Pada.Tinanta(dhatu=d, prayoga=getattr(Prayoga, prayoga.capitalize()),
                            lakara=getattr(Lakara, LAKARA_VIDYUT[lakara]), purusha=getattr(Purusha, PURUSHA[pur]),
                            vacana=getattr(Vacana, VACANA[vac]), **kw)

    # ── cells used by the bank builder ──
    def sub(self, stem: str, linga: str, vib: int, vac: int, pp=None):
        return self._run(self.subanta(pp if pp is not None else self.pratipadika(stem, linga), linga, vib, vac))

    def tin(self, upadesha, path_id, lakara, pur, vac, prayoga="kartari", pada=None, sanadi=(), prefixes=()):
        try:
            return self._run(self.tinanta(self.dhatu(upadesha, path_id, sanadi, prefixes), lakara, pur, vac, prayoga, pada))
        except Exception:  # noqa: BLE001
            return set(), []

    def krt(self, upadesha, path_id, krt, linga="pulliṅga", sanadi=(), prefixes=()):
        from vidyut.prakriya import Krt, Pratipadika
        try:
            pp = Pratipadika.krdanta(self.dhatu(upadesha, path_id, sanadi, prefixes), getattr(Krt, krt))
        except Exception:  # noqa: BLE001
            return set(), []
        return self.sub("", linga, 1, 1, pp=pp)

    def taddhita(self, stem, name, linga="pulliṅga"):
        from vidyut.prakriya import Pratipadika, Taddhita
        try:
            pp = Pratipadika.taddhitanta(Pratipadika.basic(stem), getattr(Taddhita, name))
        except Exception:  # noqa: BLE001
            return set(), []
        return self.sub("", linga, 1, 1, pp=pp)

    def split_back(self, res: str, a: str, b: str) -> bool | None:
        """Vidyut's sandhi rules split ``res`` back into ``a`` + ``b``; None when the rule data is absent."""
        from bench.oracle_kosha import DATA
        rules = DATA / "sandhi" / "rules.csv"
        if not rules.exists():
            return None
        if self._splitter is None:
            from vidyut.sandhi import Splitter
            self._splitter = Splitter.from_csv(str(rules))
        for w in {res, res.replace("'", "")}:
            for i in range(1, len(w)):
                if any((x.first, x.second) == (a, b) for x in self._splitter.split_at(w, i)):
                    return True
        return False

    # ── the worker protocol ──
    def handle(self, q: dict) -> Any:
        op = q["op"]
        if op == "subgrid":
            pp = self.pratipadika(q["stem"], q["linga"], q.get("nyap"))
            return [sorted(self._run(self.subanta(pp, q["linga"], vb, vc))[0]) for vb in range(1, 9) for vc in (1, 2, 3)]
        if op == "tingrid":
            try:
                d = self.dhatu(q["upadesha"], q["path_id"], q.get("sanadi") or (), q.get("prefixes") or ())
            except Exception as ex:  # noqa: BLE001
                return {"error": f"{type(ex).__name__}: {ex}"[:200]}
            return [sorted(self._run(self.tinanta(d, q["lakara"], pu, vc, q.get("prayoga") or "kartari", q.get("pada")))[0])
                    for pu in (3, 2, 1) for vc in (1, 2, 3)]
        if op == "krt":
            out = {}
            for k in q["krts"]:
                out[k] = {lg: sorted(self.krt(q["upadesha"], q["path_id"], k, linga, q.get("sanadi") or (),
                                              q.get("prefixes") or ())[0])
                          for lg, linga in (("pum", "pulliṅga"), ("stri", "strīliṅga"), ("napum", "napuṃsaka"))}
            return out
        if op == "taddhita":
            return {n: sorted(self.taddhita(q["stem"], n, q.get("linga") or "pulliṅga")[0]) for n in q["names"]}
        if op == "namadhatu":
            from vidyut.prakriya import Dhatu, Pratipadika, Sanadi
            try:
                d = Dhatu.nama(Pratipadika.basic(q["stem"]), nama_sanadi=getattr(Sanadi, q["pratyaya"]))
            except Exception as ex:  # noqa: BLE001
                return {"error": f"{type(ex).__name__}: {ex}"[:200]}
            return [sorted(self._run(self.tinanta(d, q.get("lakara") or "laT", pu, vc))[0])
                    for pu in (3, 2, 1) for vc in (1, 2, 3)]
        if op == "steps":
            if "vibhakti" in q:
                pp = self.pratipadika(q["stem"], q["linga"], q.get("nyap"))
                return self._history(self.subanta(pp, q["linga"], q["vibhakti"], q["vacana"]))
            d = self.dhatu(q["upadesha"], q["path_id"], q.get("sanadi") or (), q.get("prefixes") or ())
            return self._history(self.tinanta(d, q["lakara"], q["purusha"], q["vacana"], q.get("prayoga") or "kartari",
                                              q.get("pada")))
        if op == "split":
            return self.split_back(q["res"], q["a"], q["b"])
        if op == "lipi":
            from vidyut.lipi import Scheme, transliterate
            return {s: transliterate(q["text"], Scheme.Slp1, getattr(Scheme, s)) for s in q["to"]}
        if op == "taddhita_reverse":      # which base + taddhita (+ liṅga) regenerates this nominative?
            from vidyut.prakriya import Pratipadika, Taddhita
            names = [n for n in dir(Taddhita) if n[:1].isalpha() and n not in ("name", "value", "choices", "from_string", "anubandhas")]
            want, hits = set(q["forms"]), []
            for base in q["bases"]:
                for n in names:
                    try:
                        pp = Pratipadika.taddhitanta(Pratipadika.basic(base), getattr(Taddhita, n))
                    except Exception:  # noqa: BLE001
                        continue
                    for linga in q.get("lingas") or list(LINGA_VIDYUT):
                        for p in self._history(self.subanta(pp, linga, 1, 1)):
                            if p["text"] in want:
                                hits.append({"base": base, "pratyaya": n, "linga": linga, "form": p["text"], "steps": p["steps"]})
            return hits
        if op == "krt_reverse":           # which dhātu + kṛt (+ liṅga) regenerates this nominative?
            from vidyut.prakriya import Krt, Pratipadika
            names = [n for n in dir(Krt) if n[:1].isalpha() and n not in ("name", "value", "choices", "from_string", "anubandhas", "drshya")]
            want, hits = set(q["forms"]), []
            for up, path_id in q["dhatus"]:
                try:
                    d = self.dhatu(up, path_id)
                except Exception:  # noqa: BLE001
                    continue
                for n in names:
                    try:
                        pp = Pratipadika.krdanta(d, getattr(Krt, n))
                    except Exception:  # noqa: BLE001
                        continue
                    for linga in q.get("lingas") or list(LINGA_VIDYUT):
                        for p in self._history(self.subanta(pp, linga, 1, 1)):
                            if p["text"] in want:
                                hits.append({"dhatu": up, "path_id": path_id, "krt": n, "linga": linga, "form": p["text"],
                                             "steps": p["steps"]})
            return hits
        if op == "names":
            from vidyut.prakriya import Krt, Taddhita
            skip = {"name", "value", "choices", "from_string", "anubandhas", "drshya"}
            return {"krt": [n for n in dir(Krt) if n[:1].isalpha() and n not in skip],
                    "taddhita": [n for n in dir(Taddhita) if n[:1].isalpha() and n not in skip]}
        if op == "ping":
            return "pong"
        raise ValueError(f"unknown op {op!r}")


def serve() -> int:
    v = Vidyut()
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            out = {"ok": v.handle(json.loads(line))}
        except Exception as ex:  # noqa: BLE001 — one bad request must not kill the worker
            out = {"error": f"{type(ex).__name__}: {ex}"[:300]}
        sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    if "--serve" in sys.argv:
        raise SystemExit(serve())
    print(json.dumps(Vidyut().handle(json.load(sys.stdin)), ensure_ascii=False))
