import uuid
from sqlalchemy import text

def generate_id():
    return str(uuid.uuid4())


def run_query(db, query):
    query_type = query.split(" ")[0].upper()
    if query_type == "INSERT" or query_type == "UPDATE":
        with db as session:
            session.execute(text(query))
            session.commit()
    else:
        with db as session:
            result = session.execute(text(query))
            rows = [row[0] for row in result.fetchall()]
        return rows


def check_db_connect(db):
    try:
        with db as connection:
            connection.execute(text("SELECT 1"))
        print("Database is connected!")
    except Exception as e:
        print("Failed to connect to the database.", str(e))