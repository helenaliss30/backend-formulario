# routes.py
from flask import Flask, Blueprint, request, jsonify
from controllers.PersonaController import PersonaController
from controllers.RegisterController import RegisterController
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app) 
# Crear un Blueprint para las rutas
routes = Blueprint("routes", __name__)
MONGO_URI = "mongodb://localhost:27017/mi_base_de_datos"
client = MongoClient(MONGO_URI)
db = client["mi_base_de_datos"]
usuarios_collection = db["registro"]

@routes.route("/personas", methods=["POST"])
def create_user():
    persona_controller = PersonaController()
    
    id_persona, message, status_code = persona_controller.postPersona(request.json)
    print(request.json)
    if status_code == 400:
        return jsonify({"message": message}), status_code
    if status_code == 201:
        return jsonify({"message": message, "id": str(id_persona)}), status_code
    else:
        return jsonify({"message": message}), status_code

@routes.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    usuario= usuarios_collection.find_one({"email": email})
    print(email)
    print(usuario)
    print(password)
    if usuario and usuario.get("password") == password:
        # Las credenciales son válidas, devuelve un mensaje de éxito
        response_data = {"message": "Inicio de sesión exitoso"}
        return jsonify(response_data), 200
    else:
        # Las credenciales son inválidas, devuelve un mensaje de error
        response_data = {"message": "Credenciales inválidas"}
        return jsonify(response_data), 401

@routes.route("/registro", methods=["POST"])
def register_user():
    register_controller = RegisterController()
    
    id_persona, message, status_code = register_controller.postPersona(request.json)
    print(request.json)
    if status_code == 400:
        return jsonify({"message": message}), status_code
    if status_code == 201:
        return jsonify({"message": message, "id": str(id_persona)}), status_code
    else:
        return jsonify({"message": message}), status_code
