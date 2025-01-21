"""
Your task is to write a Python program to convert 
temperatures to and from Celsius, Cahrenheit.

In the centigrade scale, which is also called the 
Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
In the Fahrenheit scale, water freezes at 32 degrees and boils at 
212 degrees.

Note : User should be prompted twice:

- to enter a temperature,
- to enter a shortcut for given scale (C for Celsius, F for Fahrenheit).

Formula : C/5 = F-32/9, where C = temperature in Celsius and F = temperature in Fahrenheit.
"""

scale = input(
    "Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: ")
temp = int(input("Input the value of temperature you'd like to convert  : "))
o_convention = None
result = None

if scale == "C":
    result = int(round((9 * temp) / 5 + 32))
    o_convention = "Fahrenheit"
elif scale == "F":
    result = int(round((temp - 32) * 5 / 9))
    o_convention = "Celsius"
else:
    print("Input proper convention!")
print("The temperature in", o_convention, "is", result, "degrees.")
