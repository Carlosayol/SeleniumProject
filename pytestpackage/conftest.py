import pytest

#Function level
@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level tear down")

#Module level
@pytest.fixture(scope="class")
def ModulesetUp(request, browser, osType):
    print("Running module level setup")
    if browser=="chrome":
        value = 10
        print("Running test on Chrome")
    else:
        value = 20
        print("Running test on FF")
    if request.cls is not None:
        request.cls.value = value

    yield value
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