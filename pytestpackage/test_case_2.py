import pytest

@pytest.fixture()
def setUp():
    print("Una vez antes por metodo")
    yield
    print("Una vez despues por metodo")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")