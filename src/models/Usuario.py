class Usuario:
    def __init__(
        self,
        correo_electronico,
        contrasenia,
    ):
        self.correo_electronico = correo_electronico
        self.contrasenia = contrasenia

    def toDBCollection(self):
        return {
            "correo_electronico": self.correo_electronico,
            "contrasenia": self.contrasenia,
        }
