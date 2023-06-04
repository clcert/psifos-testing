from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import (
    OPERATIVE_URL,
    NAME_ELECTION,
    TIMEOUT,
    LOGIN_SITE,
)
import time

def login_voter(driver, voter_name, voter_password):

    # Ir a la página web
    driver.get(f"{OPERATIVE_URL}/{NAME_ELECTION}/vote")

    if LOGIN_SITE == "clcert":
        username_element_id = "id_username"
        password_element_id = "id_password"
    if LOGIN_SITE == "uchile":
        username_element_id = "usernameInput"
        password_element_id = "passwordInput"

    # Rellenamos el formulario del votante
    voter_name_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, username_element_id))
    )
    voter_name_input.send_keys(voter_name)

    voter_password_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, password_element_id))
    )
    voter_password_input.send_keys(voter_password)

    voter_password_input.send_keys(Keys.ENTER)