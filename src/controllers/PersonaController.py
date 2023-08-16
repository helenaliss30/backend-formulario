from utils.validation import validation_persona
from models.Persona import Persona
import db.database as database
from bson.objectid import ObjectId


class PersonaController:
    def __init__(self):
        self.db = database.dbConnection()

    def postPersona(self, data):
        personas = self.db["personas"]
        validation_error = validation_persona(data)
        print(validation_error)
        if validation_error:
            return None, validation_error, 400, False
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
        return id_persona.inserted_id, "Persona Guardada Exitosamente", 201, True

    def getPersonas(self):
        personas = self.db["personas"]
        personas_list = []

        for persona_data in personas.find():
            persona = Persona(
                id=str(persona_data["_id"]),
                nombre=persona_data["nombre"],
                apellido=persona_data["apellido"],
                edad=persona_data["edad"],
                cedula=persona_data["cedula"],
                correo_electronico=persona_data["correo_electronico"],
                enfermedades=persona_data["enfermedades"],
                alergias=persona_data["alergias"],
                medicamentos=persona_data["medicamentos"],
            )
            personas_list.append(persona.toDBCollection())

        return personas_list, "Lista de personas obtenida exitosamente", 200, True

    def updatePersona(self, persona_id, data):
        personas = self.db["personas"]
        validation_error = validation_persona(data)
        if validation_error:
            return persona_id, validation_error, 400, False

        persona_data = personas.find_one({"_id": ObjectId(persona_id)})
        if not persona_data:
            return persona_id, "Persona no encontrada", 404, False

        updated_persona = Persona(
            nombre=data["nombre"],
            apellido=data["apellido"],
            edad=data["edad"],
            cedula=data["cedula"],
            correo_electronico=data["correo_electronico"],
            enfermedades=data["enfermedades"],
            alergias=data["alergias"],
            medicamentos=data["medicamentos"],
        )

        personas.update_one(
            {"_id": ObjectId(persona_id)}, {"$set": updated_persona.toDBCollection()}
        )
        return persona_id, "Persona actualizada exitosamente", 200, True

    def deletePersona(self, persona_id):
        personas = self.db["personas"]

        result = personas.delete_one({"_id": ObjectId(persona_id)})

        if result.deleted_count > 0:
            return persona_id, "Persona eliminada exitosamente", 200, True
        else:
            return persona_id, "Persona no encontrada", 404, False

    def getPersona(self, persona_id):
        personas = self.db["personas"]

        persona_data = personas.find_one({"_id": ObjectId(persona_id)})

        if persona_data:
            persona = Persona(
                id=str(persona_data["_id"]),
                nombre=persona_data["nombre"],
                apellido=persona_data["apellido"],
                edad=persona_data["edad"],
                cedula=persona_data["cedula"],
                correo_electronico=persona_data["correo_electronico"],
                enfermedades=persona_data["enfermedades"],
                alergias=persona_data["alergias"],
                medicamentos=persona_data["medicamentos"],
            )
            return persona.toDBCollection(), "Persona obtenida exitosamente", 200, True
        else:
            return persona_id, "Persona no encontrada", 404, False
