import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def check_table_exists(conn, table):
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
    cursor = conn.execute(query)
    data = cursor.fetchall()
    if len(data) > 0:
        return True
    else:
        return False

def create_table(conn, table, query):
    if check_table_exists(conn, 'People'):
        print(f'{table} Table created')
    else:
        print(f'ERROR: {table} table was not created')

def get_all_records(conn, table):
    query = f'SELECT * FROM {table}'
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

def create_record(conn, table, data):
    query = f'INSERT INTO "{table}" ("FirstName", "Surname") VALUE (?,?);'
    cur = conn.cursor()
    cur.execute(query, data)
    conn.commit()
    return cur.lastrowid

def main():
    database = 'test.db'

    conn = create_connection(database)

    with conn:
        if not check_table_exists(conn, 'People'):
            query = """CREATE TABLE "People" (
	                "id"	INTEGER NOT NULL UNIQUE,
	                "firstName"	TEXT NOT NULL,
	                "surName"	TEXT NOT NULL,
	                "age"	INTEGER NOT NULL,
	                PRIMARY KEY("id" AUTOINCREMENT)
                    """
            create_table(conn, 'People', query)
        else:
            print('People table does not exist')


if __name__=='__main__':
    main()