print("Temperature Convertor \n")

print("\n1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius")
con = int(input("Type the number to choose ur conversion : "))

temp = float(input("Enter the temperature : "))

if con == 1:
    convert = temp * 9/5 + 32
    print(f"The converted value of {temp}°C  is {convert:.2f}°F")
elif con == 2:
    convert = (temp - 32) * 5/9
    print(f"The converted value of {temp}°F  is {convert:.2f}°C")
else:
    print(f"The entered value {con} is not valid")