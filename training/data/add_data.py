from training import data_and_control_flow
import uuid
count = 10
request_id = []
for i in range(count):
    request_id.append(uuid.uuid4())
for i in range(count):
    # record = {
    #     # "role":str(input("Enter the role:")),
    #     # "message":str(input("Enter the message")),
    #     # "token_count":str(input("Enter the token count:"))
    #        "request_id":request_id[i]
    # }
    data_and_control_flow.datas[i]["request_id"] = str(request_id[i])
with open("data_and_control_flow.py","w") as f:
    f.write(f"datas={repr(data_and_control_flow.datas)}")