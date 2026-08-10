from functools import lru_cache
@lru_cache
def token_price_calculator(token):
    print("The calculated price ")
    return token*0.01267
token_1 = token_price_calculator(90)
token_2 =token_price_calculator(80)
token_3 = token_price_calculator(90)
print(token_1)
print(token_2)
print(token_3)