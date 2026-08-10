# 1.Regular Expression for json
import re
content = """
```json
{
"employee_name":"அலிஸ்",
"department_name":"IT",
"expense-amount":2300,
"status":"pending"
}
```
"""
def json_extract(json_content)->str|None:
    json_match = re.search(r"^\s*```(?:json)?\s*\n*?(.*?)\n*?\s*```\s*$",json_content,re.DOTALL)
    if json_match:
        return json_match.group(1)
    return None
# 2.Regular Expression for phone number and for a form "ABC-1234"
phone_no =  "என் எண் 9876543210"
def extract_phone_no(phone_no)->str|None:
    check_phone_number = r"\d{10}"
    phone_match = re.search(check_phone_number,phone_no)
    if phone_match:
        return int(phone_match.group())
    else:
        return None
form = "ABC-1234"
def extract_form(form)->str|None:
    check_form = r"^[A-Z]{3}-\d{4}"
    form_match = re.fullmatch(check_form,form)
    if form_match:
        print("Valid form")
    else:
        print("Not Valid form")
# 3.Replace the phone number in the text with [PHONE]
text = "ஆலிஸின் தொடர்பு எண் 2345996801"
def replace_the_number(text)->str|None:
    check_text = r"\d{10}"
    changed_text = re.sub(check_text,"[PHONE]",text)
    print(changed_text)
json_extract(content)
extract_phone_no(phone_no)
extract_form(form)
replace_the_number(text)