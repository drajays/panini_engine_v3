"""data/reference/kaumudi/order.json — the book order of the LSK and SK (numbers only), served by /api/kaumudi-order and used on /sutra/<id>."""
from webui.app import app, _kaumudi_nav


def test_lsk_numbers_match_ashtadhyayi_com():
    nav = _kaumudi_nav("6.1.77")                       # ashtadhyayi.com/sutraani/lsk15 is iko yaṇaci
    assert nav["lsk"]["n"] == 15 and nav["sk"]["n"] == 47
    assert nav["lsk"]["prev"] and nav["lsk"]["next"]
    assert _kaumudi_nav("1.3.3")["lsk"]["n"] == 1      # halantyam opens both books
    assert "lsk" not in _kaumudi_nav("8.4.68")         # a a is not in the LSK


def test_pages_and_api():
    c = app.test_client()
    o = c.get("/api/kaumudi-order").get_json()
    assert o["6.1.77"]["lsk"] == 15 and len({v["lsk"] for v in o.values() if "lsk" in v}) == sum("lsk" in v for v in o.values())
    h = c.get("/sutra/6.1.77").get_data(as_text=True)
    assert "लघुकौमुदी-15" in h and "सिद्धान्तकौमुदी-47" in h
    assert 's-view-bar' in c.get("/sutras").get_data(as_text=True)
