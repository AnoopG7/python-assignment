# Write a recursive function power(base, exp) that computes base^exp.
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
base=int(input("Enter the base"))
exp=int(input("Enter the power"))
print(base, "to the power", exp, "is", power(base, exp))