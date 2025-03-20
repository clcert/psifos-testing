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

    # Accedemos a la sección de Desencriptación
    decrypt_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content-home-admin']/section[2]/div/div[1]/ul/li[4]/button"))
    )
    decrypt_button.click()

    # Seleccionar elección única
    check_election = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content-home-admin']/section[2]/div/div[2]/div[3]/input"))
    )
    check_election.click()
    
    # Apretar botón para continuar
    continue_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content-home-admin']/section[2]/div/div[2]/div[1]/button"))
    )
    continue_button.click()
    
    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DIRECTORY_PATH}/LlavePrivada_{trustee_name}.key"
    )
    
    time.sleep(45)

    # check_decrypt(feedback)


def decrypt():
    for trustee in TRUSTEES:
        trustee_decrypt(trustee["user"], trustee["password"])
        time.sleep(2)
