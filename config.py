import os

from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

NAME_ELECTION = os.environ.get("NAME_ELECTION")

INFO_URL = os.environ.get("INFO_URL")
OPERATIVE_URL = os.environ.get("OPERATIVE_URL")
URL_ADMIN = os.environ.get("URL_ADMIN")

TRUSTEE_NAME_1 = os.environ.get("TRUSTEE_NAME_1")
TRUSTEE_PASSWORD_1 = os.environ.get("TRUSTEE_PASSWORD_1")
TRUSTEE_EMAIL_1 = os.environ.get("TRUSTEE_EMAIL_1")

TRUSTEE_NAME_2 = os.environ.get("TRUSTEE_NAME_2")
TRUSTEE_PASSWORD_2 = os.environ.get("TRUSTEE_PASSWORD_2")
TRUSTEE_EMAIL_2 = os.environ.get("TRUSTEE_EMAIL_2")

TRUSTEE_NAME_3 = os.environ.get("TRUSTEE_NAME_3")
TRUSTEE_PASSWORD_3 = os.environ.get("TRUSTEE_PASSWORD_3")
TRUSTEE_EMAIL_3 = os.environ.get("TRUSTEE_EMAIL_3")

VOTER_NAME = os.environ.get("VOTER_NAME")
VOTER_PASSWORD = os.environ.get("VOTER_PASSWORD")

DIRECTORY_PATH = os.environ.get("DIRECTORY_PATH")
VOTERS_FILE_NAME = os.environ.get("VOTERS_FILE_NAME")
VOTERS_LOGIN_FILE_NAME = os.environ.get("VOTERS_LOGIN_FILE_NAME")

TIMEOUT = os.environ.get("TIMEOUT")
LOGIN_SITE = os.environ.get("LOGIN_SITE")
