from models.admin_model import get_admin_by_email, create_job, get_all_jobs , update_job
from flask import request

def login_admin(email,password):
    admin = get_admin_by_email(email)

    if  not admin:
        return {"error": "admin not found"}, 404
    
    if admin["password"] != password:
        return {"error": "Invalid password"}, 401
    
    return{
        "message": "Login successful",
        "admin_id" : admin["user_id"],
        "name" : admin["name"]
    }, 200

def create_job_service(data):
    title = data.get("title")
    description = data.get("description")
    location = data.get("location")
    company_name = data.get("company_name")
    job_type = data.get("job_type")
    closing_date = data.get("closing_date")
    admin_id = data.get("admin_id")

    if not title or not company_name or not job_type or not admin_id:
        return {"error": "Missing required fields"}, 400 
    
    if job_type not in ["full-time", "part-time"]:
        return {"error": "Invalid job type"}, 400

    create_job(
        title,
        description,
        location,
        company_name,
        job_type,
        closing_date,
        admin_id)
    
    return {"message" : "Job created successfully"}, 201

# create for get jobs service 
def get_all_jobs_service():
    jobs = get_all_jobs()
    return {
        "jobs": jobs
    },200

# Update the job service 
def update_job_service(job_id, admin_id):
    data = request.get_json()

    updated_rows = update_job(
        job_id = job_id,
        title = data["title"],
        description = data["description"],
        location = data["location"],
        company_name = data["company_name"],
        job_type = data["job_type"],
        closing_date = data["closing_date"],
        admin_id = admin_id
    )
    if updated_rows == 0:
        return {"error": "Job not found or no changes made"}, 404
    
    return {"message": "Job updated successfully"}, 200

