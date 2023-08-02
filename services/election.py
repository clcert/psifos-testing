from config import (
    INFO_URL,
    OPERATIVE_URL,
    ADMIN_USER,
    ADMIN_PASSWORD,
    NAME_ELECTION,
)

import requests
import base64


def get_election_result(short_name):
    # Realiza una solicitud GET a una URL
    response = requests.get(f"{INFO_URL}/election/{short_name}/result")
    return response

def get_election(short_name):
    # Realiza una solicitud GET a una URL
    response = requests.get(f"{INFO_URL}/election/{short_name}")
    return response


def delete_election():
    # Definir la URL y los parámetros
    url = OPERATIVE_URL + "/delete-election/" + NAME_ELECTION
    token = login()

    # Configurar las cabeceras de la solicitud
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    # Realizar la solicitud GET
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Elección eliminada con éxito!")


def login():
    # Definir la URL y las credenciales
    url = OPERATIVE_URL + "/login"
    username = ADMIN_USER
    password = ADMIN_PASSWORD

    # Codificar las credenciales en base64
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode("utf-8")

    # Configurar las cabeceras de la solicitud
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json",
    }

    # Realizar la solicitud POST
    response = requests.post(url, headers=headers)

    # Obtener la respuesta
    resp = response.json()

    # Hacer algo con la respuesta
    return resp["token"]
