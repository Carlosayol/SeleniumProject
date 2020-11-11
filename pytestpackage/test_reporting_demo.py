import pytest
from pytestpackage.class_to_test import ClassDemoTest

@pytest.mark.usefixtures("ModulesetUp","setUp")
class TestReportingDemo():

    #Esto crea el fixture y hace que todos los metodos test lo usen como fixture
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = ClassDemoTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2,8)
        assert result == 10
        print("Running class method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(2,8)
        assert result > 10
        print("Running class method B")