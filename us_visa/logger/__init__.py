import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)

LOG_FORMAT = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"

# File handler — saves logs to file
file_handler = logging.FileHandler(logs_path)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Console handler — prints logs to terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[file_handler, console_handler],
)