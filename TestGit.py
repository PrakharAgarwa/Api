import unittest

from Git import Hw04


class TestHw04(unittest.TestCase):
    def testusername(self):
        self.assertEqual(Hw04('??'),False)
    def testusername2(self):
        self.assertEqual(Hw04('WSS'),False)
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()