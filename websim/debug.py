import logging

# Enable debug logs for WebSim
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def log_debug(message):
    logger.debug(f"[WebSim Debug] {message}")
