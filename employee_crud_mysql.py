import pymysql
def connectDb():
    connection=None
    try:
        connection = pymysql.connect(
        host='localhost',
        user="root",
        password="ritin150",
        database="rk_db",
        port=3306,
        charset='utf8')
        print("Connected to MySQL database successfully")
    except:
        print("Failed to connect to MySQL database")
    return connection
def disconnectDB(connection):
    try:
        connection.close()
        print("Disconnected from MySQL database successfully")
    except:
        print("Failed to disconnect from MySQL database")
def create_db():
    query = "CREATE DATABASE IF NOT EXISTS rk_db"
    connection = connectDb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Database created successfully")
        cursor.close
        disconnectDB(connection)
    except Exception as e:
        print(f"Failed to create database: {e}")
        disconnectDB(connection)
connection=connectDb()


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        department VARCHAR(100) NOT NULL
    )
    """
    connection = connectDb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows= cursor.fetchall()
        print("Table created successfully")
        cursor.close()
        disconnectDB(connection)
    except Exception as e:
        print(f"Failed to create table: {e}")
        disconnectDB(connection)




def print_all_employees():
    query = "SELECT * FROM employees"
    connection = connectDb()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        disconnectDB(connection)
    except Exception as e:
        print(f"Failed to fetch employees: {e}")
        disconnectDB(connection)
def print_data_employees():
    a=int(input("Enter the number of employees to fetch: "))
    query = "SELECT * FROM employees WHERE id = %s"
    connection = connectDb()
    try:
        cursor = connection.cursor()
        cursor.execute(query, (a,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        disconnectDB(connection)
    except Exception as e:
        print(f"Failed to fetch employees: {e}")
        disconnectDB(connection)
create_db()
create_table()
print_all_employees()
print_data_employees()
