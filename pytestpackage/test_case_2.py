import pytest

@pytest.fixture()
def setUp():
    print("case 2 setup")
    yield
    print("case 2 tear down")

def test_methodA(setUp):
    print("Running case 2 method A")

def test_methodB(setUp):
    print("Running case 2 method B")