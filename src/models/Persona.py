class Persona:
    def __init__(
        self,
        id=None,  # Agregar _id como parámetro opcional con valor predeterminado None
        nombre=None,
        apellido=None,
        edad=None,
        cedula=None,
        correo_electronico=None,
        enfermedades=None,
        alergias=None,
        medicamentos=None,
    ):
        self.id = id  # Asignar el valor de _id al atributo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        self.correo_electronico = correo_electronico
        self.enfermedades = enfermedades
        self.alergias = alergias
        self.medicamentos = medicamentos

    def toDBCollection(self):
        data = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "cedula": self.cedula,
            "correo_electronico": self.correo_electronico,
            "enfermedades": self.enfermedades,
            "alergias": self.alergias,
            "medicamentos": self.medicamentos,
        }
        if self.id:
            data["id"] = self.id
        return data
