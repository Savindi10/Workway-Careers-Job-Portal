from flask import Flask
from routes.admin import admin_routes
from routes.user import user_routes

app = Flask(__name__)

app.register_blueprint(admin_routes)
app.register_blueprint(user_routes)

@app.route("/")
def home():
    return {"status": "Backend running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
