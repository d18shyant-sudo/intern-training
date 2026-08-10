from decimal import Decimal
from cost import calculator
from training.utils.role import Role
import uuid
request_id = []
for i in range(10):
    request_id.append(uuid.uuid4())
    print(request_id[i])
datas=[{'role': Role.USER.value, 
        'message': 'hi', 
        'token_count': 1},
       {'role': Role.ASSISTANT.value,
         'message': 'hello have a great day how can i help you', 
         'token_count': 9},
         {'role': Role.USER.value,
           'message': '2+5', 
           'token_count': 3}, 
         {'role':  Role.ASSISTANT.value, 
          'message': '7 ,what is the next thing you need ?', 
          'token_count': 9}, 
         {'role':Role.USER.value,
           'message': 'what is the difference between the integer and float?', 
           'token_count': 8},
           {'role':  Role.ASSISTANT.value, 
            'message': 'Thats a most confusing thing.Integers are used to stor all natural number from negative to positive.float is used to store the all floating values.', 
            'token_count': 26},
             {'role': Role.USER.value, 
              'message': ' then what is the difference between int and short .why do short is exist even though integer stores such a big values ?', 
              'token_count': 24}, 
             {'role':  Role.ASSISTANT.value,
               'message': 'Thats a great question.this where all beginner get stuck integers is all most used in day to day tasks but short is not used as much since through short only upto few number store if the numbers is in range then we can use the short if we cant then integer since integer can store upto a large extend', 
               'token_count': 60},
               {'role': Role.USER.value, 
                'message': 'then ok fine bye',
                  'token_count': 4}, 
             {'role':  Role.ASSISTANT.value, 
              'message': 'bye have a great day!',
                'token_count': 5}]
for index,data in enumerate(datas):
    cost = calculator.calculate_price(token=data["token_count"],price=0.0000231)
    print(f"{index}  {data}    cost:{cost:.6f}")
    print("\n")
new_datas = []
for data in datas:
    new_datas=sorted(datas,key=lambda x:x["token_count"],reverse=True)
for index,data in enumerate(new_datas):
    print(index,data)
comrehension_data = [data for data in sorted(datas,key=lambda x:x["token_count"],reverse=True)]
for index,data in enumerate(comrehension_data):
    print(index,data)
print(new_datas==comrehension_data)
with open("token.txt","r") as file:
    for token in file:
        try :
            value =  int(token)
            print(value)
        except ValueError:
            print("Invalid token")
total_with_float = 0.0
for data in datas:
    total_with_float += float(data['token_count'])*0.0000231
total_with_decimal = Decimal("0")
for data in datas:
    total_with_decimal += Decimal(data['token_count']*0.0000231)
print(total_with_float)
print(total_with_decimal)


word = "உலகம்"
b_word = word.encode("utf-8")
print(len(word))
print(len(b_word))
a=datas
a[0]["token_count"] = 10
print(datas)
print(calculate.calculate_price.__doc__)
print(calculator.token_count)