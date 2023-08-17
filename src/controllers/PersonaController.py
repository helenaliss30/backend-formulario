from utils.validation import validation_persona

from flask import jsonify
from models.Persona import Persona
import db.database as database
import cloudinary
import cloudinary.uploader
import cloudinary.api


class PersonaController:
    def __init__(self):
        self.db = database.dbConnection()

    
    def postPersona(self, data):
        cloudinary.config(
            cloud_name="dmhajzmnv",
            api_key="742899162884941",
            api_secret="twesgKRPJA58mehL7ijuLH-WGys",
        )

       

        personas = self.db["personas"]
        validation_error = validation_persona(data)
        if validation_error:
            return None, validation_error, 400
        print(validation_error)
        # Configuración de la carpeta y el nombre personalizado
        folder_name = "imagenes_personas"  # Nombre de la carpeta en Cloudinary
        image_name = f"{data['cedula']}_qr_image"  # Nombre personalizado de la imagen

        # Opciones de carga con la carpeta y el nombre personalizado
        options = {
            "folder": folder_name,
            "public_id": image_name,
            "overwrite": True  # Si deseas sobrescribir si la imagen ya existe con el mismo nombre
        }

        resultado_subida = cloudinary.uploader.upload(data['qr_image'], **options)
        persona = Persona(
            data["nombre"],
            data["apellido"],
            data["edad"],
            data["cedula"],
            data["correo_electronico"],
            data["enfermedades"],
            data["alergias"],
            data["medicamentos"],
            resultado_subida["secure_url"]
        )
        personaCollection = persona.toDBCollection()
        id_persona = personas.insert_one(personaCollection)
        return id_persona.inserted_id, "Persona Guardada Exitosamente", 201
