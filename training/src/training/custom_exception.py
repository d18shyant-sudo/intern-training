class ClaimLimitError(Exception):
    pass
try:
    claim_amount = int(input("Enter the claim:"))
    if claim_amount > 5000:
        raise ClaimLimitError("The claim should be less than 5000")
    print("Claim approved")
except ClaimLimitError as e:
    print(e)