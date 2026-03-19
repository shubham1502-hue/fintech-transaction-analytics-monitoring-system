import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Vegito9616",
    database="payments_analytics"
)

df = pd.read_sql("SELECT * FROM transactions", conn)
df.to_csv("transactions_clean.csv", index=False)