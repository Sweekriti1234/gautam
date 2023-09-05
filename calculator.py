def add(num1, num2):
    return num1 + num2 #this function adds numbers

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        return "cannot divide by zero"

def user_input():
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    return num1, num2

while True:
    print("please select an operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Diviion")
    print("5. Exit")
    print("Welcome to the calculator")
    print("------------------------------------------------------")

    sel = input("please enter 1 to 5:")
     
    if sel=="5":
        print("thank you for using calculator")
        break

    if sel=="1":
        num1, num2 =user_input()
        result = add(num1, num2)
        print(f"ans: {result}")
    elif sel=="2":
        num1, num2= user_input()
        result = sub(num1, num2)
        print(f'ans: {result}')
    elif sel=="3":
        num1, num2 = user_input()
        result = mul(num1, num2)
        print(f"ans: {result}")
    elif sel=="4":
        num1, num2 = user_input()
        result = div(num1, num2)
        print(f'ans: {result}')
    else:
        print("Invalid input and choice. Please try again")

    print("-----------------------------------------------------")
