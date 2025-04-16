import os
import unittest
# import the mock decorator
from unittest import mock

from main import FileWorker


class TestRmCase(unittest.TestCase):
    
    @mock.patch("main.os.path")  # mock_patch
    @mock.patch("main.os")  # mock_os
    def test_rm_failure(self, mock_os, mock_path):
        # Create the fileworker object
        fw = FileWorker()
        
        # Mocking to make the file non-existent
        mock_path.isfile.return_value = False
        
        # Trying to delete the non existent file
        fw.rm("any path")
        
        # Check to see if it doesn't the deletion
        self.assertFalse(mock_os.remove.called, "Failed to remove the file because it does not exist")

   
    @mock.patch("main.os.path")  # mock_patch
    @mock.patch("main.os")  # mock_os
    def test_rm_success(self, mock_os, mock_path):
        # Create the fileworker object
        fw = FileWorker()
        
        # Mocking to make the file exist
        mock_path.isfile.return_value = True
        
        # Trying to delete the existent file
        fw.rm("any path")
        
        # # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")
