from flask import jsonify
from models.Register import Register
import db.database as database


class RegisterController:
    def __init__(self):
        self.db = database.dbConnection()

    def postPersona(self, data):
        registros = self.db["registro"]
        registro = Register(
            data["email"],
            data["password"],
           
        )
        personaCollection = registro.toDBCollection()
        id_persona = registros.insert_one(personaCollection)
        return id_persona.inserted_id, "Registro Exitoso", 201