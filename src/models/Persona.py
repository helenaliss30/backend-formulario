class Persona:
    def __init__(
        self,
        nombre,
        apellido,
        edad,
        cedula,
        correo_electronico,
        enfermedades,
        alergias,
        medicamentos,
        qr_url,  # Nuevo campo qr_url
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        self.correo_electronico = correo_electronico
        self.enfermedades = enfermedades
        self.alergias = alergias
        self.medicamentos = medicamentos,
        self.qr_url = qr_url  # Asignación del nuevo campo qr_url


    def toDBCollection(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "cedula": self.cedula,
            "correo_electronico": self.correo_electronico,
            "enfermedades": self.enfermedades,
            "alergias": self.alergias,
            "medicamentos": self.medicamentos,
            "qr_url": self.qr_url,  # Inclusión del nuevo campo qr_url en el diccionario

        }
