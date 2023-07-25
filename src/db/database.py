# db.py

from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb://localhost:27017/mi_base_de_datos"


def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        database = client["mi_base_de_datos"]
        print("Conexión exitosa")
    except ConnectionError as e:
        print("Error de conexión: ", e)
    return database
