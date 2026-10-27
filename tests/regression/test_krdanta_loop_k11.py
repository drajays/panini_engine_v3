"""K11 — the bhāve kṛts and their apavādas (3.3.18 ghañ, 3.3.57 ap, 3.3.90 naṅ, 3.3.94 ktin, 3.3.115 lyuṭ, 3.3.126 khal ; gender is the vivakṣā of
striyām / napuṃsake / puṃsi). Para sūtras that are apavādas take the site from ghañ; a later apavāda (3.3.103) from ktin."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

B = dict(artha="BAva")
CASES = [   # (dhātu id, upapada, linga, vivakṣā, form that must be one of the readings)
    ("01.0381", None, "pulliṅga", B, "pAWaH"),            # ghañ: पाठः (3.3.18)
    ("01.0001", None, "pulliṅga", B, "BavaH"),            # ap: u-final (3.3.57)
    ("01.1124", None, "pulliṅga", B, "taraH"),            # ap: ṛ-final
    ("01.1157", None, "pulliṅga", B, "yajYaH"),           # naṅ: यज्ञः (3.3.90), no vṛddhi (ṅit)
    ("01.0381", None, "strīliṅga", B, "paWitiH"),         # ktin: striyām (3.3.94), apavāda of ghañ
    ("01.0001", None, "strīliṅga", B, "BUtiH"),           # ktin beats ap
    ("08.0010", None, "strīliṅga", B, "kftiH"),           # कृतिः
    ("01.0381", None, "napuṃsaka", B, "paWanam"),         # lyuṭ: napuṃsake bhāve (3.3.115)
    ("08.0010", ("su", "karman"), "pulliṅga", {}, "sukaraH"),       # khal 3.3.126 (no mum: su is an avyaya, 6.3.67)
    ("08.0010", ("dus", "karman"), "pulliṅga", {}, "duskaraH"),
]


@pytest.mark.parametrize("ref,up,linga,kw,want", CASES, ids=lambda c: None)
def test_bhave_krdanta(ref, up, linga, kw, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, linga, upapada=up, **kw))}
    assert want in got, sorted(got)


def test_gender_is_a_vivaksha_not_a_leftover():
    """The same dhātu and meaning: pulliṅga takes ghañ, strīliṅga ktin — and neither leaks into the other."""
    pul = {b.surface_slp1 for b in explore(lambda: derive_krdanta("01.0381", 1, 1, "pulliṅga", **B))}
    stri = {b.surface_slp1 for b in explore(lambda: derive_krdanta("01.0381", 1, 1, "strīliṅga", **B))}
    assert "paWitiH" not in pul and "pAWA" not in stri, (sorted(pul), sorted(stri))
