from utils.validation import validation_persona

from flask import jsonify
from models.Persona import Persona
import db.database as database


class PersonaController:
    def __init__(self):
        self.db = database.dbConnection()

    def postPersona(self, data):
        personas = self.db["personas"]
        validation_error = validation_persona(data)
        print(validation_error)
        if validation_error:
            return None, validation_error, 400
        persona = Persona(
            data["nombre"],
            data["apellido"],
            data["edad"],
            data["cedula"],
            data["correo_electronico"],
            data["enfermedades"],
            data["alergias"],
            data["medicamentos"],
        )
        personaCollection = persona.toDBCollection()
        id_persona = personas.insert_one(personaCollection)
        print(personaCollection)
        return id_persona.inserted_id, "Persona Guardada Exitosamente", 201
