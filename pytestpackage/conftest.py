import pytest

#Function level
@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level tear down")

#Module level
@pytest.fixture(scope="module")
def ModulesetUp(browser, osType):
    print("Running module level setup")
    if browser=="chrome":
        print("Running test on Chrome")
    else:
        print("Running test on FF")
    yield
    print("Running module level tear down")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")