import pytest

def test_methodA(ModulesetUp,setUp):
    print("Running conftest 1 method A")

def test_methodB(ModulesetUp,setUp):
    print("Running conftest 1 method B")