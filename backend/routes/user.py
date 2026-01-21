from flask import Blueprint, request, jsonify
from services.user_service import login_user, view_jobs_service , view_job_details_service, apply_job_service

user_routes = Blueprint("user", __name__, url_prefix="/user")

# user login
@user_routes.route("/login", methods=["POST"])
def user_login():
    data = request.json

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email and password required"}), 400

    response, status = login_user(data["email"], data["password"])
    return jsonify(response), status


# get all jobs 
@user_routes.route("/jobs", methods=["GET"])
def view_jobs():
    return view_jobs_service()

# get job details by ID
@user_routes.route("/jobs/<int:job_id>", methods=["GET"])
def view_job_details(job_id):
    return view_job_details_service(job_id)

# apply for a job
@user_routes.route("/jobs/<int:job_id>/apply", methods=["POST"])
def apply_job(job_id):
    data = request.get_json()
    response,status = apply_job_service(job_id,data)
    return jsonify(response), status
   