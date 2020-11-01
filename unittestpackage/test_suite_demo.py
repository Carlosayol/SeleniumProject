import unittest
#from unittestpackage.test_class1 import TestClass1
#from unittestpackage.test_class2 import TestClass2
# Corre desde pycharm pero no desde terminal, revisar lectura 168
from test_class1 import TestClass1
from test_class2 import TestClass2

# Se obtienen todas las pruebas de las dos clases
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Se crea una test suite
suite_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(suite_test)