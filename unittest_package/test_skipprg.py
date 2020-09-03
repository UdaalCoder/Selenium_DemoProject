import  unittest

class TestSkip(unittest.TestCase):
    a = int(input("enter a :"))
    b = int(input("enter b "))

    @unittest.skip("just skipping")
    def test_add(self):
        print("\na+b = ", self.a + self.b)
        self.assertEqual(self.a, 0, "a is not zero")

    @unittest.expectedFailure
    def test_sub(self):
        print("\na-b = ", self.c - self.b)

    @unittest.skipIf(a == b, "a is equal to b")  # true --> skip,false --> execute
    def test_mul(self):
        print("\na*b = ", self.a * self.b)

    @unittest.skipUnless(b!=0,"b is not zero")# true --> execute , false --> skip
    def test_div(self):
        print("\na/b = ", self.a / self.b)

