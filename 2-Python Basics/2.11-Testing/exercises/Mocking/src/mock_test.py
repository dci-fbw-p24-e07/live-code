from app import rm

import mock
import unittest

class RmTestCase(unittest.TestCase):
    # Task2
    @mock.patch('app.os.path')
    @mock.patch('app.os')
    def test_rm1(self, mock_os, mock_path):
        # set up the mock set file is exist
        mock_path.isfile.return_value = True
        rm("somefile1.txt")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("somefile1.txt")
    
    # Task3
    @mock.patch('app.os.path')
    @mock.patch('app.os')
    def test_rm2(self, mock_os, mock_path):
        # set up the mock set file is not exist
        mock_path.isfile.return_value = False
        rm('somefile1')
        # test that rm called os.remove with the right parameters
        self.assertFalse(mock_os.remove.called)
    
    # Task5
    @mock.patch('app.os.path')
    @mock.patch('app.os')
    def test_rm2(self, mock_os, mock_path):
        # set up the mock set file is not exist
        mock_path.isfile.return_value = False
        
        # test that rm will rise FileNotFoundError if the file not exist
        with self.assertRaises(FileNotFoundError):
            rm('somefile1')

if __name__ == '__main__':
    unittest.main()