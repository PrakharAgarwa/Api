import unittest
from unittest.mock import patch, MagicMock

from Git import Hw04


class TestHw04(unittest.TestCase):
    @patch('Git.Hw04')
    def testusername(self,A):
        self.assertEqual(Hw04('1wdwaw'),False)
    @patch('Git.requests')
    def testusername2(self,B):
        mock_response= MagicMock()
        mock_response.status_code !=200
        mock_response.json.return_value="No Account Found"
        B.get.return_value=mock_response
        self.assertEqual(Hw04('ABSaS'),False)
    @patch('Git.Hw04')
    def testusername3(self,C):
        self.assertEqual(Hw04('PrakharAgarwa'),True)
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
