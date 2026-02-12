# learn what cursor does for pyodbc and any sql related library

import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=CS-16\\SQLEXPRESS2025;"
    "DATABASE=LibraryManagementComp260;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

def search_book(name: str):
    query_fstring = "SELECT * FROM Book " + f"WHERE BookName LIKE '{name}%';"
    return query_fstring


userinput = input("Enter a book name you want to see more details of: ")

cursor.execute(search_book(userinput)) # search book returns query

# get column names
rows = cursor.fetchall()
columns = [column[0] for column in cursor.description]

for row in rows:
    for column, value in zip(columns, row):
        print(f"{column}: {value}")
    print("-" * 40)
