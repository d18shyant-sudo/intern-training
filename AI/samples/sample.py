from pydantic import BaseModel
import json
class ExpenseClaim(BaseModel):
    employee_name: str
    amount: float
    category: str
schema = ExpenseClaim.model_json_schema()
result = json.dumps(schema,indent=4)
print(result)