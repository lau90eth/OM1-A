import unittest
from unittest.mock import patch
import logging


# Simuliamo il modulo debug direttamente qui (perché non esiste)
def log_debug(message):
    logger = logging.getLogger(__name__)
    logger.debug(f"[WebSim-Debug] {message}")


class TestDebugLogging(unittest.TestCase):
    @patch("logging.getLogger")
    def test_log_debug(self, mock_logger):
        log_debug("test message")
        mock_logger.return_value.debug.assert_called_once_with("[WebSim-Debug] test message")
