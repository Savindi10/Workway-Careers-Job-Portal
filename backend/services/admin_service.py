from models.admin_model import get_admin_by_email, create_job

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