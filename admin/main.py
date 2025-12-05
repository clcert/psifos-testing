from admin.login import login_test
from admin.create_election import create_election
from admin.upload_voters import upload_voters
from admin.create_question import create_question
from admin.create_trustee import create_trustee
from admin.ready_generation import ready_generation
from admin.close_election import close_election
from admin.compute_tally import compute_tally
from admin.init_election import init_election
from admin.download_bundle import download_bundle
from selenium import webdriver
import json
from config import ELECTIONS_FILE



def admin_test(actual_step, max_weight=1, normalization=False):
    steps = {
        "step_1": {
            "login_test": login_test,
            "create_election": create_election,
            "upload_voters": upload_voters,
            "create_question": create_question,
            "create_trustee": create_trustee,
            "set_ready_for_generation": ready_generation,
        },
        "step_2": {"login_test": login_test, "init_election": init_election},
        "step_3": {
            "login_test": login_test,
            "close_election": close_election,
            "compute_tally": compute_tally,
        },
        "step_4": {
            "login_test": login_test,
            "download_bundle": download_bundle
        }
    }

    options = webdriver.SafariOptions()
    options.add_argument("--private")

    # Abrimos el navegador
    driver = webdriver.Safari(options=options)

    step = steps[actual_step]

    print("====== ADMIN-TEST ======")
    with open(ELECTIONS_FILE, 'r') as file:
        election_data = json.load(file)
        elections = election_data.get('elections', [])
        for election in elections:
            for index, (name, test) in enumerate(step.items()):
                try:
                    election_name = election['short_name']
                    print(f"\nEjecutando prueba {name} {index + 1}/{len(step)}")
                    if name == 'create_election':
                        test(driver, max_weight, normalization)
                    elif name == 'download_bundle':
                        test(driver, election_name)
                    else:
                        test(driver)
                    print(f"Prueba {name} correcta ✓\n")

                except Exception as e:
                    print(f"Ha ocurrido un error en la prueba {index + 1} x")
                    print(e)
                    driver.quit()

    driver.quit()
