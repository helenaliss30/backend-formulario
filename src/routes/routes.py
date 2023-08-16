# routes.py
from flask import Flask, Blueprint, request
from controllers.PersonaController import PersonaController
from controllers.UsuarioController import UsuarioController
import jwt  # Importa PyJWT para verificar el token
from functools import wraps

app = Flask(__name__)

# Crear un Blueprint para las rutas
routes = Blueprint("routes", __name__)

secret_key = "your-secret-key"


def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token:
            try:
                token_parts = token.split(" ")
                if len(token_parts) == 2 and token_parts[0] == "Bearer":
                    token = token_parts[1]
                else:
                    return {"message": "Token inválido"}, 401

                payload = jwt.decode(token, secret_key, algorithms=["HS256"])
                current_user = payload["email"]
                return f(current_user, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                return {
                    "message": "Su Sesión ya ha expirado, Vuelva a iniciar sesión"
                }, 401
            except jwt.InvalidTokenError:
                return {"message": "Token Inválido"}, 401
        else:
            return {"message": "No se ha iniciado sesión correctamente"}, 401

    return decorated


@routes.route("/personas/create", methods=["POST"])
@jwt_required
def create_user(current_user):
    persona_controller = PersonaController()

    id_persona, message, status_code, ok = persona_controller.postPersona(request.json)

    if status_code == 400:
        return {"message": message, "data": None, "ok": ok}, status_code
    if status_code == 201:
        return {"message": message, "data": str(id_persona), "ok": ok}, status_code
    else:
        return {"message": message, "data": None, "ok": ok}, status_code


@routes.route("/personas/list", methods=["GET"])
@jwt_required
def get_personas(current_user):
    persona_controller = PersonaController()

    personas_list, message, status_code, ok = persona_controller.getPersonas()

    return {"message": message, "data": personas_list, "ok": ok}, status_code


@routes.route("/personas/find/<persona_id>", methods=["GET"])
@jwt_required
def get_persona(current_user, persona_id):
    persona_controller = PersonaController()

    persona_data, message, status_code, ok = persona_controller.getPersona(persona_id)
    if status_code == 200:
        return {"message": message, "data": (persona_data), "ok": ok}, status_code
    return {"message": message, "data": None, ok: ok}, status_code


@routes.route("/personas/update/<persona_id>", methods=["PUT"])
@jwt_required
def update_persona(current_user, persona_id):
    persona_controller = PersonaController()
    _, message, status_code, ok = persona_controller.updatePersona(
        persona_id, request.json
    )
    return {"message": message, "data": (persona_id), "ok": ok}, status_code


@routes.route("/personas/delete/<persona_id>", methods=["DELETE"])
@jwt_required
def delete_persona(current_user, persona_id):
    persona_controller = PersonaController()
    _, message, status_code, ok = persona_controller.deletePersona(persona_id)
    return {"message": message, "data": (persona_id), "ok": ok}, status_code


@routes.errorhandler(404)
def not_found(error=None):
    return {"message": "Resource Not Found " + request.url, "status": 404, "ok": False}


@routes.route("/auth/register", methods=["POST"])
def register_user():
    usuario_controller = UsuarioController()
    data = request.json
    result, message, status_code, ok = usuario_controller.registerUsuario(data)
    return {"message": message, "data": result, "ok": ok}, status_code


@routes.route("/auth/login", methods=["POST"])
def login_user():
    usuario_controller = UsuarioController()
    data = request.json
    result, message, status_code, ok = usuario_controller.loginUsuario(data)
    return {"message": message, "data": result, "ok": ok}, status_code


@routes.route("/auth/renew-token", methods=["POST"])
@jwt_required
def renew_token(current_user):
    usuario_controller = (
        UsuarioController()
    )  # Obtiene la identidad del usuario del token
    result, message, status_code, ok = usuario_controller.renewTokenUsuario(
        current_user
    )
    return {"message": message, "data": result, "ok": ok}, status_code
