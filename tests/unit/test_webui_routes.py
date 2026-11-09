"""Web UI routes: every page renders, every old URL redirects, every menu/home link resolves.

/patha builds its form index on first request (~45 s), so its tab is checked by route only.
"""
from __future__ import annotations

import re
from urllib.parse import urlparse, parse_qs

import pytest

from webui.app import app, _TABS, _MOVED

PAGES = [
    "/", "/shabdarupa", "/dhaturupa", "/reader", "/sutras", "/sutra/1.1.1", "/sutra/6.1.87", "/yantrashala",
    "/prakriya", "/prakriya?kind=subanta&w=rAma", "/practice", "/learn", "/docs/data/index.json", "/docs/transliterate.js",
    "/pipelines", "/sig", "/tests",
] + [f"/{sec}?tab={k}" for sec, tabs in _TABS.items() for k, _l, fn in tabs[1:] if k != "patha"]

# Old URL -> where it must land (path, tab).
MOVED = {
    "/derive": ("/shabdarupa", "derive"), "/matrix": ("/shabdarupa", "matrix"), "/showcase": ("/shabdarupa", "showcase"),
    "/sarvanama": ("/shabdarupa", "sarvanama"), "/paradigm": ("/shabdarupa", "matrix"), "/special": ("/shabdarupa", "showcase"),
    "/shabda": ("/shabdarupa", None), "/lab": ("/shabdarupa", "derive"), "/krdanta": ("/dhaturupa", "krdanta"),
    "/bhatti": ("/reader", "bhatti"), "/patha": ("/reader", "patha"), "/text": ("/reader", "text"),
    "/devendra": ("/", None), "/dik": ("/", None),
    "/tinanta": ("/dhaturupa", None), "/tinanta/all": ("/dhaturupa", None), "/dhatufilters": ("/dhaturupa", None),
    "/prakriya/tinanta": ("/dhaturupa", None), "/dhatupatha": ("/dhaturupa", None),
    "/coverage": ("/yantrashala", None), "/review": ("/yantrashala", None),
}


@pytest.fixture(scope="module")
def client():
    return app.test_client()


@pytest.mark.parametrize("path", PAGES)
def test_page_renders(client, path):
    r = client.get(path)
    r.close()                       # static files are streamed
    assert r.status_code == 200


@pytest.mark.parametrize("old", sorted(MOVED))
def test_old_url_redirects(client, old):
    r = client.get(old + "?stem=rAma")
    assert r.status_code in (301, 302)
    u = urlparse(r.headers["Location"])
    want_path, want_tab = MOVED[old]
    assert u.path == want_path
    assert parse_qs(u.query).get("tab", [None])[0] == want_tab


def test_every_moved_url_is_tested():
    assert set(_MOVED) <= set(MOVED)


def test_tab_bar_and_student_menu(client):
    html = client.get("/shabdarupa?tab=matrix").get_data(as_text=True)
    assert 'class="tabbar"' in html and 'class="on"' in html
    menu = html.split("</header>")[0]
    for dev in ("/pipelines", "/sig", "/tests"):
        assert f'href="{dev}"' not in menu       # developer pages live under यन्त्रशाला only


def test_every_link_on_home_and_menu_resolves(client):
    html = client.get("/").get_data(as_text=True)
    links = {h.split("?")[0].split("#")[0] for h in re.findall(r'href="(/[^"]*)"', html)}
    adapter = app.url_map.bind("localhost")
    for path in sorted(links - {""}):
        if not path.startswith("/static/"):
            adapter.match(path)


def test_every_sutra_has_a_page(client):
    from webui.app import _sutras_json
    assert client.get("/sutra/3.2.1").status_code == 200          # may be a placeholder; still explorable
    assert client.get("/sutra/9.9.9").status_code == 404
    assert len(_sutras_json()) > 3900


def test_sutra_page_shows_status_and_examples(client):
    html = client.get("/sutra/6.1.87").get_data(as_text=True)
    assert "implemented" in html and "Kāśikā examples" in html


def test_menu_has_seven_sections(client):
    menu = client.get("/").get_data(as_text=True).split("</header>")[0]
    for href in ("/learn", "/practice", "/shabdarupa", "/prakriya", "/sutras", "/reader", "/yantrashala"):
        assert f'href="{href}"' in menu


