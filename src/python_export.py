import pandas as pd
import mysql.connector
import os
from pathlib import Path

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database=os.getenv("MYSQL_DATABASE", "payments_analytics")
)

df = pd.read_sql("SELECT * FROM transactions", conn)
output_path = Path("data/processed/transactions_clean.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)
