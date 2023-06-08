from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT
from services.election import get_election

NUM_ANSWERS = 3

import time


def check_init_election():
    response = get_election(NAME_ELECTION)

    json_data = response.json()
    if json_data["election_status"] != "Started":
        raise Exception("La elección no ha sido iniciada con éxito")


def init_election(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    time.sleep(1)
    # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Abrimos el modal de iniciar elección
    init_election = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='init-election']"))
    )
    init_election.click()

    # Presionamos el boton del modal
    button_init_election = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-init-election"))
    )
    button_init_election.click()

    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-message"))
    )

    check_init_election()
