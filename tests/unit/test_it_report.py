from __future__ import annotations

from tools.it_report import main


def test_it_report_names_each_it(capsys):
    assert main(["qukfY", "--krt", "Kac", "--sup", "jas"]) == 0
    out = capsys.readouterr().out
    assert "qvit" in out and "Yit" in out          # डुकृञ्: ḍvit (1.3.5), ñit (1.3.3)
    assert "Kit" in out and "cit" in out           # खच्: khit (1.3.8), cit (1.3.3)
    assert "jit" in out and "अस्" in out           # जस्: ज् it (1.3.7), स् kept (1.3.4)
