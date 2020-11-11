import pytest
from pytestpackage.class_to_test import ClassDemoTest

@pytest.mark.usefixtures("ModulesetUp","setUp")
class TestClassDemo():

    #Esto crea el fixture y hace que todos los metodos test lo usen como fixture
    @pytest.fixture(autouse=True)
    def classSetup(self, ModulesetUp):
        self.abc = ClassDemoTest(self.value)

    def test_methodA(self):
        result = self.abc.sumNumbers(2,8)
        assert result == 20
        print("Running class method A")

    def test_methodB(self):
        print("Running class method B")