import HtmlTestRunner
import unittest
test_runner = HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\reports\\")

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

if __name__ =="__main__":
    unittest.main(testRunner=test_runner,verbosity=2)
