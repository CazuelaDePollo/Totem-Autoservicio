from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from tkinter import* #importa todo de tkinder
from tkinter import ttk
from tkinter import messagebox


url = "mongodb+srv://PlayerYee:Yanli1001*@baseplayeryee.rqwmun6.mongodb.net/?retryWrites=true&w=majority"
#"mongodb+srv://PlayerYee:Yanli1001*@baseplayeryee.rqwmun6.mongodb.net/test"

def conexion():
    #crea una nueva conexion
    cliente = MongoClient(url, server_api=ServerApi('1'))

    #confirmar la conexion

    try:
        cliente.admin.command('ping')
        
        db = cliente.Autoservicio
        return db
    except Exception as e:
        print(e)




