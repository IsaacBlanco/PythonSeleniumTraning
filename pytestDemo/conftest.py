import pytest


@pytest.fixture(scope="class")
def setup():
    print("This will execute fisrt beofre test")
    yield
    print("this will execute last after test")


@pytest.fixture()
def dataLoad():
    print("user profile is being created")
    return ["Valac", "Shiro", "SValac@shiro.com"]


@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def crossBrowser(request):
    return request.param


@pytest.fixture(params=[("Chrome","Shiro", "pws123"), ("Firefox", "Valac", "123pwd"), ("Edge", "Elfo", "Dongo")])
def crossBrowserMultiple(request):
    return request.param
