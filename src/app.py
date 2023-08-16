from flask import Flask
from routes.routes import routes
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.register_blueprint(routes, url_prefix="/api/v1")


if __name__ == "__main__":
    app.run(debug=True)
