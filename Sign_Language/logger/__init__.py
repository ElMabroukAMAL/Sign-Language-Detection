# logger to track the code (if we got error or no) , debug the code

import logging
import os 
from datetime import datetime
from from_root import from_root

#when we run the code , it create a log file

#name of log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#location of log file : from_root is the root(main) directory of the project, 'log' is the name
log_path = os.path.join(from_root(), 'log', LOG_FILE)
os.makedirs(log_path, exist_ok=True)

lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=lOG_FILE_PATH,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)