from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from voter.login_voter import login_voter
from config import TIMEOUT, DIRECTORY_PATH, VOTERS_LOGIN_FILE_NAME, TYPE_QUESTION

import random
import time
import csv
import threading


def print_vote(question_number, choices_list):
    options = [0] * 5
    if 3 not in choices_list and 4 not in choices_list:
        for choice in choices_list:
            options[choice] = 1
    elif choices_list[-1] == 3:
        options[3] = 1
    elif choices_list[-1] == 4:
        options[4] = 1
    else:
        options[choices_list[-1]] = 1
    
    print("Question #" + str(question_number) + ": " + str(options))

def vote_question(driver, question_number, number_choices=1):
    choices_list = []
    for i in range(number_choices):
        choice = random.randint(0, 2 + 2)
        while choice in choices_list:
            choice = random.randint(0, 2 + 2)
        choices_list.append(choice)
        # Elegimos la alternativa
        if choice <= 2:
            input_id = f"question-{question_number - 1}-answer-{choice}"
        elif choice == 3:
            input_id = f"white"
        else:
            input_id = f"null"
        input_answers = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.ID, input_id)
            )
        )
        input_answers.click()
    print_vote(question_number, choices_list)

    # Siguiente
    next_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "next-button"))
    )
    next_button.click()

def vote_mixnet(driver):
    
    for i in range(6):

        # Esperar a que el elemento select aparezca en la página
        select_element = driver.find_elements(By.CLASS_NAME, "css-b62m3t-container")
        select_element[i].click()
        time.sleep(1)
        list_box = driver.find_element(By.ID, f'react-select-{i + 2}-listbox')
        hijos = list_box.find_element(By.XPATH, './*')
        nietos = hijos.find_elements(By.XPATH, './*')
        nietos[i].click()

    # Siguiente
    next_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "next-button"))
    )
    next_button.click()


def process_voter(voter_login, voter_password):
    options = webdriver.ChromeOptions()
    options.add_argument("--private")

    # Abrimos el navegador
    driver = webdriver.Chrome(options=options)

    login_voter(driver, voter_login, voter_password)
    time.sleep(2)

    if TYPE_QUESTION == 'mixnet':
        vote_mixnet(driver)

    else:
        vote_question(driver, 1, 1)
        time.sleep(1)
        vote_question(driver, 2, 2)

    # Enviar voto
    send_button = WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='proceed_button']"))
    )
    # Ejecuta JavaScript para realizar el scroll hasta el final de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    send_button.click()

    # El voto ha sido enviado con exito
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "back-vote-button"))
    )


def vote_normal(driver):
    options = webdriver.ChromeOptions()
    options.add_argument("--private")

    # Abre el archivo CSV en modo lectura
    with open(f"{DIRECTORY_PATH}/{VOTERS_LOGIN_FILE_NAME}.csv", "r") as archivo_csv:
        # Crea un lector de CSV
        lector_csv = csv.reader(archivo_csv)
        lector_csv = list(lector_csv)
        final_array = split_array(lector_csv, 3)
        threads = []

        # Itera sobre cada fila del archivo CSV
        for fila in final_array:
            # Separa los elementos de la fila
            for i in range(len(fila)):
                voter_login = fila[i][0]
                voter_password = fila[i][1]

                t = threading.Thread(
                    target=process_voter, args=(voter_login, voter_password)
                )
                t.start()
                threads.append(t)

            for t in threads:
                t.join()


def split_array(array, split_length):
    arreglos_divididos = []
    for i in range(0, len(array), split_length):
        arreglos_divididos.append(array[i : i + split_length])
    return arreglos_divididos
