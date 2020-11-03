import pytest

@pytest.fixture()
def setUp():
    print("case 3 setup")
    yield
    print("case 3 tear down")

def test_case3_methodA(setUp):
    print("Running case3 method A")

def test_case3_methodB(setUp):
    print("Running case3 method B")