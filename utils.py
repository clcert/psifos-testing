from services.election import delete_election, get_election
from config import (
    DIRECTORY_PATH,
    TRUSTEE_NAME_1,
    TRUSTEE_NAME_2,
    TRUSTEE_NAME_3,
    NAME_ELECTION,
)
from selenium import webdriver

import os


def clear_test():
    try:
        election = get_election(NAME_ELECTION)
        if election.status_code == 200:
            # Al terminar eliminamos la elección
            delete_election()

        # Eliminar archivo de trustee
        ruta_archivo = (
            f"{DIRECTORY_PATH}/trustee_key_{TRUSTEE_NAME_1}_{NAME_ELECTION}.txt"
        )
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)

        # Eliminar archivo de trustee
        ruta_archivo = (
            f"{DIRECTORY_PATH}/trustee_key_{TRUSTEE_NAME_2}_{NAME_ELECTION}.txt"
        )
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)

        # Eliminar archivo de trustee
        ruta_archivo = (
            f"{DIRECTORY_PATH}/trustee_key_{TRUSTEE_NAME_3}_{NAME_ELECTION}.txt"
        )
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)

        print("Datos limpiados")

    except Exception:
        raise ("No se ha podido limpiar luego de los test")


def get_driver_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--private")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    )

    return options
