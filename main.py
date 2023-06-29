# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print("Please select an operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
    print("The result of multiplication is:", add(num1, num2))

elif choice == '2':
    print("The result of multiplication is: ", subtract(num1, num2))

elif choice == '3':
    print("The result of multiplication is:", multiply(num1, num2))

elif choice == '4':
    if num2 == 0:
        print("You cannot divide by 0")
    else:
        print("The result of multiplication is:", divide(num1, num2))

