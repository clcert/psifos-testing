from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import URL_ADMIN, NAME_ELECTION, TIMEOUT, TYPE_QUESTION, DIRECTORY_PATH
from services.election import get_election

import time

NUM_ANSWERS = 3


def check_question():
    response = get_election(NAME_ELECTION)
    if response.status_code != 200:
        raise Exception("La elección no se ha creado")

    json_data = response.json()
    if json_data["questions"] == "":
        raise Exception("Las preguntas no han sido creadas")


def add_question(driver, question_number, select_number=1, choices_number=3):
    # Completamos los formularios
    add_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='add-question']"))
    )
    add_question.click()

    name_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, f"//*[@id='name-{question_number}']"))
    )
    name_input.send_keys(f"Pregunta {question_number}")

    input_max_options = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[@id='question-{question_number}-max-answers']")
        )
    )

    input_max_options.clear()
    input_max_options.send_keys(f"{select_number}")

    # Enviamos los datos para crear
    button_add_option = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[@id='add-option-{question_number}']")
        )
    )

    for i in range(choices_number):
    # Ejecuta JavaScript para realizar el scroll hasta el final de la página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1)
        button_add_option.click()

        # Esperamos a la pantalla de inicio
        input_option = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//*[@id='question-{question_number}-text-option-{i}']")
            )
        )
        input_option.send_keys(f"Respuesta {i + 1}")

def add_question_mixnet(driver, question_number):
    # Completamos los formularios
    add_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='add-question']"))
    )
    add_question.click()

    name_input = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, f"//*[@id='name-{question_number}']"))
    )
    name_input.send_keys(f"Pregunta {question_number}")

    # Esperamos a que el elemento select aparezca en la página
    select_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, f"//*[@id='select_type_question']"))
    )

    # Creamos un objeto de la clase Select con el elemento
    select = Select(select_element)

    # Seleccionamos la opción 'mixnet' por su valor o texto visible (depende del caso)
    select.select_by_value('mixnet_question')  # Opción por valor

    input_max_options = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[@id='question-{question_number}-max-answers']")
        )
    )

    input_max_options.clear()
    input_max_options.send_keys(f"6")

    # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Esperamos a que el campo de entrada aparezca en la página
    file_input_element = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, f"//*[@id='fileinput']"))
    )

    # Enviamos la ruta del archivo al campo de entrada utilizando el método send_keys
    file_input_element.send_keys(f"{DIRECTORY_PATH}/mixnet-example.txt")

    time.sleep(3)



def create_question(driver):

    type_question = {
        'mixnet': mixnet_question,
        'normal': normal_question
    }

    type_question[TYPE_QUESTION](driver)


def normal_question(driver):
    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    time.sleep(1)
   # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Accedemos a crear preguntas
    button_create_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='button-add-questions']"))
    )
    button_create_question.click()

    add_question(driver, 1, 1, 3)
    add_question(driver, 2, 2, 3)

    save_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='button-save-questions']"))
    )
    save_question.click()
    time.sleep(1)

    # Esperamos a la pantalla de inicio
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='election-subtitle']"))
    )

    check_question()

def mixnet_question(driver):

    # Ir a la página web
    driver.get(f"{URL_ADMIN}/admin/{NAME_ELECTION}/panel")

    time.sleep(1)
   # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Accedemos a crear preguntas
    button_create_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='button-add-questions']"))
    )
    button_create_question.click()

    add_question_mixnet(driver, 1)

    save_question = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='button-save-questions']"))
    )
    save_question.click()
    time.sleep(1)

    # Esperamos a la pantalla de inicio
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='election-subtitle']"))
    )

    check_question()
