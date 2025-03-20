from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from trustee.login_trustee import login_trustee
from services.election import get_election
from selenium import webdriver
from utils import get_driver_options

from config import NAME_ELECTION, TIMEOUT, DIRECTORY_PATH, TRUSTEES

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

    # Accedemos a la sección de sincronización
    sync_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content-home-admin']/section[2]/div/div[1]/ul/li[2]/button"))
    )
    sync_button.click()
    
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
    
    # Apretar botón Generar Claves para descargar archivo
    generate_keys = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content-home-admin']/section[2]/div/div[2]/div[1]/button[2]"))
    )
    generate_keys.click()
    
    time.sleep(5)
    
    # Subimos el archivo
    drop_zone = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "file-input"))
    )
    drop_zone.send_keys(
        f"{DIRECTORY_PATH}/LlavePrivada_{trustee_name}.key"
    )

    time.sleep(120)


def key_generator():
    trustee_threads = []
    for trustee in TRUSTEES:
        # Crear un objeto Thread
        trustee_thread = threading.Thread(
            target=trustee_generator_key, args=(trustee["user"], trustee["password"])
        )
        trustee_threads.append(trustee_thread)

    for t in trustee_threads:
        t.start()
        time.sleep(2)

    for t in trustee_threads:
        t.join()

    check_key()
