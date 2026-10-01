from pipelines.subanta import derive

ETAD = [["एषः", "एतौ", "एते"], ["एतम्", "एतौ", "एतान्"], ["एतेन", "एताभ्याम्", "एतैः"], ["एतस्मै", "एताभ्याम्", "एतेभ्यः"],
        ["एतस्मात्", "एताभ्याम्", "एतेभ्यः"], ["एतस्य", "एतयोः", "एतेषाम्"], ["एतस्मिन्", "एतयोः", "एतेषु"]]
KIM = [["कः", "कौ", "के"], ["कम्", "कौ", "कान्"], ["केन", "काभ्याम्", "कैः"], ["कस्मै", "काभ्याम्", "केभ्यः"],
       ["कस्मात्", "काभ्याम्", "केभ्यः"], ["कस्य", "कयोः", "केषाम्"], ["कस्मिन्", "कयोः", "केषु"]]


def _grid(stem):
    return [[derive(stem, v, n).flat_dev() for n in (1, 2, 3)] for v in range(1, 8)]


def test_etad_pulliṅga_21_cells():  # 7.2.106 t→s (एषः), 7.2.113 is idam-only
    assert _grid("etad") == ETAD


def test_kim_pulliṅga_21_cells():  # 7.2.103 किमः कः is the apavāda of 7.2.102
    assert _grid("kim") == KIM


def test_kim_neuter_singular_keeps_stem():  # su/am luk'd (7.1.23) → no vibhakti for 7.2.102/103
    assert [derive("kim", v, 1, linga="napuṃsaka").flat_dev() for v in (1, 2)] == ["किम्", "किम्"]
