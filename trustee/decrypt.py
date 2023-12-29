from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from trustee.login_trustee import login_trustee
from utils import get_driver_options

from config import NAME_ELECTION, TIMEOUT, DIRECTORY_PATH, TRUSTEES

import time


def check_decrypt(element):
    if element.text != "Desencriptación Parcial enviada exitosamente ✓":
        raise Exception("Las desencriptaciones no han sido calculados")


def trustee_decrypt(trustee_name, trustee_password):
    options = get_driver_options()

    # Abrimos el navegador
    driver = webdriver.Chrome(options=options)

    login_trustee(driver, trustee_name, trustee_password)

    # Accedemos a la etapa 3
    button_decrypt = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "upload-key"))
    )
    button_decrypt.click()

    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DIRECTORY_PATH}/trustee_key_{trustee_name}_{NAME_ELECTION}.txt"
    )

    # Esperamos a que el proceso se complete
    feedback = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-message-2"))
    )

    # check_decrypt(feedback)


def decrypt():
    for trustee in TRUSTEES:
        trustee_decrypt(trustee["user"], trustee["password"])
        time.sleep(2)
