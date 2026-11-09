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
