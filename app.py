# app.py
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv() 

# Now import other modules
import get
import datetime
import logging
import time
import os

# === LOGGING SETUP === 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
formatter = logging.Formatter(
   "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# === TIMEZONE SETUP ===
os.environ['TZ'] = 'US/Pacific'
time.tzset()

def main():
    # Use the logger configured above, not logging.basicConfig 
    start_time = datetime.datetime.now()
    logger.info(f'Started at {start_time}')
    
    get.get()
    
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    logger.info(f'Finished at {end_time}. Elapsed time: {elapsed_time}')

if __name__ == '__main__':
    main()
