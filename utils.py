from services.election import delete_election, get_election, get_election_result
from config import (
    DIRECTORY_PATH,
    TRUSTEES,
    NAME_ELECTION,
)
from selenium import webdriver
import json
import os


def print_results():
    try:
        election_result = get_election_result(NAME_ELECTION)
        if election_result.status_code == 200:
            election_result_json = json.loads(election_result.json())
            for idx, q in enumerate(election_result_json):
                print(f"Question #{idx}: {q['ans_results']}")
    except Exception:
        raise ("No se ha podido imprimir los resultados de la elección")

def clear_test():
    try:
        election = get_election(NAME_ELECTION)
        if election.status_code == 200:
            # Al terminar eliminamos la elección
            delete_election()

        for trustee in TRUSTEES:
            # Eliminar archivo de trustee
            ruta_archivo = (
                f"{DIRECTORY_PATH}/trustee_key_{trustee['user']}_{NAME_ELECTION}.txt"
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
