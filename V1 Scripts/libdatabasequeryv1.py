# learn what cursor does for pyodbc and any sql related library

import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=CS-16\\SQLEXPRESS2025;"
    "DATABASE=LibraryManagementComp260;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()

def view_available_books():
    print("Available Books")
    print("-------------------------------------\n")
    query = "SELECT * FROM Book;"
    return query

def search_book():
    print("Search A Book")
    print("-------------------------------------\n")
    name = input("Enter book name: ")
    query = "SELECT * FROM Book " + f"WHERE BookName LIKE '{name}%';"
    return query


# turn this into dictionary mapping instead

def menu_prompt():
    print("Library Database Query System\n")
    print("1. Search Book, 2. View available books, 3. Quit\n")

    userinput = input("Enter your choice: ")
    match userinput:
        case "1":
            print("-------------------------------------\n")
            run_query(search_book())
        case "2":
            print("-------------------------------------\n")
            run_query(view_available_books())
        case "3":
            print("-------------------------------------\n")
            quit()
        case _:
            print("-------------------------------------\n")
            print("Your input was invalid, try again.\n")
            print("-------------------------------------\n")
            return menu_prompt()

def run_query(query):
    cursor.execute(query) # search book returns query

    # get column names
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    for row in rows:
        for column, value in zip(columns, row):
            print(f"{column}: {value}")
        print("-" * 40)

    menu_prompt()

menu_prompt()