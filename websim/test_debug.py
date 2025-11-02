import unittest
from unittest.mock import patch
from .debug import log_debug

class TestDebugLogging(unittest.TestCase):
    @patch('logging.getLogger')
    def test_log_debug(self, mock_logger):
        log_debug("test message")
        mock_logger().debug.assert_called_with("[WebSim Debug] test message")

if __name__ == '__main__':
    unittest.main()
