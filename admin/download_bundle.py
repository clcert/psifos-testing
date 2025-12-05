from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, TIMEOUT
from services.election import get_election

import time


def download_bundle(driver, election_name):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{election_name}/panel")

    time.sleep(1)
    # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Abrimos el modal de iniciar elección
    download_bundle = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='bundle-button-download']"))
    )
    download_bundle.click()

    # Esperamos que se descargue el bundle
    # TODO: mejorar esto para solamente esperar lo que dura la descarga (ni más, ni menos)
    time.sleep(10)
