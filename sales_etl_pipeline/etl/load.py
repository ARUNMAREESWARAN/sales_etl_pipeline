import logging
from sqlalchemy import create_engine, text


def create_schema_if_not_exists(engine):
    with engine.connect() as conn:
        conn.execute(text("""
                          CREATE TABLE IF NOT EXISTS sales
                          (
                              id INT AUTO_INCREMENT PRIMARY KEY,
                              customer_name VARCHAR(255) NOT NULL,
                              product_name VARCHAR(255),
                              quantity INT,
                              unit_price DECIMAL(10,2),
                              total_price DECIMAL(12,2),
                              sale_date DATE,
                              sale_month VARCHAR(7)
                          )
                          """))
        logging.info("Ensured sales table exists.")
def load(df, user, password, host, port, database):
    try:
        connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'
        engine = create_engine(connection_string)
        create_schema_if_not_exists(engine)
        # Replace table content with new data
        df.to_sql('sales', con=engine, if_exists='replace', index=False)
        logging.info(f"Loaded {len(df)} rows into MySQL table 'sales'")
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise
