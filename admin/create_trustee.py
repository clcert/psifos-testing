from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import (
    URL_ADMIN,
    NAME_ELECTION,
    TIMEOUT,
    TRUSTEE_NAME_1,
    TRUSTEE_NAME_2,
    TRUSTEE_NAME_3,
)
from services.election import get_election

import time

NUM_ANSWERS = 3


def check_trustee():
    response = get_election(NAME_ELECTION)

    json_data = response.json()
    trustees = json_data["trustees"]
    if len(trustees) == 0 and trustees[0]["name"] != "ahevia":
        raise Exception("El custodio no ha sido creado con exito")


def add_trustee(driver, name_trustee, login_id, trustee_email):
    # Entramos al formulario del custodio
    button_trustee = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "add-trustee"))
    )
    button_trustee.click()

    button_trustee_modal = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "next-trustee"))
    )
    button_trustee_modal.click()

    # Rellenamos el formulario del custodio
    trustee_name_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "trustee-name"))
    )
    trustee_name_input.send_keys(name_trustee)

    trustee_id_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "trustee-id"))
    )
    trustee_id_input.send_keys(login_id)

    trustee_email_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "trustee-email"))
    )
    trustee_email_input.send_keys(trustee_email)

    # Enviamos la información del custodio
    send_trustee = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "send-trustee"))
    )
    send_trustee.click()
    time.sleep(1)


def create_trustee(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    time.sleep(1)
    # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Accedemos a crear una elección
    button_create_trustee = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='button-add-trustee']"))
    )
    button_create_trustee.click()

    add_trustee(driver, TRUSTEE_NAME_1, TRUSTEE_NAME_1, TRUSTEE_NAME_1)
    add_trustee(driver, TRUSTEE_NAME_2, TRUSTEE_NAME_2, TRUSTEE_NAME_2)
    add_trustee(driver, TRUSTEE_NAME_3, TRUSTEE_NAME_3, TRUSTEE_NAME_3)

    check_trustee()
