print("Calculator Program")

a = float(input("\nEnter the Value 1: "))
b = float(input("Enter the Value 2: "))

print("\n1. Add \n2. Subtract \n3. Multiply \n4. Division")
operator = int(input("Enter the number to choose the operator: "))

if operator == 1:
    print(f"{a} + {b} = {a + b}")
elif operator == 2:
    print(f"{a} - {b} = {a - b}")
elif operator == 3:
    print(f"{a} * {b} = {a * b}")
elif operator == 4:
    if b == 0:
        print("Error: cannot divide by zero")
    else: 
        print(f"{a} / {b} = {a / b}")
else:
    print("Invalid Entry")