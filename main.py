from admin.main import admin_test
from trustee.main import trustee_test
from voter.main import voter_test
from utils import clear_test, print_results

import sys
import time


def execute_test():
    try:
        # Al terminar eliminamos la elección
        clear_test()

        # Ejecutamos los test step_1 del administrador
        admin_test("step_1")

        # Ejecutamos los test del trustee
        trustee_test("step_1")

        # Ejecutamos los test step_2 del administrador
        admin_test("step_2")

        # Test del votante
        voter_test("step_1")

        # Ejecutamos los test step_3 del administrador
        admin_test("step_3")

        # Ejecutamos los test step_2 del trustee
        trustee_test("step_2")        

        # Imprimir resultado de la elección
        time.sleep(10)
        print_results()

    except Exception:
        raise ("Ha ocurrido un error")

    # Al terminar eliminamos la elección
    clear_test()


if __name__ == "__main__":
    clear = False

    if len(sys.argv) > 1:
        # Argumento para limpiar los test
        clear = True if sys.argv[1] == "clear" else False

    if clear:
        clear_test()

    else:
        execute_test()
