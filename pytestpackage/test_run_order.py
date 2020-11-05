import pytest

#D A C B = Run order

@pytest.mark.run(order=2)
def test_order_methodA(ModulesetUp,setUp):
    print("Running method A")

@pytest.mark.run(order=4)
def test_order_methodB(ModulesetUp,setUp):
    print("Running method B")

@pytest.mark.run(order=3)
def test_order_methodC(ModulesetUp,setUp):
    print("Running method C")

@pytest.mark.run(order=1)
def test_order_methodD(ModulesetUp,setUp):
    print("Running method D")