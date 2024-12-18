from trustee.key_generator import key_generator
from trustee.check_key import check_sk
from trustee.decrypt import decrypt
from trustee.login_trustee import login_trustee
from selenium import webdriver
from config import DIRECTORY_PATH

import traceback


def trustee_test(actual_step):
    steps = {
        "step_1": {
            "key_generator": key_generator,
            # "check_sk": check_sk,
        },
        "step_2": {"decrypt": decrypt},
    }

    options = webdriver.ChromeOptions()
    options.add_argument("--private")
    options.add_argument(f"--download.default_directory={DIRECTORY_PATH}")
    options.add_argument("--download.prompt_for_download=False")

    step = steps[actual_step]

    print("====== TRUSTEE-TEST ======")
    for index, (name, test) in enumerate(step.items()):
        try:
            print(f"\nEjecutando prueba {name} {index + 1}/{len(step)}")
            test()
            print(f"Prueba {name} correcta ✓\n")

        except Exception as e:
            print(f"Ha ocurrido un error en la prueba {index + 1} x")
            print(e)
            traceback.print_exc()

