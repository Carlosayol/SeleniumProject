import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a,"a no es true")
        b = False
        self.assertFalse(b,"b es true")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a,b,msg="a no es igual a b")

if __name__ == '__main__':
    unittest.main(verbosity=2)