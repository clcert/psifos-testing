# PsifosVoting Testing Suite
Script que realiza disintas pruebas a una instancia de PsifosVoting.

## Tests
1. Login de admin
2. Creación de elección
3. Subir padrón de votantes
4. Crear preguntas
5. Crear custodios de claves
6. Creación de claves
7. Iniciar elección
8. Envío de votos
9. Cerrar elección
10. Computar *tally* de la elección
11. Envío de desencriptaciones parciales
12. Cálculo del resultado de la elección

## Comandos
### Ejecutar las pruebas
```
$ python main.py
```

### Limpiar los archivos y elecciones de prueba
```
$ python main.py clear
```

## Configuración

Para correr los test se debe generar un .env con la siguiente información

- `ADMIN_USER`: nombre del usuario admin.
- `ADMIN_PASSWORD`: contraseña del usuario admin.

- `NAME_ELECTION`: nombre de la elección a crear.

- `URL_ADMIN`: URL de la pantalla de login del usuario admin.
- `OPERATIVE_URL`: URL del backend operativo.
- `INFO_URL`: URL del backend informativo.

- `LOGIN_SITE`: pantalla de login, opciones: `clcert`, `clave-unica` o `uchile`.
- `TYPE_QUESTION`: tipo de pregunta, opciones: `normal` o `mixnet`.

- `DIRECTORY_PATH`: directorio donde se guardan los archivos (generalmente, el archivo donde se descargan las claves de los custodios de clave).
- `VOTERS_FILE_NAME`: archivo (.csv) con el padrón de la elección.
- `VOTERS_LOGIN_FILE_NAME`: archivo (.csv) con los nombres de usuario y contraseñas de cada votante.
- `TRUSTEES_FILE_NAME`: archivo (.json) con los nombres de usuario y contraseñas de cada custodio de clave.

- `TIMEOUT`: 30000
