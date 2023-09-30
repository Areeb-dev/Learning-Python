import uuid
from sqlalchemy import text

def generate_id():
    return str(uuid.uuid4())


def run_query(db, query):
    with db as session:
        result = session.execute(text(query))
        print('result',result)
        rows = [row[0] for row in result.fetchall()]  
    return rows
