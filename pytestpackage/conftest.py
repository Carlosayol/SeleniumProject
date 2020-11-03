import pytest

@pytest.fixture()
def setUp():
    print("Running conftest setup")
    yield
    print("Running conftest tear down")

@pytest.fixture(scope="module")
def ModulesetUp():
    print("Running conftest setup for module")
    yield
    print("Running conftest tear down for module")