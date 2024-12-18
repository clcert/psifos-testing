from admin.main import admin_test
from trustee.main import trustee_test
from voter.main import voter_test
from utils import clear_test, print_results

import sys
import time
import argparse


def execute_all_tests(max_weight, normalization):
    try:
        # Al iniciar eliminamos la elección (si existiese)
        clear_test()

        # Ejecutamos los test step_1 del administrador
        admin_test("step_1", max_weight, normalization)

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
        print_results(max_weight, normalization)

    except Exception:
        raise ("Ha ocurrido un error")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', default=False)
    parser.add_argument('-w', '--max_weight', type=int, default=1)
    parser.add_argument('-n', '--normalization', action='store_true', default=False)
    args = parser.parse_args()
    
    if args.clear:
        clear_test()

    else:
        execute_all_tests(args.max_weight, args.normalization)
