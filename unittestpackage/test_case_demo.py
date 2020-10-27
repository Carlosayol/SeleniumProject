import unittest

class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print("Se corre una vez antes de cada test")

    def test_methodA(self):
        print("Metodo A")

    def test_methodB(self):
        print("Metodo B")

    def tearDown(self):
        print("Se corre una vez despues de cada test")

if __name__ == '__main__':
    unittest.main(verbosity=2)
