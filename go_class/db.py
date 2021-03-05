from os import path as os_path
import sqlite3

import click

from .schema import instructions

def get_db(auto_init=True):
    """
    Funcion que retornara acceso la base de
    datos
    """
    dirname = os_path.dirname(__file__)
    path = os_path.join(dirname, "data/")

    db = sqlite3.connect(path + "data.db")
    c = db.cursor()

    if (auto_init):
        try:
            c.execute("SELECT null FROM class")
        except sqlite3.OperationalError:
            click.echo("La base de datos aún no se a inicializado\nInicializando...")
            init_db()
            click.echo("La base de datos se a inicializado correctamente.")

    return db, c

def init_db() -> None:
    db, c = get_db(auto_init=False)

    try:
        for i in instructions:
            c.execute(i)
    except:
        pass

    db.commit()
            