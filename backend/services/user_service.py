from flask import request
from models.user_model import get_user_by_email, create_user, get_all_jobs, get_job_by_id , insert_application
from pymysql.err import IntegrityError
from werkzeug.security import check_password_hash

# Used for safe login (supports old plain passwords + new hashed)
def verify_password(db_password, input_password):
    if db_password.startswith("pbkdf2:") or db_password.startswith("scrypt:"):
        return check_password_hash(db_password, input_password)

    return db_password == input_password


# User Registration
def register_user(name, email, password):
    existing_user = get_user_by_email(email)

    if existing_user:
        return {"error": "Email already exists"}, 400

    user_id = create_user(name, email, password)

    return {
        "message": "User registered successfully",
        "user_id": user_id,
        "name": name
    }, 201

    
# user login 
def login_user(email, password):
    user = get_user_by_email(email)

    if not user:
        return {"error": "User not found"}, 404
    
    if not verify_password(user["password"], password):
        return {"error": "Invalid password"}, 401

    
    return {
        "message": "Login successful",
        "user_id": user["user_id"],
        "name": user["name"]
    }, 200

# view all jobs 
def view_jobs_service():
    jobs = get_all_jobs()
    return {"jobs": jobs}, 200

# View job details (by ID specific job)
def view_job_details_service(job_id):
    job = get_job_by_id(job_id)
    if job:
        return {"job": job}, 200
    else:
        return {"error": "Job not found"}, 404

# Insert job application 
def apply_job_service(job_id,data):
    user_id = data.get("user_id")
    resume_url = data.get("resume_url")

    if not user_id  or not resume_url:
        return {"error": "Missing required fields"}, 400

    try:
     insert_application(
           user_id,
           job_id,
           resume_url
     )
    except IntegrityError:
        return {"error": "You have already applied for this job"}, 409
    
    return {"message": "Application submitted successfully"}, 201