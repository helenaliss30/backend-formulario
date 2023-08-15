from flask import Flask
from routes.routes import routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)