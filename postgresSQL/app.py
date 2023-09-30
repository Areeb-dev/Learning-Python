from flask import Flask, jsonify, request
from flask_cors import CORS
from helpers import generate_id, run_query,check_db_connect
from dotenv import load_dotenv
from config.database import engine, Base, SessionLocal
from config.models import Student

db = SessionLocal()

load_dotenv()

app = Flask(__name__)
CORS(app)


def startup_db():
    Base.metadata.create_all(bind=engine)


@app.route("/")
def index():
    return jsonify({"success": True, "message": "Welcome To Flask APIs"})


@app.route("/add-student", methods=["POST"])
def add_student():
    try:
        body = request.get_json()

        if "name" not in body or "email" not in body:
            return jsonify({"success": False, "error": "Both Fields are required"})
        
        name = body["name"]
        email = body["email"]

        new_user = Student(id=generate_id(),name=name, email=email)
        db.add(new_user)
        db.commit()

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
        print('result',result)
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
    check_db_connect(engine)
    app.run(debug=True)
