"""tools.test_impact: changed line ranges map to the qualnames of the defs they touch; anything outside a def selects everything."""
import subprocess

from tools import test_impact as ti

SRC = '''import os
X = 1

class C:
    def m(self):
        return 1

    @staticmethod
    def s():
        def inner():
            return 2
        return inner

def f():
    return 3
'''


def test_changed_functions(tmp_path, monkeypatch):
    run = lambda *a: subprocess.run(["git", *a], cwd=tmp_path, check=True, capture_output=True)
    run("init", "-q"); run("config", "user.email", "t@t"); run("config", "user.name", "t")
    (tmp_path / "m.py").write_text(SRC); run("add", "."); run("commit", "-qm", "x")
    monkeypatch.setattr(ti, "_ROOT", tmp_path)

    def edit(old, new):
        (tmp_path / "m.py").write_text(SRC.replace(old, new))
        try:
            return ti.changed_functions("m.py")
        finally:
            run("checkout", "m.py")

    assert edit("return 1", "return 11") == {"C.m"}
    assert edit("return 2", "return 22") == {"C.s", "C.s.<locals>.inner"}
    assert edit("return 3", "return 33") == {"f"}
    assert edit("X = 1", "X = 2") is None                    # module level
    assert edit("import os", "import os, sys") is None
