from models.admin_model import get_admin_by_email

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