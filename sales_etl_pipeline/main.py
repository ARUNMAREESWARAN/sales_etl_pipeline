from etl.extract import extract
from etl.transform import transform
from etl.load import load
from etl.utils import load_config, setup_logging
import logging


def main():
    setup_logging()
    logging.info("Starting ETL process")

    config = load_config()

    try:
        df = extract(config['csv_path'])
        df = transform(df)
        load(df, config['user'], config['password'], config['host'], config['port'], config['database'])
        logging.info("ETL process completed successfully")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")


if __name__ == '__main__':
    main()
