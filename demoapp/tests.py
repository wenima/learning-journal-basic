import pytest
from pyramid import testing

@pytest.fixture
def testapp():
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)

@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request

def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import home_page
    response = home_page(req)
    assert response.startswith("<h1")

def test_home_page_has_iterable(req):
    from .views import home_page
    reponse = home_page(req)
    assert hasattr(response["entries"], "__iter__")

def test_home_page_has_list(testapp):
    response = testapp.get("/", status = 200)
    inner_html = response.html
