# 🧾 Sales Data ETL Pipeline

This project is a simple ETL (Extract, Transform, Load) pipeline built with Python. It reads raw sales data from a CSV file, cleans and transforms it, and loads the results into a MySQL database. It includes configuration via `.env` files and logging for monitoring.

---

## 📦 Features

- ✅ Extracts data from CSV
- 🧹 Cleans and transforms data (null removal, formatting, calculated fields)
- 💾 Loads clean data into a MySQL table
- 🔧 Configuration through `.env` file
- 🪵 Logging for tracking success/failure

---

## 🧰 Tech Stack

- Python 3.8+
- Pandas
- MySQL
- SQLAlchemy
- dotenv
- Logging

---

## 📁 Project Structure

```
sales_etl_pipeline/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── utils.py
├── config/
│   └── .env
├── data/
│   └── raw_sales.csv
├── etl.log
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/sales_etl_pipeline.git
cd sales_etl_pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your `.env` file in `config/.env`:

```dotenv
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=sales_db
CSV_PATH=data/raw_sales.csv
```

### 4. Run the pipeline

```bash
python main.py
```

---

## 📊 Output Example

After running the pipeline, data is cleaned and inserted into a `sales` table in your MySQL database.

---

## 🚀 Future Improvements

- Add data validation
- Streamlit dashboard
- Load to cloud database (e.g., AWS RDS, BigQuery)
- Unit tests

---

## 👨‍💻 Author

- Arun Mareeswaran