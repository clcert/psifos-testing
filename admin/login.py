from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, ADMIN_USER, ADMIN_PASSWORD, TIMEOUT

def login_test(driver):

    # Ir a la página web
    driver.get(URL_ADMIN)

    # Encontrar y completar el formulario de inicio de sesión
    username_element = driver.find_element("id", "user-login")
    username_element.send_keys(ADMIN_USER)

    password_element = driver.find_element("id", "clave-login")
    password_element.send_keys(ADMIN_PASSWORD)

    submit_element = driver.find_element(By.CLASS_NAME, "footer-register-button")
    submit_element.click()

    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "election-subtitle"))
    )