from voter.vote_normal import vote_normal
from selenium import webdriver

import traceback


def voter_test(actual_step):
    steps = {
        "step_1": {
            "vote_normal": vote_normal,
        }
    }

    options = webdriver.ChromeOptions()
    options.add_argument("--private")

    # Abrimos el navegador
    driver = webdriver.Chrome(options=options)

    step = steps[actual_step]

    print("====== VOTER-TEST ======")
    for index, (name, test) in enumerate(step.items()):
        try:
            print(f"\nEjecutando prueba {name} {index + 1}/{len(step)}")
            test(driver)
            print(f"Prueba {name} correcta ✓\n")

        except Exception as e:
            print(f"Ha ocurrido un error en la prueba {index + 1} x")
            print(e)
            traceback.print_exc()
            driver.quit()

    driver.quit()