def test_derivation_apis_feed_the_shared_view(client):
    r = client.post("/api/derive", json={"stem": "rAma", "vibhakti": 3, "vacana": 1, "linga": "pulliṅga"}).get_json()
    assert r["surface_slp1"] == "rAmeRa" and r["trace"][0]["sutra_id"]
    k = client.post("/api/krdanta", json={"dhatu_id": "BU", "krt_type": "tfc"}).get_json()
    assert k["surface_dev"] == "भविता"


def test_learn_page_is_offline_and_rewired(client):
    html = client.get("/learn").get_data(as_text=True)
    assert "googleapis" not in html and "/docs/data/index.json" in html


def test_no_external_hosts_in_pages(client):
    for p in ("/", "/prakriya", "/practice", "/learn", "/sutras"):
        assert not re.search(r'(?:src|href)="https?://(?!127\.0\.0\.1|localhost)', client.get(p).get_data(as_text=True)), p


TAB_PAGES = ["/shabdarupa", "/shabdarupa?tab=derive", "/shabdarupa?tab=matrix", "/shabdarupa?tab=showcase", "/shabdarupa?tab=sarvanama",
             "/dhaturupa", "/dhaturupa?tab=krdanta", "/reader", "/reader?tab=bhatti", "/reader?tab=text", "/pipelines"]


@pytest.mark.parametrize("path", TAB_PAGES)
def test_derivation_pages_use_the_shared_view(client, path):
    """Every page that shows a derivation loads prakriya.js and none keeps the retired renderer."""
    html = client.get(path).get_data(as_text=True)
    assert "prakriya.js" in html
    for dead in ("lipi.js", 'class="trace-filter"', 'id="sutra-detail"', "Lipi.", "engSteps"):
        assert dead not in html, dead


def test_retired_trace_js_is_a_shim(client):
    r = client.get("/static/trace.js"); js = r.get_data(as_text=True); r.close()
    assert "Prakriya.mount" in js and "renderStep" not in js
    r = client.get("/static/lipi.js"); r.close()
    assert r.status_code == 404


def test_bold_font_is_bundled(client):
    r = client.get("/static/fonts.css"); css = r.get_data(as_text=True); r.close()
    assert "Bold.woff" in css and "http" not in css
    r = client.get("/static/fonts/NotoSansDevanagari-Bold.woff"); r.close()
    assert r.status_code == 200


def test_letters_carry_origin_sutras(client):
    r = client.post("/api/tinanta", json={"dhatu": "BU", "lakara": "laT", "purusha": 3, "vacana": 1}).get_json()
    origins = {tuple(l["origin"]) for l in r["letters"]}
    assert ("6.1.78",) in origins and ("3.1.68",) in origins and ("3.4.78",) in origins
    assert "".join(l["slp1"] for l in r["letters"]) == r["surface_slp1"]


def test_what_if_disabler_is_display_only(client):
    from engine.state import State
    before = State.__init__
    r = client.post("/api/derive", json={"stem": "rAma", "vibhakti": 3, "vacana": 1, "disable": "7.1.12"}).get_json()
    assert r["surface_dev"] == "रामेण"                                    # the real derivation is untouched
    w = r["whatif"]
    assert w["disabled"] == ["7.1.12"] and w["surface_dev"] != r["surface_dev"]
    assert any(s["sutra_id"] == "7.1.12" and s["status"] == "BLOCKED" for s in w["trace"])
    assert State.__init__ is before                                         # patch undone
    again = client.post("/api/derive", json={"stem": "rAma", "vibhakti": 3, "vacana": 1}).get_json()
    assert again["surface_dev"] == "रामेण" and "whatif" not in again


@pytest.mark.parametrize("url,body", [
    ("/api/tinanta", {"dhatu": "BU", "lakara": "laT", "purusha": 3, "vacana": 1, "disable": ["7.3.84"]}),
    ("/api/krdanta", {"dhatu_id": "BU", "krt_type": "tfc", "disable": "7.3.84"}),
])
def test_what_if_on_every_derivation_api(client, url, body):
    r = client.post(url, json=body).get_json()
    assert r["whatif"]["surface_dev"] != r["surface_dev"] and r["letters"]


def test_lk_list_and_shared_view_features(client):
    assert "6.1.87" in client.get("/api/lk-sutras").get_json()
    r = client.get("/static/prakriya.js"); js = r.get_data(as_text=True); r.close()
    for feature in ("beginner", "kaumudi", "shastriya", "pk-letters", "pk-sid-in", "inspect"):
        assert feature in js
