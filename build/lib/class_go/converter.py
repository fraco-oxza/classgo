# ===================================
# Archivo donde se almacenan todas
# las funciones relacionadas a la
# transformacion de variables
# ==================================


def date_list(date: str) -> list:
    # str(del(",")) -> list<int>
    # "2, 5, 6" -> [2,5,6]

    days = date.split(",")  # Divide el string
    c_days = []  # Se almacenara la lista revisada

    for day in days:
        # Se revisa la lista para que sea un entero y este en el rango 0-7
        c_days.append(int(day))  # Se transforma a entero
        if not (int(day) > 0 and int(day) <= 7):
            raise AssertionError

    return c_days   # Se retorna la lista de enteros


def date_str(days: list or tuple) -> str:
    # list<int> -> str(del(","))
    # [2,3,7] -> "2,3,7"

    c_days = ""  # Se almacenara el str

    for day in days:
        # elemento por elemento se añade y se suma una coma al final
        c_days += str(day) + ","

    return c_days[:-1]  # Se devuelve sin la ultima coma, ya que sobra


def hour_list(hour: str) -> list:
    # str(del(":")) -> list<int>
    # "23:59" -> [23, 59]

    c_hour = hour.split(":")  # Se divide el string
    if len(c_hour) != 2:
        raise AssertionError

    # Se convierte a numero entero
    c_hour[0] = int(c_hour[0])
    c_hour[1] = int(c_hour[1])

    # Se revisa que sea una hora valida
    if not (c_hour[0] < 24 and c_hour[0] >= 0):
        raise AssertionError
    if not (c_hour[1] < 60 and c_hour[1] >= 0):
        raise AssertionError

    return c_hour  # Se retorna la hora convertida
