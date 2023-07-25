# routes.py
from flask import Flask, Blueprint, request
from controllers.PersonaController import PersonaController

app = Flask(__name__)

# Crear un Blueprint para las rutas
routes = Blueprint("routes", __name__)


@routes.route("/personas", methods=["POST"])
def create_user():
    persona_controller = PersonaController()

    id_persona, message, status_code = persona_controller.postPersona(request.json)

    if status_code == 400:
        return {"message": message}, status_code
    if status_code == 201:
        return {"message": message, "id": str(id_persona)}, status_code
    else:
        return {"message": message}, status_code
