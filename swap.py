print("Enter the values to Swap \n")
num1 = int(input("Enter the value of A: "))
num2 = int(input("Enter the value of B: "))
print(f"Before Swap values are A = {num1} and B = {num2}")

# temp = num1
# num1 = num2
# num2 = temp

num1, num2 = num2, num1

print(f"After Swap values are A = {num1} and B = {num2}")
