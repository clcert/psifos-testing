from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from trustee.login_trustee import login_trustee
from services.election import get_election
from selenium import webdriver
from utils import get_driver_options

from config import (
    NAME_ELECTION,
    TIMEOUT,
    DIRECTORY_PATH,
    TRUSTEE_NAME_1,
    TRUSTEE_PASSWORD_1,
    TRUSTEE_NAME_2,
    TRUSTEE_PASSWORD_2,
    TRUSTEE_NAME_3,
    TRUSTEE_PASSWORD_3,
)

import time
import threading


def check_key():
    response = get_election(NAME_ELECTION)

    json_data = response.json()
    trustees = json_data["trustees"]
    if trustees[0]["public_key"] == "":
        raise Exception("La clave no ha sido generada con éxito")


def trustee_generator_key(trustee_name, trustee_password):
    options = get_driver_options()

    # Abrimos el navegador
    driver = webdriver.Chrome(options=options)

    login_trustee(driver, trustee_name, trustee_password)

    # Accedemos a la etapa 1
    button_key_generator = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "init-key-generator"))
    )
    button_key_generator.click()

    # Descargamos la key
    button_download_key = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "download-key"))
    )
    button_download_key.click()

    time.sleep(3)

    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DIRECTORY_PATH}/trustee_key_{trustee_name}_{NAME_ELECTION}.txt"
    )

    time.sleep(25)


def key_generator():
    # Crear un objeto Thread
    trustee_1 = threading.Thread(
        target=trustee_generator_key, args=(TRUSTEE_NAME_1, TRUSTEE_PASSWORD_1)
    )
    trustee_2 = threading.Thread(
        target=trustee_generator_key, args=(TRUSTEE_NAME_2, TRUSTEE_PASSWORD_2)
    )
    trustee_3 = threading.Thread(
        target=trustee_generator_key, args=(TRUSTEE_NAME_3, TRUSTEE_PASSWORD_3)
    )

    # Iniciar el hilo
    trustee_1.start()
    time.sleep(2)
    trustee_2.start()
    time.sleep(2)
    trustee_3.start()

    # Esperar a que el hilo termine (opcional)
    trustee_1.join()
    trustee_2.join()
    trustee_3.join()
    check_key()
