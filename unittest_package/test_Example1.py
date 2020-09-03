import unittest

#unittest.Testcase
class TestCalculator(unittest.TestCase):
    a= int(input("enter a :"))
    b= int(input("enter b "))

    def test_add(self):
        print("\na+b = ",self.a+self.b)
        self.assertEqual(self.a,0,"a is not zero")

    def test_sub(self):
        print("\na-b = ",self.c-self.b)

    def test_mul(self):
        print("\na*b = ",self.a*self.b)

    def test_div(self):
        print("\na/b = ",self.a/self.b)

#print(__name__) #test_Example1.py  /__main__

# if __name__ == "__main__":
#     unittest.main()
