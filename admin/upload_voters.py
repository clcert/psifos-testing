from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT, DIRECTORY_PATH, VOTERS_FILE_NAME
from services.election import get_election

NUM_ANSWERS = 3


def check_init_election(element):

    election_response = get_election(NAME_ELECTION)   

    json_data = election_response.json()
    total_voters = json_data["total_voters"]

    if element.text != "Los votantes se han subido con éxito" and total_voters == 0:
        raise Exception("Los votantes no han sido subidos con éxito")


def upload_voters(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    # Abrimos el modal de subir votantes
    button_add = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-add-voters"))
    )
    button_add.click()

    # Subimos el archivo
    file_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "fileinput"))
    )
    file_input.send_keys(f"{DIRECTORY_PATH}/{VOTERS_FILE_NAME}.csv")

    # Presionamos el boton del modal
    button_upload_voters = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "button-upload-voters"))
    )
    button_upload_voters.click()

    # Esperamos que termine el proceso
    feedback = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "feedback-upload"))
    )

    check_init_election(feedback)
