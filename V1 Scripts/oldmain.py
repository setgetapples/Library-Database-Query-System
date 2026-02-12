# learn what cursor does for pyodbc and any sql related library

import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=CS-16\SQLEXPRESS2025;"
    "DATABASE=Library Management Comp260;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM Account")




# get column names
rows = cursor.fetchall()
columns = [column[0] for column in cursor.description]

for row in rows:
    for column, value in zip(columns, row):
        print(f"{column}: {value}")
    print("-" * 40)
