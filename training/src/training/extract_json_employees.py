import json
import logging
logging.basicConfig(level=logging.WARNING)
from pathlib import Path
from datetime import datetime,UTC
from time import perf_counter
file_path = Path("employees.json")
try:
    start = perf_counter()
    with open(file_path,"r") as file:
        employees = json.load(file)
    for employee in employees:
        print(employee["id"])
        print(employee["name"])
        print(employee["department"])
    end = perf_counter()
except json.JSONDecodeError as e:
    logging.warning("Invalid json")
    logging.warning(e)
except FileNotFoundError :
    logging.warning("employees.json file is not founded")
print(datetime.now(UTC))
print(f"Time taken :{end-start:.6f} seconds")