
import pytest
import ofjustpy as oj
import sys
from addict import Dict
import webapp_main

app = oj.load_app()

links = [
     "/",
    "/demo_basic_capabilities",
    "/demo_advanced_capabilities",
    "/demo_markdown_formatting",
    "/demo_pycode_formatting",
    "/examples/index",
    "/examples/static_webpages/example_001",
    "/examples/static_webpages/example_002",
    "/examples/static_webpages/example_003",
    "/examples/static_webpages/example_004",
    "/examples/static_webpages/example_005",
    "/examples/static_webpages/example_006",
    "/examples/static_webpages/example_007",
    "/examples/input_webpages/example_001",
    "/examples/input_webpages/example_002",
    "/examples/input_webpages/example_003",
    "/examples/input_webpages/example_004",
    
    "/examples/mutable_webpages/example_001",
    "/examples/mutable_webpages/example_002",
    "/examples/mutable_webpages/example_003",
    "/examples/mutable_webpages/example_004",
    "/examples/mutable_webpages/example_005",
    "/examples/mutable_webpages/example_006",
    "/examples/mutable_webpages/example_007",
    "/examples/mutable_webpages/example_008"

    
]

from starlette.testclient import TestClient

@pytest.fixture
def testclient():
    client = TestClient(app)
    return client


@pytest.fixture(name="website_link", params=links)
def _website_link(request):
    return request.param

def test_td(website_link, testclient):
    response = testclient.get(website_link)
    assert response.status_code == 200

