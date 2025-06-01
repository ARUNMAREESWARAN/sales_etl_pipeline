import logging
import pandas as pd


def transform(df):
    try:
        original_len = len(df)

        # Drop rows with nulls in important columns
        df = df.dropna(subset=['customer_name', 'quantity', 'unit_price'])

        # Normalize customer names
        df['customer_name'] = df['customer_name'].str.title().str.strip()

        # Calculate total price
        df['total_price'] = df['quantity'] * df['unit_price']

        # Create sale_month if sale_date present
        if 'sale_date' in df.columns:
            df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')
            df = df.dropna(subset=['sale_date'])
            df['sale_month'] = df['sale_date'].dt.to_period('M').astype(str)

        logging.info(f"Transformed data from {original_len} to {len(df)} rows")
        return df
    except Exception as e:
        logging.error(f"Failed to transform data: {e}")
        raise
