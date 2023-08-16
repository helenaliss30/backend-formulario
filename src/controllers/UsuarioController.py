from utils.validation import validation_user

from flask import jsonify
from models.Usuario import Usuario
import db.database as database
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
import jwt
import datetime

secret_key = "your-secret-key"


class UsuarioController:
    def __init__(self):
        self.db = database.dbConnection()

    def registerUsuario(self, data):
        usuarios = self.db["usuarios"]
        validation_error = validation_user(data)
        if validation_error:
            return None, validation_error, 400, False
        password = data["contrasenia"]
        hashed_password = pbkdf2_sha256.hash(password)
        usuario = Usuario(data["correo_electronico"], hashed_password)
        usuarioCollection = usuario.toDBCollection()

        id_usuario = usuarios.insert_one(usuarioCollection)
        print(usuarioCollection)
        payload = {
            "email": usuarioCollection["correo_electronico"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }
        access_token = jwt.encode(payload, secret_key, algorithm="HS256")
        print("HOlaaaaa")
        return (
            {"id": str(id_usuario.inserted_id), "access_token": access_token},
            "Usuario Registrado Exitosamente",
            201,
            True,
        )

    def loginUsuario(self, data):
        usuarios = self.db["usuarios"]
        usuario_data = usuarios.find_one(
            {"correo_electronico": data["correo_electronico"]}
        )
        if usuario_data and pbkdf2_sha256.verify(
            data["contrasenia"], usuario_data["contrasenia"]
        ):
            payload = {
                "email": usuario_data["correo_electronico"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            }
            access_token = jwt.encode(payload, secret_key, algorithm="HS256")
            return (
                {
                    "email": usuario_data["correo_electronico"],
                    "access_token": access_token,
                },
                "Inicio de sesión exitoso",
                200,
                True,
            )
        return None, "Credenciales inválidas", 401, False

    def renewTokenUsuario(self, data):
        payload = {
            "email": data,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }
        new_access_token = jwt.encode(payload, secret_key, algorithm="HS256")
        return (
            {"access_token": new_access_token},
            "Sesión renovada exitosamente",
            200,
            True,
        )
