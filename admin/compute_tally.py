from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT
from services.election import get_election

NUM_ANSWERS = 3
import time

def check_compute_election():
    response = get_election(NAME_ELECTION)

    json_data = response.json()
    if json_data["election_status"] != "Tally computed":
        raise Exception("La elección no ha computado el tally con éxito")


def compute_tally(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

   # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)

    # Abrimos el modal de iniciar elección
    compute_tally = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "compute-tally"))
    )
    compute_tally.click()

    # Presionamos el boton del modal
    button_compute_tally = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-compute-tally"))
    )
    button_compute_tally.click()

    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-message"))
    )

    check_compute_election()
