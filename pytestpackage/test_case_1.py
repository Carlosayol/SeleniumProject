"""
comandos utiles:
py.test test_file.py -- corre los tests del archivo test_file
py.test filepath -- corre todos los tests dentro del filepath
py.test test_file.py::test_method -- solo corre el test_method dentro del test_file

-s para mostrar los prints
-v para verbose
"""

import pytest

@pytest.fixture()
def setUp():
    print("case 1 setup")

def test_methodA(setUp):
    print("Running case 1 method A")

def test_methodB(setUp):
    print("Running case 1 method B")