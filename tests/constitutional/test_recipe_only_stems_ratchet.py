"""The (stem, liṅga) pairs still on the recipe path (rules missing) may only shrink."""
from pipelines.subanta import _RECIPE_ONLY

CEILING = 7  # 2026-10-03: idam*, tad/yad/etad/tyad/kim strī, kim napuṃsaka


def test_recipe_only_pairs_never_grow():
    assert len(_RECIPE_ONLY) <= CEILING, sorted(_RECIPE_ONLY)
