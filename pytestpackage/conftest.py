import pytest

#Function level
@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level tear down")

#Module level
@pytest.fixture(scope="module")
def ModulesetUp():
    print("Running module level setup")
    yield
    print("Running module level tear down")