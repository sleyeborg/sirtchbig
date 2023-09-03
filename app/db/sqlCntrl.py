import sqlite3


def controller(username, password):
    print('controller')
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    );
    """

    insert_query = """
        INSERT INTO users (username, password) VALUES (?, ?);
    """

    cursor.execute(create_table_query)

    # Example data for insertion
    user_data = [(username, password)]

    # Insert multiple rows
    cursor.executemany(insert_query, user_data)

    # Commit the changes to the database
    conn.commit()
    print('controlled')
    cursor.close()
    conn.close()
