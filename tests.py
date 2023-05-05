import pytest 
import sqlite3

@pytest.fixture(scope="module")
def sqlite_db():
    # Connect to the database
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()

    # Create a table
    c.execute("""CREATE TABLE object_data
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  email TEXT)""")

    # Insert some data
    c.execute("INSERT INTO users VALUES (1, 'Alice', 'alice@example.com')")
    c.execute("INSERT INTO users VALUES (2, 'Bob', 'bob@example.com')")

    # Commit the changes
    conn.commit()

    # Yield the connection object so it can be used in tests
    yield conn

    # Close the connection
    conn.close()

def test_my_function(sqlite_db):
    # Use the connection object to run queries
    c = sqlite_db.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

    # Assert that the data is what we expect
    assert rows == [(1, 'Alice', 'alice@example.com'), (2, 'Bob', 'bob@example.com')]
