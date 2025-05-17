import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def log_info(msg):
    logging.info(msg)

def log_warn(msg):
    logging.warning(msg)

def log_error(msg):
    logging.error(msg)
