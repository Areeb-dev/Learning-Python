from flask import Flask, jsonify, request
from flask_cors import CORS
from helpers import generate_id, run_query, check_db_connect
from dotenv import load_dotenv
from config.database import engine, Base, SessionLocal

db = SessionLocal()

load_dotenv()

app = Flask(__name__)
CORS(app)


def startup_db():
    Base.metadata.create_all(bind=engine)


@app.route("/")
def index():
    return jsonify(
        {
            "success": True,
            "message": "Welcome To Flask APIs",
            "db": check_db_connect(db),
        }
    )


@app.route("/add-student", methods=["POST"])
def add_student():
    try:
        body = request.get_json()

        if "name" not in body or "email" not in body:
            return jsonify({"success": False, "error": "Both Fields are required"})

        name = body["name"]
        email = body["email"]
        id=generate_id()
      
        sql_query = f"INSERT INTO student (id, name, email) VALUES ('{id}', '{name}', '{email}')"

        run_query(db, sql_query)

        return jsonify(
            {
                "success": True,
                "message": "Data Added successfully",
            }
        )

    except Exception as e:
        print(f"Error {e}")
        return jsonify(
            {
                "success": False,
                "message": "Something Went Wrong Please Try Again",
                "error": str(e),
            }
        )


@app.route("/get-students", methods=["GET"])
def get_students():
    try:
        select_query = f"SELECT row_to_json(t) FROM (SELECT * FROM student)t"

        result = run_query(db, select_query)
        print("result", result)
        return jsonify(
            {
                "success": True,
                "data": result,
            }
        )

    except Exception as e:
        print(f"Error {e}")
        return jsonify(
            {
                "success": False,
                "message": "Something Went Wrong Please Try Again",
                "error": str(e),
            }
        )


if __name__ == "__main__":
    startup_db()
    app.run(debug=True)
