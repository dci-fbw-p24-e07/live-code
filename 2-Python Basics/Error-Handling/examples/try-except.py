even_numbers = [2, 4, 6, 8, 10, 12, 14]

try:
    print(even_numbers[3])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError as error:
    print(f"Error: {error}")
    

# program to print the reciprocal of even numbers 
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number")
else:
    reciprocal = 1 / num
    print(reciprocal)


# Function to divide

def divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Denominator cannot be zero.")
    else:
        print(result)
    finally:
        print("This is the finally block")

    
x = int(input("Enter numerator: "))
y = int(input("Enter denominator: "))

divide(x, y)

try:
    