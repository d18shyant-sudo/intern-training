from pydantic import BaseModel
class Message(BaseModel):
    role:str
    content:str
class Medication(BaseModel):
    name: str
    dose : str | None = None
message = Message(role="User",content="Hi what is the use of pydantic")
medication1 = Medication(name="Paracetomol")
medication2 = Medication(name="DOLO 650",dose="500 mcg")
print(message)
print(medication1)
print(medication2)