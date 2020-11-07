import proxy_check.proxy_config
import sqlite3
from sqlite3 import Error

sep = ", "
val = "?, "
n = len(proxy_check.proxy_config.COLUMNS) - 1
qry = sep.join(proxy_check.proxy_config.COLUMNS)

db_results = []

def add_AP(database_file, new_ap):
    query = "INSERT INTO " + proxy_check.proxy_config.TABLE + " (" + qry + ") VALUES (" + val * n + "?);"
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query, list(new_ap))
    cursor.close()
    connection.commit()
    connection.close()

def get_all(database_file):
    query = (
        "SELECT * FROM " + proxy_check.proxy_config.TABLE + " ;"
    )
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    for i in results:
      db_results.append(i)

def get_name(database_file, ap):
    query = (
        "SELECT * FROM " + proxy_check.proxy_config.TABLE + " WHERE " + proxy_check.proxy_config.COLUMN + "='" + ap + "';"
    )
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    for i in results:
        print(i[0:4])


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    # create a database connection
    conn = create_connection(proxy_check.proxy_config.DATABASE)
    # create tables
    if conn is not None:
        # create projects table
        print("Creating Database")
        create_table(conn, proxy_check.proxy_config.CREATE_TABLE)
    else:
        print("Error! cannot create the database connection.")
