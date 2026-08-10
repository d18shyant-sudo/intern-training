import re
def extract_phone_no(phone_no)->str|None:
    check_phone_number = r"\d{10}"
    phone_match = re.search(check_phone_number,phone_no)
    if phone_match:
        return int(phone_match.group())
    else:
        return None