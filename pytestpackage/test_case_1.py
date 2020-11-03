import pytest

@pytest.fixture()
def setUp():
    print("Una vez por metodo")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")