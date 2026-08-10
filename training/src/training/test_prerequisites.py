import json
from training.Regex import json_extract,extract_phone_no
from training.message_mode import Message
from training.cost import calculator
from training.json_model import Employee
def test_json_extract():
    test = """
    ```json
    {
    "employee_name":alice,
    "employee_id":123
    }
    ```
    """
    result = json_extract(test)
    assert result == """{
    "employee_name":alice,
    "employee_id":123
    }"""
def test_extract_phone_no():
    text = "alice contact number is 4789388323"
    result = extract_phone_no(text)
    assert result == 4789388323
def test_cost_calculation():
    result = calculator.calculate_price(token=200,price=0.025)
    assert result == 5 
def test_json_load():
    with open("employees.json","r") as file:
        datas = json.load(file)
    employees = [Employee(**data) for data in datas]
    assert employees[0].id == 101
    assert employees[0].name == "Robert"
    assert  employees[0].department == "IT"