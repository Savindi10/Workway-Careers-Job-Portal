from flask import Blueprint, request, jsonify
from services.admin_service import login_admin, create_job_service, get_all_jobs_service , update_job_service

admin_routes = Blueprint("admin", __name__, url_prefix="/admin")

@admin_routes.route("/login", methods=["POST"])
def admin_login():
    data = request.json
    response, status = login_admin(data["email"], data["password"])
    return jsonify(response), status 

# CREATE JOB ROUTE
@admin_routes.route("/jobs", methods=["POST"])
def add_job():
    data = request.json
    response, status = create_job_service(data)
    return jsonify(response), status


# READ JOBS ROUTE 
@admin_routes.route("/jobs", methods=["GET"])
def get_jobs():
    response, status = get_all_jobs_service()
    return jsonify(response), status
   
# UPDATE JOB ROUTE
@admin_routes.route("/jobs/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    admin_id = 1 # temp 
    response, status = update_job_service(job_id, admin_id)
    return jsonify(response), status