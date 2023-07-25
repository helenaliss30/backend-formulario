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
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        self.correo_electronico = correo_electronico
        self.enfermedades = enfermedades
        self.alergias = alergias
        self.medicamentos = medicamentos

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
        }
