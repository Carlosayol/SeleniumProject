import unittest

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("-" * 20)
        print("Class 2 -> class level setUp")
        print("-" * 20)

    def setUp(self):
        print("Class 2 -> setUp")

    def test_methodA(self):
        print("Class 2 -> metodo A")

    def test_methodB(self):
        print("Class 2 -> metodo B")

    def tearDown(self):
        print("Class 2 -> class level tearDown")

    @classmethod
    def tearDownClass(cls):
        print("-" * 20)
        print("Se corre una vez cuando se acaben las pruebas de la clase")
        print("-" * 20)


if __name__ == '__main__':
    unittest.main(verbosity=2)