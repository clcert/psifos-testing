from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT
from services.election import get_election

NUM_ANSWERS = 3


def check_close_election():
    response = get_election(NAME_ELECTION)

    json_data = response.json()
    if json_data["election_status"] != "Ended":
        raise Exception("La elección no ha sido cerrada con éxito")


def close_election(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    # Abrimos el modal de cerrar elección
    close_election = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "close-election"))
    )
    close_election.click()

    # Presionamos el boton del modal
    button_close_election = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-close-election"))
    )
    button_close_election.click()

    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-message"))
    )

    check_close_election()
