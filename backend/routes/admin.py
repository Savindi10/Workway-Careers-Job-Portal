from flask import Blueprint, request, jsonify
from services.admin_service import login_admin, create_job_service

admin_routes = Blueprint("admin", __name__, url_prefix="/admin")

@admin_routes.route("/login", methods=["POST"])
def admin_login():
    data = request.json
    response, status = login_admin(data["email"], data["password"])
    return jsonify(response), status 


@admin_routes.route("/jobs", methods=["POST"])
def add_job():
    data = request.json
    response, status = create_job_service(data)
    return jsonify(response), status

