# Logs folder is created by this

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs will be created in cwd
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# above two lines will create whole path of folder and file
os.makedirs(logs_path,exist_ok=True)

# we make this for logging config filename so that our log will go in that file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,

)



