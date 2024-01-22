def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error! Division by zero.")
        return None
    return x / y

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '4':
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in ('1', '2', '3'):
        print("Invalid input. Please enter a valid choice.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("Result: {} + {} = {}".format(num1, num2, result))
    elif choice == '2':
        result = multiply(num1, num2)
        print("Result: {} * {} = {}".format(num1, num2, result))
    elif choice == '3':
        result = divide(num1, num2)
        if result is not None:
            print("Result: {} / {} = {}".format(num1, num2, result))
