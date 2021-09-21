import unittest
from Examples import Example


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")

    def setUp(self):
        print("This will run after every method")

    def tearDown(self):
        print("This will after every method")

    # def test_add(self):
    #     result = Example.add(self, 30, 20)
    #     self.assertEqual(result, 50)
    #     # ------
    #     self.assertEqual(Example.add(self, 10, 20), 30)
    #     self.assertEqual(Example.add(self, 0, 0), 0)
    #     self.assertEqual(Example.add(self, -1, 1), 0)
    #
    # def test_sub(self):
    #     result = Example.sub(self, 50, 30)
    #     self.assertEqual(result, 20)

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()
