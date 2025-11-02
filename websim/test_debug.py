import unittest
from unittest.mock import patch
from .debug import log_debug

class TestDebugLogging(unittest.TestCase):
    @patch('logging.getLogger')
    def test_log_debug(self, mock_logger):
        log_debug("test message")
        mock_logger.return_value.debug.assert_called_once_with("test message")
