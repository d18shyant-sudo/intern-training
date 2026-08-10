from decimal import Decimal
from model import message
from utils.role import Role
from price import Token
from collections import defaultdict
import uuid
import logging
import json
import re
from extract import extract_phone_no
logging.basicConfig(level=logging.WARNING)
with open("storage.json","r") as file:
        datas = json.load(file)
def filter_records(data):
    total_token = 0
    total_cost_of_token = Decimal("0")
    totals = defaultdict(Decimal)
    token_calculator = Token()
    price = Decimal("0.00245")

    for data in datas:
        try:
            record = message(**data)

            phone_number = extract_phone_no(record.content)

            if phone_number is not None:
                print("Phone:", phone_number)

            if isinstance(record.token, int):
                total_token += record.token

                total_cost_of_token += token_calculator.calculate_price(
                    record.token,
                    price,
                )

                totals[record.role] += (
                    Decimal(record.token) * price
                )

        except Exception as e:
            logging.warning(
                "Skipping invalid record: %s",
                data,
            )
            logging.warning(
                "Reason: %s",
                e,
            )

            continue

    print("Per-role totals:", dict(totals))
    print("Total tokens:", total_token)
    print("Total cost:", total_cost_of_token)


filter_records(datas)