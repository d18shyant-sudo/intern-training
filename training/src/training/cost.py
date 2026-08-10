class calculate:
  def __init__(self):
    self.token_count = 0
    self.token = 0
    self.price = 0.0
  def calculate_price(self,token=0,price=0.0):
    """This method is used to calculate the price of token used"""
    self.token = token
    result = self.token*price
    self.token_count += token
    return result
calculator = calculate()
def main():
  result = calculator.calculate_price(token=1000,price=0.0000123)
  print(result)
if __name__ == "__main__":
  main()
