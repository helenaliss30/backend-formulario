import re


def validation_persona(data):
    required_fields = [
        "nombre",
        "apellido",
        "edad",
        "cedula",
        "correo_electronico",
        "enfermedades",
        "alergias",
        "medicamentos",
    ]

    # Verificar que todos los campos requeridos estén presentes y no estén vacíos
    for field in required_fields:
        if field not in data or not data[field]:
            return f"El campo '{field}' es obligatorio y no puede estar vacío."

    # Verificar que la cedula tenga exactamente 10 dígitos
    if len(str(data["cedula"])) != 10:
        return "La cédula debe tener exactamente 10 dígitos."

    # Verificar que el correo electrónico tenga un formato válido con una expresión regular
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, data["correo_electronico"]):
        return "El correo electrónico no tiene un formato válido."

    # Verificar que las listas de enfermedades, alergias y medicamentos no estén vacías
    if not isinstance(data["enfermedades"], list) or not data["enfermedades"]:
        return "La lista de enfermedades no puede estar vacía."

    if not isinstance(data["alergias"], list) or not data["alergias"]:
        return "La lista de alergias no puede estar vacía."

    if not isinstance(data["medicamentos"], list) or not data["medicamentos"]:
        return "La lista de medicamentos no puede estar vacía."

    # Aquí puedes agregar otras reglas de validación según tus necesidades
    # Por ejemplo, verificar que la edad sea un número entero positivo, etc.

    return None


def validation_user(data):
    required_fields = [
        "correo_electronico",
        "contrasenia",
        "confirmar_contrasenia",
    ]
    for field in required_fields:
        if field not in data or not data[field]:
            return f"El campo '{field}' es obligatorio y no puede estar vacío."

    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, data["correo_electronico"]):
        return "El correo electrónico no tiene un formato válido."

    if str(data["contrasenia"]) != str(data["confirmar_contrasenia"]):
        print("La contraseña no coinciden")
        return "La contraseña no coinciden"

    return None
