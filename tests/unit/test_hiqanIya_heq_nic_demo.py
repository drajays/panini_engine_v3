import sutras  # noqa: F401

from pipelines.hiqanIya_heq_nic_anIyar_demo import derive_hiqanIya


def test_hiqanIya_surface() -> None:
    s = derive_hiqanIya()
    assert s.flat_slp1() == "hiqanIya"


def test_guRa_blocked_after_Reraniwi() -> None:
    s = derive_hiqanIya()
    hit = any(e.get("sutra_id") == "7.3.86" and e.get("status") == "APPLIED" for e in s.trace)
    assert not hit
