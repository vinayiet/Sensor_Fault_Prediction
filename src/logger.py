# Logging is important for keep tracking the events that happen in the application
# also helps in loggin and debugging

import datetime 
import logging
import os
LOG_FILE = f'{datetime.datetime.now().strftime("%m_%d_%y_%H_%M_%S")}'

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO
)