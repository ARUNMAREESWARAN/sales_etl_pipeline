import pandas as pd
import logging

def extract(csv_path):
    try:
        df = pd.read_csv(csv_path)
        logging.info(f"Extracted {len(df)} rows from {csv_path}")
        return df
    except Exception as e:
        logging.error(f"Failed to extract data: {e}")
        raise
