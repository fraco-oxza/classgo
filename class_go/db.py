# ===================================
# Archivo donde se almacenan las 
# funciones que permiten la conexión
# con la base de datos SQLite3
# ===================================

from os import path as os_path
import sqlite3

import click

from .schema import instructions


def get_db(auto_init=True):
    """
    Funcion que retornara acceso la base de
    datos
    """
    dirname = os_path.dirname(__file__) #Directorio donde se encuentra este archivo
    path = os_path.join(dirname, "database/") #Directorio donde se encuentra la base de datos
     
    print(path)

    db = sqlite3.connect(path + "data.db") # Se conecta a la base de datos
    c = db.cursor() #Crea un cursor

    if (auto_init): #Revisa si la base de datos tiene las tablas creadas
        try:
            c.execute("SELECT null FROM class")
            c.execute("SELECT null FROM bouquet")
        except sqlite3.OperationalError: #Si no las tiene, las crea
            click.echo("La base de datos aún no se a inicializado\nInicializando...")
            init_db() #Inicializa la base de datos
            click.echo("La base de datos se a inicializado correctamente.")

    return db, c #Retornamos la conexión


def init_db() -> None:
    """
    Funcion encargada ejecutar las
    instrucciones almacenadas en 
    schema.py para inicializar la base
    de datos
    """
    db, c = get_db(auto_init=False) #Trae la base de datos
    # auto_init = False, esta para evitar un bucle 
    # infinito cuando la funcion get_db trate de inicializar
    # la base de datos

    try:
        for i in instructions:
            c.execute(i) #Ejecuta cada instrucción
    except:
        pass

    db.commit()
            