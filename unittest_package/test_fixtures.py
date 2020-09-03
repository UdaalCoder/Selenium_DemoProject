import unittest

def setUpModule():
    print("Set up module!!!!!!")

def tearDownModule():
    print("tear down module!!!!!!")

class TestFixEx(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n in setup class")

    @classmethod
    def tearDownClass(cls):
        print("\n in teardown class")

    def setUp(self):
        print("\nin setup")

    def tearDown(self):
        print("\nin teardown")

    def test_f1(self):
        print("\nin f1")

    def test_f2(self):
        print("\nin f2")

class TestCalculator(unittest.TestCase):
    a= int(input("enter a :"))
    b= int(input("enter b "))

    def test_add(self):
        print("\na+b = ",self.a+self.b)

    def test_sub(self):
        print("\na-b = ",self.a-self.b)

    def test_mul(self):
        print("\na*b = ",self.a*self.b)

    def test_div(self):
        print("\na/b = ",self.a/self.b)