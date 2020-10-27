import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("-"*20)
        print("Se corre una vez en cuanto se ejecute la clase")
        print("-" * 20)

    def setUp(self):
        print("Se corre una vez antes de cada test")

    def test_methodA(self):
        print("Metodo A")

    def test_methodB(self):
        print("Metodo B")

    def tearDown(self):
        print("Se corre una vez despues de cada test")

    @classmethod
    def tearDownClass(cls):
        print("-" * 20)
        print("Se corre una vez cuando se acaben las pruebas de la clase")
        print("-" * 20)

if __name__ == '__main__':
    unittest.main(verbosity=2)