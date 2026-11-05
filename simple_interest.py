print("Find your Simple Interest\n")
principal_amount = float(input("Enter ur Principal Amount: "))
interest_rate = float(input("Enter ur Interest Rate per year in percentage: "))
time = float(input("Enter ur Time in years: "))
print(f"\nPrincipal Amount = {principal_amount} \nInterest Rate per year = {interest_rate}% \nTime = {time} years \n")
SI = (principal_amount * interest_rate * time) /  100

print(f"The Simple Interest is {SI}")