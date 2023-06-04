from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from trustee.login_trustee import login_trustee
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


def check_key(element):
    if element.text != "Clave verificada exitosamente ✔":
        raise ("La clase no se ha verificado correctamente")


def verify_trustee(trustee_name, trustee_password):
    options = get_driver_options()

    # Abrimos el navegador
    driver = webdriver.Chrome(options=options)

    login_trustee(driver, trustee_name, trustee_password)

    # Accedemos a la etapa 1
    button_key_generator = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "verify-key"))
    )
    button_key_generator.click()

    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DIRECTORY_PATH}/trustee_key_{trustee_name}_{NAME_ELECTION}.txt"
    )

    # Esperamos a que el proceso se complete
    finish_check = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-check"))
    )

    check_key(finish_check)


def check_sk():
    verify_trustee(TRUSTEE_NAME_1, TRUSTEE_PASSWORD_1)
    time.sleep(2)
    verify_trustee(TRUSTEE_NAME_2, TRUSTEE_PASSWORD_2)
    time.sleep(2)
    verify_trustee(TRUSTEE_NAME_3, TRUSTEE_PASSWORD_3)
