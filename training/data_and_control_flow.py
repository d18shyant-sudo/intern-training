from collections import Counter,defaultdict
datas=[{'role': 'user', 'message': 'hi', 'token_count': 1, 'request_id': '6e1d890a-8374-45bd-9684-27dee02f3b95'}, 
       {'role': 'assistant', 'message': 'hello have a great day how can i help you', 'token_count': 9, 'request_id': 'c2a5fed0-c6fb-46c1-878d-69282cc6c21c'}, 
       {'role': 'user', 'message': '2+5', 'token_count': 3, 'request_id': '17b1fdf7-e699-49dd-811b-4ca0aa513269'}, 
       {'role': 'assistant', 'message': '7 ,what is the next thing you need ?', 'token_count': 9, 'request_id': 'ae7fe671-0901-457e-961e-e431be0fb0bb'}, 
       {'role': 'user', 'message': 'what is the difference between the integer and float?', 'token_count': 8, 'request_id': '7b42c9dd-bfde-4535-adc9-affcd2925b8c'},
         {'role': 'assistant', 'message': 'Thats a most confusing thing.Integers are used to stor all natural number from negative to positive.float is used to store the all floating values.', 'token_count': 26, 'request_id': 'd32b6735-2f52-466b-8de4-aa524a869662'}, 
         {'role': 'user', 'message': ' then what is the difference between int and short .why do short is exist even though integer stores such a big values ?', 'token_count': 24, 'request_id': 'e8956e97-f728-4b57-9567-115b06a4f604'}, 
         {'role': 'assistant', 'message': 'Thats a great question.this where all beginner get stuck integers is all most used in day to day tasks but short is not used as much since through short only upto few number store if the numbers is in range then we can use the short if we cant then integer since integer can store upto a large extend', 'token_count': 60, 'request_id': 'be45896d-8038-4659-8583-fdaebc6f3002'},
           {'role': 'user', 'message': 'then ok fine bye', 'token_count': 4, 'request_id': 'd17ff004-91ba-4c6e-811b-75a19927501c'}, {'role': 'assistant', 'message': 'bye have a great day!', 'token_count': 5, 'request_id': 'da96166e-16be-4af4-8f18-9b91d181a282'}]
role_count = Counter(record['role'] for record in datas)
print(role_count)
totals = defaultdict(int)
for record in datas:
    totals[record['role']] += 1
print(totals)