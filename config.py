import os
import json

from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

NAME_ELECTION = os.environ.get("NAME_ELECTION")

URL_ADMIN = os.environ.get("URL_ADMIN")
OPERATIVE_URL = os.environ.get("OPERATIVE_URL")
INFO_URL = os.environ.get("INFO_URL")

LOGIN_SITE = os.environ.get("LOGIN_SITE")
TYPE_QUESTION = os.environ.get("TYPE_QUESTION")

DIRECTORY_PATH = os.environ.get("DIRECTORY_PATH")
VOTERS_FILE_NAME = os.environ.get("VOTERS_FILE_NAME")
VOTERS_LOGIN_FILE_NAME = os.environ.get("VOTERS_LOGIN_FILE_NAME")
TRUSTEES_FILE_NAME = os.environ.get("TRUSTEES_FILE_NAME")

TIMEOUT = os.environ.get("TIMEOUT")

# Lee el archivo JSON con los trustees
with open(DIRECTORY_PATH + "/" + TRUSTEES_FILE_NAME + ".json", "r") as f:
    TRUSTEES = json.load(f)
