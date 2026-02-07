from flask import Flask
from routes.admin import admin_routes
from routes.user import user_routes
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, resources={r"/user/*": {"origins": "*"}})
'''CORS(app, resources={
    r"/user/*": {"origins": "*"},
    r"/admin/*": {"origins": "*"}
})'''

CORS(app, origins="http://localhost:3000")
app.register_blueprint(admin_routes)
app.register_blueprint(user_routes)

@app.route("/")
def home():
    return {"status": "Backend running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
