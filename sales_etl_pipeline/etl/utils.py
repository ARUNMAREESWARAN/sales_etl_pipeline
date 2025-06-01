import logging
from dotenv import load_dotenv
import os

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler("etl.log"),
            logging.StreamHandler()
        ]
    )

def load_config():
    load_dotenv(dotenv_path='config/.env')
    config = {
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'host': os.getenv('MYSQL_HOST'),
        'port': int(os.getenv('MYSQL_PORT')),
        'database': os.getenv('MYSQL_DATABASE'),
        'csv_path': os.getenv('CSV_PATH')
    }
    return config
