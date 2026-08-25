employee_data = {101:{"name":"alice","age":23,"salary":20000},102:{"name":"bob","age":24,"salary":32000},"103":{"name":"charlie","age":24,"salary":25000}}
def get_employee(emp_id):
    return employee_data.get(emp_id)
def calculate_bonus(salary:int):
    return salary+salary*0.2
